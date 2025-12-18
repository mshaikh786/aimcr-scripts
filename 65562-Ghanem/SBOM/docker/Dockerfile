FROM nvcr.io/nvidia/cuda:12.1.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# -----------------------------
# 1) OS deps (Python, build tools, common libs)
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv python3-dev \
    build-essential cmake ninja-build git curl ca-certificates pkg-config \
    libopenblas0 libomp5 \
    libjpeg-turbo8 libpng16-16 \
    ffmpeg libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Optional: make "python" available
RUN ln -sf /usr/bin/python3 /usr/local/bin/python

# -----------------------------
# 2) Create venv
# -----------------------------
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

# Upgrade pip tooling
RUN pip install --upgrade pip setuptools wheel

# -----------------------------
# 3) Install PyTorch 2.2.2 (CUDA 12.1 wheels)
# -----------------------------
RUN pip install --extra-index-url https://download.pytorch.org/whl/cu121 \
    torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2

# -----------------------------
# 4) Install PyG stack (matching torch 2.2.2 + cu121)
#    Prefer wheels from data.pyg.org (avoids compiling)
# -----------------------------
# NOTE: The PyG wheel index depends on Torch+CUDA version.
# For torch==2.2.2 and cu121:
ENV PYG_WHL_INDEX="https://data.pyg.org/whl/torch-2.2.2+cu121.html"

RUN pip install --no-cache-dir  --no-build-isolation \ 
    torch-scatter==2.1.2 \
    torch-sparse==0.6.18 \
    torch-cluster==1.6.3 \
    -f ${PYG_WHL_INDEX}

# Install torch-geometric itself.
# Your list says "pyg 2.5.2" (PyPI: pyg) but the main library is torch-geometric.
# We'll install torch-geometric==2.5.2 (the typical intended package).
RUN pip install --no-cache-dir torch-geometric==2.5.2

# -----------------------------
# 5) Install the remaining Python stack (pinned versions)
# -----------------------------
RUN pip install --no-cache-dir \
    pytorch-lightning==2.2.1 \
    torchmetrics==1.3.2 \
    accelerate==1.6.0 \
    numpy==1.26.4 \
    scipy==1.12.0 \
    pandas==2.2.1 \
    scikit-learn==1.4.1.post1 \
    matplotlib==3.8.3 \
    numba==0.59.1 \
    einops==0.7.0 \
    e3nn==0.5.5 \
    ase==3.23.0 \
    rdkit==2023.9.5 \
    deepchem==2.8.0 \
    transformers==4.51.3 \
    lmdb==1.4.1 \
    wandb==0.16.5

# -----------------------------
# 6) Quick sanity check (prints versions at build time)
# -----------------------------
RUN python - << 'PY'
import torch
print("torch:", torch.__version__, "cuda:", torch.version.cuda)
import torchvision, torchaudio
print("torchvision:", torchvision.__version__)
print("torchaudio:", torchaudio.__version__)
try:
    import torch_geometric
    print("torch_geometric:", torch_geometric.__version__)
except Exception as e:
    print("torch_geometric import failed:", e)
PY

WORKDIR /workspace
CMD ["bash"]

