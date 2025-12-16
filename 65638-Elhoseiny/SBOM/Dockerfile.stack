FROM nvcr.io/nvidia/pytorch:25.05-py3

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir \
    deepspeed==0.18.2 \
    accelerate==1.12.0 \
    transformers==4.57.3 
