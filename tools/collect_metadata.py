#!/usr/bin/env python3
"""
collect_metadata.py

Read an inspection config YAML (config.yaml) and collect metadata for each
software component:

- PyPI metadata (if a PyPI URL exists)
- GitHub metadata (if a GitHub URL exists)
- SBOM / Trivy log file info (if sbom_log is set)
- Simple license/permissibility summary
- A *manual* placeholder for ARM / AArch64 support (no automation)

Outputs a single JSON document to stdout:

{
  "project_name": ...,
  "snapshot_date": ...,
  "generated_at": ...,
  "components": [
      {
        "id": ...,
        "name": ...,
        "version": ...,
        "environment": ...,
        "distribution_channels": [...],
        "declared_function": "...",
        "sbom": {...},
        "pypi": {...},
        "github": {...},
        "ngc_url": "...",
        "arch_support": {
            "arm_aarch64_available": "",
            "arm_build_url": "",
            "note": "TODO: manually check ARM/AArch64 support ..."
        },
        "license": {...}
      },
      ...
  ]
}
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml


# -----------------------------
# HTTP helper
# -----------------------------

def shorten_license_text(lic: str) -> str:
    """
    Normalize/shorten PyPI license strings so we don't dump full license texts
    into inspection_data.json.

    - If it's already short and single-line, keep it.
    - If it's long or multi-line, return a short summary with a pointer to the
      full license file / page.
    """
    if not lic:
        return ""

    s = lic.strip()
    # If it's short and single-line, just keep it
    if len(s) <= 120 and "\n" not in s and "\r" not in s:
        return s

    low = s.lower()

    if "apache" in low:
        return "Apache-2.0 (see project license file for full text)"
    if "bsd" in low:
        return "BSD-style license (see project license file for full text)"
    if "mit" in low:
        return "MIT license (see project license file for full text)"
    if "gpl" in low or "gnu general public license" in low:
        return "GPL-family license (see project license file for full text)"
    if "lgpl" in low:
        return "LGPL-family license (see project license file for full text)"
    if "mpl" in low or "mozilla public license" in low:
        return "MPL-family license (see project license file for full text)"

    # Fallback: keep only the first line
    first_line = s.splitlines()[0].strip()
    return f"{first_line} ... (see project license file for full text)"

def safe_get_json(url, headers=None, timeout=15):
    try:
        resp = requests.get(url, headers=headers or {}, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None


# -----------------------------
# URL / channel helpers
# -----------------------------

def classify_url_type(url):
    """
    Roughly classify a URL into one of: pypi, github, ngc, docker, other.
    """
    if not url:
        return "other"
    host = (urlparse(url).netloc or "").lower()
    if "pypi.org" in host:
        return "pypi"
    if "github.com" in host:
        return "github"
    if "ngc.nvidia.com" in host or "nvcr.io" in host:
        return "ngc"
    if "docker.io" in host or "ghcr.io" in host:
        return "docker"
    return "other"


def guess_pypi_url_from_github(github_url):
    """
    Try to infer a PyPI project URL from a GitHub repo URL.

    Strategy:
      - Extract repo name from https://github.com/owner/repo[...]
      - Try a few candidate PyPI project names based on that repo name.
      - For each candidate, call https://pypi.org/pypi/<name>/json
        and accept the first that returns valid JSON.

    Returns:
      "https://pypi.org/project/<name>/" or "" if nothing works.
    """
    if not github_url:
        return ""

    parsed = urlparse(github_url)
    if "github.com" not in (parsed.netloc or ""):
        return ""

    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return ""

    repo_name = parts[1]  # owner/repo -> repo

    candidates = []
    base = repo_name
    candidates.append(base)
    candidates.append(base.lower())
    candidates.append(base.replace("_", "-"))
    candidates.append(base.replace("-", "_"))

    seen = set()
    candidates = [c for c in candidates if not (c in seen or seen.add(c))]

    for name in candidates:
        api_url = f"https://pypi.org/pypi/{name}/json"
        data = safe_get_json(api_url, timeout=10)
        if data and isinstance(data, dict) and data.get("info"):
            return f"https://pypi.org/project/{name}/"

    return ""


def infer_channels_from_component(component):
    """
    Given whatever distribution_channels the config has (often just ONE),
    infer useful URLs for pypi / github / ngc without requiring the user
    to list them all manually.

    Returns a dict:
      {
        "pypi_url": "... or ''",
        "github_url": "... or ''",
        "ngc_url": "... or ''",
        "primary_type": "pypi|github|ngc|docker|other",
        "primary_url": "..."
      }
    """
    chans = component.get("distribution_channels") or []
    primary_url = ""
    primary_type = "other"

    if chans:
        primary_url = chans[0].get("url") or ""
        primary_type = chans[0].get("type") or classify_url_type(primary_url)
        primary_type = primary_type or classify_url_type(primary_url)

    pypi_url = ""
    github_url = ""
    ngc_url = ""

    # 1) Fill obvious ones from explicit channels
    for ch in chans:
        url = ch.get("url") or ""
        ctype = ch.get("type") or classify_url_type(url)
        if ctype == "pypi" and not pypi_url:
            pypi_url = url
        elif ctype == "github" and not github_url:
            github_url = url
        elif ctype == "ngc" and not ngc_url:
            ngc_url = url

    # 2) If we have PyPI but no GitHub, try to discover GitHub from PyPI project_urls
    if pypi_url and not github_url:
        tmp_meta = get_pypi_metadata(pypi_url)
        proj_urls = tmp_meta.get("project_urls") or {}
        for _, url in proj_urls.items():
            if "github.com" in (url or "").lower():
                github_url = url
                break

    # 3) If we have GitHub but no PyPI, try to guess PyPI project name from repo name
    if github_url and not pypi_url:
        guessed_pypi = guess_pypi_url_from_github(github_url)
        if guessed_pypi:
            pypi_url = guessed_pypi

    return {
        "pypi_url": pypi_url,
        "github_url": github_url,
        "ngc_url": ngc_url,
        "primary_type": primary_type,
        "primary_url": primary_url,
    }


# -----------------------------
# PyPI metadata
# -----------------------------

def get_pypi_metadata(pypi_url, expected_version=None):
    """
    Fetch basic metadata from PyPI.

    Returns:
      {
        "project_name": ...,
        "name": ...,
        "version": ...,
        "summary": ...,
        "home_page": ...,
        "project_urls": {...},
        "license": ...,
      }
    """
    if not pypi_url:
        return {}

    parsed = urlparse(pypi_url)
    if "pypi.org" not in (parsed.netloc or ""):
        return {}

    path_parts = [p for p in parsed.path.split("/") if p]
    project_name = None
    try:
        idx = path_parts.index("project")
        project_name = path_parts[idx + 1]
    except (ValueError, IndexError):
        if path_parts:
            project_name = path_parts[-1]

    if not project_name:
        return {}

    api_url = f"https://pypi.org/pypi/{project_name}/json"
    data = safe_get_json(api_url, timeout=15)
    if not data:
        return {"project_name": project_name, "error": "Failed to fetch PyPI metadata."}

    info = data.get("info", {})
    releases = data.get("releases", {}) or {}

    version = expected_version or info.get("version")
    if expected_version and expected_version not in releases:
        version = info.get("version")
    raw_license = info.get("license") or ""
    license_short = shorten_license_text(raw_license)

    meta = {
        "project_name": project_name,
        "name": info.get("name") or project_name,
        "version": version,
        "summary": info.get("summary") or "",
        "home_page": info.get("home_page") or "",
        "project_urls": info.get("project_urls") or {},
        "license": license_short,
    }
    return meta


# -----------------------------
# GitHub metadata
# -----------------------------

def parse_github_repo_slug(github_url):
    """
    Convert https://github.com/owner/repo[...] into 'owner/repo'.
    """
    if not github_url:
        return None
    parsed = urlparse(github_url)
    if "github.com" not in (parsed.netloc or ""):
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1]}"


def get_github_metadata(github_url, expected_version=None):
    """
    Fetch basic metadata from GitHub repo:
    - stars, forks, open issues
    - license
    - last push / last commit date (approx)
    """
    slug = parse_github_repo_slug(github_url)
    if not slug:
        return {}

    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    base = f"https://api.github.com/repos/{slug}"
    repo_json = safe_get_json(base, headers=headers, timeout=15)
    if not repo_json:
        return {"slug": slug, "error": "Failed to fetch GitHub repo metadata."}

    default_branch = repo_json.get("default_branch") or "main"

    # Get last commit on default branch (approx "last active")
    commits_url = f"{base}/commits?sha={default_branch}&per_page=1"
    commits_json = safe_get_json(commits_url, headers=headers, timeout=15) or []
    last_commit_date = None
    if isinstance(commits_json, list) and commits_json:
        commit = commits_json[0].get("commit", {})
        author = commit.get("author") or {}
        last_commit_date = author.get("date")

    license_info = repo_json.get("license") or {}
    gh_license = {
        "key": license_info.get("key"),
        "name": license_info.get("name"),
        "spdx_id": license_info.get("spdx_id"),
    }

    meta = {
        "slug": slug,
        "full_name": repo_json.get("full_name"),
        "description": repo_json.get("description") or "",
        "stargazers_count": repo_json.get("stargazers_count"),
        "forks_count": repo_json.get("forks_count"),
        "open_issues_count": repo_json.get("open_issues_count"),
        "watchers_count": repo_json.get("watchers_count"),
        "default_branch": default_branch,
        "created_at": repo_json.get("created_at"),
        "updated_at": repo_json.get("updated_at"),
        "pushed_at": repo_json.get("pushed_at"),
        "last_commit_date": last_commit_date,
        "license": gh_license,
    }
    return meta


# -----------------------------
# Manual ARM / arch placeholder
# -----------------------------

def manual_arch_support_placeholder():
    """
    Return a placeholder dict for ARM/AArch64 support to be filled manually.
    """
    return {
        "arm_aarch64_available": "",
        "arm_build_url": "",
        "note": (
            "TODO: manually check ARM/AArch64 support (e.g. NGC, conda-forge, "
            "PyPI wheels, vendor containers) and update 'arm_aarch64_available' "
            "to 'Yes' or 'No' and 'arm_build_url' with the relevant image or wheel."
        ),
    }


# -----------------------------
# SBOM / log file info
# -----------------------------

def sbom_info_for_component(component, config_dir):
    """
    Build a small info dict about the SBOM / Trivy log for this component.

    Expected config structure:
      sbom_log: "stack.log"       # relative to config_dir, or absolute path

    Returns:
      {
        "path": "absolute/or/relative/path",
        "exists": bool,
        "size_bytes": int or None,
        "modified_at": ISO8601 or None,
      }
    """
    sbom_path_value = component.get("sbom_log")
    if not sbom_path_value:
        return {
            "path": None,
            "exists": False,
            "size_bytes": None,
            "modified_at": None,
        }

    sbom_path = Path(sbom_path_value)
    if not sbom_path.is_absolute():
        sbom_path = (config_dir / sbom_path).resolve()

    info = {
        "path": str(sbom_path),
        "exists": sbom_path.exists(),
        "size_bytes": None,
        "modified_at": None,
    }

    if sbom_path.exists():
        stat = sbom_path.stat()
        info["size_bytes"] = stat.st_size
        info["modified_at"] = datetime.fromtimestamp(stat.st_mtime).isoformat()

    return info


# -----------------------------
# License / permissibility
# -----------------------------

def infer_license_permissibility(component, pypi_meta, github_meta):
    """
    Very simple license/permissibility aggregator.

    Returns:
      {
        "raw_license_strings": [...],
        "effective_license": "...",
        "permissive": bool or None,
        "notes": "...",
    }
    """
    declared = component.get("declared_license") or ""
    pypi_lic = (pypi_meta or {}).get("license") or ""
    gh_lic = (github_meta or {}).get("license", {}).get("spdx_id") or \
             (github_meta or {}).get("license", {}).get("name") or ""

    raw_licenses = [v for v in [declared, pypi_lic, gh_lic] if v]

    joined = " ".join(raw_licenses).lower()
    permissive_keywords = ["apache", "bsd", "mit", "isc"]
    copyleft_keywords = ["gpl", "agpl", "lgpl"]

    permissive = None
    notes = ""
    if any(k in joined for k in permissive_keywords):
        permissive = True
        notes = "Detected permissive license family (e.g. Apache/BSD/MIT)."
    elif any(k in joined for k in copyleft_keywords):
        permissive = False
        notes = "Detected copyleft license family (e.g. GPL/AGPL/LGPL)."
    elif raw_licenses:
        notes = "License detected but could not classify as clearly permissive or copyleft."
    else:
        notes = "No license information detected from config/PyPI/GitHub."

    effective = raw_licenses[0] if raw_licenses else ""

    return {
        "raw_license_strings": raw_licenses,
        "effective_license": effective,
        "permissive": permissive,
        "notes": notes,
    }


# -----------------------------
# Config & CLI
# -----------------------------

def load_config(path):
    """Load YAML inspection config with project_name, snapshot_date, components."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Collect metadata (PyPI, GitHub, SBOM) for software components "
            "defined in a YAML inspection config and emit a combined JSON "
            "report to stdout. ARM/AArch64 support is left as a manual "
            "placeholder per component."
        )
    )
    parser.add_argument(
        "config",
        help="Path to inspection config YAML file (e.g. meta/config.yaml).",
    )
    return parser.parse_args()


