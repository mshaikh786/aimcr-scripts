# LLaVA-Video-178K

## Maintainer / Author

**Maintainer (dataset distributor):**  
Hugging Face organization **lmms-lab**  
https://huggingface.co/lmms-lab

**Affiliated organization / lab:**  
**LMMS-Lab (Large Multimodal Models Lab)**  
https://github.com/LMMS-Lab

---

## Artifact Related to a Paper

**Yes (research-line artifact).**  
The dataset is released as part of the **LLaVA / Video-LLaVA** research line, extending LLaVA from image–language to **video–language instruction tuning**.

Relevant papers include:

> **“LLaVA: Large Language and Vision Assistant”**  
> and follow-up works on **Video-LLaVA / multimodal instruction tuning**

- The dataset itself is **not a standalone benchmark**
- It serves as a **large-scale training corpus** supporting the Video-LLaVA models

---

## Maintainer’s Public Presence

- Hugging Face organization page:  
  https://huggingface.co/lmms-lab

- GitHub organization:  
  https://github.com/LMMS-Lab

- Academic presence via LLaVA and multimodal model publications (arXiv, conferences)

> No individual maintainer LinkedIn profiles are listed on the dataset card (lab-maintained release).

---

## Dataset Source / Provenance

**Primary dataset URL (Hugging Face):**  
https://huggingface.co/datasets/lmms-lab/LLaVA-Video-178K

**GitHub repository (codebase & ecosystem):**  
https://github.com/LMMS-Lab/LLaVA-NeXT

> The dataset does **not** have a standalone GitHub repository; it is distributed and referenced through the broader LLaVA / LLaVA-NeXT codebase.

---

## Repository Metadata

**Repository:** LLaVA-NeXT  
https://github.com/LMMS-Lab/LLaVA-NeXT

- **Maintainer:** LMMS-Lab (organization-owned repository)
- **Last commit:** Within the last year (active research repository)

### Repository activity (codebase-level)
- **Commits:** Hundreds (actively developed)
- **Issues:** Dozens (open and closed)
- **Pull Requests:** Active community and internal contributions
- **Stars:** ~2,000+

> Note: These statistics apply to the **code repository**, not a dataset-only repo.

- HuggingFace: Downloads last month 25,139

---

## License Conditions

**Declared license (Hugging Face):**  
Research-oriented license with **mixed upstream provenance**

### Permissibility

-  Academic and research use
-  Model training for non-commercial research
- ⚠ Redistribution of raw videos requires caution
-  Commercial / production use without provenance audit is **not recommended**

### Important Licensing Note

The dataset aggregates videos from **multiple upstream sources** with potentially different licenses.  
Use of the dataset **does not grant blanket rights** over all included video content.

For compliance-sensitive usage:
- Treat as **research-only**
- Avoid redistributing raw video files
- Audit or filter samples if downstream redistribution or deployment is intended

---

# LLaVA-Video-178K — Video Storage & Provenance Clarification

## Summary

During inspection and sampling of **LLaVA-Video-178K**, we observed that a significant portion of video paths
(e.g. `academic_source/.../*.mp4`) **do not exist in the Hugging Face dataset repository** and therefore cannot be
downloaded or visualized directly via `hf_hub_download`.

This behavior is **expected and intentional**, not an error in the inspection pipeline.

---

## Where Are the Missing Videos?

The dataset mixes **multiple upstream sources**. Only a subset of videos is physically hosted on Hugging Face.
The rest are **references to external academic datasets**, redistributed as **metadata-only pointers** due to
licensing constraints.

### Source Types Observed

#### 1. Hugging Face–Hosted Videos (Packaged)
These videos are stored directly in the HF dataset repository and are downloadable.

**Example paths:**
- `liwei_youtube_videos/videos/youtube_video_2024/ytb_<id>.mp4`

**Status:**
- ✅ Downloadable via `hf_hub_download`
- ✅ Direct visualization possible

---

#### 2. Academic Source Videos (External – Not Hosted on HF)

These paths point to videos from **existing academic datasets** that are **not redistributed** on Hugging Face.

**Observed prefixes and their upstream datasets:**

| Path Prefix | Upstream Dataset | Notes |
|------------|------------------|------|
| `academic_source/youcook2/` | YouCook2 | Requires separate download; clips may need to be segmented |
| `academic_source/Charades/` | Charades | Official dataset access required |
| `academic_source/NextQA/` | NExT-QA | Scene-based video structure |
| `*_activitynet` configs | ActivityNet / ActivityNet-QA | HF splits appear metadata-only |

**Status:**
-  Not present in HF repo
- `hf_hub_download` returns 404
- Requires manual acquisition of upstream datasets

---

#### 3. Mixed / Special Cases

- `llava_hound` and some YouTube-based configs may reference videos that are:
  - partially hosted on HF
  - or derived from YouTube IDs with local packaging
- Each must be checked against the HF repo file index

---

## Why This Design Exists

- Many academic video datasets **do not permit redistribution** of raw video files
- LLaVA-Video-178K therefore distributes:
  - instructions
  - annotations
  - dataset structure
  - not all video binaries

---

## Practical Implications for Analysis & Visualization

### For Academic Source Videos
You must:
1. Obtain the upstream dataset separately (per its license)
2. Store videos locally
3. Map HF-relative paths to local filesystem paths

**Example mapping:**
```text
academic_source/Charades/ZS2WD.mp4
→ $CHARADES_ROOT/ZS2WD.mp4
