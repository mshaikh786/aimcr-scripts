import importlib
import sys

packages = {
    "torch": "torch",
    "torchvision": "torchvision",
    "torchaudio": "torchaudio",
    "torch_geometric": "torch_geometric",
    "torch_scatter": "torch_scatter",
    "torch_sparse": "torch_sparse",
    "torch_cluster": "torch_cluster",
    "pytorch_lightning": "pytorch_lightning",
    "torchmetrics": "torchmetrics",
    "accelerate": "accelerate",
    "numpy": "numpy",
    "scipy": "scipy",
    "pandas": "pandas",
    "scikit_learn": "sklearn",
    "matplotlib": "matplotlib",
    "numba": "numba",
    "einops": "einops",
    "e3nn": "e3nn",
    "ase": "ase",
    "rdkit": "rdkit",
    "deepchem": "deepchem",
    "transformers": "transformers",
    "lmdb": "lmdb",
    "wandb": "wandb",
}

print(f"Python version: {sys.version}\n")

for name, module_name in packages.items():
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"{name:20s}: {version}")
    except Exception as e:
        print(f"{name:20s}: FAILED ({e})")
