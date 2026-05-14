# STARNet Installation Guide

STARNet is installed from source. The recommended workflow below clones the official STARNet repository, creates a fresh conda environment, installs the pinned dependencies, and verifies the import.

::::{grid} 1 1 3 3
:gutter: 2

:::{grid-item-card} 1. Clone
Get the official STARNet source repository.
:::

:::{grid-item-card} 2. Install
Run the quick installer to create a reproducible `starnet` environment.
:::

:::{grid-item-card} 3. Verify
Activate the environment and confirm that `import STARNet as ST` works.
:::

::::

## Prerequisites

- Linux is the validated platform. macOS and Windows through WSL may work but are not actively tested.
- A working `conda` or `mamba` installation is required.
- Python **3.11** is used by the validated environment in this repository.
- GPU-enabled dependencies are installed by default because STARNet's GRN workflows use GPU-accelerated model components.

## Quick Install

Use this path unless you need to customize each installation step.

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
bash install.sh
```

The installer will:

- create or update a dedicated conda environment named `starnet`
- install the pinned Python dependencies
- install STARNet in editable mode from the local repository checkout
- verify that `import STARNet as ST` succeeds

To use a different environment name:

```bash
bash install.sh --env-name starnet-review
```

After installation, activate the environment:

```bash
conda activate starnet
```

## Manual Install

If you prefer to run the steps manually, clone the repository first:

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
```

::::{tab-set}

:::{tab-item} Mamba
```bash
mamba env create -n starnet -f environment-conda.yml
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
conda run -n starnet python -m pip install --no-deps --no-build-isolation -e .
conda activate starnet
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

STARNet installs GPU-enabled PyTorch dependencies, so downloads can be large. The quick installer uses your active `pip` configuration first. If that fails during wheel download, it retries once with official PyPI.

For manual installation, use the same fallback pattern:

```bash
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
```

### libstdc++ / CXXABI Errors

On some systems, the system `libstdc++` may be picked before the active conda environment, causing errors for optional genomics tooling. If this happens, export the active environment library path before running GRN inference:

```bash
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
```

### GPU Support

GPU support is part of the recommended environment because STARNet's GRN workflows depend on GPU-accelerated model components. For optional CuPy acceleration, install the CuPy build matching your CUDA toolkit after STARNet is installed.
