# Models Mentioned in the Proposal

## Explicitly Named Foundation / Vision Models

Appears in perception, geometric understanding, and 3D reasoning components of the proposal.

- [Map Anything](#map-anything)
- [Depth Anything V3](#depth-anything-v3)

---

## Map Anything
**Family:** Map Anything  
**Source:** Meta AI (Facebook Research)  
**Documentation / Code Links:**  
- https://github.com/facebookresearch/map-anything
- https://arxiv.org/abs/2509.13414

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**Map Anything** is a research model released by **Meta AI (Facebook Research)**.  
It is designed as a **foundation model for dense correspondence and mapping**, extending the “Anything” paradigm (e.g., Segment Anything) into **geometric and spatial representation learning**.

The model focuses on producing **dense, consistent mappings across images**, enabling tasks such as:
- Dense correspondence
- Visual alignment
- Geometric reasoning
- Multi-view consistency

#### 1.2 Who owns it?
- **Owner:** Meta AI  
- **Organization:** Meta Platforms, Inc.

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Parameter count:**  
  - **Not publicly disclosed**
  - The repository does not specify a fixed parameter size; Map Anything is presented as a research framework rather than a single canonical checkpoint size.

---

#### 2.2 Training Token / Sample Count
- **Training data scale:**  
  - Exact image count or dataset size is **not disclosed**.
  - Training relies on **large-scale image datasets** with geometric and correspondence supervision, potentially including synthetic and real-world multi-view data.

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  
  - Not reported in the paper or repository.
  - No official training compute or utilization benchmarks are provided.

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**  
  - Large-scale visual datasets designed for learning dense correspondences and mappings across images.
  - Emphasis on spatial alignment rather than semantic labeling.

- **Data provenance:**  
  - Public and internal research datasets commonly used within Meta AI research.
  - Exact dataset composition and licensing are not enumerated in the public release.

---

#### 3.2 Fine-tuning / Adaptation
- The model is intended to be **adaptable** to downstream tasks such as:
  - 3D reconstruction
  - Multi-view geometry
  - Visual localization
- Fine-tuning strategies are task-dependent and left to downstream users.

---

## Depth Anything V3
**Family:** Depth Anything  
**Source:** ByteDance Seed  
**Documentation / Code Links:**  
- https://github.com/ByteDance-Seed/depth-anything-3
- https://arxiv.org/abs/2511.10647

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**Depth Anything V3** is developed by **ByteDance Seed**, ByteDance’s advanced research division.  
It is the third major iteration of the **Depth Anything** family, a set of **foundation monocular depth estimation models** designed to generalize across scenes, domains, and camera types.

Depth Anything V3 emphasizes:
- Strong zero-shot depth generalization
- Robust performance across indoor and outdoor environments
- Improved metric depth consistency compared to earlier versions

#### 1.2 Who owns it?
- **Owner:** ByteDance  
- **Organization:** ByteDance Seed

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Parameter count:**  
  - Multiple model sizes are provided (e.g., small, base, large variants).
  - Exact parameter counts vary by backbone and are **not consistently enumerated** in the public documentation.

---

#### 2.2 Training Token / Sample Count
- **Training data scale:**  
  - Trained on **millions of images** using a combination of:
    - Metric depth datasets
    - Relative depth data
    - Pseudo-labeled depth generated at scale

- **Exact sample counts:** Not explicitly disclosed.

---

#### 2.3 MFU / Training Compute Utilization
- **Model FLOPs or MFU:**  
  - No official MFU or training efficiency metrics are published.

---

### 3. Training Dataset Information

#### 3.1 Pre-training Data
- **Dataset description:**  
  - A mixture of real-world depth datasets, synthetic data, and large-scale pseudo-labeled depth maps.
  - Designed to reduce domain bias and improve cross-dataset generalization.

- **Data provenance:**  
  - Public depth datasets and internally generated annotations.
  - Specific dataset names and proportions are partially described but not fully itemized.

---

#### 3.2 Fine-tuning / Specialization
- Depth Anything V3 supports:
  - Zero-shot depth inference
  - Optional fine-tuning for domain-specific scenes (e.g., indoor robotics, autonomous driving)
- The released checkpoints are intended to work **out-of-the-box** without task-specific retraining.

---