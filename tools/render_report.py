#!/usr/bin/env python3

import json
import sys
import re
from datetime import datetime


def slugify(name, version=None):
    """
    Create an anchor-friendly slug like:
      "PyTorch", "2.2.2" -> "pytorch-222"
    """
    base = name if version is None else f"{name}-{version}"
    s = base.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def yn(val):
    if val is True:
        return "Yes"
    if val is False:
        return "No"
    return "Unknown"


def format_date_iso(iso_str):
    if not iso_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception:
        return iso_str


def main():
    if len(sys.argv) < 2:
        print("Usage: render_report.py inspection_data.json", file=sys.stderr)
        sys.exit(1)

    json_path = sys.argv[1]
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    project_name = data.get("project_name", "Software Stack Inspection")
    snapshot_date = data.get("snapshot_date", "")
    generated_at = data.get("generated_at", "")

    components = data.get("components", [])

    # ---------- HEADER ----------
    print(f"# Software Stack Inspection – {project_name}")
    print()
    if snapshot_date:
        print(f"- **Snapshot date:** {snapshot_date}")
    if generated_at:
        print(f"- **Generated at:** {format_date_iso(generated_at)}")
    print()

    # ---------- AGENDA ----------
    print("## Agenda")
    print()
    for comp in components:
        name = comp.get("name", "Unknown")
        version = comp.get("version", "")
        slug = slugify(name, version)
        print(f"- [{name} {version}](#{slug})")
    print()
    print("---")
    print()

    # ---------- PER-COMPONENT SECTIONS ----------
    for comp in components:
        name = comp.get("name", "Unknown")
        version = comp.get("version", "")
        environment = comp.get("environment", "")
        slug = slugify(name, version)

        sbom = comp.get("sbom", {}) or {}
        pypi = comp.get("pypi", {}) or {}
        github = comp.get("github", {}) or {}
        gh_rel = comp.get("github_release", {}) or {}
        license_info = comp.get("license", {}) or {}
        perms = comp.get("permissibility", {}) or {}

        # Distribution channels
        dist_channels = comp.get("distribution_channels", []) or []

        # Anchor
        print(f"<a id=\"{slug}\"></a>")
        print(f"## {name} ({version})")
        print()
        print(f"**Software Name:**  {name}  \\")
        print(f"**Version:**  {version}  \\")
        print(f"**Environment / Image:**  {environment}")
        print()
        print("---")
        print()

        # 1. Summary – left as TODO for now
        print("### 1. Summary")
        print()
        # You can later post-process this or hand-edit:
        print("> TODO: Add project-specific summary describing how this package is used in the workload.")
        print()
        print("---")
        print()

        # 2. SBOM
        print("### 2. SBOM Extract (from Trivy)")
        print()
        sbom_path = sbom.get("path") or "N/A"
        print(f"- **SBOM / Trivy log file:** `{sbom_path}`")
        print(f"- **Exists:** {yn(sbom.get('exists'))}")
        if sbom.get("exists"):
            size = sbom.get("size_bytes")
            mtime = sbom.get("mtime")
            size_str = f"{size} bytes" if size is not None else "N/A"
            print(f"- **Size:** {size_str}")
            print(f"- **Last modified:** {format_date_iso(mtime)}")
        print()
        print("---")
        print()

        # 3. Software Source / Provenance
        print("### 3. Software Source / Provenance")
        print()

        # 3.1 Source channels
        print("#### 3.1 Source Channel")
        print()
        if not dist_channels:
            print("- No distribution channels recorded in config.")
        else:
            for ch in dist_channels:
                ch_type = ch.get("type", "unknown")
                url = ch.get("url", "")
                label = ch_type.capitalize()
                if ch_type.lower() == "pypi":
                    label = "PyPI"
                elif ch_type.lower() == "github":
                    label = "GitHub"
                print(f"- **{label}:** {url}")
        print()

        # 3.2 GitHub repo metadata
        print("#### 3.2 GitHub Repository Metadata")
        print()
        if github:
            owner = github.get("owner") or "N/A"
            full_name = github.get("full_name") or "N/A"
            desc = github.get("description") or "N/A"
            stars = github.get("stargazers_count")
            forks = github.get("forks_count")
            open_issues = github.get("open_issues_count")
            last_commit = github.get("last_commit_date")
            activity = github.get("activity_health", "Unknown")

            print(f"- **Owner / Organization:**  {owner}")
            print(f"- **Repository:**  {full_name}")
            print(f"- **Description:**  {desc}")
            print(f"- **Stars:**  {stars if stars is not None else 'N/A'}")
            print(f"- **Forks:**  {forks if forks is not None else 'N/A'}")
            print(f"- **Open Issues:**  {open_issues if open_issues is not None else 'N/A'}")
            print(f"- **Last Commit Date:**  {last_commit or 'N/A'}")
            print(f"- **Activity Health:**  {activity}")
        else:
            print("- No GitHub repository metadata found (no GitHub URL or API error).")
        print()

        # 3.3 GitHub release for this version
        print(f"#### 3.3 GitHub Release (version {version})")
        print()
        if gh_rel and not gh_rel.get("error"):
            print(f"- **Tag name:** {gh_rel.get('tag_name', 'N/A')}")
            print(f"- **Release name:** {gh_rel.get('name', 'N/A')}")
            print(f"- **Published at:** {gh_rel.get('published_at', 'N/A')}")
            print(f"- **Release URL:** {gh_rel.get('html_url', 'N/A')}")
            print(f"- **Draft:** {yn(gh_rel.get('draft'))}")
            print(f"- **Prerelease:** {yn(gh_rel.get('prerelease'))}")
        else:
            msg = gh_rel.get("error") if gh_rel.get("error") else "No matching GitHub release found."
            print(f"- {msg}")
        print()

        # 3.4 PyPI metadata
        print("#### 3.4 PyPI Metadata")
        print()
        if pypi:
            print(f"- **PyPI package name:** {pypi.get('package_name', 'N/A')}")
            print(f"- **PyPI version considered:** {pypi.get('version', 'N/A')}")
            print(f"- **Release upload time:** {pypi.get('release_upload_time', 'N/A')}")
            print(f"- **Summary:** {pypi.get('summary', 'N/A')}")
            home_page = pypi.get("home_page")
            if home_page:
                print(f"- **Homepage:** {home_page}")
            project_urls = pypi.get("project_urls") or {}
            if project_urls:
                print("- **Project URLs:**")
                for key, url in project_urls.items():
                    print(f"  - {key}: {url}")
        else:
            print("- No PyPI metadata (no PyPI URL or API error).")
        print()
        print("---")
        print()

        # 4. License Analysis
        print("### 4. License Analysis")
        print()

        # 4.1 License type
        print("#### 4.1 License Type")
        print()

        lic_spdx = license_info.get("spdx_id")
        raw_lic_name = license_info.get("name")

        # Normalize / shorten license name so we don't dump full license texts
        def normalize_license_name(name):
            if not name:
                return "Unknown"
            # Collapse whitespace/newlines
            cleaned = " ".join(str(name).split())
            # If it's very long, just point to upstream instead of printing it all
            if len(cleaned) > 120:
                return "Custom / see upstream license text"
            return cleaned

        spdx_display = lic_spdx or "Unknown"
        lic_display = normalize_license_name(raw_lic_name)

        print(f"- **SPDX ID:** {spdx_display}")
        print(f"- **License name:** {lic_display}")
        print()


        # 4.2 Permissibility Summary
        print("#### 4.2 Permissibility Summary")
        print()
        print("| Question                           | Answer   |")
        print("|------------------------------------|----------|")
        print(f"| Can be used for academic purposes? | {yn(perms.get('academic'))} |")
        print(f"| Can be used for commercial use?    | {yn(perms.get('commercial'))} |")
        print(f"| Modification allowed?              | {yn(perms.get('modification'))} |")
        print(f"| Redistribution allowed?            | {yn(perms.get('redistribution'))} |")
        print(f"| Attribution required?              | {yn(perms.get('attribution'))} |")
        print(f"| Copyleft obligations?              | {yn(perms.get('copyleft'))} |")
        print()
        print("---")
        print()

    # End of report


if __name__ == "__main__":
    main()
