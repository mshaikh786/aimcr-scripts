# Software Stack Inspection – Brain-3D-FM

- **Snapshot date:** 2026-01-06
- **Generated at:** 2026-01-06 12:27:55 UTC

## Agenda

- [Pytorch Latest](#pytorch-latest)
- [DeepSpeed Latest](#deepspeed-latest)
- [FlashAttention-2 Latest](#flashattention-2-latest)
- [Scanpy/Squidpy Latest](#scanpy-squidpy-latest)

---

<a id="pytorch-latest"></a>
## Pytorch (Latest)

**Software Name:**  Pytorch  \
**Version:**  Latest  \
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

- **GitHub:** https://github.com/pytorch/pytorch

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  96378
- **Forks:**  26428
- **Open Issues:**  17906
- **Last Commit Date:**  2026-01-06T12:01:39Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version Latest)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.0.2
- **Release upload time:** N/A
- **Summary:** 

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Open Source BSD

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
- **ARM build source / URL:** PyPI aarch64 wheels: https://pypi.org/project/torch/#files ; see also vendor ARM GPU containers (e.g. NVIDIA GH200 / Grace Hopper images on NGC)
- **Notes:** PyTorch provides official manylinux aarch64 binaries and ARM support for NVIDIA platforms (e.g. Jetson / GH200). Still recommended to validate on the specific Shaheen III software stack and CUDA/toolchain versions.

---

<a id="deepspeed-latest"></a>
## DeepSpeed (Latest)

**Software Name:**  DeepSpeed  \
**Version:**  Latest  \
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

- **Other:** https://www.deepspeed.ai
- **GitHub:** https://github.com/deepspeedai/DeepSpeed

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  deepspeedai/DeepSpeed
- **Description:**  DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective.
- **Stars:**  41161
- **Forks:**  4680
- **Open Issues:**  1251
- **Last Commit Date:**  2026-01-05T15:53:40Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version Latest)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.18.3
- **Release upload time:** N/A
- **Summary:** DeepSpeed library
- **Homepage:** http://deepspeed.ai
- **Project URLs:**
  - Documentation: https://deepspeed.readthedocs.io
  - Homepage: http://deepspeed.ai
  - Source: https://github.com/deepspeedai/DeepSpeed

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Open Source (Apache 2.0)

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

- **ARM/aarch64 build available?**: Yes (via source build; no official aarch64 wheels on PyPI)
- **ARM build source / URL:** https://github.com/deepspeedai/DeepSpeed (build from source on ARM/aarch64 with a compatible CUDA + PyTorch stack)
- **Notes:** DeepSpeed does not currently provide prebuilt manylinux aarch64 wheels; however, users report successful builds on ARM platforms by compiling from source. Validate performance and compatibility on Shaheen III GPUs.

---

<a id="flashattention-2-latest"></a>
## FlashAttention-2 (Latest)

**Software Name:**  FlashAttention-2  \
**Version:**  Latest  \
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

- **GitHub:** https://github.com/Dao-AI-Lab/flash-attention

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  N/A
- **Description:**  N/A
- **Stars:**  N/A
- **Forks:**  N/A
- **Open Issues:**  N/A
- **Last Commit Date:**  N/A
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version Latest)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.0.0
- **Release upload time:** N/A
- **Summary:** Flash Attention2 operator on Huawei Ascend 910A.
- **Homepage:** https://gitee.com/mindspore/acctransformer
- **Project URLs:**
  - Homepage: https://gitee.com/mindspore/acctransformer

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Open Source (BSD)

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

- **ARM/aarch64 build available?**: Yes (via source build; CUDA kernels can be compiled on ARM hosts)
- **ARM build source / URL:** https://github.com/Dao-AI-Lab/flash-attention (build from source on ARM/aarch64 with appropriate CUDA toolkit and GPU architecture flags)
- **Notes:** No official aarch64 wheels are provided. FlashAttention-2 is typically built from source on ARM servers/accelerators (e.g. Grace Hopper) by compiling the CUDA extensions directly. Ensure nvcc, GPU arch flags (sm_*), and toolchain match Shaheen III.

---

<a id="scanpy-squidpy-latest"></a>
## Scanpy/Squidpy (Latest)

**Software Name:**  Scanpy/Squidpy  \
**Version:**  Latest  \
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

- **Other:** https://monai.io
- **GitHub:** https://github.com/scverse/squidpy

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scverse/squidpy
- **Description:**  Spatial Single Cell Analysis in Python
- **Stars:**  546
- **Forks:**  101
- **Open Issues:**  91
- **Last Commit Date:**  2025-12-17T23:46:51Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version Latest)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.7.0
- **Release upload time:** N/A
- **Summary:** Spatial Single Cell Analysis in Python
- **Project URLs:**
  - Bug Tracker: https://github.com/scverse/squidpy/issues
  - Documentation: https://squidpy.readthedocs.io
  - Home-page: https://github.com/scverse/squidpy
  - Source: https://github.com/scverse/squidpy

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Apache-2.0

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

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/squidpy/#files
- **Notes:** Squidpy ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

