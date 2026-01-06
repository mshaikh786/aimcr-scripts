# Models Mentioned in the Proposal

## ⚠️ No Explicit AI / LLM Models Specified

### AI Models – Unspecified / Application-Level Usage

Train a multimodal transformer foundation model to reconstruct a 3D brain atlas 
from scRNA-seq + ST + H&E, enabling virtual slicing and mapping of new sections

**Family:** Not specified  
**Source:** Existing / off-the-shelf deep learning models  
**Documentation / Code Links:**  
_Not provided in the proposal_

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

The proposal does **not introduce, name, or commit to any specific AI or LLM architecture**. Instead, it describes the use of **generic deep learning and machine learning models** as computational tools to support the project’s scientific objectives.

Any AI models used are implicitly assumed to come from **standard, widely available model families** (e.g., convolutional neural networks or transformer-based models), but these are referenced only at a **conceptual level**, not as concrete implementations.

### 1.2 Who owns it?

Because no specific models are named:

- **Ownership:** Not specified  
- **Licensing:** Not specified  
- **Model origin:** Assumed to be public or pre-existing research / industry models  

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

- **Not specified**
- No mention of:
  - Parameter counts  
  - Model depth or width  
  - Scaling regimes (millions vs billions)  


### 2.2 Compute / MFU

- Significant GPU resources are requested
- 180,000 CPU core hours and 95,000 GPU core hours requested. 
up to L≈ 8k
- 10 - 200 CPU nodes required.
- 4 - 44 GPU nodes required (upto 176 GPUs).
- Compute justification is based on:
  - Simulation complexity  
  - Data processing workloads  
  - Repeated training and inference cycles  
- Scaling:
  - A standard fusion-training run will use 16 - 24 GPU nodes (4× GH200 per node; 64 - 96 GPUs total) for 16 - 24 hours.
  - Encoder pretraining (RNA, ST, H&E) will use 8 - 12 GPU nodes (32 - 48 GPUs) 
for 8 - 12 hours per encoder.

- No MFU reported.

AI models are treated as **supporting tools**, not as research artifacts.

---