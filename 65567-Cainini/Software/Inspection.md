# Software Inspection Dossier

## Agenda

1. [multiweave-collaboration-framework](#multiweave-collaboration-framework)
2. [vLLM](#vllm)
3. [PyTorch](#pytorch)

## multiweave-collaboration-framework
**Software Name:**  multiweave-collaboration-framework  \
**Version:**  0.x 

---

### 1. Summary

Efficient batched inference for large language 
models, enabling high throughput on GH200 
GPUs, and reducing per‑query overhead compared 
to naïve inference. 

---


### 2. Software Source / Provenance

#### 3.1 Source Channel
- **Ownership / Licensing:**  KAUST (to be released 
under an open‑source license, e.g., MIT or 
Apache‑2.0, where possible
- **Exact URL:**  TBD

---

## PyTorch

**Software Name:**  PyTorch \
**Version:**   2.8 \
**Environment / Image:**   Nvidia NGC Image: nvcr.io/nvidia/pytorch:25.12-py3

---

### 1. Summary

PyTorch is an open-source deep learning framework developed and maintained by Meta (Facebook AI Research) and the 
PyTorch open-source community. It provides tensor computation with strong GPU acceleration, automatic differentiation, 
and a flexible programming model widely adopted for research, prototyping, and production AI systems.

---


### 2. Software Source / Provenance

#### 2.1 Source Channel
- **Distribution channel:** 
  - PyPI (pip wheels)  
  - Conda (conda-forge, pytorch channels)  
  - GitHub (source code)
- **Exact URL:** https://github.com/pytorch/pytorch

#### 2.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  PyTorch Foundation (Linux Foundation) / Meta  
- **Last Commit Date:**  Today
- **Number of Stars:**  96K
- **Number of Issues (Open/Closed):** 5K+ 
- **Number of PRs (Open/Closed):**  1.7K
- **Total Commits:**  97K
- **Activity Health:** Active

#### 2.3 Package Release History
- **Latest release date:**  Nov 12
- **Frequency of releases:** monthly

---

### 3. License Analysis

#### 3.1 License Type
- **License:** BSD 3-Clause License  
- **License URL:** https://github.com/pytorch/pytorch/blob/main/LICENSE

#### 3.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |
---

## vLLM
**Software Name:**    vLLM \
**Version:**    0.13 \
**Environment / Image:** Nvidia NGC Image: nvcr.io/nvidia/vllm:25.12.post1-py3

---

### 1. Summary

vLLM is a fast and easy-to-use library for LLM inference and serving. The NVIDIA vLLM NGC Container is optimized for GPU acceleration, and contains a validated set of libraries that enable and optimize GPU performance.

---

### 2. Software Source / Provenance

#### 2.1 Source Channel
- **Distribution channel:** 
  - GitHub (source code)
- **Exact URL:**   - https://github.com/vllm-project/vllm

#### 2.2 GitHub Repository Metadata (as of 4/1/2026)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  vllm-project
- **Last Commit Date:**  Today
- **Number of Stars:**  66.8K
- **Number of Issues (Open/Closed):** 1.8K  
- **Number of PRs (Open/Closed):**  1.3K
- **Total Commits:**  12.6K
- **Activity Health:** Active

#### 2.3 Package Release History
- **Latest release date:**  2 weeks ago
- **Frequency of releases:** Biweekly

---

### 3. License Analysis

#### 3.1 License Type
- **License:**  Apache-2.0 license 
- **License URL:** https://github.com/vllm-project/vllm?tab=Apache-2.0-1-ov-file#

#### 3.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |