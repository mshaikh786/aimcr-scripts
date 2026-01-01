## Open Catalyst

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
- **Access Method:** Direct download of pre-sharded LMDB files (https://fair-chem.github.io/catalysts/datasets/summary)
- **GtHub Repo**: https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/data/oc
- **Provenance:** Curated and released by Meta as a standalone dataset.
- **Maintenance Status:** Last commit on GitHub was on July 2025.

### Associated paper:

- Open Catalyst 2020
    - _Open Catalyst 2020 (OC20) Dataset and Community Challenges_
    - **arXiv**: arXiv:2010.09990
    - **Publication Date**: October 2020
- Open Catalyst 2022
    - _The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts_
    - **arXiv**: arXiv:2206.08917
    - **Publication Date**: Submitted on 17 Jun 2022 (v1), last revised 7 Mar 2023 (this version, v3)

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

Perform a rigorous, large-scale comparison
between supervised and self-supervised pre-trainings. Therefore, we are planning to run
parallel hyperparameter optimizations for both the supervised and the self-supervised
setups. We will train these models using a diverse collection of state-of-the-art datasets that
span a wide range of molecular and materials systems