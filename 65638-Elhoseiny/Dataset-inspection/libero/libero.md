# LIBERO

## Maintainer / Author

- **Primary artifact related to a peer-reviewed paper**:  
  Yes. LIBERO is associated with the paper  
  *“LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning”*  
  (arXiv:2306.03310).

- **Maintainer / Organization**:  
  The dataset is maintained by the **Lifelong Robot Learning** group, with
  contributions affiliated with **Google DeepMind**.

- **Public presence**:  
  - Official GitHub repository: https://github.com/Lifelong-Robot-Learning/LIBERO  
  - Hugging Face organization: https://huggingface.co/physical-intelligence  

---

## Dataset Source / Provenance

- **Hugging Face dataset page**:  
  https://huggingface.co/datasets/physical-intelligence/libero  
  - Downloads (last month): **25,029**

- **GitHub repository**:  
  https://github.com/Lifelong-Robot-Learning/LIBERO/tree/master  
  - Last commit: ~9 months ago  
  - Maintainer: Google DeepMind  
  - Statistics:
    - Stars: ~1.3k  
    - Commits: 41  
    - Pull Requests: 9  
    - Issues: 69  

LIBERO is distributed as a **task-oriented benchmark suite** built on top of
the robosuite simulation framework, designed for language-conditioned robot
manipulation and lifelong learning research.

---

## License Conditions

- **Hugging Face license**: CC-BY-4.0  
- **GitHub repository license**: MIT License  

### Permissibility
- Permitted for **academic and research use**
- Redistribution requires inclusion of the original license
- Attribution to the original authors is required under CC-BY-4.0

---

## Distribution and Sampling Semantics

LIBERO supports downloading its benchmark suites via **Hugging Face as a
distribution backend** using the `--use-huggingface` flag.

However, the dataset remains **task-oriented** by design:

- The **smallest accessible unit** is a **full task file** (`.hdf5`) within a suite
- Each task file contains a fixed number of **expert demonstrations (episodes)**
- **Episode-level or partial task sampling is intentionally unsupported**

This design contrasts with large-scale raw datasets such as **RoboMIND** or
**Open X-Embodiment**, where individual episodes can be arbitrarily sampled.

As a result, LIBERO should be treated as a **benchmark suite**, not as a
streamable or record-level dataset.

