# Software Stack Inspection – 4D Reconstruction and Volume Estimation

- **Snapshot date:** 2026-01-07
- **Generated at:** 2026-01-07 09:35:49 UTC

## Agenda

- [PyTorch 2.9.1](#pytorch-2-9-1)
- [TorchVision 0.24.1](#torchvision-0-24-1)
- [PyTorch3D 0.7.4](#pytorch3d-0-7-4)
- [DeepSpeed 0.18.2](#deepspeed-0-18-2)
- [Open3D 0.19.0](#open3d-0-19-0)
- [OpenCV-Python (opencv-python) 4.12.0.88](#opencv-python-opencv-python-4-12-0-88)
- [NumPy 2.3.5](#numpy-2-3-5)
- [SciPy 1.16.3](#scipy-1-16-3)
- [pandas 2.3.3](#pandas-2-3-3)
- [scikit-learn 1.7.2](#scikit-learn-1-7-2)
- [scikit-image 0.25.2](#scikit-image-0-25-2)
- [Matplotlib 3.10.7](#matplotlib-3-10-7)
- [Seaborn 0.13.2](#seaborn-0-13-2)
- [Weights & Biases (wandb) 0.23.1](#weights-biases-wandb-0-23-1)
- [Hydra (hydra-core) 1.3.2](#hydra-hydra-core-1-3-2)
- [tqdm 4.67.1](#tqdm-4-67-1)

---

<a id="pytorch-2-9-1"></a>
## PyTorch (2.9.1)

**Software Name:**  PyTorch  \
**Version:**  2.9.1  \
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

- **Other:** https://pytorch.org/

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 2.9.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD 3-Clause

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
- **ARM build source / URL:** https://pypi.org/project/torch/
- **Notes:** manylinux aarch64 wheel is available on PyPI - and docker images are also available on NGC.

---

<a id="torchvision-0-24-1"></a>
## TorchVision (0.24.1)

**Software Name:**  TorchVision  \
**Version:**  0.24.1  \
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

- **Other:** https://pytorch.org/vision

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 0.24.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD 3-Clause

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/30/65/ac0a3f9be6abdbe4e1d82c915d7e20de97e7fd0e9a277970508b015309f3/torchvision-0.24.1-cp313-cp313-manylinux_2_28_aarch64.whl
- **Notes:** manylinux aarch64 wheel is available on PyPI

---

<a id="pytorch3d-0-7-4"></a>
## PyTorch3D (0.7.4)

**Software Name:**  PyTorch3D  \
**Version:**  0.7.4  \
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

- **Other:** https://pytorch3d.org

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 0.7.4)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD License

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

- **ARM/aarch64 build available?**: No
- **ARM build source / URL:** -
- **Notes:** No aarch64 wheels available on PyPI and no mention of ARM support on the project's github repo

---

<a id="deepspeed-0-18-2"></a>
## DeepSpeed (0.18.2)

**Software Name:**  DeepSpeed  \
**Version:**  0.18.2  \
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

- **GitHub:** https://github.com/microsoft/DeepSpeed

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  deepspeedai/DeepSpeed
- **Description:**  DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective.
- **Stars:**  41170
- **Forks:**  4680
- **Open Issues:**  1249
- **Last Commit Date:**  2026-01-07T08:32:17Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.18.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.18.2
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

- **ARM/aarch64 build available?**: Through source build
- **ARM build source / URL:** -
- **Notes:** No available aarch64 wheel on PyPI. Pip installation will build all of the extensions/ops just-in-time (JIT) using torch's JIT C++ extension loader that relies on ninja to build and dynamically link them at runtime.

---

<a id="open3d-0-19-0"></a>
## Open3D (0.19.0)

**Software Name:**  Open3D  \
**Version:**  0.19.0  \
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

- **GitHub:** https://github.com/isl-org/Open3D

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  isl-org/Open3D
- **Description:**  Open3D: A Modern Library for 3D Data Processing
- **Stars:**  13176
- **Forks:**  2507
- **Open Issues:**  1328
- **Last Commit Date:**  2026-01-05T22:38:56Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.19.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.19.0
- **Release upload time:** N/A
- **Summary:** Open3D: A Modern Library for 3D Data Processing.
- **Homepage:** https://www.open3d.org
- **Project URLs:**
  - Documentation: https://www.open3d.org/docs
  - Homepage: https://www.open3d.org
  - Issues: https://github.com/isl-org/Open3D/issues
  - Source code: https://github.com/isl-org/Open3D

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

- **ARM/aarch64 build available?**: Not directly, but through source build - Also, note that the following disclaimer is written on their documentation: "Open3D provides experimental support for 64-bit ARM architecture (arm64 or aarch64) on Linux"
- **ARM build source / URL:** -
- **Notes:** For v0.19.0 specified, there is no manylinux aarch64 on PyPI. However, it is available in older versions like 0.14.1. There is documentation for compiling Open3D on ARM64 Linux, but it is experimental support.

---

<a id="opencv-python-opencv-python-4-12-0-88"></a>
## OpenCV-Python (opencv-python) (4.12.0.88)

**Software Name:**  OpenCV-Python (opencv-python)  \
**Version:**  4.12.0.88  \
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

- **PyPI:** https://pypi.org/project/opencv-python/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  opencv/opencv-python
- **Description:**  Automated CI toolchain to produce precompiled opencv-python, opencv-python-headless, opencv-contrib-python and opencv-contrib-python-headless packages.
- **Stars:**  5139
- **Forks:**  981
- **Open Issues:**  181
- **Last Commit Date:**  2026-01-06T10:31:06Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 4.12.0.88)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 4.12.0.88
- **Release upload time:** N/A
- **Summary:** Wrapper package for OpenCV python bindings.
- **Homepage:** https://github.com/opencv/opencv-python
- **Project URLs:**
  - Homepage: https://github.com/opencv/opencv-python

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Apache 2.0

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/62/3a/440bd64736cf8116f01f3b7f9f2e111afb2e02beb2ccc08a6458114a6b5d/opencv_python-4.12.0.88-cp37-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="numpy-2-3-5"></a>
## NumPy (2.3.5)

**Software Name:**  NumPy  \
**Version:**  2.3.5  \
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

- **PyPI:** https://pypi.org/project/numpy/2.3.5/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  numpy/numpy
- **Description:**  The fundamental package for scientific computing with Python.
- **Stars:**  31171
- **Forks:**  11927
- **Open Issues:**  2400
- **Last Commit Date:**  2026-01-06T20:05:09Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.3.5)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.3.5
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
- **License name:** BSD License

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/7d/e4/68d2f474df2cb671b2b6c2986a02e520671295647dad82484cde80ca427b/numpy-2.3.5-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="scipy-1-16-3"></a>
## SciPy (1.16.3)

**Software Name:**  SciPy  \
**Version:**  1.16.3  \
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

- **PyPI:** https://pypi.org/project/scipy/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scipy/scipy
- **Description:**  SciPy library main repository
- **Stars:**  14318
- **Forks:**  5578
- **Open Issues:**  1749
- **Last Commit Date:**  2026-01-07T08:08:49Z
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
- **License name:** BSD License

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/16/9d/d9e148b0ec680c0f042581a2be79a28a7ab66c0c4946697f9e7553ead337/scipy-1.16.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="pandas-2-3-3"></a>
## pandas (2.3.3)

**Software Name:**  pandas  \
**Version:**  2.3.3  \
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

- **PyPI:** https://pypi.org/project/pandas/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pandas-dev/pandas
- **Description:**  Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
- **Stars:**  47498
- **Forks:**  19476
- **Open Issues:**  3595
- **Last Commit Date:**  2026-01-06T22:12:54Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.3.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.3.3
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

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** https://files.pythonhosted.org/packages/f9/88/702bde3ba0a94b8c73a0181e05144b10f13f29ebfc2150c3a79062a8195d/pandas-2.3.3-cp314-cp314t-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl
- **Notes:** aarch64 wheel available on PyPI

---

<a id="scikit-learn-1-7-2"></a>
## scikit-learn (1.7.2)

**Software Name:**  scikit-learn  \
**Version:**  1.7.2  \
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

- **PyPI:** https://pypi.org/project/scikit-learn/1.7.2/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scikit-learn/scikit-learn
- **Description:**  scikit-learn: machine learning in Python
- **Stars:**  64532
- **Forks:**  26582
- **Open Issues:**  2119
- **Last Commit Date:**  2026-01-06T14:26:20Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.7.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.7.2
- **Release upload time:** N/A
- **Summary:** A set of python modules for machine learning and data mining
- **Project URLs:**
  - download: https://pypi.org/project/scikit-learn/#files
  - homepage: https://scikit-learn.org
  - release notes: https://scikit-learn.org/stable/whats_new
  - source: https://github.com/scikit-learn/scikit-learn
  - tracker: https://github.com/scikit-learn/scikit-learn/issues

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

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** https://files.pythonhosted.org/packages/99/7e/290362f6ab582128c53445458a5befd471ed1ea37953d5bcf80604619250/scikit_learn-1.7.2-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl
- **Notes:** aarch64 wheel available on PyPI

---

<a id="scikit-image-0-25-2"></a>
## scikit-image (0.25.2)

**Software Name:**  scikit-image  \
**Version:**  0.25.2  \
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

- **PyPI:** https://pypi.org/project/scikit-image/0.25.2/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scikit-image/scikit-image
- **Description:**  Image processing in Python
- **Stars:**  6418
- **Forks:**  2353
- **Open Issues:**  857
- **Last Commit Date:**  2026-01-06T16:39:33Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.25.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.25.2
- **Release upload time:** N/A
- **Summary:** Image processing in Python
- **Project URLs:**
  - documentation: https://scikit-image.org/docs/stable
  - download: https://pypi.org/project/scikit-image/#files
  - homepage: https://scikit-image.org
  - source: https://github.com/scikit-image/scikit-image
  - tracker: https://github.com/scikit-image/scikit-image/issues

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

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** https://files.pythonhosted.org/packages/4e/63/3368902ed79305f74c2ca8c297dfeb4307269cbe6402412668e322837143/scikit_image-0.25.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
- **Notes:** aarch64 wheel is available on PyPI

---

<a id="matplotlib-3-10-7"></a>
## Matplotlib (3.10.7)

**Software Name:**  Matplotlib  \
**Version:**  3.10.7  \
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

- **PyPI:** https://pypi.org/project/matplotlib/3.10.7/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  matplotlib/matplotlib
- **Description:**  matplotlib: plotting with Python
- **Stars:**  22190
- **Forks:**  8170
- **Open Issues:**  1544
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
- **License name:** Matplotlib license (BSD-compatible)

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/77/b5/e6ca22901fd3e4fe433a82e583436dd872f6c966fca7e63cf806b40356f8/matplotlib-3.10.7-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl
- **Notes:** aarch64 wheel available on PyPI

---

<a id="seaborn-0-13-2"></a>
## Seaborn (0.13.2)

**Software Name:**  Seaborn  \
**Version:**  0.13.2  \
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

- **PyPI:** https://pypi.org/project/seaborn/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  mwaskom/seaborn
- **Description:**  Statistical data visualization in Python
- **Stars:**  13660
- **Forks:**  2074
- **Open Issues:**  200
- **Last Commit Date:**  2025-12-24T15:21:16Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.13.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.13.2
- **Release upload time:** N/A
- **Summary:** Statistical data visualization
- **Project URLs:**
  - Docs: http://seaborn.pydata.org
  - Source: https://github.com/mwaskom/seaborn

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

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/seaborn/#files
- **Notes:** seaborn ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="weights-biases-wandb-0-23-1"></a>
## Weights & Biases (wandb) (0.23.1)

**Software Name:**  Weights & Biases (wandb)  \
**Version:**  0.23.1  \
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

- **PyPI:** https://pypi.org/project/wandb/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  wandb/wandb
- **Description:**  The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.
- **Stars:**  10706
- **Forks:**  806
- **Open Issues:**  804
- **Last Commit Date:**  2026-01-07T00:51:06Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.23.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.23.1
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

- **ARM/aarch64 build available?**: Yes
- **ARM build source / URL:** https://files.pythonhosted.org/packages/96/b6/fd465827c14c64d056d30b4c9fcf4dac889a6969dba64489a88fc4ffa333/wandb-0.23.1-py3-none-manylinux_2_28_aarch64.whl
- **Notes:** aarch64 wheel available on PyPI

---

<a id="hydra-hydra-core-1-3-2"></a>
## Hydra (hydra-core) (1.3.2)

**Software Name:**  Hydra (hydra-core)  \
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
- **Stars:**  10082
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

<a id="tqdm-4-67-1"></a>
## tqdm (4.67.1)

**Software Name:**  tqdm  \
**Version:**  4.67.1  \
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

- **PyPI:** https://pypi.org/project/tqdm/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  tqdm/tqdm
- **Description:**  :zap: A Fast, Extensible Progress Bar for Python and CLI
- **Stars:**  30834
- **Forks:**  1419
- **Open Issues:**  582
- **Last Commit Date:**  2024-11-12T13:35:33Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 4.67.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 4.67.1
- **Release upload time:** N/A
- **Summary:** Fast, Extensible Progress Meter
- **Project URLs:**
  - changelog: https://tqdm.github.io/releases
  - homepage: https://tqdm.github.io
  - repository: https://github.com/tqdm/tqdm
  - wiki: https://github.com/tqdm/tqdm/wiki

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
- **ARM build source / URL:** https://pypi.org/project/tqdm
- **Notes:** tqdm ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

