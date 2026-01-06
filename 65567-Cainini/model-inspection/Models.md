# Models Mentioned in the Proposal

# 1️⃣ MultiWeave collaboration Framework 

## The proposal doesn't mention specific models to be used, instead they'll build a cross-model collaboration framework from scratch.

The main goal is Coordinating cross‑model collaboration among multiple large language models, implementing contextual bandit and baseline routing algorithms, logging, and evaluation.
However, they didn't specify which LLMs are going to be used.

**CPU Core hours requested:** 100,000
**GPU Core hours requested:** 100,000
**Base estimated GPU-hours:**
30,720 (core experiments)
+ 38,400 (scaling & ablations)
+ 28,800 (hyperparameter tuning, debugging, and new methods)
= 97,920 GPU-hours
**Minimum size of runs (CPUs nodes)** 1–8 nodes for pre/post‑processing batches as needed.
**Maximum size of runs (CPUs nodes)** N/A 
**Minimum size of runs (GPUs nodes)** 1 node (4 GH200 GPUs) for small models or 
prototype runs.
**Maximum size of runs (GPUs nodes)** Up to 64 nodes (256 GH200 GPUs) for tests 
that require larger models or extensive parallelization.

The project aims to implement the following algorithms:
* Contextual bandit algorithms implemented in PyTorch / Python.
Paper: https://arxiv.org/abs/2505.23720 
Author: Arun Verma (Singapore-MIT Alliance for Research and Technology)
*  Baseline routers: supervised gating networks, static policies based on model 
confidence, and simple ensemble strategies.
* Evaluation framework: orchestration of multiple LLMs using PyTorch + Transformers + vLLM for scalable inference.

---