# Software Stack Inspection – DAC ShaheenIII GPU Stack

- **Snapshot date:** 2025-12-18
- **Generated at:** 2025-12-18 11:15:21 UTC

## Agenda

- [PyTorch 2.2.2](#pytorch-2-2-2)
- [torchvision 0.17.2](#torchvision-0-17-2)
- [torchaudio 2.2.2](#torchaudio-2-2-2)
- [PyTorch Geometric (pyg) 2.5.2](#pytorch-geometric-pyg-2-5-2)
- [torch-scatter 2.1.2](#torch-scatter-2-1-2)
- [torch-sparse 0.6.18](#torch-sparse-0-6-18)
- [torch-cluster 1.6.3](#torch-cluster-1-6-3)
- [PyTorch Lightning 2.2.1](#pytorch-lightning-2-2-1)
- [TorchMetrics 1.3.2](#torchmetrics-1-3-2)
- [NumPy 1.26.4](#numpy-1-26-4)
- [SciPy 1.12.0](#scipy-1-12-0)
- [pandas 2.2.1](#pandas-2-2-1)
- [scikit-learn 1.4.1.post1](#scikit-learn-1-4-1-post1)
- [Matplotlib 3.8.3](#matplotlib-3-8-3)
- [Numba 0.59.1](#numba-0-59-1)
- [einops 0.7.0](#einops-0-7-0)
- [e3nn 0.5.5](#e3nn-0-5-5)
- [ASE 3.23.0](#ase-3-23-0)
- [RDKit 2023.9.5](#rdkit-2023-9-5)
- [DeepChem 2.8.0](#deepchem-2-8-0)
- [Transformers 4.51.3](#transformers-4-51-3)
- [lmdb (py-lmdb) 1.4.1](#lmdb-py-lmdb-1-4-1)
- [Weights & Biases (wandb) 0.16.5](#weights-biases-wandb-0-16-5)

---

<a id="pytorch-2-2-2"></a>
## PyTorch (2.2.2)

**Software Name:**  PyTorch  \
**Version:**  2.2.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torch/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  pytorch
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  95987
- **Forks:**  26271
- **Open Issues:**  17896
- **Last Commit Date:**  2025-12-18T10:42:08Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 2.2.2)

- **Tag name:** v2.2.2
- **Release name:** PyTorch 2.2.2 Release, bug fix release
- **Published at:** 2024-03-27T22:27:02Z
- **Release URL:** https://github.com/pytorch/pytorch/releases/tag/v2.2.2
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torch
- **PyPI version considered:** 2.2.2
- **Release upload time:** 2024-03-27T21:06:46.500208Z
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

- **SPDX ID:** NOASSERTION
- **License name:** Other

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="torchvision-0-17-2"></a>
## torchvision (0.17.2)

**Software Name:**  torchvision  \
**Version:**  0.17.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torchvision/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  pytorch
- **Repository:**  pytorch/vision
- **Description:**  Datasets, Transforms and Models specific to Computer Vision
- **Stars:**  17379
- **Forks:**  7183
- **Open Issues:**  1182
- **Last Commit Date:**  2025-12-05T14:01:04Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 0.17.2)

- **Tag name:** v0.17.2
- **Release name:** TorchVision 0.17.2 Release
- **Published at:** 2024-03-28T15:37:14Z
- **Release URL:** https://github.com/pytorch/vision/releases/tag/v0.17.2
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torchvision
- **PyPI version considered:** 0.17.2
- **Release upload time:** 2024-03-27T21:11:38.064849Z
- **Summary:** image and video datasets and models for torch deep learning
- **Homepage:** https://github.com/pytorch/vision
- **Project URLs:**
  - Homepage: https://github.com/pytorch/vision

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** BSD-3-Clause
- **License name:** BSD 3-Clause "New" or "Revised" License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="torchaudio-2-2-2"></a>
## torchaudio (2.2.2)

**Software Name:**  torchaudio  \
**Version:**  2.2.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torchaudio/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  pytorch
- **Repository:**  pytorch/audio
- **Description:**  Data manipulation and transformation for audio signal processing, powered by PyTorch
- **Stars:**  2799
- **Forks:**  750
- **Open Issues:**  314
- **Last Commit Date:**  2025-12-17T17:32:15Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 2.2.2)

- **Tag name:** v2.2.2
- **Release name:** TorchAudio 2.2.2 Release
- **Published at:** 2024-03-28T15:39:10Z
- **Release URL:** https://github.com/pytorch/audio/releases/tag/v2.2.2
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torchaudio
- **PyPI version considered:** 2.2.2
- **Release upload time:** 2024-03-27T21:12:31.998081Z
- **Summary:** An audio package for PyTorch
- **Homepage:** https://github.com/pytorch/audio
- **Project URLs:**
  - Homepage: https://github.com/pytorch/audio

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** BSD-2-Clause
- **License name:** BSD 2-Clause "Simplified" License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="pytorch-geometric-pyg-2-5-2"></a>
## PyTorch Geometric (pyg) (2.5.2)

**Software Name:**  PyTorch Geometric (pyg)  \
**Version:**  2.5.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/pyg/

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 2.5.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** pyg
- **PyPI version considered:** 2.5.2
- **Release upload time:** None
- **Summary:** Python Package Manager
- **Homepage:** http://pyg.readthedocs.org/
- **Project URLs:**
  - Download: http://pypi.python.org/pypi/pyg
  - Homepage: http://pyg.readthedocs.org/

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Unknown
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

---

<a id="torch-scatter-2-1-2"></a>
## torch-scatter (2.1.2)

**Software Name:**  torch-scatter  \
**Version:**  2.1.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torch-scatter/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  rusty1s
- **Repository:**  rusty1s/pytorch_scatter
- **Description:**  PyTorch Extension Library of Optimized Scatter Operations
- **Stars:**  1716
- **Forks:**  204
- **Open Issues:**  15
- **Last Commit Date:**  2025-08-12T12:52:23Z
- **Activity Health:**  Moderate

#### 3.3 GitHub Release (version 2.1.2)

- **Tag name:** 2.1.2
- **Release name:** 2.1.2
- **Published at:** 2023-10-06T08:48:33Z
- **Release URL:** https://github.com/rusty1s/pytorch_scatter/releases/tag/2.1.2
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torch-scatter
- **PyPI version considered:** 2.1.2
- **Release upload time:** 2023-10-06T08:49:07.081822Z
- **Summary:** PyTorch Extension Library of Optimized Scatter Operations
- **Homepage:** https://github.com/rusty1s/pytorch_scatter
- **Project URLs:**
  - Download: https://github.com/rusty1s/pytorch_scatter/archive/2.1.2.tar.gz
  - Homepage: https://github.com/rusty1s/pytorch_scatter

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

<a id="torch-sparse-0-6-18"></a>
## torch-sparse (0.6.18)

**Software Name:**  torch-sparse  \
**Version:**  0.6.18  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torch-sparse/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  rusty1s
- **Repository:**  rusty1s/pytorch_sparse
- **Description:**  PyTorch Extension Library of Optimized Autograd Sparse Matrix Operations
- **Stars:**  1093
- **Forks:**  159
- **Open Issues:**  20
- **Last Commit Date:**  2025-08-12T12:53:29Z
- **Activity Health:**  Moderate

#### 3.3 GitHub Release (version 0.6.18)

- **Tag name:** 0.6.18
- **Release name:** 0.6.18
- **Published at:** 2023-10-06T08:51:23Z
- **Release URL:** https://github.com/rusty1s/pytorch_sparse/releases/tag/0.6.18
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torch-sparse
- **PyPI version considered:** 0.6.18
- **Release upload time:** 2023-10-06T08:51:55.326459Z
- **Summary:** PyTorch Extension Library of Optimized Autograd Sparse Matrix Operations
- **Homepage:** https://github.com/rusty1s/pytorch_sparse
- **Project URLs:**
  - Download: https://github.com/rusty1s/pytorch_sparse/archive/0.6.18.tar.gz
  - Homepage: https://github.com/rusty1s/pytorch_sparse

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

<a id="torch-cluster-1-6-3"></a>
## torch-cluster (1.6.3)

**Software Name:**  torch-cluster  \
**Version:**  1.6.3  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torch-cluster/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  rusty1s
- **Repository:**  rusty1s/pytorch_cluster
- **Description:**  PyTorch Extension Library of Optimized Graph Cluster Algorithms
- **Stars:**  904
- **Forks:**  161
- **Open Issues:**  28
- **Last Commit Date:**  2025-08-12T12:52:56Z
- **Activity Health:**  Moderate

#### 3.3 GitHub Release (version 1.6.3)

- **Tag name:** 1.6.3
- **Release name:** 1.6.3
- **Published at:** 2023-10-12T06:54:28Z
- **Release URL:** https://github.com/rusty1s/pytorch_cluster/releases/tag/1.6.3
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torch-cluster
- **PyPI version considered:** 1.6.3
- **Release upload time:** 2023-10-12T06:52:43.728644Z
- **Summary:** PyTorch Extension Library of Optimized Graph Cluster Algorithms
- **Homepage:** https://github.com/rusty1s/pytorch_cluster
- **Project URLs:**
  - Download: https://github.com/rusty1s/pytorch_cluster/archive/1.6.3.tar.gz
  - Homepage: https://github.com/rusty1s/pytorch_cluster

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

<a id="pytorch-lightning-2-2-1"></a>
## PyTorch Lightning (2.2.1)

**Software Name:**  PyTorch Lightning  \
**Version:**  2.2.1  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/pytorch-lightning/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  Lightning-AI
- **Repository:**  N/A
- **Description:**  N/A
- **Stars:**  N/A
- **Forks:**  N/A
- **Open Issues:**  N/A
- **Last Commit Date:**  N/A
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.2.1)

- github_releases_request_failed: 404 Client Error: Not Found for url: https://api.github.com/repos/Lightning-AI/pytorch-lightnin/releases?per_page=100

#### 3.4 PyPI Metadata

- **PyPI package name:** pytorch-lightning
- **PyPI version considered:** 2.2.1
- **Release upload time:** 2024-03-04T18:59:32.538292Z
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

- **SPDX ID:** Unknown
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

---

<a id="torchmetrics-1-3-2"></a>
## TorchMetrics (1.3.2)

**Software Name:**  TorchMetrics  \
**Version:**  1.3.2  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/torchmetrics/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  Lightning-AI
- **Repository:**  Lightning-AI/torchmetrics
- **Description:**  Machine learning metrics for distributed, scalable PyTorch applications.
- **Stars:**  2379
- **Forks:**  468
- **Open Issues:**  122
- **Last Commit Date:**  2025-12-17T23:16:59Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 1.3.2)

- **Tag name:** v1.3.2
- **Release name:** Minor patch release
- **Published at:** 2024-03-18T12:39:22Z
- **Release URL:** https://github.com/Lightning-AI/torchmetrics/releases/tag/v1.3.2
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** torchmetrics
- **PyPI version considered:** 1.3.2
- **Release upload time:** 2024-03-18T12:45:43.976448Z
- **Summary:** PyTorch native Metrics
- **Homepage:** https://github.com/Lightning-AI/torchmetrics
- **Project URLs:**
  - Bug Tracker: https://github.com/Lightning-AI/torchmetrics/issues
  - Documentation: https://torchmetrics.rtfd.io/en/latest/
  - Download: https://github.com/Lightning-AI/torchmetrics/archive/master.zip
  - Homepage: https://github.com/Lightning-AI/torchmetrics
  - Source Code: https://github.com/Lightning-AI/torchmetrics

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Apache-2.0
- **License name:** Apache License 2.0

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="numpy-1-26-4"></a>
## NumPy (1.26.4)

**Software Name:**  NumPy  \
**Version:**  1.26.4  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/numpy/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  numpy
- **Repository:**  numpy/numpy
- **Description:**  The fundamental package for scientific computing with Python.
- **Stars:**  31038
- **Forks:**  11858
- **Open Issues:**  2392
- **Last Commit Date:**  2025-12-17T23:48:08Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 1.26.4)

- **Tag name:** v1.26.4
- **Release name:** 
- **Published at:** 2024-02-06T00:32:23Z
- **Release URL:** https://github.com/numpy/numpy/releases/tag/v1.26.4
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** numpy
- **PyPI version considered:** 1.26.4
- **Release upload time:** 2024-02-05T23:48:01.194769Z
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

- **SPDX ID:** NOASSERTION
- **License name:** Other

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="scipy-1-12-0"></a>
## SciPy (1.12.0)

**Software Name:**  SciPy  \
**Version:**  1.12.0  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/scipy/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  scipy
- **Repository:**  scipy/scipy
- **Description:**  SciPy library main repository
- **Stars:**  14265
- **Forks:**  5556
- **Open Issues:**  1770
- **Last Commit Date:**  2025-12-18T11:14:40Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 1.12.0)

- **Tag name:** v1.12.0
- **Release name:** SciPy 1.12.0
- **Published at:** 2024-01-20T22:00:44Z
- **Release URL:** https://github.com/scipy/scipy/releases/tag/v1.12.0
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** scipy
- **PyPI version considered:** 1.12.0
- **Release upload time:** 2024-01-20T21:10:31.498221Z
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

- **SPDX ID:** BSD-3-Clause
- **License name:** BSD 3-Clause "New" or "Revised" License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="pandas-2-2-1"></a>
## pandas (2.2.1)

**Software Name:**  pandas  \
**Version:**  2.2.1  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/pandas/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  pandas-dev
- **Repository:**  pandas-dev/pandas
- **Description:**  Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
- **Stars:**  47340
- **Forks:**  19417
- **Open Issues:**  3607
- **Last Commit Date:**  2025-12-18T10:56:43Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 2.2.1)

- **Tag name:** v2.2.1
- **Release name:** Pandas 2.2.1
- **Published at:** 2024-02-23T15:29:27Z
- **Release URL:** https://github.com/pandas-dev/pandas/releases/tag/v2.2.1
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** pandas
- **PyPI version considered:** 2.2.1
- **Release upload time:** 2024-02-23T15:30:19.248570Z
- **Summary:** Powerful data structures for data analysis, time series, and statistics
- **Project URLs:**
  - documentation: https://pandas.pydata.org/docs/
  - homepage: https://pandas.pydata.org
  - repository: https://github.com/pandas-dev/pandas

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** BSD-3-Clause
- **License name:** BSD 3-Clause "New" or "Revised" License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="scikit-learn-1-4-1-post1"></a>
## scikit-learn (1.4.1.post1)

**Software Name:**  scikit-learn  \
**Version:**  1.4.1.post1  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/scikit-learn/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  scikit-learn
- **Repository:**  scikit-learn/scikit-learn
- **Description:**  scikit-learn: machine learning in Python
- **Stars:**  64318
- **Forks:**  26507
- **Open Issues:**  2127
- **Last Commit Date:**  2025-12-18T10:22:37Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 1.4.1.post1)

- **Tag name:** 1.4.1.post1
- **Release name:** Scikit-learn 1.4.1.post1
- **Published at:** 2024-02-15T16:07:32Z
- **Release URL:** https://github.com/scikit-learn/scikit-learn/releases/tag/1.4.1.post1
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** scikit-learn
- **PyPI version considered:** 1.4.1.post1
- **Release upload time:** 2024-02-16T08:56:53.322559Z
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

- **SPDX ID:** BSD-3-Clause
- **License name:** BSD 3-Clause "New" or "Revised" License

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="matplotlib-3-8-3"></a>
## Matplotlib (3.8.3)

**Software Name:**  Matplotlib  \
**Version:**  3.8.3  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/matplotlib/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  matplotlib
- **Repository:**  matplotlib/matplotlib
- **Description:**  matplotlib: plotting with Python
- **Stars:**  22134
- **Forks:**  8144
- **Open Issues:**  1558
- **Last Commit Date:**  2025-12-17T23:14:07Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 3.8.3)

- **Tag name:** v3.8.3
- **Release name:** REL: v3.8.3
- **Published at:** 2024-02-15T00:38:17Z
- **Release URL:** https://github.com/matplotlib/matplotlib/releases/tag/v3.8.3
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** matplotlib
- **PyPI version considered:** 3.8.3
- **Release upload time:** 2024-02-15T01:48:12.751570Z
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

- **SPDX ID:** Unknown
- **License name:** License agreement for matplotlib versions 1.3.0 and later
         =========================================================
         
         1. This LICENSE AGREEMENT is between the Matplotlib Development Team
         ("MDT"), and the Individual or Organization ("Licensee") accessing and
         otherwise using matplotlib software in source or binary form and its
         associated documentation.
         
         2. Subject to the terms and conditions of this License Agreement, MDT
         hereby grants Licensee a nonexclusive, royalty-free, world-wide license
         to reproduce, analyze, test, perform and/or display publicly, prepare
         derivative works, distribute, and otherwise use matplotlib
         alone or in any derivative version, provided, however, that MDT's
         License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
         2012- Matplotlib Development Team; All Rights Reserved" are retained in
         matplotlib  alone or in any derivative version prepared by
         Licensee.
         
         3. In the event Licensee prepares a derivative work that is based on or
         incorporates matplotlib or any part thereof, and wants to
         make the derivative work available to others as provided herein, then
         Licensee hereby agrees to include in any such work a brief summary of
         the changes made to matplotlib .
         
         4. MDT is making matplotlib available to Licensee on an "AS
         IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
         IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
         DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
         FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
         WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
         
         5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
          FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
         LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
         MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
         THE POSSIBILITY THEREOF.
         
         6. This License Agreement will automatically terminate upon a material
         breach of its terms and conditions.
         
         7. Nothing in this License Agreement shall be deemed to create any
         relationship of agency, partnership, or joint venture between MDT and
         Licensee.  This License Agreement does not grant permission to use MDT
         trademarks or trade name in a trademark sense to endorse or promote
         products or services of Licensee, or any third party.
         
         8. By copying, installing or otherwise using matplotlib ,
         Licensee agrees to be bound by the terms and conditions of this License
         Agreement.
         
         License agreement for matplotlib versions prior to 1.3.0
         ========================================================
         
         1. This LICENSE AGREEMENT is between John D. Hunter ("JDH"), and the
         Individual or Organization ("Licensee") accessing and otherwise using
         matplotlib software in source or binary form and its associated
         documentation.
         
         2. Subject to the terms and conditions of this License Agreement, JDH
         hereby grants Licensee a nonexclusive, royalty-free, world-wide license
         to reproduce, analyze, test, perform and/or display publicly, prepare
         derivative works, distribute, and otherwise use matplotlib
         alone or in any derivative version, provided, however, that JDH's
         License Agreement and JDH's notice of copyright, i.e., "Copyright (c)
         2002-2011 John D. Hunter; All Rights Reserved" are retained in
         matplotlib  alone or in any derivative version prepared by
         Licensee.
         
         3. In the event Licensee prepares a derivative work that is based on or
         incorporates matplotlib  or any part thereof, and wants to
         make the derivative work available to others as provided herein, then
         Licensee hereby agrees to include in any such work a brief summary of
         the changes made to matplotlib.
         
         4. JDH is making matplotlib  available to Licensee on an "AS
         IS" basis.  JDH MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
         IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, JDH MAKES NO AND
         DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
         FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
         WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
         
         5. JDH SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
          FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
         LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
         MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
         THE POSSIBILITY THEREOF.
         
         6. This License Agreement will automatically terminate upon a material
         breach of its terms and conditions.
         
         7. Nothing in this License Agreement shall be deemed to create any
         relationship of agency, partnership, or joint venture between JDH and
         Licensee.  This License Agreement does not grant permission to use JDH
         trademarks or trade name in a trademark sense to endorse or promote
         products or services of Licensee, or any third party.
         
         8. By copying, installing or otherwise using matplotlib,
         Licensee agrees to be bound by the terms and conditions of this License
         Agreement.
         ----
         
         This binary distrubution of Matplotlib can also bundle the following software
         (depending on the build):
         
         Name: AMS Fonts
         Files: matplotlib/tests/cmr10.pfb
         Description: Type-1 version of one of Knuth's Computer Modern fonts
         License: OFL-1.1
           The cmr10.pfb file is a Type-1 version of one of Knuth's Computer Modern fonts.
           It is included here as test data only, but the following license applies.
         
           Copyright (c) 1997, 2009, American Mathematical Society (http://www.ams.org).
           All Rights Reserved.
         
           "cmb10" is a Reserved Font Name for this Font Software.
           "cmbsy10" is a Reserved Font Name for this Font Software.
           "cmbsy5" is a Reserved Font Name for this Font Software.
           "cmbsy6" is a Reserved Font Name for this Font Software.
           "cmbsy7" is a Reserved Font Name for this Font Software.
           "cmbsy8" is a Reserved Font Name for this Font Software.
           "cmbsy9" is a Reserved Font Name for this Font Software.
           "cmbx10" is a Reserved Font Name for this Font Software.
           "cmbx12" is a Reserved Font Name for this Font Software.
           "cmbx5" is a Reserved Font Name for this Font Software.
           "cmbx6" is a Reserved Font Name for this Font Software.
           "cmbx7" is a Reserved Font Name for this Font Software.
           "cmbx8" is a Reserved Font Name for this Font Software.
           "cmbx9" is a Reserved Font Name for this Font Software.
           "cmbxsl10" is a Reserved Font Name for this Font Software.
           "cmbxti10" is a Reserved Font Name for this Font Software.
           "cmcsc10" is a Reserved Font Name for this Font Software.
           "cmcsc8" is a Reserved Font Name for this Font Software.
           "cmcsc9" is a Reserved Font Name for this Font Software.
           "cmdunh10" is a Reserved Font Name for this Font Software.
           "cmex10" is a Reserved Font Name for this Font Software.
           "cmex7" is a Reserved Font Name for this Font Software.
           "cmex8" is a Reserved Font Name for this Font Software.
           "cmex9" is a Reserved Font Name for this Font Software.
           "cmff10" is a Reserved Font Name for this Font Software.
           "cmfi10" is a Reserved Font Name for this Font Software.
           "cmfib8" is a Reserved Font Name for this Font Software.
           "cminch" is a Reserved Font Name for this Font Software.
           "cmitt10" is a Reserved Font Name for this Font Software.
           "cmmi10" is a Reserved Font Name for this Font Software.
           "cmmi12" is a Reserved Font Name for this Font Software.
           "cmmi5" is a Reserved Font Name for this Font Software.
           "cmmi6" is a Reserved Font Name for this Font Software.
           "cmmi7" is a Reserved Font Name for this Font Software.
           "cmmi8" is a Reserved Font Name for this Font Software.
           "cmmi9" is a Reserved Font Name for this Font Software.
           "cmmib10" is a Reserved Font Name for this Font Software.
           "cmmib5" is a Reserved Font Name for this Font Software.
           "cmmib6" is a Reserved Font Name for this Font Software.
           "cmmib7" is a Reserved Font Name for this Font Software.
           "cmmib8" is a Reserved Font Name for this Font Software.
           "cmmib9" is a Reserved Font Name for this Font Software.
           "cmr10" is a Reserved Font Name for this Font Software.
           "cmr12" is a Reserved Font Name for this Font Software.
           "cmr17" is a Reserved Font Name for this Font Software.
           "cmr5" is a Reserved Font Name for this Font Software.
           "cmr6" is a Reserved Font Name for this Font Software.
           "cmr7" is a Reserved Font Name for this Font Software.
           "cmr8" is a Reserved Font Name for this Font Software.
           "cmr9" is a Reserved Font Name for this Font Software.
           "cmsl10" is a Reserved Font Name for this Font Software.
           "cmsl12" is a Reserved Font Name for this Font Software.
           "cmsl8" is a Reserved Font Name for this Font Software.
           "cmsl9" is a Reserved Font Name for this Font Software.
           "cmsltt10" is a Reserved Font Name for this Font Software.
           "cmss10" is a Reserved Font Name for this Font Software.
           "cmss12" is a Reserved Font Name for this Font Software.
           "cmss17" is a Reserved Font Name for this Font Software.
           "cmss8" is a Reserved Font Name for this Font Software.
           "cmss9" is a Reserved Font Name for this Font Software.
           "cmssbx10" is a Reserved Font Name for this Font Software.
           "cmssdc10" is a Reserved Font Name for this Font Software.
           "cmssi10" is a Reserved Font Name for this Font Software.
           "cmssi12" is a Reserved Font Name for this Font Software.
           "cmssi17" is a Reserved Font Name for this Font Software.
           "cmssi8" is a Reserved Font Name for this Font Software.
           "cmssi9" is a Reserved Font Name for this Font Software.
           "cmssq8" is a Reserved Font Name for this Font Software.
           "cmssqi8" is a Reserved Font Name for this Font Software.
           "cmsy10" is a Reserved Font Name for this Font Software.
           "cmsy5" is a Reserved Font Name for this Font Software.
           "cmsy6" is a Reserved Font Name for this Font Software.
           "cmsy7" is a Reserved Font Name for this Font Software.
           "cmsy8" is a Reserved Font Name for this Font Software.
           "cmsy9" is a Reserved Font Name for this Font Software.
           "cmtcsc10" is a Reserved Font Name for this Font Software.
           "cmtex10" is a Reserved Font Name for this Font Software.
           "cmtex8" is a Reserved Font Name for this Font Software.
           "cmtex9" is a Reserved Font Name for this Font Software.
           "cmti10" is a Reserved Font Name for this Font Software.
           "cmti12" is a Reserved Font Name for this Font Software.
           "cmti7" is a Reserved Font Name for this Font Software.
           "cmti8" is a Reserved Font Name for this Font Software.
           "cmti9" is a Reserved Font Name for this Font Software.
           "cmtt10" is a Reserved Font Name for this Font Software.
           "cmtt12" is a Reserved Font Name for this Font Software.
           "cmtt8" is a Reserved Font Name for this Font Software.
           "cmtt9" is a Reserved Font Name for this Font Software.
           "cmu10" is a Reserved Font Name for this Font Software.
           "cmvtt10" is a Reserved Font Name for this Font Software.
           "euex10" is a Reserved Font Name for this Font Software.
           "euex7" is a Reserved Font Name for this Font Software.
           "euex8" is a Reserved Font Name for this Font Software.
           "euex9" is a Reserved Font Name for this Font Software.
           "eufb10" is a Reserved Font Name for this Font Software.
           "eufb5" is a Reserved Font Name for this Font Software.
           "eufb7" is a Reserved Font Name for this Font Software.
           "eufm10" is a Reserved Font Name for this Font Software.
           "eufm5" is a Reserved Font Name for this Font Software.
           "eufm7" is a Reserved Font Name for this Font Software.
           "eurb10" is a Reserved Font Name for this Font Software.
           "eurb5" is a Reserved Font Name for this Font Software.
           "eurb7" is a Reserved Font Name for this Font Software.
           "eurm10" is a Reserved Font Name for this Font Software.
           "eurm5" is a Reserved Font Name for this Font Software.
           "eurm7" is a Reserved Font Name for this Font Software.
           "eusb10" is a Reserved Font Name for this Font Software.
           "eusb5" is a Reserved Font Name for this Font Software.
           "eusb7" is a Reserved Font Name for this Font Software.
           "eusm10" is a Reserved Font Name for this Font Software.
           "eusm5" is a Reserved Font Name for this Font Software.
           "eusm7" is a Reserved Font Name for this Font Software.
           "lasy10" is a Reserved Font Name for this Font Software.
           "lasy5" is a Reserved Font Name for this Font Software.
           "lasy6" is a Reserved Font Name for this Font Software.
           "lasy7" is a Reserved Font Name for this Font Software.
           "lasy8" is a Reserved Font Name for this Font Software.
           "lasy9" is a Reserved Font Name for this Font Software.
           "lasyb10" is a Reserved Font Name for this Font Software.
           "lcircle1" is a Reserved Font Name for this Font Software.
           "lcirclew" is a Reserved Font Name for this Font Software.
           "lcmss8" is a Reserved Font Name for this Font Software.
           "lcmssb8" is a Reserved Font Name for this Font Software.
           "lcmssi8" is a Reserved Font Name for this Font Software.
           "line10" is a Reserved Font Name for this Font Software.
           "linew10" is a Reserved Font Name for this Font Software.
           "msam10" is a Reserved Font Name for this Font Software.
           "msam5" is a Reserved Font Name for this Font Software.
           "msam6" is a Reserved Font Name for this Font Software.
           "msam7" is a Reserved Font Name for this Font Software.
           "msam8" is a Reserved Font Name for this Font Software.
           "msam9" is a Reserved Font Name for this Font Software.
           "msbm10" is a Reserved Font Name for this Font Software.
           "msbm5" is a Reserved Font Name for this Font Software.
           "msbm6" is a Reserved Font Name for this Font Software.
           "msbm7" is a Reserved Font Name for this Font Software.
           "msbm8" is a Reserved Font Name for this Font Software.
           "msbm9" is a Reserved Font Name for this Font Software.
           "wncyb10" is a Reserved Font Name for this Font Software.
           "wncyi10" is a Reserved Font Name for this Font Software.
           "wncyr10" is a Reserved Font Name for this Font Software.
           "wncysc10" is a Reserved Font Name for this Font Software.
           "wncyss10" is a Reserved Font Name for this Font Software.
         
           This Font Software is licensed under the SIL Open Font License, Version 1.1.
           This license is copied below, and is also available with a FAQ at:
           http://scripts.sil.org/OFL
         
           -----------------------------------------------------------
           SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
           -----------------------------------------------------------
         
           PREAMBLE
           The goals of the Open Font License (OFL) are to stimulate worldwide
           development of collaborative font projects, to support the font creation
           efforts of academic and linguistic communities, and to provide a free and
           open framework in which fonts may be shared and improved in partnership
           with others.
         
           The OFL allows the licensed fonts to be used, studied, modified and
           redistributed freely as long as they are not sold by themselves. The
           fonts, including any derivative works, can be bundled, embedded, 
           redistributed and/or sold with any software provided that any reserved
           names are not used by derivative works. The fonts and derivatives,
           however, cannot be released under any other type of license. The
           requirement for fonts to remain under this license does not apply
           to any document created using the fonts or their derivatives.
         
           DEFINITIONS
           "Font Software" refers to the set of files released by the Copyright
           Holder(s) under this license and clearly marked as such. This may
           include source files, build scripts and documentation.
         
           "Reserved Font Name" refers to any names specified as such after the
           copyright statement(s).
         
           "Original Version" refers to the collection of Font Software components as
           distributed by the Copyright Holder(s).
         
           "Modified Version" refers to any derivative made by adding to, deleting,
           or substituting -- in part or in whole -- any of the components of the
           Original Version, by changing formats or by porting the Font Software to a
           new environment.
         
           "Author" refers to any designer, engineer, programmer, technical
           writer or other person who contributed to the Font Software.
         
           PERMISSION & CONDITIONS
           Permission is hereby granted, free of charge, to any person obtaining
           a copy of the Font Software, to use, study, copy, merge, embed, modify,
           redistribute, and sell modified and unmodified copies of the Font
           Software, subject to the following conditions:
         
           1) Neither the Font Software nor any of its individual components,
           in Original or Modified Versions, may be sold by itself.
         
           2) Original or Modified Versions of the Font Software may be bundled,
           redistributed and/or sold with any software, provided that each copy
           contains the above copyright notice and this license. These can be
           included either as stand-alone text files, human-readable headers or
           in the appropriate machine-readable metadata fields within text or
           binary files as long as those fields can be easily viewed by the user.
         
           3) No Modified Version of the Font Software may use the Reserved Font
           Name(s) unless explicit written permission is granted by the corresponding
           Copyright Holder. This restriction only applies to the primary font name as
           presented to the users.
         
           4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
           Software shall not be used to promote, endorse or advertise any
           Modified Version, except to acknowledge the contribution(s) of the
           Copyright Holder(s) and the Author(s) or with their explicit written
           permission.
         
           5) The Font Software, modified or unmodified, in part or in whole,
           must be distributed entirely under this license, and must not be
           distributed under any other license. The requirement for fonts to
           remain under this license does not apply to any document created
           using the Font Software.
         
           TERMINATION
           This license becomes null and void if any of the above conditions are
           not met.
         
           DISCLAIMER
           THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
           OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
           COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
           INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
           DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
           FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
           OTHER DEALINGS IN THE FONT SOFTWARE.
         
         
         
         Name: BaKoMa Fonts
         Files: matplotlib/mpl-data/fonts/ttf/cm*.ttf matplotlib/mpl-data/fonts/afm/cm*.afm 
         Description: Computer Modern Fonts in PostScript Type 1 and TrueType font formats.
         License: BaKoMa Fonts Licence
                 BaKoMa Fonts Licence
                 --------------------
         
             This licence covers two font packs (known as BaKoMa Fonts Collection,
             which is available at `CTAN:fonts/cm/ps-type1/bakoma/'):
         
               1) BaKoMa-CM (1.1/12-Nov-94)
                  Computer Modern Fonts in PostScript Type 1 and TrueType font formats.
         
               2) BaKoMa-AMS (1.2/19-Jan-95)
                  AMS TeX fonts in PostScript Type 1 and TrueType font formats.
              
             Copyright (C) 1994, 1995, Basil K. Malyshev. All Rights Reserved.
         
             Permission to copy and distribute these fonts for any purpose is 
             hereby granted without fee, provided that the above copyright notice, 
             author statement and this permission notice appear in all copies of 
             these fonts and related documentation.
         
             Permission to modify and distribute modified fonts for any purpose is 
             hereby granted without fee, provided that the copyright notice, 
             author statement, this permission notice and location of original 
             fonts (http://www.ctan.org/tex-archive/fonts/cm/ps-type1/bakoma)
             appear in all copies of modified fonts and related documentation.
         
             Permission to use these fonts (embedding into PostScript, PDF, SVG
             and printing by using any software) is hereby granted without fee. 
             It is not required to provide any notices about using these fonts.
         
            Basil K. Malyshev
            INSTITUTE FOR HIGH ENERGY PHYSICS
            IHEP, OMVT
            Moscow Region
            142281 PROTVINO
            RUSSIA
         
            E-Mail:	bakoma@mail.ru
                 or	malyshev@mail.ihep.ru
         
         
         
         
         Name: ColorBrewer Color Schemes
         Files: lib/matplotlib/_cm.py
         Description: Color schemes from ColorBrewer
         License: Apache-2.0
           Apache-Style Software License for ColorBrewer software and ColorBrewer Color Schemes
         
           Copyright (c) 2002 Cynthia Brewer, Mark Harrower, and The Pennsylvania State University.
         
           Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
           You may obtain a copy of the License at
         
           http://www.apache.org/licenses/LICENSE-2.0
         
           Unless required by applicable law or agreed to in writing, software distributed
           under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
           CONDITIONS OF ANY KIND, either express or implied. See the License for the
           specific language governing permissions and limitations under the License.
         
         
         Name: Courier 10
         Files: matplotlib/tests/Courier10PitchBT-Bold.pfb
         Description: Courier 10 font, used in tests.
         License: Bitstream-Charter
           The Courier10PitchBT-Bold.pfb file is a Type-1 version of
           Courier 10 Pitch BT Bold by Bitstream, obtained from
           <https://ctan.org/tex-archive/fonts/courierten>. It is included
           here as test data only, but the following license applies.
         
         
           (c) Copyright 1989-1992, Bitstream Inc., Cambridge, MA.
         
           You are hereby granted permission under all Bitstream propriety rights
           to use, copy, modify, sublicense, sell, and redistribute the 4 Bitstream
           Charter (r) Type 1 outline fonts and the 4 Courier Type 1 outline fonts
           for any purpose and without restriction; provided, that this notice is
           left intact on all copies of such fonts and that Bitstream's trademark
           is acknowledged as shown below on all unmodified copies of the 4 Charter
           Type 1 fonts.
         
           BITSTREAM CHARTER is a registered trademark of Bitstream Inc.
         
         
         
         Name: JSXTools resize observer
         Files: 
         Description: Minimal polyfill for the ResizeObserver API
         License: CC0-1.0
           # CC0 1.0 Universal
         
           ## Statement of Purpose
         
           The laws of most jurisdictions throughout the world automatically confer
           exclusive Copyright and Related Rights (defined below) upon the creator and
           subsequent owner(s) (each and all, an “owner”) of an original work of
           authorship and/or a database (each, a “Work”).
         
           Certain owners wish to permanently relinquish those rights to a Work for the
           purpose of contributing to a commons of creative, cultural and scientific works
           (“Commons”) that the public can reliably and without fear of later claims of
           infringement build upon, modify, incorporate in other works, reuse and
           redistribute as freely as possible in any form whatsoever and for any purposes,
           including without limitation commercial purposes. These owners may contribute
           to the Commons to promote the ideal of a free culture and the further
           production of creative, cultural and scientific works, or to gain reputation or
           greater distribution for their Work in part through the use and efforts of
           others.
         
           For these and/or other purposes and motivations, and without any expectation of
           additional consideration or compensation, the person associating CC0 with a
           Work (the “Affirmer”), to the extent that he or she is an owner of Copyright
           and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and
           publicly distribute the Work under its terms, with knowledge of his or her
           Copyright and Related Rights in the Work and the meaning and intended legal
           effect of CC0 on those rights.
         
           1. Copyright and Related Rights. A Work made available under CC0 may be
              protected by copyright and related or neighboring rights (“Copyright and
              Related Rights”). Copyright and Related Rights include, but are not limited
              to, the following:
              1. the right to reproduce, adapt, distribute, perform, display, communicate,
                 and translate a Work;
              2. moral rights retained by the original author(s) and/or performer(s);
              3. publicity and privacy rights pertaining to a person’s image or likeness
                 depicted in a Work;
              4. rights protecting against unfair competition in regards to a Work,
                 subject to the limitations in paragraph 4(i), below;
              5. rights protecting the extraction, dissemination, use and reuse of data in
                 a Work;
              6. database rights (such as those arising under Directive 96/9/EC of the
                 European Parliament and of the Council of 11 March 1996 on the legal
                 protection of databases, and under any national implementation thereof,
                 including any amended or successor version of such directive); and
              7. other similar, equivalent or corresponding rights throughout the world
                 based on applicable law or treaty, and any national implementations
                 thereof.
         
           2. Waiver. To the greatest extent permitted by, but not in contravention of,
              applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
              unconditionally waives, abandons, and surrenders all of Affirmer’s Copyright
              and Related Rights and associated claims and causes of action, whether now
              known or unknown (including existing as well as future claims and causes of
              action), in the Work (i) in all territories worldwide, (ii) for the maximum
              duration provided by applicable law or treaty (including future time
              extensions), (iii) in any current or future medium and for any number of
              copies, and (iv) for any purpose whatsoever, including without limitation
              commercial, advertising or promotional purposes (the “Waiver”). Affirmer
              makes the Waiver for the benefit of each member of the public at large and
              to the detriment of Affirmer’s heirs and successors, fully intending that
              such Waiver shall not be subject to revocation, rescission, cancellation,
              termination, or any other legal or equitable action to disrupt the quiet
              enjoyment of the Work by the public as contemplated by Affirmer’s express
              Statement of Purpose.
         
           3. Public License Fallback. Should any part of the Waiver for any reason be
              judged legally invalid or ineffective under applicable law, then the Waiver
              shall be preserved to the maximum extent permitted taking into account
              Affirmer’s express Statement of Purpose. In addition, to the extent the
              Waiver is so judged Affirmer hereby grants to each affected person a
              royalty-free, non transferable, non sublicensable, non exclusive,
              irrevocable and unconditional license to exercise Affirmer’s Copyright and
              Related Rights in the Work (i) in all territories worldwide, (ii) for the
              maximum duration provided by applicable law or treaty (including future time
              extensions), (iii) in any current or future medium and for any number of
              copies, and (iv) for any purpose whatsoever, including without limitation
              commercial, advertising or promotional purposes (the “License”). The License
              shall be deemed effective as of the date CC0 was applied by Affirmer to the
              Work. Should any part of the License for any reason be judged legally
              invalid or ineffective under applicable law, such partial invalidity or
              ineffectiveness shall not invalidate the remainder of the License, and in
              such case Affirmer hereby affirms that he or she will not (i) exercise any
              of his or her remaining Copyright and Related Rights in the Work or (ii)
              assert any associated claims and causes of action with respect to the Work,
              in either case contrary to Affirmer’s express Statement of Purpose.
         
           4. Limitations and Disclaimers.
              1. No trademark or patent rights held by Affirmer are waived, abandoned,
                 surrendered, licensed or otherwise affected by this document.
              2. Affirmer offers the Work as-is and makes no representations or warranties
                 of any kind concerning the Work, express, implied, statutory or
                 otherwise, including without limitation warranties of title,
                 merchantability, fitness for a particular purpose, non infringement, or
                 the absence of latent or other defects, accuracy, or the present or
                 absence of errors, whether or not discoverable, all to the greatest
                 extent permissible under applicable law.
              3. Affirmer disclaims responsibility for clearing rights of other persons
                 that may apply to the Work or any use thereof, including without
                 limitation any person’s Copyright and Related Rights in the Work.
                 Further, Affirmer disclaims responsibility for obtaining any necessary
                 consents, permissions or other rights required for any use of the Work.
              4. Affirmer understands and acknowledges that Creative Commons is not a
                 party to this document and has no duty or obligation with respect to this
                 CC0 or use of the Work.
         
           For more information, please see
           http://creativecommons.org/publicdomain/zero/1.0/.
         
         
         Name: QHull
         Files: matplotlib/_qhull.*.so
         Description: Convex hull, Delaunay triangulation, Voronoi diagrams, Halfspace intersection
         License: Qhull
                               Qhull, Copyright (c) 1993-2020
                               
                                       C.B. Barber
                                      Arlington, MA 
                                     
                                          and
         
                  The National Science and Technology Research Center for
                   Computation and Visualization of Geometric Structures
                                   (The Geometry Center)
                                  University of Minnesota
         
                                  email: qhull@qhull.org
         
           This software includes Qhull from C.B. Barber and The Geometry Center.  
           Files derived from Qhull 1.0 are copyrighted by the Geometry Center.  The
           remaining files are copyrighted by C.B. Barber.  Qhull is free software 
           and may be obtained via http from www.qhull.org.  It may be freely copied, 
           modified, and redistributed under the following conditions:
         
           1. All copyright notices must remain intact in all files.
         
           2. A copy of this text file must be distributed along with any copies 
              of Qhull that you redistribute; this includes copies that you have 
              modified, or copies of programs or other software products that 
              include Qhull.
         
           3. If you modify Qhull, you must include a notice giving the
              name of the person performing the modification, the date of
              modification, and the reason for such modification.
         
           4. When distributing modified versions of Qhull, or other software 
              products that include Qhull, you must provide notice that the original 
              source code may be obtained as noted above.
         
           5. There is no warranty or other guarantee of fitness for Qhull, it is 
              provided solely "as is".  Bug reports or fixes may be sent to 
              qhull_bug@qhull.org; the authors may or may not act on them as 
              they desire.
         
         
         Name: Qt4 Editor
         Files: matplotlib/backends/qt_editor
         Description: Module creating PyQt4 form dialogs/layouts to edit various type of parameters
         License: MIT
           Module creating PyQt4 form dialogs/layouts to edit various type of parameters
         
         
           formlayout License Agreement (MIT License)
           ------------------------------------------
         
           Copyright (c) 2009 Pierre Raybaut
         
           Permission is hereby granted, free of charge, to any person
           obtaining a copy of this software and associated documentation
           files (the "Software"), to deal in the Software without
           restriction, including without limitation the rights to use,
           copy, modify, merge, publish, distribute, sublicense, and/or sell
           copies of the Software, and to permit persons to whom the
           Software is furnished to do so, subject to the following
           conditions:
         
           The above copyright notice and this permission notice shall be
           included in all copies or substantial portions of the Software.
         
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
           OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
           NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
           HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
           WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
           FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
           OTHER DEALINGS IN THE SOFTWARE.
           """
         
         
         Name: Solarized
         Files: matplotlib/mpl-data/stylelib/Solarize_Light2.mplstyle
         Description: Solarized color scheme/style
         License: MIT
           https://github.com/altercation/solarized/blob/master/LICENSE
           Copyright (c) 2011 Ethan Schoonover
         
           Permission is hereby granted, free of charge, to any person obtaining a copy
           of this software and associated documentation files (the "Software"), to deal
           in the Software without restriction, including without limitation the rights
           to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
           copies of the Software, and to permit persons to whom the Software is
           furnished to do so, subject to the following conditions:
         
           The above copyright notice and this permission notice shall be included in
           all copies or substantial portions of the Software.
         
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
           IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
           FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
           AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
           LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
           OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
           THE SOFTWARE.
         
         
         Name: Stix fonts
         Files: matplotlib/mpl-data/fonts/ttf/STIX*.ttf
         Description: STIX fonts
         License:
           TERMS AND CONDITIONS
         
              1. Permission is hereby granted, free of charge, to any person 
           obtaining a copy of the STIX Fonts-TM set accompanying this license 
           (collectively, the "Fonts") and the associated documentation files 
           (collectively with the Fonts, the "Font Software"), to reproduce and 
           distribute the Font Software, including the rights to use, copy, merge 
           and publish copies of the Font Software, and to permit persons to whom 
           the Font Software is furnished to do so same, subject to the following 
           terms and conditions (the "License").
         
              2. The following copyright and trademark notice and these Terms and 
           Conditions shall be included in all copies of one or more of the Font 
           typefaces and any derivative work created as permitted under this 
           License:
         
             Copyright (c) 2001-2005 by the STI Pub Companies, consisting of 
           the American Institute of Physics, the American Chemical Society, the 
           American Mathematical Society, the American Physical Society, Elsevier, 
           Inc., and The Institute of Electrical and Electronic Engineers, Inc. 
           Portions copyright (c) 1998-2003 by MicroPress, Inc. Portions copyright 
           (c) 1990 by Elsevier, Inc. All rights reserved. STIX Fonts-TM is a 
           trademark of The Institute of Electrical and Electronics Engineers, Inc.
         
              3. You may (a) convert the Fonts from one format to another (e.g., 
           from TrueType to PostScript), in which case the normal and reasonable 
           distortion that occurs during such conversion shall be permitted and (b) 
           embed or include a subset of the Fonts in a document for the purposes of 
           allowing users to read text in the document that utilizes the Fonts. In 
           each case, you may use the STIX Fonts-TM mark to designate the resulting 
           Fonts or subset of the Fonts.
         
              4. You may also (a) add glyphs or characters to the Fonts, or modify 
           the shape of existing glyphs, so long as the base set of glyphs is not 
           removed and (b) delete glyphs or characters from the Fonts, provided 
           that the resulting font set is distributed with the following 
           disclaimer: "This [name] font does not include all the Unicode points 
           covered in the STIX Fonts-TM set but may include others." In each case, 
           the name used to denote the resulting font set shall not include the 
           term "STIX" or any similar term.
         
              5. You may charge a fee in connection with the distribution of the 
           Font Software, provided that no copy of one or more of the individual 
           Font typefaces that form the STIX Fonts-TM set may be sold by itself.
         
              6. THE FONT SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY 
           KIND, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTIES 
           OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT 
           OF COPYRIGHT, PATENT, TRADEMARK OR OTHER RIGHT. IN NO EVENT SHALL 
           MICROPRESS OR ANY OF THE STI PUB COMPANIES BE LIABLE FOR ANY CLAIM, 
           DAMAGES OR OTHER LIABILITY, INCLUDING, BUT NOT LIMITED TO, ANY GENERAL, 
           SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES, WHETHER IN AN 
           ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM OR OUT OF THE USE OR 
           INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS IN THE FONT 
           SOFTWARE.
         
              7. Except as contained in the notice set forth in Section 2, the 
           names MicroPress Inc. and STI Pub Companies, as well as the names of the 
           companies/organizations that compose the STI Pub Companies, shall not be 
           used in advertising or otherwise to promote the sale, use or other 
           dealings in the Font Software without the prior written consent of the 
           respective company or organization.
         
              8. This License shall become null and void in the event of any 
           material breach of the Terms and Conditions herein by licensee.
         
              9. A substantial portion of the STIX Fonts set was developed by 
           MicroPress Inc. for the STI Pub Companies. To obtain additional 
           mathematical fonts, please contact MicroPress, Inc., 68-30 Harrow 
           Street, Forest Hills, NY 11375, USA - Phone: (718) 575-1816.
         
         
         Name: Yorick Colormaps
         Files: lib/matplotlib/_cm.py
         Description: Gist/Yorick colormaps
         License:
           BSD-style license for gist/yorick colormaps.
         
           Copyright:
         
             Copyright (c) 1996.  The Regents of the University of California.
                  All rights reserved.
         
           Permission to use, copy, modify, and distribute this software for any
           purpose without fee is hereby granted, provided that this entire
           notice is included in all copies of any software which is or includes
           a copy or modification of this software and in all copies of the
           supporting documentation for such software.
         
           This work was produced at the University of California, Lawrence
           Livermore National Laboratory under contract no. W-7405-ENG-48 between
           the U.S. Department of Energy and The Regents of the University of
           California for the operation of UC LLNL.
         
         
                       DISCLAIMER
         
           This software was prepared as an account of work sponsored by an
           agency of the United States Government.  Neither the United States
           Government nor the University of California nor any of their
           employees, makes any warranty, express or implied, or assumes any
           liability or responsibility for the accuracy, completeness, or
           usefulness of any information, apparatus, product, or process
           disclosed, or represents that its use would not infringe
           privately-owned rights.  Reference herein to any specific commercial
           products, process, or service by trade name, trademark, manufacturer,
           or otherwise, does not necessarily constitute or imply its
           endorsement, recommendation, or favoring by the United States
           Government or the University of California.  The views and opinions of
           authors expressed herein do not necessarily state or reflect those of
           the United States Government or the University of California, and
           shall not be used for advertising or product endorsement purposes.
         
         
                   AUTHOR
         
           David H. Munro wrote Yorick and Gist.  Berkeley Yacc (byacc) generated
           the Yorick parser.  The routines in Math are from LAPACK and FFTPACK;
           MathC contains C translations by David H. Munro.  The algorithms for
           Yorick's random number generator and several special functions in
           Yorick/include were taken from Numerical Recipes by Press, et. al.,
           although the Yorick implementations are unrelated to those in
           Numerical Recipes.  A small amount of code in Gist was adapted from
           the X11R4 release, copyright M.I.T. -- the complete copyright notice
           may be found in the (unused) file Gist/host.c.
         

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="numba-0-59-1"></a>
## Numba (0.59.1)

**Software Name:**  Numba  \
**Version:**  0.59.1  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/numba/

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 0.59.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** numba
- **PyPI version considered:** 0.59.1
- **Release upload time:** 2024-03-19T14:50:44.268920Z
- **Summary:** compiling Python code using LLVM
- **Homepage:** https://numba.pydata.org
- **Project URLs:**
  - Homepage: https://numba.pydata.org

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Unknown
- **License name:** BSD

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="einops-0-7-0"></a>
## einops (0.7.0)

**Software Name:**  einops  \
**Version:**  0.7.0  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/einops/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  arogozhnikov
- **Repository:**  arogozhnikov/einops
- **Description:**  Flexible and powerful tensor operations for readable and reliable code (for pytorch, jax, TF and others)
- **Stars:**  9321
- **Forks:**  390
- **Open Issues:**  34
- **Last Commit Date:**  2025-11-24T08:46:32Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 0.7.0)

- **Tag name:** v0.7.0
- **Release name:** V0.7.0: torch.compile, preserve axis identity, array api
- **Published at:** 2023-10-01T01:13:00Z
- **Release URL:** https://github.com/arogozhnikov/einops/releases/tag/v0.7.0
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** einops
- **PyPI version considered:** 0.7.0
- **Release upload time:** 2023-10-01T01:13:46.178588Z
- **Summary:** A new flavour of deep learning operations
- **Project URLs:**
  - Homepage: https://github.com/arogozhnikov/einops

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

<a id="e3nn-0-5-5"></a>
## e3nn (0.5.5)

**Software Name:**  e3nn  \
**Version:**  0.5.5  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/e3nn/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  e3nn
- **Repository:**  e3nn/e3nn
- **Description:**  A modular framework for neural networks with Euclidean symmetry
- **Stars:**  1191
- **Forks:**  173
- **Open Issues:**  31
- **Last Commit Date:**  2025-12-18T01:51:01Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 0.5.5)

- **Tag name:** 0.5.5
- **Release name:** 0.5.5
- **Published at:** 2025-02-02T23:07:11Z
- **Release URL:** https://github.com/e3nn/e3nn/releases/tag/0.5.5
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** e3nn
- **PyPI version considered:** 0.5.5
- **Release upload time:** 2025-02-02T23:07:30.536043Z
- **Summary:** Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors.
- **Project URLs:**
  - changelog: https://github.com/e3nn/e3nn/blob/main/.github/CHANGELOG.md
  - documentation: https://docs.e3nn.org/
  - homepage: https://e3nn.org
  - repository: https://github.com/e3nn/e3nn.git

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** NOASSERTION
- **License name:** Other

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="ase-3-23-0"></a>
## ASE (3.23.0)

**Software Name:**  ASE  \
**Version:**  3.23.0  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/ase/

#### 3.2 GitHub Repository Metadata

- No GitHub repository metadata found (no GitHub URL or API error).

#### 3.3 GitHub Release (version 3.23.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** ase
- **PyPI version considered:** 3.23.0
- **Release upload time:** 2024-05-31T20:17:29.520625Z
- **Summary:** Atomic Simulation Environment
- **Project URLs:**
  - Homepage: https://ase-lib.org/
  - Issues: https://gitlab.com/ase/ase/issues/
  - Repository: https://gitlab.com/ase/ase.git

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Unknown
- **License name:** Unknown

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="rdkit-2023-9-5"></a>
## RDKit (2023.9.5)

**Software Name:**  RDKit  \
**Version:**  2023.9.5  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/rdkit/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  kuelumbus
- **Repository:**  N/A
- **Description:**  N/A
- **Stars:**  N/A
- **Forks:**  N/A
- **Open Issues:**  N/A
- **Last Commit Date:**  N/A
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2023.9.5)

- github_releases_request_failed: 404 Client Error: Not Found for url: https://api.github.com/repos/kuelumbus/rdkit-pyp/releases?per_page=100

#### 3.4 PyPI Metadata

- **PyPI package name:** rdkit
- **PyPI version considered:** 2023.9.5
- **Release upload time:** 2024-02-14T09:19:29.070821Z
- **Summary:** A collection of chemoinformatics and machine-learning software written in C++ and Python
- **Homepage:** https://github.com/kuelumbus/rdkit-pypi
- **Project URLs:**
  - Homepage: https://github.com/kuelumbus/rdkit-pypi
  - RDKit: http://rdkit.org/
  - RDKit on Github: https://github.com/rdkit/rdkit

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Unknown
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

---

<a id="deepchem-2-8-0"></a>
## DeepChem (2.8.0)

**Software Name:**  DeepChem  \
**Version:**  2.8.0  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/deepchem/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  deepchem
- **Repository:**  deepchem/deepchem
- **Description:**  Democratizing Deep-Learning for Drug Discovery, Quantum Chemistry, Materials Science and Biology
- **Stars:**  6409
- **Forks:**  1966
- **Open Issues:**  858
- **Last Commit Date:**  2025-12-17T19:53:46Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 2.8.0)

- **Tag name:** 2.8.0
- **Release name:** 2.8.0 Initial Release
- **Published at:** 2024-04-03T16:21:23Z
- **Release URL:** https://github.com/deepchem/deepchem/releases/tag/2.8.0
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** deepchem
- **PyPI version considered:** 2.8.0
- **Release upload time:** 2024-04-02T02:20:39.079984Z
- **Summary:** Deep learning models for drug discovery,         quantum chemistry, and the life sciences.
- **Homepage:** https://github.com/deepchem/deepchem
- **Project URLs:**
  - Documentation: https://deepchem.readthedocs.io/en/latest/
  - Homepage: https://github.com/deepchem/deepchem
  - Source: https://github.com/deepchem/deepchem

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

<a id="transformers-4-51-3"></a>
## Transformers (4.51.3)

**Software Name:**  Transformers  \
**Version:**  4.51.3  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/transformers/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  huggingface
- **Repository:**  huggingface/transformers
- **Description:**  🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 
- **Stars:**  154005
- **Forks:**  31478
- **Open Issues:**  2143
- **Last Commit Date:**  2025-12-18T10:57:05Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 4.51.3)

- **Tag name:** v4.51.3
- **Release name:** Patch release v4.51.3
- **Published at:** 2025-04-14T15:51:52Z
- **Release URL:** https://github.com/huggingface/transformers/releases/tag/v4.51.3
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** transformers
- **PyPI version considered:** 4.51.3
- **Release upload time:** 2025-04-14T08:13:43.023193Z
- **Summary:** State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
- **Homepage:** https://github.com/huggingface/transformers
- **Project URLs:**
  - Homepage: https://github.com/huggingface/transformers

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** Apache-2.0
- **License name:** Apache License 2.0

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Yes |
| Can be used for commercial use?    | Yes |
| Modification allowed?              | Yes |
| Redistribution allowed?            | Yes |
| Attribution required?              | Yes |
| Copyleft obligations?              | No |

---

<a id="lmdb-py-lmdb-1-4-1"></a>
## lmdb (py-lmdb) (1.4.1)

**Software Name:**  lmdb (py-lmdb)  \
**Version:**  1.4.1  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/lmdb/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  jnwatson
- **Repository:**  jnwatson/py-lmdb
- **Description:**  Universal Python binding for the LMDB 'Lightning' Database
- **Stars:**  726
- **Forks:**  114
- **Open Issues:**  25
- **Last Commit Date:**  2025-11-17T02:28:22Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 1.4.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** lmdb
- **PyPI version considered:** 1.4.1
- **Release upload time:** 2023-04-06T14:53:19.915455Z
- **Summary:** Universal Python binding for the LMDB 'Lightning' Database
- **Homepage:** http://github.com/jnwatson/py-lmdb/
- **Project URLs:**
  - Homepage: http://github.com/jnwatson/py-lmdb/

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** NOASSERTION
- **License name:** Other

#### 4.2 Permissibility Summary

| Question                           | Answer   |
|------------------------------------|----------|
| Can be used for academic purposes? | Unknown |
| Can be used for commercial use?    | Unknown |
| Modification allowed?              | Unknown |
| Redistribution allowed?            | Unknown |
| Attribution required?              | Unknown |
| Copyleft obligations?              | Unknown |

---

<a id="weights-biases-wandb-0-16-5"></a>
## Weights & Biases (wandb) (0.16.5)

**Software Name:**  Weights & Biases (wandb)  \
**Version:**  0.16.5  \
**Environment / Image:**  Python package (PyPI)

---

### 1. Summary

> TODO: Add project-specific summary describing how this package is used in the workload.

---

### 2. SBOM Extract (from Trivy)

- **SBOM / Trivy log file:** `stack.log`
- **Exists:** Yes
- **Size:** 2099638 bytes
- **Last modified:** 2025-12-18 10:39:14 UTC

---

### 3. Software Source / Provenance

#### 3.1 Source Channel

- **PyPI:** https://pypi.org/project/wandb/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  wandb
- **Repository:**  wandb/wandb
- **Description:**  The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.
- **Stars:**  10636
- **Forks:**  800
- **Open Issues:**  796
- **Last Commit Date:**  2025-12-17T18:56:54Z
- **Activity Health:**  Active

#### 3.3 GitHub Release (version 0.16.5)

- **Tag name:** v0.16.5
- **Release name:** v0.16.5
- **Published at:** 2024-03-25T19:03:45Z
- **Release URL:** https://github.com/wandb/wandb/releases/tag/v0.16.5
- **Draft:** No
- **Prerelease:** No

#### 3.4 PyPI Metadata

- **PyPI package name:** wandb
- **PyPI version considered:** 0.16.5
- **Release upload time:** 2024-03-25T19:01:38.043415Z
- **Summary:** A CLI and library for interacting with the Weights & Biases API.
- **Project URLs:**
  - Bug Reports: https://github.com/wandb/wandb/issues
  - Documentation: https://docs.wandb.ai/
  - Source: https://github.com/wandb/wandb

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** MIT
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

---

