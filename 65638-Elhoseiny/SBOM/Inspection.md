# Software Inspection Dossier

## Agenda

1. [Alibaba ROLL](#alibaba-roll)
2. [RLinf](#rlinf)
3. [DeepSpeed](#deepspeed)
4. [Hugging Face Accelerate](#hugging-face-accelerate)
5. [PyTorch](#pytorch)
6. [Hugging Face Transformers](#hugging-face-transformers)
7. [FlashAttention](#flash-attention)

## Alibaba ROLL
**Software Name:**  Alibaba ROLL  \
**Version:**  0.1.1 \
**Environment / Image:** roll-registry.cn-hangzhou.cr.aliyuncs.com/roll/pytorch:nvcr-25.06-py3-torch280-vllm0102  

---

## 1. Summary
ROLL (Reinforcement Learning Operations Lifecycle) is an open-source framework by Alibaba DAMO Academy designed to 
streamline the development, training, and deployment of RL-based and LLM-enhanced systems. It provides distributed 
training support, RL pipelines, multi-agent orchestration, and integration with modern AI toolchains such as PyTorch, 
vLLM, Triton, and other inference accelerators. \
In this environment, ROLL is included as part of a larger AI container image containing PyTorch 2.8.0, vLLM 0.10.2, and 
other inference/training frameworks. The software is used for high-performance RL workflows and agent training with 
distributed GPU support.
---

## 2. SBOM Extract (from Trivy)
[View SBOM log](roll.log)

---

## 3. Software Source / Provenance

### 3.1 Source Channel
- **Distribution channel:** GitHub (open-source repository)  
- **Exact URL:**  https://github.com/alibaba/ROLL

### 3.2 GitHub Repository Metadata (as of December 16th, 2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  Alibaba DAMO Academy
- **Last Commit Date:**  Today
- **Number of Stars:**  2.5K
- **Number of Issues (Open/Closed):**  61
- **Number of PRs (Open/Closed):**  6
- **Total Commits:**  368
- **Activity Health:** Active

### 3.3 Package Release History
- **Latest release date:**  Second week of December 2025
- **Frequency of releases:** monthly

---

## 4. License Analysis

### 4.1 License Type
- **License:** Apache 2.0
- **License URL:**  https://github.com/alibaba/ROLL/blob/main/LICENSE

### 4.2 Permissibility Summary
| Question                           | Answer                                |
|------------------------------------|---------------------------------------|
| Can be used for academic purposes? | Yes                                   |
| Can be used for commercial use?    | Yes                                   |
| Modification allowed?              | Yes                                   |



---

## RLinf
**Software Name:**  RLinf \
**Version:** 0.1
**Environment / Image:** rlinf/rlinf:agentic-rlinf0.1-torch2.6.0-openvla-openvlaoft-pi0   

---

## 1. Summary

RLinf is an open-source, flexible and scalable reinforcement learning (RL) infrastructure designed for post-training 
optimization of **foundation models** (including LLMs, VLMs, and VLAs) via RL algorithms. It provides a backbone for 
continuous fine-tuning and scalable RL training workflows, supporting a variety of training modes, large-scale 
distributed configurations, and integrations with model backends and simulators.
---

## 2. SBOM Extract (from Trivy)
[View SBOM log](rlinf.log)

---

## 3. Software Source / Provenance

### 3.1 Source Channel
- **Distribution channel:** GitHub (open-source repository)  \
- **Exact URL:** https://github.com/RLinf/RLinf

### 3.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  RLinf organization on GitHub
- **Last Commit Date:** December 16, 2025.
- **Number of Stars:**  1.7K
- **Number of Issues (Open/Closed):** 65
- **Number of PRs (Open/Closed):**  36
- **Total Commits:**  200
- **Activity Health:** Active

### 3.3 Package Release History
- **Latest release date:**  No major releases yet just version 0.1
- **Frequency of releases:** --

---

## 4. License Analysis

### 4.1 License Type
- **License:** Apache License 2.0
- **License URL:** https://github.com/RLinf/RLinf/blob/main/LICENSE

### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |

---

## DeepSpeed
**Software Name:**  DeepSpeed \
**Version:** 0.18.2
**Environment / Image:** PyPI Package 

---

## 1. Summary

DeepSpeed is an open-source deep learning optimization library developed by Microsoft to enable efficient training and 
inference of large-scale models, including large language models (LLMs). It provides advanced system-level optimizations 
such as ZeRO (Zero Redundancy Optimizer), tensor and pipeline parallelism, activation checkpointing, offloading 
strategies, and optimized CUDA kernels.
---

## 2. SBOM Extract (from Trivy)
[View SBOM log](torch-stack.log)

---

## 3. Software Source / Provenance

### 3.1 Source Channel
- **Distribution channel:**
  - PyPI (Python package)  
  - GitHub (source code)
- **Exact URL:** https://github.com/microsoft/DeepSpeed

### 3.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  Microsoft
- **Last Commit Date:** 4 days ago
- **Number of Stars:**  41K
- **Number of Issues (Open/Closed):** 1.1K
- **Number of PRs (Open/Closed):**  102
- **Total Commits:**  3,004
- **Activity Health:** Active

### 3.3 Package Release History
- **Latest release date:**  Last week
- **Frequency of releases:** monthly

---

## 4. License Analysis

### 4.1 License Type
- **License:** Apache License 2.0
- **License URL:** https://github.com/deepspeedai/DeepSpeed/blob/master/LICENSE

### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |

---

## Hugging Face Accelerate
  
**Software Name:**   Hugging Face Accelerate \
**Version:**   1.12.0 \
**Environment / Image:**   PyPI Package

---

## 1. Summary
Hugging Face Accelerate is an open-source library developed by Hugging Face that simplifies the process of training and 
running deep learning models across different hardware configurations, including single GPU, multi-GPU, multi-node, TPU, 
and CPU setups. It provides a unified interface that abstracts away distributed training complexity while remaining 
compatible with popular frameworks such as PyTorch, DeepSpeed, and Fully Sharded Data Parallel (FSDP).
---

## 2. SBOM Extract (from Trivy)
[View SBOM log](torch-stack.log)

---

## 3. Software Source / Provenance

### 3.1 Source Channel
- **Distribution channel:** 
  - PyPI (Python package)  
  - GitHub (source code)
- **Exact URL:** https://github.com/huggingface/accelerate

### 3.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  Hugging Face  
- **Last Commit Date:**  Today
- **Number of Stars:**  9.4K
- **Number of Issues (Open/Closed):** 88  
- **Number of PRs (Open/Closed):**  11
- **Total Commits:**  1,891
- **Activity Health:** Active

### 3.3 Package Release History
- **Latest release date:**  Last month
- **Frequency of releases:** monthly

---

## 4. License Analysis

### 4.1 License Type
- **License:** Apache License 2.0
- **License URL:** https://github.com/huggingface/accelerate/blob/main/LICENSE

### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |

---

## PyTorch

**Software Name:**  PyTorch \
**Version:**   2.8 \
**Environment / Image:**   Docker Image: nvcr.io/nvidia/pytorch:25.05-py3

---

### 1. Summary
PyTorch is an open-source deep learning framework developed and maintained by Meta (Facebook AI Research) and the 
PyTorch open-source community. It provides tensor computation with strong GPU acceleration, automatic differentiation, 
and a flexible programming model widely adopted for research, prototyping, and production AI systems.
---

### 2. SBOM Extract (from Trivy)
[View SBOM log](torch-stack.log)

---

### 3. Software Source / Provenance

#### 3.1 Source Channel
- **Distribution channel:** 
  - PyPI (pip wheels)  
  - Conda (conda-forge, pytorch channels)  
  - GitHub (source code)
- **Exact URL:** https://github.com/pytorch/pytorch

#### 3.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  PyTorch Foundation (Linux Foundation) / Meta  
- **Last Commit Date:**  Today
- **Number of Stars:**  96K
- **Number of Issues (Open/Closed):** 5K+ 
- **Number of PRs (Open/Closed):**  1.7K
- **Total Commits:**  97K
- **Activity Health:** Active

#### 3.3 Package Release History
- **Latest release date:**  Nov 12
- **Frequency of releases:** monthly

---

### 4. License Analysis

#### 4.1 License Type
- **License:** BSD 3-Clause License  
- **License URL:** https://github.com/pytorch/pytorch/blob/main/LICENSE

#### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |
---

## Hugging Face Transformers
**Software Name:**    Hugging Face Transformers  \
**Version:**    4.57.3 \
**Environment / Image:** PyPI Package   

---

### 1. Summary
Hugging Face Transformers is an open-source library that provides state-of-the-art implementations of transformer-based 
models for natural language processing (NLP), computer vision (CV), audio, and multimodal tasks. It supports a wide range of architectures such as BERT, GPT, T5, LLaMA, ViT, and many others, and integrates tightly with PyTorch, TensorFlow, and JAX.
---

### 2. SBOM Extract (from Trivy)
[View SBOM log](torch-stack.log)

---

### 3. Software Source / Provenance

#### 3.1 Source Channel
- **Distribution channel:** 
  - PyPI (Python package)  
  - GitHub (source code)
- **Exact URL:**   - https://github.com/huggingface/transformers

#### 3.2 GitHub Repository Metadata (as of 16/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  Hugging Face
- **Last Commit Date:**  Today
- **Number of Stars:**  154K
- **Number of Issues (Open/Closed):** 1.1K  
- **Number of PRs (Open/Closed):**  1.1K
- **Total Commits:**  21K
- **Activity Health:** Active

#### 3.3 Package Release History
- **Latest release date:**  3 weeks ago
- **Frequency of releases:** monthly

---

### 4. License Analysis

#### 4.1 License Type
- **License:**  Apache-2.0 license 
- **License URL:** https://github.com/huggingface/transformers/blob/main/LICENSE

#### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |

---

## FlashAttention

**Software Name:**   FlashAttention \
**Version:**    2.8.3 \
**Environment / Image:** Built from source for ARM (aarch64)   

---

### 1. Summary
FlashAttention is an open-source CUDA-based library developed by the Dao-AILab research group that provides highly 
optimized implementations of attention mechanisms for transformer models. It significantly reduces memory usage and 
improves performance by fusing attention operations and leveraging GPU-specific optimizations.
---

### 2. SBOM Extract (from Trivy)

---

### 3. Software Source / Provenance

#### 3.1 Source Channel
- **Distribution channel:**
  - GitHub (source code)  
  - PyPI (source distribution; wheels typically available for x86_64 only)
- **Exact URL:** https://github.com/Dao-AILab/flash-attention

#### 3.2 GitHub Repository Metadata (as of 17/12/2025)
*(Fill only if applicable)*  

- **Maintainer / Organization:**  Dao-AILab 
- **Last Commit Date:**  16/12/2025
- **Number of Stars:**  21.1K
- **Number of Issues (Open/Closed):**  909
- **Number of PRs (Open/Closed):**  88
- **Total Commits:**  1.2K
- **Activity Health:** Active

#### 3.3 Package Release History
- **Latest release date:**  August 14th, 2025
- **Frequency of releases:** weekly-monthly

---

### 4. License Analysis

#### 4.1 License Type
- **License:** BSD 3-Clause License
- **License URL:** https://github.com/Dao-AILab/flash-attention/blob/main/LICENSE

#### 4.2 Permissibility Summary
| Question                           | Answer |
|------------------------------------|--------|
| Can be used for academic purposes? | Yes    |
| Can be used for commercial use?    | Yes    |
| Modification allowed?              | Yes    |




