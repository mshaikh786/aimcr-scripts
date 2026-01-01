# Models Mentioned in the Proposal

# 1️⃣ EquiformerV2

## EquiformerV2 – Large (typical research configuration)

**Family:** Equiformer
**Source:** Academic research (ETH Zürich, Meta FAIR contributors)
**Primary Domain:** Atomistic ML / Molecular & Materials Modeling
**Documentation / Code Links:**

* Paper: [https://arxiv.org/abs/2306.12059](https://arxiv.org/abs/2306.12059)
* Code (FAIRChem / Open Catalyst): [https://github.com/atomicarchitects/equiformer_v2](https://github.com/atomicarchitects/equiformer_v2)

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

EquiformerV2 is the second-generation **equivariant graph Transformer** designed for atomistic systems. It was introduced to improve scalability, stability, and expressiveness over the original Equiformer, particularly for **large-scale molecular and materials datasets**.

It is widely used within the **FAIRChem / Open Catalyst** ecosystem and serves as a backbone for foundation-style atomistic models.

### 1.2 Who owns it?

* **Authors:** Yi-Lun Liao et al.
* **Affiliations:** ETH Zürich, Meta FAIR (research collaboration)
* **License:** MIT (research-friendly)

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

* **Typical range:** ~10M → 100M+ parameters
* **Large configurations:** 80–120M parameters (dataset- and cutoff-dependent)

Unlike LLMs, parameter count depends on:

* Number of transformer layers
* Maximum spherical harmonic degree
* Hidden channel width
* Radial basis resolution

### 2.2 Training Data Scale

* **Atoms seen during training:** up to **billions of atoms**
* **Structures:** tens of millions (OC20, ODAC, OMol-scale datasets)
* No tokenization — operates directly on **3D atomic point clouds**

### 2.3 Compute / MFU

* **Training regime:** multi-node GPU (A100 / GH200-class)
* **Scaling:** near-linear up to 512 GPUs
* **MFU:** not publicly reported
  (atomistic models are memory-bound and neighbor-graph–limited rather than FLOP-saturated)

---

## 3. Training Dataset Information

### 3.1 Pretraining Data

* OC20 / OC22 (catalyst slabs)
* ODAC 23 / 25 (MOFs for DAC)
* OMol / OMat (molecules & materials)

### 3.2 Supervision vs Self-Supervision

* Traditionally: **fully supervised** (energy, forces)
* In *this proposal*: **extended to self-supervised**

  * Flow-matching
  * Diffusion
  * Autoregressive atom generation

---

# 2️⃣ GemNet-OC

## GemNet-OC – Large

**Family:** GemNet
**Source:** TU Munich
**Primary Domain:** Molecular & Materials GNNs
**Documentation / Code Links:**

* Paper: [https://www.cs.cit.tum.de/daml/gemnet/](https://www.cs.cit.tum.de/daml/gemnet/)
* Code: [https://github.com/TUM-DAML/gemnet_tf](https://github.com/TUM-DAML/gemnet_tf)

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

GemNet-OC is a **directional message-passing GNN** explicitly designed for **chemical accuracy** in force and energy prediction. It was created as a successor to SchNet/DimeNet-style models with stronger geometric inductive biases.

### 1.2 Who owns it?

* **Authors:** Johannes Gasteiger et al.
* **Institutions:** TU Munich, Meta FAIR
* **License:** MIT

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

* **Typical range:** ~5M → 40M parameters
* Smaller than EquiformerV2 but highly parameter-efficient

### 2.2 Training Data Scale

* Millions to tens of millions of atomic structures
* Designed for **dense local chemistry**, not global topology

### 2.3 Compute / MFU

* Strong GPU efficiency for single-node and small multi-node runs
* Less scalable than transformers at very large node counts
* MFU not reported

---

## 3. Training Dataset Information

### 3.1 Pretraining Data

* OC20 / OC22
* ODAC datasets

### 3.2 Training Objective

* Supervised regression:

  * Atomic energies
  * Forces
  * Virials

### 3.3 Role in the Proposal

* **Baseline supervised model**
* Comparison target vs self-supervised EquiformerV2 / UMA
* Control to show gains from topology-aware SSL

---

# 3️⃣ UMA (Universal Models for Atoms)

## UMA – Large

**Family:** UMA
**Source:** Meta FAIR (FAIRChem)
**Primary Domain:** Foundation Models for Atomistic Systems
**Documentation / Code Links:**

* Paper: [https://arxiv.org/abs/2506.23971](https://arxiv.org/abs/2506.23971)
* Code: [https://github.com/FAIR-Chem/fairchem](https://github.com/FAIR-Chem/fairchem)

---

## 1. Source / Provenance

### 1.1 Where is it coming from?

UMA is Meta FAIR’s **explicit attempt at a foundation model for atoms**, analogous in spirit to GPT-style pretraining but grounded in **equivariant physics-aware representations**.

It unifies multiple datasets, tasks, and chemical domains into a **single pretrained backbone**.

### 1.2 Who owns it?

* **Owner:** Meta AI (FAIRChem)
* **License:** MIT / FAIR open research license

---

## 2. Model Characteristics

### 2.1 Number of Trainable Parameters

* **Small:** ~20–30M
* **Medium:** ~60–80M
* **Large:** ~120–200M+

These numbers vary with:

* eSEN transformer depth
* Angular resolution
* Cutoff radius

### 2.2 Training Data Scale

* **Hundreds of millions of structures**
* **>50 billion atoms** (as stated in proposal)
* Trained across:

  * Molecules
  * Crystals
  * MOFs
  * Catalysts

### 2.3 Compute / MFU

* Designed for **multi-node GPU scaling**
* Log-linear scaling up to **512 GPUs**
* MFU not publicly disclosed (again, neighbor search dominates)

---

## 3. Training Dataset Information

### 3.1 Pretraining Data

* OC20 / OC22
* ODAC 23 / 25
* OMol / OMat
* In-house MOF datasets

### 3.2 Training Paradigm

* **Originally:** supervised (E/F/V)
* **In this project:** extended to:

  * Self-supervised flow matching
  * Diffusion
  * Autoregressive atom modeling

