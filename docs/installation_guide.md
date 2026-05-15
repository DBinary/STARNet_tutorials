# STARNet Installation Guide

STARNet is installed from source. The recommended workflow below clones the official STARNet repository, creates a fresh environment, installs the pinned dependencies, and verifies the import.

::::{grid} 1 1 3 3
:gutter: 2

:::{grid-item-card} 1. Prepare
Install prerequisites (git, conda or micromamba).
:::

:::{grid-item-card} 2. Install
Create a reproducible `starnet` environment and install STARNet.
:::

:::{grid-item-card} 3. Verify
Activate the environment and confirm that STARNet works correctly.
:::

::::

## Prerequisites

- **Linux** is the validated platform. macOS and Windows through WSL may work but are not actively tested.
- **Python 3.11** — managed by conda/micromamba, not your system Python.
- **git** — [install git](https://git-scm.com/downloads)
- **conda** (recommended) or **micromamba**:
  - [Miniforge](https://github.com/conda-forge/miniforge) (conda + conda-forge)
  - [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) (standalone, faster alternative)
- **`curl`** — needed by the Miniforge installer (pre-installed on most Linux distributions).
- **Disk space**: ~3 GB for packages (mainly PyTorch + CUDA libraries).
- **GPU**: NVIDIA GPU with driver supporting CUDA ≥ 12.8 (PyTorch 2.10 ships with CUDA 12.8 libraries).

:::{dropdown} Check what you already have
```bash
git --version
conda --version || micromamba --version
nvidia-smi  # check GPU driver / CUDA version
```
:::

## Install

The recommended approach uses conda. Switch to the micromamba tab if you prefer it.

**Estimated time**: 5–20 minutes depending on network speed (most time is spent downloading ~3 GB of packages).

````{tab-set}

```{tab-item} Conda (recommended)
git clone https://github.com/DBinary/STARNet.git
cd STARNet
conda env create -n starnet -f environment-conda.yml
conda run -n starnet python -m pip install -r requirements-review.txt
conda run -n starnet python -m pip install --no-deps -e .
conda activate starnet
```

```{tab-item} Micromamba
git clone https://github.com/DBinary/STARNet.git
cd STARNet
micromamba env create -n starnet -f environment-conda.yml
micromamba run -n starnet python -m pip install -r requirements-review.txt
micromamba run -n starnet python -m pip install --no-deps -e .
micromamba activate starnet
```

````

:::{note}
The `pip install -r requirements-review.txt` step installs all runtime dependencies (~200 packages). The subsequent `pip install --no-deps -e .` only registers STARNet itself — it assumes the requirements step succeeded, so **do not skip or reorder these steps**.
:::

## Verify

After activation, run these checks:

```python
# 1. Basic import and key submodules
import STARNet as ST
from STARNet import grn, model, pl, pp

# 2. GPU availability (required for GRN workflows)
import torch
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("WARNING: No GPU detected. Training will fall back to CPU.")
```

Expected output on a GPU machine:

```
CUDA available: True
GPU: NVIDIA GeForce RTX 4090
```

If the import succeeds without errors, STARNet is installed correctly.

## Troubleshooting

### Slow downloads / hash mismatches

STARNet downloads ~3 GB of GPU-enabled PyTorch dependencies. If `https://pypi.org/simple` is slow in your region, you can temporarily use a mirror. However, `requirements-review.txt` pins exact SHA256 hashes, and some mirrors serve wheels with mismatched hashes, causing errors like:

```
THESE PACKAGES DO NOT MATCH THE HASHES
```

If you hit this, remove the `-i` flag and retry with the default PyPI index:

````{tab-set}

```{tab-item} Conda
conda run -n starnet python -m pip install \
  -r requirements-review.txt
```

```{tab-item} Micromamba
micromamba run -n starnet python -m pip install \
  -r requirements-review.txt
```

````

### libstdc++ / CXXABI Errors

On some systems, the system `libstdc++` may be picked before the active environment, causing errors for optional genomics tooling. If this happens, export the active environment library path before running GRN inference:

```bash
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
```

### GPU

GPU support is enabled by default because STARNet's GRN workflows depend on GPU-accelerated model components. If `torch.cuda.is_available()` returns `False`:

1. Check your NVIDIA driver: `nvidia-smi`
2. Verify driver supports CUDA ≥ 12.8 (PyTorch 2.10 requirement)
3. Older GPUs (compute capability < 7.0) may require a CPU-only PyTorch build

For optional CuPy acceleration, install the CuPy build matching your CUDA toolkit after STARNet is installed.
