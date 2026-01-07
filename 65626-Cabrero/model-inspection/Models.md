# Models Mentioned in the Proposal

## Explicitly Named Foundation / Multimodal Models

Appears in sequence-structure-function embedding and protein search components

- [ProTrek](#protrek)

---

## ProTrek
**Family:** ProTrek  
**Source:** Westlake-REPL (Westlake University)  
**Documentation / Code Links:**  
- https://github.com/westlake-repl/ProTrek
- https://www.biorxiv.org/content/10.1101/2024.05.30.596740v2

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**ProTrek** is a **trimodal protein language model** developed by researchers in the **Westlake REPL group**. It integrates **protein sequence, structure, and function** in a unified embedding space, enabling advanced retrieval and similarity tasks across modalities. The model was released with code, pretrained weights, and deployment examples.

ProTrek’s research focus is on:
- Joint learning of sequence–structure–function relationships
- Efficient protein search and retrieval
- Scaling to large biological databases

The core idea is to bring **tri-modal supervision** (sequence ↔ structure, sequence ↔ function, structure ↔ function) into a shared representational latent space.

#### 1.2 Who owns it?
- **Owner:** Westlake REPL  
- **Organization:** Westlake University

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

ProTrek provides multiple pretrained configurations:

- **ProTrek_35M:**  
  - Sequence encoder: ~35M  
  - Structure encoder: ~35M  
  - Text encoder: ~130M  

- **ProTrek_650M:**  
  - Sequence encoder: ~650M  
  - Structure encoder: ~150M  
  - Text encoder: ~130M

These variants allow trade-offs between compute cost and representation fidelity.

---

#### 2.2 MFU / Training Compute Utilization

- **Model FLOPs or MFU:**  
  - Not officially released  
  - Varies by chosen footprint (35M vs 650M models)

ProTrek’s focus is on **biological representation quality**, not on reporting compute metrics.

---