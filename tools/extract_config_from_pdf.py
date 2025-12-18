#!/usr/bin/env python3
"""
Extract software packages from a Shaheen III proposal PDF and generate:

  - sw.csv       (Software Package, Version, URL)
  - config.yaml  (inspection config for metadata/markdown tooling)

The script:
  * Looks for the "1. Codes & Libraries" section in the PDF
  * Parses each entry (Name of Code/Library, Version, URL)
  * Writes a CSV for progress tracking
  * Writes a YAML config with components and distribution channels,
    leaving 'sbom_log' empty for manual filling.

Usage:
  extract_sw_from_pdf.py --pdf PROPOSAL.pdf --out-dir OUTPUT_DIR \
      --project-name "DAC ShaheenIII GPU Stack" \
      --snapshot-date 2025-12-18
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

import pdfplumber  # pip install pdfplumber
import yaml        # pip install pyyaml


DEFAULT_ENV = "Python package (PyPI)"


# ---------- PDF PARSING HELPERS ----------

def extract_lines(pdf_path):
    """Extract all non-empty lines of text from a PDF."""
    lines = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for line in text.splitlines():
                line = line.strip()
                if line:
                    lines.append(line)
    return lines


def slice_codes_section(lines):
    """
    Return only the lines between:

      '1. Codes & Libraries'
    and
      '2. Software Containers'

    Assumes all proposals follow this layout.
    """
    start_idx = None
    end_idx = None

    for i, ln in enumerate(lines):
        if start_idx is None and ln.startswith("1. Codes & Libraries"):
            start_idx = i
        if ln.startswith("2. Software Containers"):
            end_idx = i
            break

    if start_idx is None or end_idx is None or end_idx <= start_idx:
        return []

    return lines[start_idx:end_idx]


def parse_codes_section(lines):
    """
    Parse blocks like:

      1 Name of Code/Library: Pytorch
      Version: 2.2.2
      Ownership / Licensing: BSD 3-Clause
      URL (for Open-Source codes) https://pypi.org/project/torch/
      Function: tensor & DL framework

    Returns list of dicts: {name, version, url, ownership, function}
    """
    components = []
    current = None

    for ln in lines:
        m_name = re.match(r"^\d+\s+Name of Code/Library:\s*(.+)$", ln)
        if m_name:
            if current:
                components.append(current)
            current = {
                "name": m_name.group(1).strip(),
                "version": "",
                "url": "",
                "ownership": "",
                "function": "",
            }
            continue

        if current is None:
            continue

        if ln.startswith("Version:"):
            current["version"] = ln.replace("Version:", "", 1).strip()
        elif ln.startswith("Ownership / Licensing:"):
            current["ownership"] = ln.replace("Ownership / Licensing:", "", 1).strip()
        elif ln.startswith("URL (for Open-Source codes)"):
            current["url"] = ln.replace("URL (for Open-Source codes)", "", 1).strip()
        elif ln.startswith("Function:"):
            current["function"] = ln.replace("Function:", "", 1).strip()

    if current:
        components.append(current)

    return components


# ---------- COMMON HELPERS ----------

def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def classify_channel(url):
    u = (url or "").lower()
    if "pypi.org/project" in u:
        return "pypi"
    if "github.com" in u:
        return "github"
    if "nvcr.io" in u or "ngc.nvidia.com" in u:
        return "ngc"
    if "docker.io" in u or "ghcr.io" in u:
        return "docker"
    return "other"


# ---------- OUTPUT WRITERS ----------

def write_csv(components_raw, csv_path):
    """Write sw.csv with Software Package / Version / URL."""
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Software Package", "Version", "URL"])
        for c in components_raw:
            writer.writerow([c["name"], c["version"], c["url"]])


def build_config(project_name, snapshot_date, components_raw):
    """Build the YAML structure (dict) for config.yaml."""
    components_yaml = []

    for c in components_raw:
        name = c["name"]
        version = c["version"]
        url = c["url"]
        ownership = c["ownership"]
        func = c["function"]

        comp_id = slugify(name)
        ch_type = classify_channel(url)

        env = DEFAULT_ENV
        if ch_type in ("ngc", "docker"):
            env = "Docker / NGC image"
        elif ch_type == "github":
            env = "Built from source (GitHub)"

        comp_entry = {
            "id": comp_id,
            "name": name,
            "version": version,
            "environment": env,
            # sbom_log intentionally omitted – to be filled manually
            "distribution_channels": [
                {
                    "type": ch_type,
                    "url": url,
                }
            ],
            # nice-to-have extras from proposal
            "declared_license": ownership,
            "declared_function": func,
        }

        components_yaml.append(comp_entry)

    config = {
        "project_name": project_name,
        "snapshot_date": snapshot_date,
        "components": components_yaml,
    }
    return config


def write_config_yaml(config, yaml_path):
    """Dump YAML with extra blank lines between components for readability."""
    yaml_str = yaml.dump(
        config,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )

    # Add blank line before each top-level component block
    yaml_str = yaml_str.replace("\n- id:", "\n\n- id:")

    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(yaml_str)


# ---------- CLI ----------

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Extract '1. Codes & Libraries' from a ShaheenIII proposal PDF and "
            "generate sw.csv + config.yaml in the given output directory."
        )
    )
    parser.add_argument(
        "--pdf",
        required=True,
        help="Path to the proposal PDF file.",
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        help="Directory to write sw.csv and config.yaml into.",
    )
    parser.add_argument(
        "--project-name",
        default="ShaheenIII Project",
        help="Project name to embed in config.yaml (default: 'ShaheenIII Project').",
    )
    parser.add_argument(
        "--snapshot-date",
        default="YYYY-MM-DD",
        help="Snapshot date for the inspection config (default: 'YYYY-MM-DD').",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    pdf_path = Path(args.pdf)
    out_dir = Path(args.out_dir)

    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Reading PDF: {pdf_path}", file=sys.stderr)
    lines = extract_lines(pdf_path)

    print("[INFO] Locating '1. Codes & Libraries' section...", file=sys.stderr)
    codes_lines = slice_codes_section(lines)
    if not codes_lines:
        print("[ERROR] Could not find '1. Codes & Libraries' section.", file=sys.stderr)
        sys.exit(1)

    components_raw = parse_codes_section(codes_lines)
    print(f"[INFO] Parsed {len(components_raw)} software entries.", file=sys.stderr)

    # Paths
    csv_path = out_dir / "sw.csv"
    yaml_path = out_dir / "config.yaml"

    # Write CSV
    write_csv(components_raw, csv_path)
    print(f"[INFO] Wrote software table to: {csv_path}", file=sys.stderr)

    # Build & write YAML
    config = build_config(args.project_name, args.snapshot_date, components_raw)
    write_config_yaml(config, yaml_path)
    print(f"[INFO] Wrote inspection config to: {yaml_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
