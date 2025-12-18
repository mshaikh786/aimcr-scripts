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
- **License name:** Custom / see upstream license text

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

