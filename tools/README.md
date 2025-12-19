# ShaheenIII Software Inspection Toolkit

This mini-toolkit automates most of the workflow for inspecting software stacks
from ShaheenIII Grand Challenge proposals:

1. **Extract software list from the proposal PDF**
2. **Generate a YAML config for inspection**
3. **Fetch PyPI / GitHub metadata + SBOM info**
4. **Render a human-readable Markdown inspection report**

The toolkit consists of three scripts:

- `extract_config_from_pdf.py`
- `collect_metadata.py`
- `render_report.py`

---

## 0. Requirements

- Python 3.8+ 
- Packages:

  ```bash
  pip install pdfplumber pyyaml requests
    ```
  
## 1. extract_config_from_pdf.py

### Purpose:
Parse the proposal PDF, extract the “1. Codes & Libraries” section, and
generate:

- sw.csv – table of Software Package, Version, URL

- config.yaml – base inspection config for the rest of the pipeline

Both files are written into the same output directory.

Note: sbom_log is intentionally not filled.
You can add sbom_log entries manually later (e.g. stack.log).

### Usage:
```bash
    python tools/extract_config_from_pdf.py \
      --pdf proposals/Grand_Challenge_ShaheenIII_GPUs-DAC.pdf \
      --out-dir meta \
      --project-name "Self-Supervised Foundational Model for Chemistry and Materials Science" \
      --snapshot-date 2025-12-18
```
#### Arguments: 

- --pdf (required) \
Path to the proposal PDF file.
- --out-dir (required) \
Directory where sw.csv and config.yaml will be written
(created if it doesn’t exist).
- --project-name (optional) \
String stored as project_name in config.yaml.
Default: "ShaheenIII Project".
- --snapshot-date (optional) \
String stored as snapshot_date in config.yaml.
Default: "YYYY-MM-DD".

#### Outputs: 

1. `sw.csv`
Columns:

- Software Package 
- Version 
- URL
This is convenient to open in Excel / Google Sheets for progress tracking.

2. `config.yaml`

Example shape:
```yaml
project_name: "DAC ShaheenIII GPU Stack"
snapshot_date: "2025-12-18"

components:

- id: pytorch
  name: "PyTorch"
  version: "2.2.2"
  environment: "Python package (PyPI)"
  distribution_channels:
    - type: "pypi"
      url: "https://pypi.org/project/torch/"
  declared_license: "BSD 3-Clause"
  declared_function: "tensor & DL framework"

- id: torchvision
  ...

```

You can now adjust:
- `snapshot_date` if needed 
- environment (e.g. “inside nvcr.io/nvidia/cuda:12.1.0-base-ubuntu22.04”)
- add sbom_log fields, e.g.:
  - sbom_log: "stack.log"

## 2. collect_metadata.py

### Purpose:
Take `config.yaml`, call public APIs (PyPI + GitHub) and the local filesystem
(for SBOM logs), and produce an enriched JSON snapshot.

This is where we automatically:

- Lookup PyPI metadata for each package 
- Infer / use GitHub repository, and fetch:
  - stars, forks, open issues 
  - last commit date 
  - basic license info
- Try to match a GitHub release for the given version 
- Inspect whether the SBOM / Trivy log file exists and its size / mtime 
- Infer a simple “permissibility” classification from the license

### Usage
```bash
python tools/collect_metadata.py meta/config.yaml > meta/inspection_data.json
```
#### Inputs:
- meta/config.yaml

Must contain:
```yaml
project_name: ...
snapshot_date: ...
components:
  - id: ...
    name: ...
    version: ...
    environment: ...
    sbom_log: "stack.log"          # optional but recommended
    distribution_channels:
      - type: "pypi"
        url: "https://pypi.org/project/torch/"
      - type: "github"
        url: "https://github.com/pytorch/pytorch"
```
If a GitHub URL is missing, the script will try to infer it from PyPI
`project_urls`.

#### Outputs:
- `inspection_data.json` \
Contains all raw data that render_report.py needs to generate Markdown
(PyPI metadata, GitHub metadata, release info, local SBOM info, license
classification).

You normally don’t edit this file by hand.

---

## 3. render_report.py

### Purpose:
Turn `inspection_data.json` into a **human-readable Markdown report** with:

- Title and snapshot info
- Agenda (TOC) with links to each software section
- Per-software sections with:
  - Identity: name, version, environment 
  - SBOM/Trivy file info 
  - Source / provenance (PyPI & GitHub)
  - GitHub release info for the version 
  - License + permissibility table

### Usage:
```bash
python tools/render_report.py meta/inspection_data.json > Inspection.md
```

### Output: 

Example top of Inspection.md:
```markdown
# Software Stack Inspection – DAC ShaheenIII GPU Stack

- **Snapshot date:** 2025-12-18
- **Generated at:** 2025-12-18 14:30:12 UTC

## Agenda

- [PyTorch 2.2.2](#pytorch-222)
- [torchvision 0.17.2](#torchvision-0172)
- [...]

---

## PyTorch (2.2.2)

**Software Name:**  PyTorch  
**Version:**  2.2.2  
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.
```


You can then:
- Edit the “Summary” sections manually to be proposal-specific 
- Attach the Markdown to your proposal, export as PDF, etc.

## 4. End-to-end workflow

For a new proposal:

1. **Extract from PDF → CSV + YAML**
    ```bash
     python tools/extract_config_from_pdf.py \
      --pdf proposals/Grand_Challenge_ShaheenIII_GPUs-XYZ.pdf \
      --out-dir meta \
      --project-name "XYZ ShaheenIII GPU Stack" \
      --snapshot-date 2025-12-20
    ```


2. **Edit meta/config.yaml (if needed)**
   - Add sbom_log for each component (e.g. stack.log or one per-package)
   - Adjust environments / add missing GitHub URLs

3. **Run Trivy and write SBOM/logs to the paths you referenced in sbom_log.**

4. **Collect metadata**
    ```bash
     python tools/collect_metadata.py meta/config.yaml > meta/inspection_data.json
    ```


5. **Render Markdown report**
    ```bash
    python tools/render_report.py meta/inspection_data.json > Inspection.md 
    ```
6. **Open `Inspection.md` in your editor, fill in the human “Summary”
paragraphs, and you’re done** 

## 5. Notes / Tips

- If GitHub rate limits you:
  - Make sure GITHUB_TOKEN is set. 
  - Or temporarily reduce the number of components / metadata fields.
- If the PDF format ever changes and the extractor stops finding
“1. Codes & Libraries”, only `extract_config_from_pdf.py` needs
adjustment. The other tools stay the same.
- You can reuse the tools across projects; only the PDF and project
name/date need to change.


