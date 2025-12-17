# CinePile

## Maintainer / Author

**Maintainer (dataset distributor):**  
Hugging Face user / organization **tomg-group-umd**  
https://huggingface.co/tomg-group-umd

**Affiliated organization:**  
**University of Maryland (UMD)** – TOMG Group (Theoretical and Observational Media Group)

---

## Artifact Related to a Paper

**Yes.**  
The dataset is associated with the [paper](arxiv:2405.08813):

> **“CinePile: A Long Video Dataset for Multimodal Reasoning and Understanding”**

- Focused on **long-form movie understanding**
- Targets **multimodal reasoning**, including vision, language, and temporal context
- Introduced to support evaluation and training of **long-context video–language models**

---

## Maintainer’s Public Presence

- Hugging Face profile:  
  https://huggingface.co/tomg-group-umd

- Academic affiliation:  
  University of Maryland (UMD), research group–maintained dataset

- Public presence primarily through:
    - Hugging Face datasets
    - Associated academic publication(s)

---

## Dataset Source / Provenance

**Primary dataset URL (Hugging Face):**  
https://huggingface.co/datasets/tomg-group-umd/cinepile

**Source type:**  
Curated **movie-based video–language dataset**, constructed for research purposes.

**Provenance notes:**

- Data is derived from **movie clips / long-form cinematic content**
- Intended for **research and benchmarking** in multimodal AI
- Not a crowdsourced dataset; professionally curated and annotated

---

## Repository Metadata

- **Dataset hosting:** Hugging Face Datasets
- **Maintainer:** tomg-group-umd (academic group)
- **last commit:** 1 yar ago
- **commits:** 23
- **Access method:** Direct download via Hugging Face `datasets` library

---

## Licensing & Usage Notes

- License: Refer to the Hugging Face dataset card (research-oriented license)

- Permitted use:

    - Academic research

    - Model training & evaluation

- Restrictions:

    - subject to non-commercial or attribution requirements

    - Underlying movie content may carry additional constraints

---

## Dataset Inspection

### Methodology

- The dataset was accessed using **Hugging Face streaming mode** to avoid full downloads.
- A representative example was inspected programmatically.
- The inspection focused on:
    - Dataset keys and value types
    - Presence of Hugging Face media features (`Video`, `Image`)
    - Existence of media-like fields (`bytes`, `path`)
    - Use of external media references (e.g., URLs)

No media files were downloaded during this process.

---

### Findings

#### 1. Media Storage

- No video files are stored in the dataset
- No image files are stored in the dataset
- No Hugging Face `Video` or `Image` feature types
- No fields containing binary media (`bytes`) or file paths

#### 2. External Media References

- The dataset includes **external YouTube links** (e.g., clip URLs)
- These links act as **references only**
- The dataset itself does **not** contain thumbnails, frames, or clips

#### 3. Data Modality

The dataset is composed entirely of structured **textual data**, including:

- Movie metadata (e.g., title, year, genre)
- Scene descriptions
- Subtitle transcripts
- Multiple-choice question–answer pairs
- External references for visual grounding (URLs)
