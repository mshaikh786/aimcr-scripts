# Models Mentioned in the Proposal

## Explicitly Named Foundation / LLM Models

Appears in model scaling comparison and performance discussion

- [LLaMA 3.2 – 3B](#llama-32--3b)
- [Qwen 2.5 – 7B Instruct](#qwen-25--7b-instruct-)


---

## Project-Specific Models

These are models to be developed or trained within the project:

- ContextFlow (in-context robot foundation model)
- CompoSE (3D asset generation model/system)
- LongVu++ (long-context multimodal video understanding model)
- EfficientRL-Embodied (RL post-training framework/model stage)

---


## LLaMA 3.2 – 3B
**Family:** LLaMA 3.2  
**Source:** Meta AI / Hugging Face  
**Documentation / Model Card Links:**  
- https://huggingface.co/meta-llama/Llama-3.2-3B

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

LLaMA 3.2 – 3B is part of the Meta AI **LLaMA 3.2** family of pretrained and instruction-tuned language models hosted 
publicly on Hugging Face. It is developed and published by **Meta AI**, the research organization within Meta (formerly 
Facebook) responsible for large language model research and releases.

#### 1.2 Who owns it?
- **Owner:** Meta AI  
- **Organization:** Meta Platforms, Inc.

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:** ~3 billion  
  - The model is described as a “3B” variant, meaning ~3.2 billion parameters in its instruction-tuned form.

---

#### 2.2 Training Token Count
- **Training data scale:**  
  - LLaMA 3.2 models were pretrained on up to **9 trillion tokens** of text from publicly available sources. 
  - Broader LLaMA 3.2 family (including larger variants) is trained on significantly larger corpora, but specific 
  documentation for the 3B variant indicates this upper bound.

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  
  - Public documentation does not provide official Meta MFU (Megaflop Utilization) figures for the 3B variant. In absence of an official metric, such utilization must be inferred from training dataset size and parameter count.  
  - **No published official MFU benchmarks** specific to this model were found in Meta’s public model cards or docs.

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**  
  - Meta’s LLaMA 3.2 family was trained on **large, publicly available text corpora**.  
  - The 3B version is part of this family and inherits the general training regime. 

- **Token count:**  
  - Pre-training was performed on up to **9 trillion tokens** for the smaller models like 1B and 3B. 

- **Data provenance:**  
  - Meta has stated that training data comprises publicly available sources, though granular dataset composition 
  (specific corpora and licensing) is not fully disclosed in model cards.

#### 3.2 Fine-tuning / Instruction Tuning
- The instruction-tuned variant (often called **LLaMA-3.2-3B-Instruct**) is fine-tuned on mixtures of instruction datasets.  
- Meta’s official model pages indicate the instruction-tuned models are optimized for multilingual dialogue, summarization, and retrieval tasks. :contentReference[oaicite:6]{index=6}

---

## Qwen 2.5 – 7B Instruct 
**Family:** Qwen 2.5  
**Source:**  QwenLM / Huawei-Alibaba cooperation (Qwen consortium)  
**Documentation / Model Card Links:**  https://huggingface.co/Qwen/Qwen2.5-7B-Instruct  

---

### 1. Source / Provenance

- **Owner:** QwenLM consortium (including Alibaba Cloud / Huawei AI initiatives) 
- **Organization:** While the Qwen project does not list a single corporate owner in a canonical way, the models are released by the QwenLM organization on Hugging Face, which is associated with major Chinese AI labs (notably Huawei and Alibaba projects)

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:**  **7 billion parameters**  

---

#### 2.2 Training Token Count
- **Training data scale:**  
  - The broader Qwen 2.5 family is described in the literature as having been trained on a very large corpus — up to **18 trillion tokens** of diverse pre-training data (text and code) covering multilingual inputs.
  - While official token counts *specific to the 7B Instruct variant* are not published separately, it inherits the same pre-training regime used by the Qwen2.5 series.

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  No data available

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**  Qwen2.5 models were trained on large, heterogeneous corpora comprising multilingual text, structured data, code, and potentially syntactic corpora aggregated from public sources.  

- **Token count:**  Not disclosed

- **Data provenance:**  --

