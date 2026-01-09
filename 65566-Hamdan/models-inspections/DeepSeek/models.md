
# Models Mentioned in the Proposal

## Explicitly Named Foundation / LLM Models


- DeepSeek-LLM
- Gemma


---

## Project-Specific Models

Insert comment/remove section if not applicable

``` text
Agentic AI Platform (Top-Level Umbrella)
│
├── Protein Foundation Model Umbrella
│     ├── Enzyme Foundation Models (EFMs)
│     ├── Peptide Foundation Models (PFMs)
│     └── Protein Fusion Foundation Models (PFFMs)
│
├── Multi-Objective Reinforcement Learning Umbrella
│     ├── Enzyme RL policies
│     ├── Peptide RL policies
│     └── Fusion-protein RL policies
│
└── Domain-Specific LLM Umbrella
      ├── DeepSeek (fine-tuned)
      ├── Gemma (fine-tuned)
      └── Custom biologics-design LLMs
```

---


## Maximum Number of GPUs and GPU Hours

- **Protein Foundation Models (PFMs)**
    - **Max GPUS:** Uses **~8 NVIDIA A100 GPUs**
    - **GPU Hours:** **~120 wall-hours per full pretraining run**


- **Reinforcement Learning (RL) Models**
    - **Max GPUS:** Uses **~4 NVIDIA A100 GPUs**
    - **GPU Hours:** **~48 wall-hours per full pretraining run**

---

## DeepSeek-LLM

**Family:** [DeepSeek-LLM Seried](https://huggingface.co/collections/deepseek-ai/deepseek-llm) 

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?
- China


#### 1.2 Who owns it?
- **Organization / Owner:** [DeepSeek](https://huggingface.co/deepseek-ai/collections) (Hangzhou DeepSeek Artificial Intelligence Co., Ltd.)  
- **Founder:** [Liang Wenfeng](https://www.linkedin.com/in/wenfeng-liang-837841128/)


---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:** Not mentioned by Project Proposal, however DeepSeek-LLM has 7B and 67B va 

---

#### 2.2 Training Token Count
- **Training data scale:**  2T

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  Not Mentioned

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**  Large-scale deduplicated web corpus predominantly English + Chinese

- **Token count:**  2T

- **Data provenance:** Publicly described as Common Crawl–derived

#### 3.2 Fine-tuning / Instruction Tuning
- Not Mentioned

---

## Gemma

**Family:** [Gemma](https://huggingface.co/collections/deepseek-ai/deepseek-llm) 

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?
- United States 


#### 1.2 Who owns it?
- **Organization / Owner:** Google [https://huggingface.co/google/collections]


---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:** Not mentioned by Project Proposal

---

#### 2.2 Training Token Count
- **Training data scale:**   Not mentioned by Project Proposal

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  Not Mentioned

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**   Not mentioned by Project Proposal

- **Token count:**   Not mentioned by Project Proposal

- **Data provenance:**  Not mentioned by Project Proposal

#### 3.2 Fine-tuning / Instruction Tuning
- Not Mentioned

---

> Number of parmeters are not mentioned for any custom/off-the-shelf model.

> DeepSeek and Gemma fine-tuning GPU count and hours not mentioned

>  DeepSeek and Gemma fine-tuning datasets not mentioned 
