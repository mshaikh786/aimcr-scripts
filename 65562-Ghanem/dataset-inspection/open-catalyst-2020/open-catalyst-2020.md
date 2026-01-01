## Open Catalyst 2020

### Access Conditions
- Publicly accessible dataset


#### License Implications
- **License:** MIT License
- Permits **use, modification, distribution, and commercial use** of the dataset and software
- Allows **redistribution of the dataset and derived subsets**
- Requires preservation of **copyright notice and license text**
- **No restrictions** on field of use or downstream applications


### Ownership, Source, and Provenance
- **Owner / Curator:** [Meta](https://huggingface.co/facebook) (Facebook / Meta AI), FAIR Chemistry team
- **Primary Distribution Platform:** fair-chem / [Open Catalyst Project website](https://opencatalystproject.org/)
- **Access Method:** Direct download of pre-sharded LMDB files
- **Provenance:**
- **Maintenance Status:** 


### Associated paper:
- _Open Catalyst 2020 (OC20) Dataset and Community Challenges_
- **arXiv**: arXiv:2010.09990
- **Publication Date**: October 2020

### Country of Origin
- **Originating Organization:** Meta Platforms, Inc. (United States)  
  *(Meta Platforms Ireland Limited serves as the legal entity for EEA distribution)*

## Sample Representation
- Atomistic systems represented as:
  - Atomic numbers
  - 3D atomic positions
  - Periodic boundary conditions
  - Lattice vectors
- Labels include:
  - Total energy (eV)
  - Atomic forces (eV/Å)
  - Stress tensors (for selected tasks)
- Stored in **LMDB** format optimized for large-scale training
- Supports supervised learning tasks:
  - Structure → Energy & Forces (S2EF)
  - Initial Structure → Relaxed Structure (IS2RS)
  - Initial Structure → Relaxed Energy (IS2RE)

## Usage Justification

OC20 is used to support large-scale supervised and self-supervised pre-training comparisons, enabling topology-driven representation learning that generalizes across diverse molecular and materials systems and transfers effectively to downstream tasks.
