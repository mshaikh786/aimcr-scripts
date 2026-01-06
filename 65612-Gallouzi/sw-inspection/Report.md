# Software Stack Inspection – Yotta Infinite for Life Science

- **Snapshot date:** 2026-01-06
- **Generated at:** 2026-01-06 12:54:35 UTC

## Agenda

- [tqdm 4.67.1](#tqdm-4-67-1)
- [torch 2.9.1](#torch-2-9-1)
- [transformers 4.57.3](#transformers-4-57-3)
- [wandb 0.23.1](#wandb-0-23-1)
- [peft 0.7.0](#peft-0-7-0)
- [neo4j 6.03](#neo4j-6-03)
- [trl 0.25.1](#trl-0-25-1)

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
- **Stars:**  30833
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
- **License name:** MPL-2.0 AND MIT

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

<a id="torch-2-9-1"></a>
## torch (2.9.1)

**Software Name:**  torch  \
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

- **PyPI:** https://pypi.org/project/torch/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  pytorch/pytorch
- **Description:**  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- **Stars:**  96379
- **Forks:**  26428
- **Open Issues:**  17907
- **Last Commit Date:**  2026-01-06T12:01:39Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 2.9.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 2.9.1
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

- **ARM/aarch64 build available?**: Yes (official Linux aarch64 wheels and vendor ARM GPU containers)
- **ARM build source / URL:** PyPI aarch64 wheels: https://pypi.org/project/torch/#files ; see also NGC containers
- **Notes:** PyTorch provides official manylinux aarch64 binaries and ARM support for NVIDIA platforms (e.g. Jetson / GH200). Still recommended to validate on the specific Shaheen III software stack and CUDA/toolchain versions.

---

<a id="transformers-4-57-3"></a>
## transformers (4.57.3)

**Software Name:**  transformers  \
**Version:**  4.57.3  \
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

- **PyPI:** https://pypi.org/project/transformers/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  huggingface/transformers
- **Description:**  🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 
- **Stars:**  154657
- **Forks:**  31639
- **Open Issues:**  2161
- **Last Commit Date:**  2026-01-06T12:51:18Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 4.57.3)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 4.57.3
- **Release upload time:** N/A
- **Summary:** State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
- **Homepage:** https://github.com/huggingface/transformers
- **Project URLs:**
  - Homepage: https://github.com/huggingface/transformers

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Apache 2.0 License

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
- **ARM build source / URL:** https://pypi.org/project/transformers
- **Notes:** Transformers ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="wandb-0-23-1"></a>
## wandb (0.23.1)

**Software Name:**  wandb  \
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
- **Stars:**  10702
- **Forks:**  805
- **Open Issues:**  804
- **Last Commit Date:**  2026-01-06T01:06:15Z
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
- **License name:** MIT License (MIT License)

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
- **Notes:** ARM64 wheel available on PyPI

---

<a id="peft-0-7-0"></a>
## peft (0.7.0)

**Software Name:**  peft  \
**Version:**  0.7.0  \
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

- **PyPI:** https://pypi.org/project/peft/0.7.0/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  huggingface/peft
- **Description:**  🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning.
- **Stars:**  20403
- **Forks:**  2148
- **Open Issues:**  56
- **Last Commit Date:**  2025-12-18T10:52:52Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.7.0)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.7.0
- **Release upload time:** N/A
- **Summary:** Parameter-Efficient Fine-Tuning (PEFT)
- **Homepage:** https://github.com/huggingface/peft
- **Project URLs:**
  - Homepage: https://github.com/huggingface/peft

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Apache Software License (Apache)

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
- **ARM build source / URL:** https://pypi.org/project/peft/
- **Notes:** Peft ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="neo4j-6-03"></a>
## neo4j (6.03)

**Software Name:**  neo4j  \
**Version:**  6.03  \
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

- **PyPI:** https://pypi.org/project/neo4j/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  neo4j/neo4j-python-driver
- **Description:**  Neo4j Bolt driver for Python
- **Stars:**  1015
- **Forks:**  204
- **Open Issues:**  2
- **Last Commit Date:**  2025-12-15T13:09:46Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 6.03)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 6.0.3
- **Release upload time:** N/A
- **Summary:** Neo4j Bolt driver for Python
- **Project URLs:**
  - Changelog: https://github.com/neo4j/neo4j-python-driver/wiki
  - Discord: https://discord.com/invite/neo4j
  - Docs (API Reference): https://neo4j.com/docs/api/python-driver/current/
  - Docs (Manual): https://neo4j.com/docs/python-manual/current/
  - Forum: https://community.neo4j.com/c/drivers-stacks/python/
  - Homepage: https://neo4j.com/
  - Issue Tracker: https://github.com/neo4j/neo4j-python-driver/issues
  - Repository: https://github.com/neo4j/neo4j-python-driver

---

### 4. License Analysis

#### 4.1 License Type

- **SPDX ID:** N/A
- **License name:** Neo4j

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
- **ARM build source / URL:** https://pypi.org/project/neo4j/
- **Notes:** Neo4j ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

<a id="trl-0-25-1"></a>
## trl (0.25.1)

**Software Name:**  trl  \
**Version:**  0.25.1  \
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

- **PyPI:** https://pypi.org/project/trl/

#### 3.2 GitHub Repository Metadata

- **Owner / Organization:**  N/A
- **Repository:**  huggingface/trl
- **Description:**  Train transformer language models with reinforcement learning.
- **Stars:**  16884
- **Forks:**  2407
- **Open Issues:**  631
- **Last Commit Date:**  2026-01-06T07:45:38Z
- **Activity Health:**  Unknown

#### 3.3 GitHub Release (version 0.25.1)

- No matching GitHub release found.

#### 3.4 PyPI Metadata

- **PyPI package name:** N/A
- **PyPI version considered:** 0.25.1
- **Release upload time:** N/A
- **Summary:** Train transformer language models with reinforcement learning.
- **Project URLs:**
  - Homepage: https://github.com/huggingface/trl

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
- **ARM build source / URL:** https://pypi.org/project/trl/
- **Notes:** trl ships as a pure Python package (`py3-none-any` wheels on PyPI), so it is architecture-independent and runs on ARM/aarch64 as long as the Python ecosystem dependencies are available.

---

