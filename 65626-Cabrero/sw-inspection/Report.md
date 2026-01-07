# Software Stack Inspection – Undefined

- **Snapshot date:** 2026-01-06
- **Generated at:** 2026-01-06 14:39:40 UTC

## Agenda

- [torch 2.0.1](#torch-2-0-1)
- [torchvision 0.15.2](#torchvision-0-15-2)
- [torchaudio 2.0.2](#torchaudio-2-0-2)
- [torchmetrics 0.9.3](#torchmetrics-0-9-3)
- [pytorch-lightning 2.1.3](#pytorch-lightning-2-1-3)
- [gradio 4.43](#gradio-4-43)
- [gradio_client 1.13.0](#gradio-client-1-13-0)
- [transformers 4.28.0](#transformers-4-28-0)
- [scikit-learn 1.4.0](#scikit-learn-1-4-0)
- [tabulate 0.9.0](#tabulate-0-9-0)
- [biopython 1.83](#biopython-1-83)
- [easydict 1.13](#easydict-1-13)
- [lmdb 1.4.1](#lmdb-1-4-1)
- [multiprocess 0.70.18](#multiprocess-0-70-18)
- [pyspellchecker 0.8.2](#pyspellchecker-0-8-2)

---

<a id="torch-2-0-1"></a>
## torch (2.0.1)

**Software Name:**  torch  \
**Version:**  2.0.1  \
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

- **GitHub:** https://github.com/pytorch/pytorch

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  96377
- **Forks:**  26429
- **Open Issues:**  17912
- **Last Commit Date:**  2026-01-06T10:53:23Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.0.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.0.1
- **Release upload time:** N/A
- **Summary:** 

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD-style license

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

- **ARM/aarch64 build available?**: source build only; no official CUDA wheels
- **ARM build source / URL:** -
- **Notes:** PyTorch 2.0.1 provides CUDA 11.7/11.8 wheels for Linux x86-64 only.

---

<a id="torchvision-0-15-2"></a>
## torchvision (0.15.2)

**Software Name:**  torchvision  \
**Version:**  0.15.2  \
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

- **PyPI:** https://pypi.org/project/torchvision/0.15.2/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/vision
- **Description:**  Datasets, Transforms and Models specific to Computer Vision
- **Stars:**  17430
- **Forks:**  7195
- **Open Issues:**  1179
- **Last Commit Date:**  2026-01-06T10:09:52Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.15.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.15.2
- **Release upload time:** N/A
- **Summary:** image and video datasets and models for torch deep learning
- **Homepage:** https://github.com/pytorch/vision
- **Project URLs:**
  - Homepage: https://github.com/pytorch/vision

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD-style license

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/66/e0/cd847d4d22be88a71d5d65f5809342e7ea7ded62230e7bde7420a2105e51/torchvision-0.15.2-cp311-cp311-manylinux2014_aarch64.whl
- **Notes:** Available wheel on PyPI

---

<a id="torchaudio-2-0-2"></a>
## torchaudio (2.0.2)

**Software Name:**  torchaudio  \
**Version:**  2.0.2  \
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

- **PyPI:** https://pypi.org/project/torchaudio/2.0.2/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/audio
- **Description:**  Data manipulation and transformation for audio signal processing, powered by PyTorch
- **Stars:**  2808
- **Forks:**  754
- **Open Issues:**  314
- **Last Commit Date:**  2026-01-06T08:58:27Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.0.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.0.2
- **Release upload time:** N/A
- **Summary:** An audio package for PyTorch
- **Homepage:** https://github.com/pytorch/audio
- **Project URLs:**
  - Homepage: https://github.com/pytorch/audio

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** BSD-style license

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
- **ARM build source / URL:** https://files.pythonhosted.org/packages/dc/9c/4d2d65618034ed9833e8997c74b1bf77e3a73c4be0a2b2f80bd9f3c5988b/torchaudio-2.0.2-cp311-cp311-manylinux2014_aarch64.whl
- **Notes:** Available wheel on PyPI

---

<a id="torchmetrics-0-9-3"></a>
## torchmetrics (0.9.3)

**Software Name:**  torchmetrics  \
**Version:**  0.9.3  \
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

- **PyPI:** https://pypi.org/project/torchmetrics/0.9.3/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  Lightning-AI/torchmetrics
- **Description:**  Machine learning metrics for distributed, scalable PyTorch applications.
- **Stars:**  2390
- **Forks:**  470
- **Open Issues:**  123
- **Last Commit Date:**  2025-12-17T23:16:59Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.9.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.9.3
- **Release upload time:** N/A
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

- **SPDX ID:** N/A
- **License name:** BSD-style license

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
- **ARM build source / URL:** -
- **Notes:** torchmetrics ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="pytorch-lightning-2-1-3"></a>
## pytorch-lightning (2.1.3)

**Software Name:**  pytorch-lightning  \
**Version:**  2.1.3  \
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

- **GitHub:** https://github.com/Lightning-AI/pytorch-lightning

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  Lightning-AI/pytorch-lightning
- **Description:**  Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes.
- **Stars:**  30677
- **Forks:**  3640
- **Open Issues:**  943
- **Last Commit Date:**  2025-12-22T12:41:14Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.1.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.1.3
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

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/pytorch-lightning/2.1.3
- **Notes:** PyTorch Lightning ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="gradio-4-43"></a>
## gradio (4.43)

**Software Name:**  gradio  \
**Version:**  4.43  \
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

- **GitHub:** https://github.com/gradio-app/gradio

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  gradio-app/gradio
- **Description:**  Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work!
- **Stars:**  41211
- **Forks:**  3221
- **Open Issues:**  466
- **Last Commit Date:**  2026-01-06T11:28:26Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 4.43)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 6.2.0
- **Release upload time:** N/A
- **Summary:** Python library for easily interacting with trained machine learning models
- **Project URLs:**
  - Homepage: https://github.com/gradio-app/gradio

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
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

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/gradio/4.43.0
- **Notes:** Gradio ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="gradio-client-1-13-0"></a>
## gradio_client (1.13.0)

**Software Name:**  gradio_client  \
**Version:**  1.13.0  \
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

- **PyPI:** https://pypi.org/project/gradio-client/1.13.0/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  gradio-app/gradio
- **Description:**  Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work!
- **Stars:**  41211
- **Forks:**  3221
- **Open Issues:**  466
- **Last Commit Date:**  2026-01-06T11:28:26Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.13.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.13.0
- **Release upload time:** N/A
- **Summary:** Python library for easily interacting with trained machine learning models
- **Project URLs:**
  - Homepage: https://github.com/gradio-app/gradio

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
- **ARM build source / URL:** https://pypi.org/project/gradio-client/1.13.0
- **Notes:** gradio-client ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available

---

<a id="transformers-4-28-0"></a>
## transformers (4.28.0)

**Software Name:**  transformers  \
**Version:**  4.28.0  \
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

- **GitHub:** https://github.com/huggingface/transformers

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  huggingface/transformers
- **Description:**  🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 
- **Stars:**  154660
- **Forks:**  31639
- **Open Issues:**  2162
- **Last Commit Date:**  2026-01-06T13:31:30Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 4.28.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 4.28.0
- **Release upload time:** N/A
- **Summary:** State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
- **Homepage:** https://github.com/huggingface/transformers
- **Project URLs:**
  - Homepage: https://github.com/huggingface/transformers

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
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

### 5. Architecture / ARM / AArch64 Support

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/transformers/4.28.0/#files
- **Notes:** Transformers ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="scikit-learn-1-4-0"></a>
## scikit-learn (1.4.0)

**Software Name:**  scikit-learn  \
**Version:**  1.4.0  \
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

- **GitHub:** https://github.com/scikit-learn/scikit-learn

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  scikit-learn/scikit-learn
- **Description:**  scikit-learn: machine learning in Python
- **Stars:**  64498
- **Forks:**  26574
- **Open Issues:**  2116
- **Last Commit Date:**  2026-01-06T14:26:20Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.4.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.4.0
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
- **License name:** BSD-3-Clause license

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
- **ARM build source / URL:** https://pypi.org/project/scikit-learn/1.4.0/#files
- **Notes:** aarch64 wheels available on PyPI

---

<a id="tabulate-0-9-0"></a>
## tabulate (0.9.0)

**Software Name:**  tabulate  \
**Version:**  0.9.0  \
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

- **PyPI:** https://pypi.org/project/tabulate/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  astanin/python-tabulate
- **Description:**  Pretty-print tabular data in Python, a library and a command-line utility. Repository migrated from bitbucket.org/astanin/python-tabulate.
- **Stars:**  2500
- **Forks:**  178
- **Open Issues:**  129
- **Last Commit Date:**  2025-07-23T18:54:26Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.9.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.9.0
- **Release upload time:** N/A
- **Summary:** Pretty-print tabular data
- **Project URLs:**
  - Homepage: https://github.com/astanin/python-tabulate

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

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/tabulate
- **Notes:** Tabulate ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="biopython-1-83"></a>
## biopython (1.83)

**Software Name:**  biopython  \
**Version:**  1.83  \
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

- **GitHub:** https://github.com/biopython/biopython

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  biopython/biopython
- **Description:**  Official git repository for Biopython (originally converted from CVS)
- **Stars:**  4855
- **Forks:**  1855
- **Open Issues:**  572
- **Last Commit Date:**  2025-12-26T06:23:00Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.83)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.83
- **Release upload time:** N/A
- **Summary:** Freely available tools for computational molecular biology.
- **Homepage:** https://biopython.org/
- **Project URLs:**
  - Documentation: https://biopython.org/wiki/Documentation
  - Homepage: https://biopython.org/
  - Source: https://github.com/biopython/biopython/
  - Tracker: https://github.com/biopython/biopython/issues

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

- **ARM/aarch64 build available?**: No
- **ARM build source / URL:** -
- **Notes:** No precompiled Linux aarch64 wheel - will need build from source

---

<a id="easydict-1-13"></a>
## easydict (1.13)

**Software Name:**  easydict  \
**Version:**  1.13  \
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

- **GitHub:** https://github.com/makinacorpus/easydict

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  makinacorpus/easydict
- **Description:**  Access dict values as attributes (works recursively)
- **Stars:**  311
- **Forks:**  48
- **Open Issues:**  23
- **Last Commit Date:**  2024-03-04T12:03:03Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.13)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 1.13
- **Release upload time:** N/A
- **Summary:** Access dict values as attributes (works recursively).
- **Homepage:** https://github.com/makinacorpus/easydict
- **Project URLs:**
  - Download: http://pypi.python.org/pypi/easydict/
  - Homepage: https://github.com/makinacorpus/easydict

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** LGPL-3.0 license

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

- **ARM/aarch64 build available?**: Yes (pure Python / py3-none-any wheels)
- **ARM build source / URL:** https://pypi.org/project/easydict/#files
- **Notes:** easydict ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="lmdb-1-4-1"></a>
## lmdb (1.4.1)

**Software Name:**  lmdb  \
**Version:**  1.4.1  \
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

- **GitHub:** https://github.com/jnwatson/py-lmdb/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  jnwatson/py-lmdb
- **Description:**  Universal Python binding for the LMDB 'Lightning' Database
- **Stars:**  730
- **Forks:**  114
- **Open Issues:**  25
- **Last Commit Date:**  2025-11-17T02:28:22Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 1.4.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- No PyPI metadata (no PyPI URL or API error).

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** The OpenLDAP Public License

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
- **ARM build source / URL:** https://pypi.org/project/lmdb/1.4.1/#files
- **Notes:** manylinux aarch64 wheel available on PyPI

---

<a id="multiprocess-0-70-18"></a>
## multiprocess (0.70.18)

**Software Name:**  multiprocess  \
**Version:**  0.70.18  \
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

- **GitHub:** https://github.com/uqfoundation/multiprocess

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  uqfoundation/multiprocess
- **Description:**  better multiprocessing and multithreading in Python
- **Stars:**  689
- **Forks:**  69
- **Open Issues:**  42
- **Last Commit Date:**  2025-12-31T03:09:47Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.70.18)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.70.18
- **Release upload time:** N/A
- **Summary:** better multiprocessing and multithreading in Python
- **Homepage:** https://github.com/uqfoundation/multiprocess
- **Project URLs:**
  - Bug Tracker: https://github.com/uqfoundation/multiprocess/issues
  - Documentation: http://multiprocess.rtfd.io
  - Download: https://pypi.org/project/multiprocess/#files
  - Homepage: https://github.com/uqfoundation/multiprocess
  - Source Code: https://github.com/uqfoundation/multiprocess

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** N.A.

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
- **Notes:** No wheel available, but can build from source

---

<a id="pyspellchecker-0-8-2"></a>
## pyspellchecker (0.8.2)

**Software Name:**  pyspellchecker  \
**Version:**  0.8.2  \
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

- **GitHub:** https://github.com/barrust/pyspellchecker

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  barrust/pyspellchecker
- **Description:**  Pure Python Spell Checking http://pyspellchecker.readthedocs.io/en/latest/
- **Stars:**  768
- **Forks:**  161
- **Open Issues:**  7
- **Last Commit Date:**  2025-11-30T00:17:10Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.8.2)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.8.2
- **Release upload time:** N/A
- **Summary:** Pure python spell checker based on work by Peter Norvig
- **Project URLs:**
  - bug-tracker: https://github.com/barrust/pyspellchecker/issues
  - documentation: https://pyspellchecker.readthedocs.io/
  - homepage: https://github.com/barrust/pyspellchecker

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** MIT license

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
- **ARM build source / URL:** https://pypi.org/project/pyspellchecker/0.8.2/#files
- **Notes:** pyspellchecker ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

