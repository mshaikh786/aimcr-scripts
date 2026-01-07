# Software Stack Inspection – Integrated multi-scale modeling, protein foundation models, and autonomous AI agents

- **Snapshot date:** 2026-01-06
- **Generated at:** 2026-01-07 07:54:50 UTC

## Agenda

- [Pytorch 2.8.0](#pytorch-2-8-0)
- [vLLM Latest stable](#vllm-latest-stable)

---

<a id="pytorch-2-8-0"></a>
## Pytorch (2.8.0)

**Software Name:**  Pytorch  \
**Version:**  2.8.0  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `N/A`
- **Exists:** No

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **Other:** https://pytorch.org

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 2.8.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD 3-Clause License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes (official Linux aarch64 wheels and vendor ARM GPU containers)
- **ARM build source / URL:** PyPI aarch64 wheels: https://pypi.org/project/torch/#files ; see also NGC containers
- **Notes:** PyTorch provides official manylinux aarch64 binaries and ARM support for NVIDIA platforms (e.g. Jetson / GH200). Still recommended to validate on the specific Shaheen III software stack and CUDA/toolchain versions.

---

<a id="vllm-latest-stable"></a>
## vLLM (Latest stable)

**Software Name:**  vLLM  \
**Version:**  Latest stable  \
**Environment / Image:**  Built from source (GitHub)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `N/A`
- **Exists:** No

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **GitHub:** https://github.com/vllm-project/vllm

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  vllm-project/vllm
- **Description:**  A high-throughput and memory-efficient inference and serving engine for LLMs
- **Stars:**  66997
- **Forks:**  12428
- **Open Issues:**  3099
- **Last Commit Date:**  2026-01-07T07:36:13Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version Latest stable)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.13.0
- **Release upload time:** N/A
- **Summary:** A high-throughput and memory-efficient inference and serving engine for LLMs
- **Project URLs:**
  - Documentation: https://docs.vllm.ai/en/latest/
  - Homepage: https://github.com/vllm-project/vllm
  - Slack: https://slack.vllm.ai/

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Open Source

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** https://files.pythonhosted.org/packages/42/82/e6194ac86862c50e9ff3f58ab3eb63d71604f96723bead2fcc610821197f/vllm-0.13.0-cp38-abi3-manylinux_2_31_aarch64.whl
- **Notes:** manylinux aarch64 wheel is available on PyPI

---

