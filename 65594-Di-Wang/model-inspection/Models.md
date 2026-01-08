# Models Mentioned in the Proposal

## Explicitly Named Foundation / LLM Models

- [LLaMA](#llama)  
- [Qwen](#qwen)  
- [Megatron-LM](#megatron-lm)

---

## LLaMA 
**Family:** LLaMA  
**Source:** Meta AI (open research release)  
**Documentation / Model Card Links:**  
- https://arxiv.org/abs/2302.13971
- https://github.com/meta-llama/llama

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**LLaMA (Large Language Model Meta AI)** is a family of open-source transformer language models introduced by **Meta AI**. The original LLaMA paper presents models ranging from **7 billion to 65 billion parameters**, showing state-of-the-art performance on a wide range of NLP benchmarks using publicly available data and scaled training procedures.

#### 1.2 Who owns it?
- **Owner:** Meta AI  
- **Organization:** Meta Platforms, Inc.

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:** Not specified.  

---

#### 2.2 Training Token Count
- **Training data scale:** Trillions of tokens of multilingual and diverse corpora.  
The LLaMA paper emphasizes using **publicly available datasets** spanning web text, books, and code.

- **Token count:** LLaMA models were pretrained on up to **9 trillion tokens** from publicly available sources.

---

#### 2.3 MFU / Training Compute Utilization
- The published work does not release formal MFU (Megaflop Utilization) metrics.  

---

## Qwen  
**Family:** Qwen (Tongyi Qianwen)  
**Source:** QwenLM / Alibaba Cloud  
**Documentation / Code Links:**  
- https://github.com/QwenLM/Qwen
- https://arxiv.org/abs/2309.16609

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**Qwen** is a transformer-based language model in the **Qwen (Tongyi Qianwen)** series released by **Alibaba Cloud’s QwenLM project**. The model has been open sourced along with technical memos and is available via GitHub and model hubs (e.g., ModelScope / Hugging Face).

Qwen is designed for general-purpose language understanding and generation tasks and includes support for long contexts (up to ~8 K tokens in enhanced versions).

#### 1.2 Who owns it?
- **Owner:** QwenLM (Alibaba Cloud)  
- **Organization:** Alibaba Cloud’s research and open-source initiative

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Approximate parameter count:** Not specified.

---

#### 2.2 Training Token Count
- **Training data scale:**  
  - The model is reportedly pretrained on a **self-constructed corpus exceeding 2 trillion tokens** spanning multilingual text, web data, and code.

---

#### 2.3 MFU / Training Compute Utilization
- No official training compute or MFU figures are disclosed.

---

## Megatron-LM  
**Family:** Megatron-LM  
**Source:** NVIDIA (open research codebase)  
**Documentation / Code Links:**  
- https://github.com/NVIDIA/Megatron-LM (training framework) 
- https://arxiv.org/abs/1909.08053 (Megatron-LM training paper)

---

### 1. Source / Provenance

#### 1.1 Where is it coming from?

**Megatron-LM** is an open-source research codebase and methodology developed by **NVIDIA** for efficient training of **multi-billion parameter transformer language models**. It provides a suite of model-parallel training techniques enabling scaling to billions of parameters on GPU clusters.

The associated research paper demonstrates training of models up to ~8.3 B parameters using intra-layer and pipeline parallelism strategies. 

Megatron-LM itself is a **training framework**, not a single fixed pretrained model, and has been widely used as the foundation for many large language models and variants (e.g., GPT-style architectures).

#### 1.2 Who owns it?
- **Owner:** NVIDIA  
- **Organization:** NVIDIA Applied Deep Learning Research

---

### 2. Model Characteristics

#### 2.1 Number of Trainable Parameters
- **Parameter count:** Depends on configuration  
  - Models trained via Megatron-LM can range from millions to tens or hundreds of billions of parameters depending on architecture and training setup.  
  - No specific number specified.

---

#### 2.2 Training Token Count
- **Training data scale:** Varies by model and use case.  
  - Megatron-LM itself is a framework; it does not prescribe a specific token count.  

---

#### 2.3 MFU / Training Compute Utilization

- Scalability of Looped Transformer (1.7B) Training Under Pure Data Parallelism (DP) Benchmark results collected from representative runs on GH200-class GPUs (similar architecture to Shaheen III). 

| Node | Global Batch Size | MFU (%)  | Throughput (Tokens/s) |
|------|-------------------|----------|------------------------|
| 1    | 512               | 40–42%   | 100% (baseline)        |
| 2    | 512               | 41–43%   | 195%                   |
| 4    | 512               | 43–45%   | 380%                   |
| 8    | 512               | 42–44%   | 710%                   |
| 16   | 512               | 43–45%   | 1140%                  |


