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

## Open X-Embodiment RGB Availability Scan

This table summarizes the results of a programmatic inspection of datasets in the Open X-Embodiment collection that are
**publicly hosted on Google Cloud Storage (GCS)** rather than distributed via Hugging Face.
For each dataset, we attempted to retrieve the published metadata (`features.json`) from the official Open X-Embodiment
GCS bucket and identify the presence of real RGB image observations.

The `rgb_real` field indicates whether RGB observations are explicitly declared as available and non-placeholder in the
dataset metadata.

Errors reported in the table correspond to datasets whose metadata or data objects were not publicly accessible through
the GCS bucket at the time of inspection.

| dataset                                                       | version | rgb_real | note                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------|--------:|:--------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| language_table                                                |   0.1.0 |   True   | An RGB image of the scene.                                                                                                                                                                                                                                                                                                                     |
| stanford_hydra_dataset_converted_externally_to_rlds           |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| austin_buds_dataset_converted_externally_to_rlds              |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| furniture_bench_dataset_converted_externally_to_rlds          |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| cmu_franka_exploration_dataset_converted_externally_to_rlds   |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| ucsd_kitchen_dataset_converted_externally_to_rlds             |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| austin_sirius_dataset_converted_externally_to_rlds            |   0.1.0 |   True   | Wrist camera RGB observation.                                                                                                                                                                                                                                                                                                                  |
| utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds |   1.0.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| utokyo_saytap_converted_externally_to_rlds                    |   0.1.0 |   True   | Dummy wrist camera RGB observation.                                                                                                                                                                                                                                                                                                            |
| berkeley_mvp_converted_externally_to_rlds                     |   0.1.0 |   True   | Hand camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| kaist_nonprehensile_converted_externally_to_rlds              |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| dlr_sara_pour_converted_externally_to_rlds                    |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| asu_table_top_converted_externally_to_rlds                    |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| stanford_robocook_converted_externally_to_rlds                |   0.1.0 |   True   | Camera 1 RGB observation.                                                                                                                                                                                                                                                                                                                      |
| iamlab_cmu_pickup_insert_converted_externally_to_rlds         |   0.1.0 |   True   | Wrist camera RGB observation.                                                                                                                                                                                                                                                                                                                  |
| utaustin_mutex                                                |   0.1.0 |   True   | Wrist camera RGB observation.                                                                                                                                                                                                                                                                                                                  |
| berkeley_fanuc_manipulation                                   |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| cmu_playing_with_food                                         |   1.0.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| cmu_stretch                                                   |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| berkeley_gnm_cory_hall                                        |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| berkeley_gnm_sac_son                                          |   0.1.0 |   True   | Main camera RGB observation.                                                                                                                                                                                                                                                                                                                   |
| eth_agent_affordances                                         |   0.1.0 |  False   | Main camera RGB observation. Not available for this dataset, will be set to np.zeros.                                                                                                                                                                                                                                                          |
| kuka                                                          |   0.1.0 |   None   | features.json downloaded (kuka__0.1.0__features.json) but no image description hits                                                                                                                                                                                                                                                            |
| columbia_cairlab_pusht_real                                   |   0.1.0 |   None   | features.json downloaded (columbia_cairlab_pusht_real__0.1.0__features.json) but no image description hits                                                                                                                                                                                                                                     |
| robot_vqa                                                     |   0.1.0 |   None   | features.json downloaded (robot_vqa__0.1.0__features.json) but no image description hits                                                                                                                                                                                                                                                       |
| fractal20220817_data                                          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/fractal20220817_data/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/fractal20220817_data__0.1.0__features.json"' returned non-zero exit status 1.                                                                                   |
| bridge                                                        |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/bridge/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/bridge__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                               |
| taco_play                                                     |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/taco_play/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/taco_play__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                         |
| jaco_play                                                     |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/jaco_play/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/jaco_play__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                         |
| berkeley_cable_routing                                        |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/berkeley_cable_routing/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/berkeley_cable_routing__0.1.0__features.json"' returned non-zero exit status 1.                                                                               |
| roboturk                                                      |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/roboturk/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/roboturk__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                           |
| nyu_door_opening_surprising_effectiveness                     |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/nyu_door_opening_surprising_effectiveness/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/nyu_door_opening_surprising_effectiveness__0.1.0__features.json"' returned non-zero exit status 1.                                         |
| viola                                                         |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/viola/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/viola__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                                 |
| berkeley_autolab_ur5                                          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/berkeley_autolab_ur5/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/berkeley_autolab_ur5__0.1.0__features.json"' returned non-zero exit status 1.                                                                                   |
| toto                                                          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/toto/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/toto__0.1.0__features.json"' returned non-zero exit status 1.                                                                                                                   |
| stanford_kuka_multimodal_dataset_converted_externally_to_rlds |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/stanford_kuka_multimodal_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/stanford_kuka_multimodal_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1. |
| nyu_rot_dataset_converted_externally_to_rlds                  |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/nyu_rot_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/nyu_rot_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                                   |
| nyu_franka_play_dataset_converted_externally_to_rlds          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/nyu_franka_play_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/nyu_franka_play_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                   |
| maniskill_dataset_converted_externally_to_rlds                |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/maniskill_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/maniskill_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                               |
| ucsd_pick_and_place_dataset_converted_externally_to_rlds      |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/ucsd_pick_and_place_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/ucsd_pick_and_place_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.           |
| austin_sailor_dataset_converted_externally_to_rlds            |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/austin_sailor_dataset_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/austin_sailor_dataset_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                       |
| bc_z                                                          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/bc_z/1.0.1/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/bc_z__1.0.1__features.json"' returned non-zero exit status 1.                                                                                                                   |
| usc_cloth_sim_converted_externally_to_rlds                    |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/usc_cloth_sim_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/usc_cloth_sim_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                                       |
| utokyo_pr2_opening_fridge_converted_externally_to_rlds        |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/utokyo_pr2_opening_fridge_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/utokyo_pr2_opening_fridge_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.               |
| utokyo_xarm_pick_and_place_converted_externally_to_rlds       |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/utokyo_xarm_pick_and_place_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/utokyo_xarm_pick_and_place_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.             |
| utokyo_xarm_bimanual_converted_externally_to_rlds             |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/utokyo_xarm_bimanual_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/utokyo_xarm_bimanual_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                         |
| robo_net                                                      |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/robo_net/1.0.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/robo_net__1.0.0__features.json"' returned non-zero exit status 1.                                                                                                           |
| berkeley_rpt_converted_externally_to_rlds                     |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/berkeley_rpt_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/berkeley_rpt_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                                         |
| stanford_mask_vit_converted_externally_to_rlds                |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/stanford_mask_vit_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/stanford_mask_vit_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                               |
| tokyo_u_lsmo_converted_externally_to_rlds                     |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/tokyo_u_lsmo_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/tokyo_u_lsmo_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                                         |
| dlr_sara_grid_clamp_converted_externally_to_rlds              |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/dlr_sara_grid_clamp_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/dlr_sara_grid_clamp_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                           |
| dlr_edan_shared_control_converted_externally_to_rlds          |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/dlr_edan_shared_control_converted_externally_to_rlds/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/dlr_edan_shared_control_converted_externally_to_rlds__0.1.0__features.json"' returned non-zero exit status 1.                   |
| imperialcollege_sawyer_wrist_cam                              |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/imperialcollege_sawyer_wrist_cam/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/imperialcollege_sawyer_wrist_cam__0.1.0__features.json"' returned non-zero exit status 1.                                                           |
| qut_dexterous_manipulation                                    |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/qut_dexterous_manipulation/"' returned non-zero exit status 1.                                                                                                                                                                                                                  |
| uiuc_d3field                                                  |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/uiuc_d3field/1.1.2/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/uiuc_d3field__1.1.2__features.json"' returned non-zero exit status 1.                                                                                                   |
| cmu_play_fusion                                               |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/cmu_play_fusion/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/cmu_play_fusion__0.1.0__features.json"' returned non-zero exit status 1.                                                                                             |
| berkeley_gnm_recon                                            |    None |  False   | error: Command 'gsutil cp "gs://gdm-robotics-open-x-embodiment/berkeley_gnm_recon/0.1.0/features.json" "/ibex/project/c2320/dataset-check/huggingface/oxe_peek/features_scan/berkeley_gnm_recon__0.1.0__features.json"' returned non-zero exit status 1.                                                                                       |
| droid                                                         |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/droid/"' returned non-zero exit status 1.                                                                                                                                                                                                                                       |
| conq_hose_manipulation                                        |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/conq_hose_manipulation/"' returned non-zero exit status 1.                                                                                                                                                                                                                      |
| dobbe                                                         |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/dobbe/"' returned non-zero exit status 1.                                                                                                                                                                                                                                       |
| fmb                                                           |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/fmb/"' returned non-zero exit status 1.                                                                                                                                                                                                                                         |
| io_ai_tech                                                    |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/io_ai_tech/"' returned non-zero exit status 1.                                                                                                                                                                                                                                  |
| mimic_play                                                    |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/mimic_play/"' returned non-zero exit status 1.                                                                                                                                                                                                                                  |
| aloha_mobile                                                  |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/aloha_mobile/"' returned non-zero exit status 1.                                                                                                                                                                                                                                |
| robo_set                                                      |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/robo_set/"' returned non-zero exit status 1.                                                                                                                                                                                                                                    |
| tidybot                                                       |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/tidybot/"' returned non-zero exit status 1.                                                                                                                                                                                                                                     |
| vima_converted_externally_to_rlds                             |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/vima_converted_externally_to_rlds/"' returned non-zero exit status 1.                                                                                                                                                                                                           |
| spoc                                                          |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/spoc/"' returned non-zero exit status 1.                                                                                                                                                                                                                                        |
| plex_robosuite                                                |    None |  False   | error: Command 'gsutil ls "gs://gdm-robotics-open-x-embodiment/plex_robosuite/"' returned non-zero exit status 1.                                                                                                                                                                                                                              |


