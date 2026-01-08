# Models Mentioned in the Proposal

## Explicitly Named Vision / 3D Geometry Models

Appears in 3D shape representation, dynamic scene geometry, and generative 3D asset creation

- [3DShape2VecSet](#3dshape2vecset)  
- [4D-VGGT](#4d-vggt)  
- [Trellis](#trellis)

---

## 3DShape2VecSet  
**Family:** 3DShape2VecSet  
**Source:** GitHub / SIGGRAPH publication  
**Documentation / Code Links:**  
- https://github.com/1zb/3DShape2VecSet
- https://arxiv.org/abs/2301.11445

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**3DShape2VecSet** is a research model introduced for **3D shape representation via neural fields optimized for generative diffusion models**. The model encodes 3D shapes (from surface meshes or point clouds) using a **set of latent vectors** and builds neural fields on top of them, combining ideas from radial base-functions and transformer attention mechanisms.

This representation bridges 3D latent geometry with diffusion generative modeling, demonstrating capabilities such as:
- Unconditioned and conditioned 3D shape generation  
- Category-conditioned generation  
- Text-conditioned generation  
- Point-cloud completion and image⇒3D workflows

#### 1.2 Who owns it?
- **Owners:** KAUST, Technical University of Munich (TUM)

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

- **Parameter count:** Not explicitly specified. 

---

#### 2.2 MFU / Training Compute Utilization

- Not published in the academic release.

---

## 4D-VGGT  
**Family:** 4D-VGGT  
**Source:** arXiv / dynamic scene geometry paper  
**Documentation / Code Links:**  
- https://arxiv.org/abs/2511.18416 

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**4D-VGGT** is a recently proposed foundation model targeting **dynamic scene geometry estimation** with explicit spatio-temporal modeling. The approach addresses the heterogeneous nature of spatial and temporal features by factorizing them:
1. Adaptive visual grids supporting arbitrary views & time steps  
2. Separate spatial and temporal fusion modules  
3. Multi-task prediction heads for holistic scene understanding

This architecture extends prior work in static 3D geometry (e.g., VGGT) into the **4-dimensional space (space + time)** using attention mechanisms.

#### 1.2 Who owns it?
- **Owner:** Huazhong University of Science and Technology; National University of Singapore 

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

- **Parameter count:** Not reported in the arXiv preprint  
- Likely in the multi-hundreds of millions to billions range depending on implementation and target tasks.

---

#### 2.2 MFU / Training Compute Utilization

- Not reported.

---

## Trellis  
**Family:** Trellis (Structured 3D Latents)  
**Source:** Microsoft / GitHub  
**Documentation / Code Links:**  
- https://github.com/microsoft/TRELLIS 
- https://arxiv.org/abs/2412.01506

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**Trellis** (from the “Structured 3D Latents for Scalable and Versatile 3D Generation” paper) is a large-scale 3D generation model that learns **structured latent representations (SLAT)** to produce high-quality 3D assets in multiple output formats (radiance fields, Gaussian splats, meshes) from **text or image prompts**. It employs rectified flow transformers tailored for sparse latent grids and is trained on a large 3D asset dataset (~500 K objects) to support versatile generative tasks.

#### 1.2 Who owns it?
- **Owner:** Microsoft 
- **Organization:** Microsoft Research

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters

- **Model family sizes:**  
  - Pretrained checkpoints up to **~2 billion parameters** documented in the paper and project page.

---

#### 2.2 MFU / Training Compute Utilization

- Not reported.

---