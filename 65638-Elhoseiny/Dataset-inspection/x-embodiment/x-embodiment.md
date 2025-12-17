# X-Embodiment (Open X-Embodiment / OXE) — Dataset Investigation

---

## Maintainer / Author

### Maintainer (dataset distributor)

- **Organization:** Google DeepMind
- **Official GitHub organization:** `google-deepmind`
- **Primary repository:** `google-deepmind/open_x_embodiment`

### Artifact related to a paper authored by the maintainer?

- **Yes**
- The dataset and tooling are introduced alongside the paper:  
  **“Open X-Embodiment: Robotic Learning Datasets and RT-X Models”**
- The repository explicitly references this work and positions itself as the open dataset + tooling companion to the
  paper.

### Maintainer’s LinkedIn / website / public presence

- **Organization:** Google DeepMind (official website, blog, and GitHub presence)
- **Project website:** https://robotics-transformer-x.github.io/
- **Example lead author public presence:** Karl Pertsch (DeepMind researcher; LinkedIn + personal academic website)

---

## Dataset Source / Provenance

### Hugging Face URLs

> There is **no single canonical HF repo owned by DeepMind**. Instead, there are community and ecosystem mirrors.

- **Unofficial aggregated HF dataset:**  
  `jxu124/OpenX-Embodiment`  
  (Provides a unified loader; license shown as CC-BY-4.0 on the HF card)

- **LeRobot ecosystem collection:**  
  `lerobot/open-x-embodiment`  
  (Multiple OXE datasets converted into LeRobot format)

> Note: HF repos are **derived representations**; the GitHub repo remains the authoritative source.

---

### GitHub Repository (Official)

- **Repository:** https://github.com/google-deepmind/open_x_embodiment
- **Maintainer:** Google DeepMind
- **Purpose:**
    - Standardized access to multiple robot datasets
    - Unified RLDS episode format
    - Metadata and references for all constituent datasets

#### Repository activity (approximate)

- **Last commit:** November 27, 2024
- **Stars:** ~1.6k
- **Forks:** ~100
- **Commits:** ~27
- **Issues:** ~54
- **Pull Requests:** ~1

---

## License Conditions

### Licenses stated in the official repository

- **Software code:** Apache License 2.0
- **Data / other materials:** Creative Commons Attribution 4.0 (CC-BY 4.0)

### Permissibility

- **Academic & research use:** ✅ Allowed
- **Commercial use:** ✅ Allowed (with conditions)
- **Modification:** ✅ Allowed
- **Redistribution:** ✅ Allowed

### Obligations

- **Apache-2.0:**
    - Preserve license and copyright notices
- **CC-BY-4.0:**
    - Attribution required when redistributing or publishing derived work

### Important nuance

- Open X-Embodiment is an **aggregate benchmark**:
    - Each underlying dataset may have **its own citation requirements**
    - Users must check per-dataset metadata (linked from the repo) before redistribution or commercial deployment

---

## Notes / Risk Flags

- Hugging Face datasets are **not the authoritative source**
- License applies at the **framework level**; sub-datasets may introduce constraints
- Intended primarily for **robot learning research and benchmarking**, not turnkey commercial deployment without due
  diligence

---

# X-Embodiment RGB Availability Audit

This document describes how RGB image availability was audited across the
X-Embodiment / Open-X-Embodiment datasets.

The goal of this audit was to determine whether each dataset contains **real RGB
image observations**, whether RGB is explicitly unavailable, or whether image
presence could only be inferred structurally.


### Scope

- Total datasets analyzed: **69**
- Datasets with confirmed real RGB images: **67**
  - Confirmed via textual descriptions: **44**
  - Confirmed via schema inspection: **23**
- Datasets without real RGB images: **2**



### Dataset Access

#### 1. Resolving Dataset Access Issues (TFDS [Issue #5392](https://github.com/tensorflow/datasets/issues/5392))

