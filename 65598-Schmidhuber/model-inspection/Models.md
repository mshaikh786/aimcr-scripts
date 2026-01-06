# Models Mentioned in the Proposal

# They don't plan to use off-the-shelf LLMs like GPT, LLaMA, etc. Instead, they intend to develop, scale, and train their own AI/LLM architectures.

# Frameworks to be used in developing the model.

## FACTS: A Factored State-Space Framework For World Modelling

**Source:** KAUST (Li Nanbo)
**Documentation / Code Links:**

* Paper: [https://arxiv.org/html/2410.20922v2](https://arxiv.org/html/2410.20922v2)
* Code : [https://github.com/NanboLi/FACTS](https://github.com/NanboLi/FACTS)

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

KAUST research project

### 1.2 Who owns it?

* **Authors:** Li Nanbo et al.
* **Affiliations:** KAUST
* **License:** MIT (research-friendly)

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

* **Typical range:** ~1B - 3B parameters

### 2.2 Compute

* **GPU core hours:** 110,000
* **Scaling:** 2 simulations x 32 nodes x 4 GPUs
* MFU not reported

---

# MOSA

## Mixture of Sparse Attention (MoSA)

**Source:** KAUST
**Documentation / Code Links:**

* Paper: [https://arxiv.org/abs/2505.00315](https://arxiv.org/abs/2505.00315)
* Code: [https://github.com/piotrpiekos/MoSA](https://github.com/piotrpiekos/MoSA)

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

MOSA is a User-friendly implementation of the Mixture-of-Sparse-Attention. MoSA selects distinct tokens for each head with expert choice routing providing a content-based sparse attention mechanism.

### 1.2 Who owns it?

* **Authors:** Piotr Piękos et al.
* **Institutions:** KAUST
* **License:** MIT

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

* **Typical range:** ~1B → 3B parameters

### 2.2 Compute / MFU

* **GPU core hours:** 110,000
* **Scaling:** 2 simulations x 32 nodes x 4 GPUs
* MFU not reported

---