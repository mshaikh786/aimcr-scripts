## OMol25 

### Access Conditions
- Identity-gated access (not anonymous)
- Requires sharing contact information (HF email and username)
- Submitted information cannot be edited later
- No justification or description of intended use is required

#### License Implications
- **License:** CC-BY-4.0
- Free to use, modify, and redistribute
- Commercial use permitted
- Attribution to the dataset authors is required

### Ownership, Source, and Provenance
- **Owner / Curator:**  [Meta](https://huggingface.co/facebook) (Facebook / Meta AI), FAIR Chemistry team
- **Primary Distribution Platform:** Hugging Face
- **Repository:** https://huggingface.co/facebook/OMol25
- **Access Method:** Identity-gated download via Hugging Face
- **Provenance:** Curated and released by Meta as a standalone dataset, separate from any accompanying models or code
- **Maintenance Status:** Actively maintained (~50 commits; last update 2026-01-01)

### Associated paper:
- *OMol25: [paper title as per arXiv]*  
- arXiv: https://arxiv.org/abs/2505.08762
- **Publication Date:** 13 May 2025

### Country of Origin
- **Originating Organization:** Meta Platforms, Inc. (United States)  
  *(Meta Platforms Ireland Limited serves as the legal entity for EEA distribution)*

## Sample Representation

A single OMol25 data unit represents **one DFT-evaluated molecular structure** and consists of:

- An **ASE `Atoms` object** containing:
  - Atomic numbers (element types)
  - 3D atomic positions (Å)
  - Total energy (eV)
  - Per-atom forces (eV/Å)

- Associated **metadata** attached to the structure, including:
  - Molecular identifiers and composition
  - Global electronic properties (charge, spin, HOMO–LUMO gap)
  - DFT calculation details (basis size, SCF steps, dispersion energy)
  - Atomic-level charges and, if applicable, spins

Each entry is stored as a **key–value record in an LMDB database**, optimized for fast retrieval in machine learning workflows.

## Usage Justification

> No proposal justification, or description of intended usage.