# Software Stack Inspection – Optimization Algorithms for Machine Learning

- **Snapshot date:** 2026-01-07
- **Generated at:** 2026-01-07 08:18:36 UTC

## Agenda

- [Pytorch 2.7.1](#pytorch-2-7-1)
- [Torchvision 0.22.1](#torchvision-0-22-1)
- [Numpy 1.26.4](#numpy-1-26-4)
- [wandb 0.19.11](#wandb-0-19-11)
- [Matplotlib 3.10.3](#matplotlib-3-10-3)
- [Hydra 1.3.2](#hydra-1-3-2)
- [Pandas 2.2.3](#pandas-2-2-3)

---

<a id="pytorch-2-7-1"></a>
## Pytorch (2.7.1)

**Software Name:**  Pytorch  \
**Version:**  2.7.1  \
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

- **PyPI:** https://pypi.org/project/torch/2.7.1/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  96395
- **Forks:**  26437
- **Open Issues:**  17876
- **Last Commit Date:**  2026-01-07T07:47:44Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.7.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.7.1
- **Release upload time:** N/A
- **Summary:** Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Project URLs:**
  - Documentation: https://pytorch.org/docs
  - Forum: https://discuss.pytorch.org
  - Homepage: https://pytorch.org
  - Issue Tracker: https://github.com/pytorch/pytorch/issues
  - Repository: https://github.com/pytorch/pytorch

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/66/81/e48c9edb655ee8eb8c2a6026abdb6f8d2146abd1f150979ede807bb75dcb/torch-2.7.1-cp313-cp313-manylinux_2_28_aarch64.whl and also see NGC
- **Notes:** aarch64 wheel available on PyPI - and images available on NGC too

---

<a id="torchvision-0-22-1"></a>
## Torchvision (0.22.1)

**Software Name:**  Torchvision  \
**Version:**  0.22.1  \
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

- **PyPI:** https://pypi.org/project/torchvision/0.22.1/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/vision
- **Description:**  Datasets, Transforms and Models specific to Computer Vision
- **Stars:**  17429
- **Forks:**  7195
- **Open Issues:**  1180
- **Last Commit Date:**  2026-01-06T10:09:52Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.22.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.22.1
- **Release upload time:** N/A
- **Summary:** image and video datasets and models for torch deep learning
- **Homepage:** https://github.com/pytorch/vision
- **Project URLs:**
  - Homepage: https://github.com/pytorch/vision

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/ab/c8/2ebe90f18e7ffa2120f5c3eab62aa86923185f78d2d051a455ea91461608/torchvision-0.22.1-cp313-cp313t-manylinux_2_28_aarch64.whl
- **Notes:** aarch64 wheel available on PyPI

---

<a id="numpy-1-26-4"></a>
## Numpy (1.26.4)

**Software Name:**  Numpy  \
**Version:**  1.26.4  \
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

- **PyPI:** https://pypi.org/project/numpy/1.26.4/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  numpy/numpy
- **Description:**  The fundamental package for scientific computing with Python.
- **Stars:**  31171
- **Forks:**  11927
- **Open Issues:**  2400
- **Last Commit Date:**  2026-01-06T20:05:09Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.26.4)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.26.4
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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/79/f8/97f10e6755e2a7d027ca783f63044d5b1bc1ae7acb12afe6a9b4286eac17/numpy-1.26.4-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="wandb-0-19-11"></a>
## wandb (0.19.11)

**Software Name:**  wandb  \
**Version:**  0.19.11  \
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

- **PyPI:** https://pypi.org/project/wandb/0.19.11/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  wandb/wandb
- **Description:**  The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.
- **Stars:**  10706
- **Forks:**  806
- **Open Issues:**  804
- **Last Commit Date:**  2026-01-07T00:51:06Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.19.11)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.19.11
- **Release upload time:** N/A
- **Summary:** A CLI and library for interacting with the Weights & Biases API.
- **Project URLs:**
  - Bug Reports: https://github.com/wandb/wandb/issues
  - Documentation: https://docs.wandb.ai/
  - Source: https://github.com/wandb/wandb

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** MIT

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/68/06/8b827f16a0b8f18002d2fffa7c5a7fd447946e0d0c68aeec0dd7eb18cdd3/wandb-0.19.11-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="matplotlib-3-10-3"></a>
## Matplotlib (3.10.3)

**Software Name:**  Matplotlib  \
**Version:**  3.10.3  \
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

- **PyPI:** https://pypi.org/project/matplotlib/3.10.3/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  matplotlib/matplotlib
- **Description:**  matplotlib: plotting with Python
- **Stars:**  22190
- **Forks:**  8170
- **Open Issues:**  1544
- **Last Commit Date:**  2026-01-04T06:14:22Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 3.10.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 3.10.3
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
- **License name:** PSF

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/89/44/f3bc6b53066c889d7a1a3ea8094c13af6a667c5ca6220ec60ecceec2dabe/matplotlib-3.10.3-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- **Notes:** manylinux aarch64 wheel available

---

<a id="hydra-1-3-2"></a>
## Hydra (1.3.2)

**Software Name:**  Hydra  \
**Version:**  1.3.2  \
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

- **PyPI:** https://pypi.org/project/hydra-core/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  facebookresearch/hydra
- **Description:**  Hydra is a framework for elegantly configuring complex applications
- **Stars:**  10081
- **Forks:**  780
- **Open Issues:**  365
- **Last Commit Date:**  2025-11-29T13:53:02Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.3.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.3.2
- **Release upload time:** N/A
- **Summary:** A framework for elegantly configuring complex applications
- **Homepage:** https://github.com/facebookresearch/hydra
- **Project URLs:**
  - Homepage: https://github.com/facebookresearch/hydra

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** MIT License

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
- **ARM build source / URL:** https://pypi.org/project/hydra-core
- **Notes:** hydra-core ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="pandas-2-2-3"></a>
## Pandas (2.2.3)

**Software Name:**  Pandas  \
**Version:**  2.2.3  \
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

- **PyPI:** https://pypi.org/project/pandas/2.2.3/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pandas-dev/pandas
- **Description:**  Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
- **Stars:**  47496
- **Forks:**  19476
- **Open Issues:**  3595
- **Last Commit Date:**  2026-01-06T22:12:54Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.2.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.2.3
- **Release upload time:** N/A
- **Summary:** Powerful data structures for data analysis, time series, and statistics
- **Project URLs:**
  - documentation: https://pandas.pydata.org/docs/
  - homepage: https://pandas.pydata.org
  - repository: https://github.com/pandas-dev/pandas

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/ed/f9/e995754eab9c0f14c6777401f7eece0943840b7a9fc932221c19d1abee9f/pandas-2.2.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl
- **Notes:** manylinux aarc64 wheel available on PyPI

---