Some X-Embodiment datasets initially appeared inaccessible or incomplete when
queried through a single GCS location. As discussed in TFDS [issue #5392](https://github.com/tensorflow/datasets/issues/5392), datasets are distributed
across multiple GCS buckets and cannot be reliably discovered from one bucket
alone.

To resolve this, we explicitly probed all known Open-X-Embodiment storage
locations instead of relying on TFDS defaults.

```python
# === Buckets to try (order matters) ===
BUCKETS = [
    "gs://gdm-robotics-open-x-embodiment",
    "gs://gresearch/robotics",
]
```
By iterating over these buckets in order, datasets that were missing or
inaccessible from one location could be successfully resolved in another,
allowing reliable access to their `features.json` metadata.

#### 2. RGB Detection Methodology
Datasets were accessed through their referenced **Google Cloud Storage (GCS)**
buckets as defined by the Open-X-Embodiment / TFDS registry.

During inspection, several datasets appeared problematic at first due to:
- Missing or incomplete image descriptions in `features.json`
- Image modalities not being registered as `tfds.features.Image`
- Inconsistent TFDS/RLDS metadata layouts

This behavior is consistent with known TensorFlow Datasets (TFDS) limitations
for RLDS-based datasets, where image observations may exist structurally but are
not exposed through high-level metadata.

As a result, the audit relied on **direct schema inspection** rather than
descriptions alone.




RGB availability was determined using a **three-stage verification process**.

#### 2.1 Description-based verification

The first stage scanned human-readable descriptions inside `features.json`.

Datasets were classified as containing real RGB imagery if descriptions explicitly
mentioned RGB images, for example:
- “Main camera RGB observation”
- “Wrist camera RGB observation”
- “RGB captured by workspace camera”

Datasets meeting this criterion were marked as:

- **CONFIRMED_RGB**
- **Evidence:** description

This step confirmed RGB presence for **44 datasets**.


#### 2.2 Schema-based verification (TFDS / RLDS inspection)

Many datasets lacked explicit textual descriptions despite containing image data.
To avoid false negatives, the TFDS/RLDS feature schema was inspected directly.

The schema inspection searched for image tensors using the following signals:

- Feature paths containing image-related keywords:
  - `image`, `rgb`, `camera`, `wrist`, `front`, `left`, `right`, `top`, `side`, `fisheye`
- Presence of shape metadata under:
  - `image/shape/dimensions`
  - `tensor/shape`
- Tensor rank of **3 or 4**
- Channel dimension size of **1, 3, or 4**
- Dimension values represented as either integers or strings
  (e.g., `["480", "640", "3"]`)

This approach detects RGB imagery even when images are stored as generic tensors
rather than `tfds.features.Image`.

Datasets satisfying these structural conditions were marked as:

- **CONFIRMED_RGB**
- **Evidence:** schema

This step recovered **23 datasets** that would otherwise appear to lack RGB data.


#### 2.3 Explicit non-RGB datasets

Some datasets explicitly state that image data is unavailable or replaced with
zero-valued placeholders (e.g., `np.zeros`).

These datasets were marked as:

- **CONFIRMED_NO_RGB**
- **Evidence:** explicit_zero

Only **2 datasets** fall into this category.

---

## Final Outcome

After combining description-based and schema-based verification:

- **67 out of 69 datasets** contain real RGB image observations
- Missing descriptions do **not** imply missing RGB data
- Schema inspection is necessary for reliable auditing of RLDS datasets

This audit provides a complete and verifiable determination of RGB availability
across the X-Embodiment dataset collection.

Investigation process is available at [RGB-investigation.ipynb](RGB-investigation.ipynb)


| Dataset                                                       | Version | RGB Status       | Evidence      | RGB Paths (examples)                | Notes                                             |
|---------------------------------------------------------------|---------|------------------|---------------|-------------------------------------|---------------------------------------------------|
| language_table                                                | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | An RGB image of the scene.                        |
| stanford_hydra_dataset_converted_externally_to_rlds           | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| austin_buds_dataset_converted_externally_to_rlds              | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| furniture_bench_dataset_converted_externally_to_rlds          | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| cmu_franka_exploration_dataset_converted_externally_to_rlds   | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| ucsd_kitchen_dataset_converted_externally_to_rlds             | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| austin_sirius_dataset_converted_externally_to_rlds            | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Wrist camera RGB observation.                     |
| utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds | 1.0.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| utokyo_saytap_converted_externally_to_rlds                    | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Dummy wrist camera RGB observation.               |
| berkeley_mvp_converted_externally_to_rlds                     | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Hand camera RGB observation.                      |
| kaist_nonprehensile_converted_externally_to_rlds              | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| dlr_sara_pour_converted_externally_to_rlds                    | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| asu_table_top_converted_externally_to_rlds                    | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| stanford_robocook_converted_externally_to_rlds                | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Camera 1 RGB observation.                         |
| iamlab_cmu_pickup_insert_converted_externally_to_rlds         | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Wrist camera RGB observation.                     |
| utaustin_mutex                                                | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Wrist camera RGB observation.                     |
| berkeley_fanuc_manipulation                                   | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| cmu_playing_with_food                                         | 1.0.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| cmu_stretch                                                   | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| berkeley_gnm_cory_hall                                        | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| berkeley_gnm_sac_son                                          | 0.1.0   | CONFIRMED_RGB    | description   | –                                   | Main camera RGB observation.                      |
| eth_agent_affordances                                         | 0.1.0   | CONFIRMED_NO_RGB | explicit_zero | –                                   | Images explicitly unavailable; filled with zeros. |
| kuka                                                          | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| columbia_cairlab_pusht_real                                   | 0.1.0   | CONFIRMED_RGB    | schema        | wrist_image/image/shape             | RGB confirmed via TFDS/RLDS schema.               |
| robot_vqa                                                     | 0.1.0   | CONFIRMED_RGB    | schema        | images/sequence/feature/image/shape | RGB confirmed via TFDS/RLDS schema.               |
| fractal20220817_data                                          | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| bridge                                                        | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| jaco_play                                                     | 0.1.0   | CONFIRMED_RGB    | schema        | image_wrist/image/shape             | RGB confirmed via TFDS/RLDS schema.               |
| berkeley_cable_routing                                        | 0.1.0   | CONFIRMED_RGB    | schema        | top_image/image/shape               | RGB confirmed via TFDS/RLDS schema.               |
| roboturk                                                      | 0.1.0   | CONFIRMED_RGB    | schema        | front_rgb/image/shape               | RGB confirmed via TFDS/RLDS schema.               |
| nyu_door_opening_surprising_effectiveness                     | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| berkeley_autolab_ur5                                          | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| toto                                                          | 0.1.0   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| droid                                                         | 1.0.1   | CONFIRMED_RGB    | schema        | exterior_image_left/image/shape     | RGB confirmed via TFDS/RLDS schema.               |
| conq_hose_manipulation                                        | 0.0.1   | CONFIRMED_RGB    | schema        | hand_color_image/image/shape        | RGB confirmed via TFDS/RLDS schema.               |
| dobbe                                                         | 0.0.1   | CONFIRMED_RGB    | schema        | wrist_image/image/shape             | RGB confirmed via TFDS/RLDS schema.               |
| fmb                                                           | 0.0.1   | CONFIRMED_RGB    | schema        | image_side_1/image/shape            | RGB confirmed via TFDS/RLDS schema.               |
| io_ai_tech                                                    | 0.0.1   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| mimic_play                                                    | 0.0.1   | CONFIRMED_RGB    | schema        | front_image_1/image/shape           | RGB confirmed via TFDS/RLDS schema.               |
| aloha_mobile                                                  | 0.0.1   | CONFIRMED_RGB    | schema        | cam_high/image/shape                | RGB confirmed via TFDS/RLDS schema.               |
| robo_set                                                      | 0.0.1   | CONFIRMED_RGB    | schema        | image_left/image/shape              | RGB confirmed via TFDS/RLDS schema.               |
| tidybot                                                       | 0.0.1   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| vima_converted_externally_to_rlds                             | 0.0.1   | CONFIRMED_RGB    | schema        | frontal_image/tensor/shape          | RGB confirmed via TFDS/RLDS schema.               |
| spoc                                                          | 0.0.1   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |
| plex_robosuite                                                | 0.0.1   | CONFIRMED_RGB    | schema        | image/image/shape                   | RGB confirmed via TFDS/RLDS schema.               |


