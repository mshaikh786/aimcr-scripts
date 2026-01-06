# Software Stack Inspection – ML models for Scientific Data Compression

- **Snapshot date:** 2026-01-04
- **Generated at:** 2026-01-05 14:11:43 UTC

## Agenda

- [Pytorch 2.8.0](#pytorch-2-8-0)
- [Pytorch Lightning 2.5.5](#pytorch-lightning-2-5-5)
- [Numpy 2.3.4](#numpy-2-3-4)
- [Xarray 2025.10.1](#xarray-2025-10-1)
- [Matplotlib 3.10.7](#matplotlib-3-10-7)
- [Pyinterp 2025.11.0](#pyinterp-2025-11-0)
- [Scipy 1.16.3](#scipy-1-16-3)

---

<a id="pytorch-2-8-0"></a>
## Pytorch (2.8.0)

**Software Name:**  Pytorch  \
**Version:**  2.8.0  \
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

- **GitHub:** https://github.com/pytorch/pytorch/tree/v2.8.0

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  96345
- **Forks:**  26418
- **Open Issues:**  17929
- **Last Commit Date:**  2026-01-05T09:18:29Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.8.0)

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
- **License name:** BSD

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
- **ARM build source / URL:** Linux aarch64 CUDA wheels via https://download.pytorch.org/whl (e.g. cu128 index for 2.8.0) and NVIDIA NGC PyTorch 25.xx images with torch 2.8.0.
- **Notes:** On aarch64 (e.g. GH200), use: pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128, or NGC containers such as nvcr.io/nvidia/pytorch:25.05-py3-igpu / GH200-ready tags.

---

<a id="pytorch-lightning-2-5-5"></a>
## Pytorch Lightning (2.5.5)

**Software Name:**  Pytorch Lightning  \
**Version:**  2.5.5  \
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

- **GitHub:** https://github.com/Lightning-AI/pytorch-lightning/tree/2.5.5

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  Lightning-AI/pytorch-lightning
- **Description:**  Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes.
- **Stars:**  30675
- **Forks:**  3638
- **Open Issues:**  939
- **Last Commit Date:**  2025-12-22T12:41:14Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.5.5)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.5.5
- **Release upload time:** N/A
- **Summary:** PyTorch Lightning is the lightweight PyTorch wrapper for ML researchers. Scale your models. Write less boilerplate.
- **Homepage:** https://github.com/Lightning-AI/lightning
- **Project URLs:**
  - Bug Tracker: https://github.com/Lightning-AI/pytorch-lightning/issues
  - Documentation: https://pytorch-lightning.rtfd.io/en/latest/
  - Download: https://github.com/Lightning-AI/lightning
  - Homepage: https://github.com/Lightning-AI/lightning
  - Source Code: https://github.com/Lightning-AI/lightning

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD

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
- **ARM build source / URL:** PyPI (pure-Python wheels) and conda-forge noarch builds that work on both x86_64 and aarch64.
- **Notes:** PyTorch Lightning is pure Python; ARM support mainly depends on the underlying PyTorch and its dependencies.

---

<a id="numpy-2-3-4"></a>
## Numpy (2.3.4)

**Software Name:**  Numpy  \
**Version:**  2.3.4  \
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

- **GitHub:** https://github.com/numpy/numpy/tree/v2.3.4

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  numpy/numpy
- **Description:**  The fundamental package for scientific computing with Python.
- **Stars:**  31157
- **Forks:**  11922
- **Open Issues:**  2389
- **Last Commit Date:**  2026-01-05T11:56:36Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.3.4)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.3.4
- **Release upload time:** N/A
- **Summary:** Fundamental package for array computing in Python
- **Project URLs:**
  - documentation: https://numpy.org/doc/
  - download: https://pypi.org/project/numpy/#files
  - homepage: https://numpy.org
  - release notes: https://numpy.org/doc/stable/release
  - source: https://github.com/numpy/numpy
  - tracker: https://github.com/numpy/numpy/issues

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** NOASSERTION

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** PyPI manylinux2014_aarch64 wheels and conda-forge linux-aarch64 / osx-arm64 builds for NumPy 2.x.
- **Notes:** On aarch64, prefer conda-forge (linux-aarch64) or pip install numpy==2.3.4, which will usually pull a prebuilt ARM64 wheel.

---

<a id="xarray-2025-10-1"></a>
## Xarray (2025.10.1)

**Software Name:**  Xarray  \
**Version:**  2025.10.1  \
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

- **GitHub:** https://github.com/pydata/xarray/tree/v2025.10.1

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pydata/xarray
- **Description:**  N-D labeled arrays and datasets in Python
- **Stars:**  4049
- **Forks:**  1210
- **Open Issues:**  1358
- **Last Commit Date:**  2026-01-04T07:31:51Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2025.10.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2025.10.1
- **Release upload time:** N/A
- **Summary:** N-D labeled arrays and datasets in Python
- **Project URLs:**
  - Documentation: https://docs.xarray.dev
  - SciPy2015-talk: https://www.youtube.com/watch?v=X0pAhJgySxk
  - homepage: https://xarray.dev/
  - issue-tracker: https://github.com/pydata/xarray/issues
  - source-code: https://github.com/pydata/xarray

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

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** PyPI (pure Python) and conda-forge noarch builds usable on aarch64.
- **Notes:** xarray is implemented in pure Python; no architecture-specific binaries are required. As long as Python and NumPy are available on ARM, xarray works.

---

<a id="matplotlib-3-10-7"></a>
## Matplotlib (3.10.7)

**Software Name:**  Matplotlib  \
**Version:**  3.10.7  \
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

- **GitHub:** https://github.com/matplotlib/matplotlib/tree/v3.10.7

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  matplotlib/matplotlib
- **Description:**  matplotlib: plotting with Python
- **Stars:**  22186
- **Forks:**  8170
- **Open Issues:**  1539
- **Last Commit Date:**  2026-01-04T06:14:22Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 3.10.7)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 3.10.7
- **Release upload time:** N/A
- **Summary:** Python plotting package
- **Project URLs:**
  - Bug Tracker: https://github.com/matplotlib/matplotlib/issues
  - Documentation: https://matplotlib.org
  - Donate: https://numfocus.org/donate-to-matplotlib
  - Download: https://matplotlib.org/stable/install/index.html
  - Forum: https://discourse.matplotlib.org/
  - Homepage: https://matplotlib.org
  - Source Code: https://github.com/matplotlib/matplotlib

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Apache-2.0 (see project license file for full text)

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
- **ARM build source / URL:** Conda (and conda-forge) linux-aarch64 / osx-arm64 builds for 3.10.7 and PyPI manylinux ARM64 wheels in the 3.10.x series.
- **Notes:** On aarch64, use conda install -c conda-forge matplotlib==3.10.7 or pip install matplotlib==3.10.7 if an ARM64 wheel is available for your platform.

---

<a id="pyinterp-2025-11-0"></a>
## Pyinterp (2025.11.0)

**Software Name:**  Pyinterp  \
**Version:**  2025.11.0  \
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

- **GitHub:** https://github.com/CNES/pangeo-pyinterp/tree/2025.11.0

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  CNES/pangeo-pyinterp
- **Description:**  Python library for optimized interpolation.
- **Stars:**  133
- **Forks:**  17
- **Open Issues:**  2
- **Last Commit Date:**  2025-11-11T20:47:47Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2025.11.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD-3-Clause

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

- **ARM/aarch64 build available?**: Yes (via conda-forge; PyPI is sdist-only for this version)
- **ARM build source / URL:** https://anaconda.org/conda-forge/pyinterp provides linux-aarch64 binaries for pyinterp 2025.11.0; PyPI only has a source tarball.
- **Notes:** On aarch64, prefer conda install -c conda-forge pyinterp==2025.11.0 to avoid compiling C++ extensions from source.

---

<a id="scipy-1-16-3"></a>
## Scipy (1.16.3)

**Software Name:**  Scipy  \
**Version:**  1.16.3  \
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

- **GitHub:** https://github.com/scipy/scipy/tree/v1.16.3

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scipy/scipy
- **Description:**  SciPy library main repository
- **Stars:**  14314
- **Forks:**  5572
- **Open Issues:**  1744
- **Last Commit Date:**  2026-01-05T13:43:38Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.16.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.16.3
- **Release upload time:** N/A
- **Summary:** Fundamental algorithms for scientific computing in Python
- **Project URLs:**
  - documentation: https://docs.scipy.org/doc/scipy/
  - download: https://github.com/scipy/scipy/releases
  - homepage: https://scipy.org/
  - source: https://github.com/scipy/scipy
  - tracker: https://github.com/scipy/scipy/issues

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD-style license (see project license file for full text)

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
- **ARM build source / URL:** Conda-forge provides linux-aarch64 binaries for SciPy 1.16.3; several Linux distros (e.g. Debian/Ubuntu, Arch ARM) ship arm64 packages; PyPI offers ARM wheels for some platforms (e.g. Windows/macOS ARM).
- **Notes:** On GH200/Shaheen III, the recommended path is conda install -c conda-forge scipy==1.16.3 to get prebuilt ARM binaries instead of building from source.

---

