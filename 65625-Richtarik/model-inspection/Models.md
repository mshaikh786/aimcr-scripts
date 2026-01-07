# Models Mentioned in the Proposal

## Project-Specific Models 

These are models to be developed or trained within the project:

Authors have a private github repository containing implementation GPT models (NanoGPT, MediumGPT) in a DDP setup.

- [NanoGPT](#nanogpt)
- [MediumGPT](#mediumgpt)

---

## NanoGPT
**Family:** NanoGPT  
**Source:** nVidia / Andrej Karpathy (MIT-licensed research)  
**Documentation / Code Links:**  
- https://github.com/karpathy/nanoGPT

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**NanoGPT** is a minimal, educational implementation of transformer-based language modeling, designed to be **simple, efficient, and interpretable** rather than a large production deployment model. It was popularized in the community through **Andrej Karpathy’s** work and example notebooks, and the canonical repository is maintained with contributions from the open-source community.

The model serves both as:
- A teaching reference for transformer training
- A lightweight baseline for experimentation on smaller datasets

#### 1.2 Who owns it?
- **Owner:** Open-source community
- **Maintainer:** Primarily initiated by Andrej Karpathy

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

- **Typical parameter count:**  
  - Varies by configuration — **from ~1M to ~100M+** depending on depth, width, and vocab size  
  - No specific figure specified.

---

#### 2.2 MFU / Training Compute Utilization

- **Model FLOPs or MFU:**  
  - Not reported as an official metric in the repository  
  - Designed for **simple, efficient compute** — focusing on educational clarity rather than peak performance

---

## MediumGPT
**Family:** MediumGPT  
**Source:** OpenAI-style nomenclature (community / experimental)  
**Documentation / Code Links:**  
- (No centralized canonical repo; models are typically community assemblages)

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**MediumGPT** is a term used in community discussions to describe **mid-sized GPT-like models** — larger than NanoGPT baselines but smaller than full GPT family giants.  
It is not an official OpenAI product but rather a **descriptor for models trained with GPT architectures at intermediate scales**.

These models frequently arise from:
- Community training runs
- Academic experiments
- Custom configurations of open transformer codebases (e.g., Hugging Face Transformers, GPT-Neo families)

Examples are variants in the **tens-to-hundreds of millions or low billions of parameters**.

#### 1.2 Who owns it?
- **Owner:** open-source community  

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

- **Typical parameter range:**  
  - **~100M to ~2B** (No exact figure specified)  

---

#### 2.2 MFU / Training Compute Utilization

- **Model FLOPs or MFU:**  
  - Not mentioned.

---