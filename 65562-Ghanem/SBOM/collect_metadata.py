#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests
import yaml

PYPI_API_BASE = "https://pypi.org/pypi"
GITHUB_API_BASE = "https://api.github.com"


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_github_repo(url):
    """Return (owner, repo) from a GitHub URL, or (None, None)."""
    if not url:
        return None, None
    parsed = urlparse(url)
    if "github.com" not in parsed.netloc:
        return None, None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None, None
    owner, repo = parts[0], parts[1]
    repo = repo.rstrip(".git")
    return owner, repo


def get_pypi_metadata(pypi_url, expected_version=None):
    """Query PyPI JSON API using the project URL and try to guess a GitHub URL."""
    if not pypi_url:
        return {}

    parsed = urlparse(pypi_url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2 or parts[0] != "project":
        return {}

    package_name = parts[1]

    try:
        resp = requests.get(f"{PYPI_API_BASE}/{package_name}/json", timeout=15)
        resp.raise_for_status()
    except Exception as e:
        return {"error": f"pypi_request_failed: {e}", "package_name": package_name}

    data = resp.json()
    info = data.get("info", {})
    releases = data.get("releases", {})

    version = expected_version or info.get("version")
    version_data = releases.get(version, [])
    upload_time = None
    if version_data:
        file_meta = version_data[0]
        upload_time = file_meta.get("upload_time_iso_8601")

    # Guess GitHub repo from project_urls / home_page
    project_urls = info.get("project_urls") or {}
    candidate_urls = []

    for _, v in project_urls.items():
        if isinstance(v, str):
            candidate_urls.append(v)

    home_page = info.get("home_page")
    if home_page:
        candidate_urls.append(home_page)

    github_guess = None
    for u in candidate_urls:
        if "github.com" in u:
            github_guess = u
            break

    return {
        "package_name": package_name,
        "version": version,
        "summary": info.get("summary"),
        "license": info.get("license"),
        "home_page": home_page,
        "project_urls": project_urls,
        "release_upload_time": upload_time,
        "github_guess": github_guess,
    }


def github_request(path, token=None, params=None):
    url = f"{GITHUB_API_BASE}{path}"
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    resp.raise_for_status()
    return resp


def get_github_metadata(github_url, token=None):
    owner, repo = extract_github_repo(github_url)
    if not owner:
        return {}

    meta = {"owner": owner, "repo": repo}

    # Basic repo info
    try:
        r = github_request(f"/repos/{owner}/{repo}", token=token)
        repo_data = r.json()
    except Exception as e:
        meta["error"] = f"github_repo_request_failed: {e}"
        return meta

    license_obj = repo_data.get("license") or {}
    meta.update(
        {
            "full_name": repo_data.get("full_name"),
            "description": repo_data.get("description"),
            "stargazers_count": repo_data.get("stargazers_count"),
            "forks_count": repo_data.get("forks_count"),
            "open_issues_count": repo_data.get("open_issues_count"),
            "default_branch": repo_data.get("default_branch"),
            "license": license_obj.get("spdx_id"),
            "license_name": license_obj.get("name"),
        }
    )

    # Last commit on default branch
    default_branch = repo_data.get("default_branch") or "main"
    try:
        r = github_request(
            f"/repos/{owner}/{repo}/commits",
            token=token,
            params={"sha": default_branch, "per_page": 1},
        )
        commits = r.json()
        if isinstance(commits, list) and commits:
            commit = commits[0]
            commit_date = (
                commit.get("commit", {})
                .get("committer", {})
                .get("date", None)
            )
            meta["last_commit_date"] = commit_date
    except Exception:
        pass

    # Simple activity classification
    last_commit = meta.get("last_commit_date")
    if last_commit:
        try:
            dt = datetime.fromisoformat(last_commit.replace("Z", "+00:00"))
            delta_days = (datetime.now(timezone.utc) - dt).days
            if delta_days <= 90:
                health = "Active"
            elif delta_days <= 365:
                health = "Moderate"
            else:
                health = "Stale"
            meta["activity_health"] = health
        except Exception:
            meta["activity_health"] = "Unknown"
    else:
        meta["activity_health"] = "Unknown"

    return meta


def get_github_release_for_version(owner, repo, version, token=None):
    """
    Try to find a GitHub release corresponding to a given version.
    Heuristics:
      - Exact tag match: 'v{version}' or '{version}'
      - Fallback: tag/name containing the version string
    """
    try:
        r = github_request(
            f"/repos/{owner}/{repo}/releases",
            token=token,
            params={"per_page": 100},
        )
        releases = r.json()
    except Exception as e:
        return {"error": f"github_releases_request_failed: {e}"}

    if not isinstance(releases, list):
        return {}

    candidates = []

    for rel in releases:
        tag = (rel.get("tag_name") or "").strip()
        name = (rel.get("name") or "").strip()

        if tag == version or tag == f"v{version}":
            candidates.append((0, rel))
        elif version in tag or version in name:
            candidates.append((1, rel))

    if not candidates:
        return {}

    candidates.sort(key=lambda x: x[0])
    rel = candidates[0][1]

    return {
        "id": rel.get("id"),
        "tag_name": rel.get("tag_name"),
        "name": rel.get("name"),
        "html_url": rel.get("html_url"),
        "published_at": rel.get("published_at"),
        "draft": rel.get("draft"),
        "prerelease": rel.get("prerelease"),
    }


def infer_license_permissibility(spdx_id, name):
    lic = (spdx_id or name or "").upper()

    permissive = {"MIT", "BSD-3-CLAUSE", "BSD-2-CLAUSE", "APACHE-2.0", "ISC"}
    copyleft = {"GPL-3.0", "AGPL-3.0", "LGPL-3.0"}

    if any(k in lic for k in permissive):
        return {
            "academic": True,
            "commercial": True,
            "modification": True,
            "redistribution": True,
            "attribution": True,
            "copyleft": False,
        }
    if any(k in lic for k in copyleft):
        return {
            "academic": True,
            "commercial": True,  # but with conditions
            "modification": True,
            "redistribution": True,
            "attribution": True,
            "copyleft": True,
        }

    return {
        "academic": None,
        "commercial": None,
        "modification": None,
        "redistribution": None,
        "attribution": None,
        "copyleft": None,
    }


def check_sbom_file(path):
    info = {"path": path, "exists": False}
    if not path:
        return info
    if os.path.exists(path):
        stat = os.stat(path)
        info["exists"] = True
        info["size_bytes"] = stat.st_size
        info["mtime"] = datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat()
    return info


def main():
    if len(sys.argv) < 2:
        print("Usage: collect_metadata.py inspection_config.yaml", file=sys.stderr)
        sys.exit(1)

    config_path = sys.argv[1]
    cfg = load_config(config_path)

    github_token = os.environ.get("GITHUB_TOKEN")

    enriched_components = []

    for comp in cfg.get("components", []):
        comp_id = comp.get("id")
        name = comp.get("name")
        version = comp.get("version")
        distribution_channels = comp.get("distribution_channels", [])

        print(f"[INFO] Processing component: {comp_id} ({name})", file=sys.stderr)

        pypi_meta = {}
        pypi_url = None
        github_url = None

        # Collect URLs from config
        for ch in distribution_channels:
            ch_type = ch.get("type")
            url = ch.get("url")
            if ch_type == "pypi" and not pypi_url:
                pypi_url = url
            if ch_type == "github" and not github_url:
                github_url = url
            if not github_url and url and "github.com" in url:
                github_url = url

        # PyPI metadata (and possible GitHub guess)
        if pypi_url:
            pypi_meta = get_pypi_metadata(pypi_url, expected_version=version)

        # If GitHub URL not explicitly set, try to infer from PyPI
        if not github_url and pypi_meta.get("github_guess"):
            github_url = pypi_meta["github_guess"]

        # GitHub repo + release metadata
        github_meta = {}
        github_release_meta = {}
        if github_url:
            github_meta = get_github_metadata(github_url, token=github_token)
            owner, repo = extract_github_repo(github_url)
            if owner and repo:
                github_release_meta = get_github_release_for_version(
                    owner, repo, version, token=github_token
                )

        # License and permissibility
        license_spdx = github_meta.get("license") or None
        license_name = github_meta.get("license_name") or pypi_meta.get("license")
        perms = infer_license_permissibility(license_spdx, license_name)

        # SBOM
        sbom_log_path = comp.get("sbom_log")
        sbom_info = check_sbom_file(sbom_log_path)

        enriched = {
            "id": comp_id,
            "name": name,
            "version": version,
            "environment": comp.get("environment"),
            "distribution_channels": distribution_channels,
            "sbom": sbom_info,
            "pypi": pypi_meta,
            "github": github_meta,
            "github_release": github_release_meta,
            "license": {
                "spdx_id": license_spdx,
                "name": license_name,
            },
            "permissibility": {
                "academic": perms["academic"],
                "commercial": perms["commercial"],
                "modification": perms["modification"],
                "redistribution": perms["redistribution"],
                "attribution": perms["attribution"],
                "copyleft": perms["copyleft"],
            },
        }

        enriched_components.append(enriched)

    output = {
        "project_name": cfg.get("project_name"),
        "snapshot_date": cfg.get("snapshot_date"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "components": enriched_components,
    }

    json.dump(output, sys.stdout, indent=2, sort_keys=False)


if __name__ == "__main__":
    main()
