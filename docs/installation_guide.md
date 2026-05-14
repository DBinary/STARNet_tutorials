# STARNet Installation Guide

STARNet is installed from source. The recommended workflow below clones the official STARNet repository, creates a fresh environment, installs the pinned dependencies, and verifies the import.

::::{grid} 1 1 3 3
:gutter: 2

:::{grid-item-card} 1. Clone
Get the official STARNet source repository.
:::

:::{grid-item-card} 2. Install
Create a reproducible `starnet` environment with micromamba.
:::

:::{grid-item-card} 3. Verify
Activate the environment and confirm that `import STARNet as ST` works.
:::

::::

## Prerequisites

- Linux is the validated platform. macOS and Windows through WSL may work but are not actively tested.
- A working `micromamba` or `conda` installation is required.
- Python **3.11** is used by the validated environment in this repository.
- GPU-enabled dependencies are installed by default because STARNet's GRN workflows use GPU-accelerated model components.

## Quick Install

Use this micromamba path unless you need to customize each installation step.

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
micromamba env create -n starnet -f environment-conda.yml
micromamba run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  micromamba run -n starnet python -m pip install -r requirements-review.txt
micromamba run -n starnet python -m pip install --no-deps --no-build-isolation -e .
micromamba activate starnet
```

These commands will:

- create a dedicated environment named `starnet`
- install the pinned Python dependencies
- install STARNet in editable mode from the local repository checkout
- activate the environment for tutorial use

## Manual Install

If you prefer conda, or want to compare the full command sequence by environment manager, clone the repository first:

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
```

::::{tab-set}

:::{tab-item} Micromamba
```bash
micromamba env create -n starnet -f environment-conda.yml
micromamba run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  micromamba run -n starnet python -m pip install -r requirements-review.txt
micromamba run -n starnet python -m pip install --no-deps --no-build-isolation -e .
micromamba activate starnet
```
:::

:::{tab-item} Conda
```bash
conda env create -n starnet -f environment-conda.yml
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
conda run -n starnet python -m pip install --no-deps --no-build-isolation -e .
conda activate starnet
```
:::

::::

## Verify

After activation, verify that STARNet imports correctly:

```python
import STARNet as ST
```

## Troubleshooting

### pip Mirror / Wheel Download Errors

STARNet installs GPU-enabled PyTorch dependencies, so downloads can be large. The quick install commands use your active `pip` configuration first. If that fails during wheel download, retry once with official PyPI.

For manual installation, use the same fallback pattern:

::::{tab-set}

:::{tab-item} Micromamba
```bash
micromamba run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  micromamba run -n starnet python -m pip install -r requirements-review.txt
```
:::

:::{tab-item} Conda
```bash
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
```
:::

::::

### libstdc++ / CXXABI Errors

On some systems, the system `libstdc++` may be picked before the active environment, causing errors for optional genomics tooling. If this happens, export the active environment library path before running GRN inference:

```bash
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
```

### GPU Support

GPU support is part of the recommended environment because STARNet's GRN workflows depend on GPU-accelerated model components. For optional CuPy acceleration, install the CuPy build matching your CUDA toolkit after STARNet is installed.
