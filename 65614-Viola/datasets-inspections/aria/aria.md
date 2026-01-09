## Aria Synthetic Environments

### Access Conditions

- Must submit email to gain access.

#### License Implications

- Use the ASE dataset for **research and non-commercial purposes**
- **Download, analyze, and publish results** derived from the data
- **Cite Project Aria / Meta** as specified in the license
- Use the data to develop, evaluate, and benchmark **academic models and methods**
- Don't attempt to **identify, track, or re-identify individuals** in the data
- Don't use the data in ways that **violate privacy, ethics, or applicable laws**
- Don't remove or alter **license terms, attribution, or usage notices**

### Ownership, Source, and Provenance

- **Owner / Curator:** Meta [Project Aria](https://www.projectaria.com/) team
- **Primary Distribution Platform:** https://www.projectaria.com/datasets/ase/#download-dataset
- **Repository:** https://facebookresearch.github.io/projectaria_tools/
- **Access Method:** download via download tool (also available on [HuggingFace](https://huggingface.co/datasets/projectaria/aria-synthetic-environments))
- **Provenance:** Curated and released by Meta as a standalone dataset 


### Associated paper:

- *SceneScript: Reconstructing Scenes With An Autoregressive Structured Language Model*
- arXiv:2403.13064
- **Publication Date:** 19 Mar 2024

### Country of Origin

- **Originating Organization:** Meta Platforms, Inc. (United States)  


## Sample Representation


- 100,000 multi-room indoor scenes
- Simulated with realistic device trajectories
- Across ~2-minute trajectories
- Populated with ~8000 3D objects
- With semi-dense map representations
- Simulated sensor data per sequence:
    -  1 x outward-facing RGB camera stream
    - Simulated Aria camera & lens characteristics
- Ground Truth Annotations
    - 6DoF camera trajectory
    - 3D floor plan
    - 2D instance segmentation
    - 2D range map

### Visualization avaialable via:
```
jupyter notebook projects/AriaSyntheticEnvironment/tutorial/ase_tutorial_notebook.ipynb
```
## Usage Justification

> No proposal justification, or description of intended usage.
