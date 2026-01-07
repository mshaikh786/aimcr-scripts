    # Models Mentioned in the Proposal


## Project-Specific Models

Insert comment/remove section if not applicable

- Coordinate-based MLP Neural Networks 

---

## Coordinate-based MLP Neural Networks

- **Architecture:** Fully connected MLPs mapping spatial–temporal coordinates → climate variable values  

- **Framework:** PyTorch + PyTorch Lightning

- **Training:** From scratch (no pretrained weights)

- **Purpose:**
  - Serve as **predictors** in an error-bounded scientific data compression pipeline
  - Replace gridded climate fields with a continuous neural representation

- **Variables modeled:**
  - Geopotential
  - Temperature
  - U wind component
  - V wind component
  - Vertical velocity
  - Specific humidity

- **Model variants:**
  - **Widths:** 512 and 2,048
  - **Training objectives:** Mean Squared Error (MSE) and Absolute Error (L1)

- **Scale:**

    -   Trained on very large datasets (~200 GB per variable)
    -   Separate models per variable (6 variables × 4 model variants).
    This results in **6 separate base models**.
---

## Maximum Number of GPUs and GPU Hours

- **Max GPUS:** Uses **10 Node = 40 H200 GPUs**
- **GPU Hours:** 217,728 H200 GPU hours
---