# -----------------------------
# Main
# -----------------------------

def main():
    args = parse_args()

    config_path = Path(args.config).resolve()
    if not config_path.exists():
        raise SystemExit(f"Config file not found: {config_path}")

    config = load_config(config_path)
    config_dir = config_path.parent

    project_name = config.get("project_name", "")
    snapshot_date = config.get("snapshot_date", "")
    components_cfg = config.get("components") or []

    # One-time reminder about manual ARM step
    print(
        "[INFO] ARM/AArch64 build checks are NOT automated. "
        "Please edit 'arch_support' in inspection_data.json manually for each component.",
        file=sys.stderr,
    )

    report = {
        "project_name": project_name,
        "snapshot_date": snapshot_date,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "components": [],
    }

    for comp in components_cfg:
        comp_id = comp.get("id")
        name = comp.get("name")
        version = (comp.get("version") or "").strip()
        environment = comp.get("environment", "")
        print(f"[INFO] Processing component: {comp_id} ({name})", file=sys.stderr)
        # Infer distribution channels from minimal config
        channel_info = infer_channels_from_component(comp)
        pypi_url = channel_info["pypi_url"]
        github_url = channel_info["github_url"]
        ngc_url = channel_info["ngc_url"]

        # 1) PyPI metadata
        pypi_meta = get_pypi_metadata(pypi_url, expected_version=version) if pypi_url else {}

        # 2) GitHub metadata
        github_meta = get_github_metadata(github_url, expected_version=version) if github_url else {}

        # 3) Manual ARM / arch placeholder
        arch_support = manual_arch_support_placeholder()

        # 4) SBOM / Trivy log info
        sbom_info = sbom_info_for_component(comp, config_dir)

        # 5) License info
        license_info = infer_license_permissibility(comp, pypi_meta, github_meta)

        component_record = {
            "id": comp_id,
            "name": name,
            "version": version,
            "environment": environment,
            "distribution_channels": comp.get("distribution_channels", []),
            "declared_function": comp.get("declared_function", ""),
            "sbom": sbom_info,
            "pypi": pypi_meta,
            "github": github_meta,
            "ngc_url": ngc_url,
            "arch_support": arch_support,
            "license": license_info,
        }

        report["components"].append(component_record)

    json.dump(report, fp=sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
