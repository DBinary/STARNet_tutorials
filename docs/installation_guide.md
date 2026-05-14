# STARNet Installation Guide

## Prerequisites

STARNet currently supports **Python 3.11** for the validated installation workflow in this repository.

We recommend installing STARNet inside a fresh `conda` or `mamba` environment to avoid dependency conflicts.

### Platform Requirements

STARNet is developed and tested on Linux. macOS and Windows (WSL) may work but are not actively validated.

## Installation Methods

First, clone the official STARNet repository and enter the repository root:

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
```

### Quick Install (Recommended)

The quick installer creates a ready-to-use STARNet environment from the files bundled with the cloned repository. It will:

- create or update a dedicated conda environment
- install the pinned Python dependencies
- install STARNet in editable mode from the local repository checkout
- verify that `import STARNet as ST` succeeds

```bash
bash install.sh
```

By default this creates an environment named `starnet`, uses your existing `conda` and `pip` mirror configuration first, and installs the GPU-enabled dependency set pinned in this repository. If the active pip mirror fails during wheel download, the installer retries once with official PyPI. You can override the environment name if needed:

```bash
bash install.sh --env-name starnet-review
```

### Conda / Mamba Installation

If you prefer to run the steps manually, create the conda environment first and then install the pinned Python packages.

#### Mamba

```bash
mamba env create -n starnet -f environment-conda.yml
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
conda run -n starnet python -m pip install --no-deps --no-build-isolation -e .
```

#### Conda

```bash
conda env create -n starnet -f environment-conda.yml
conda run -n starnet python -m pip install -r requirements-review.txt || \
  PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple PIP_EXTRA_INDEX_URL= \
  conda run -n starnet python -m pip install -r requirements-review.txt
conda run -n starnet python -m pip install --no-deps --no-build-isolation -e .
```

After either method, activate the environment:

```bash
conda activate starnet
```

This pinned environment is the most stable installation path for users and the preferred workflow for reproducing the tutorial and manuscript environment.

## Usage

After installation, verify that STARNet imports correctly:

```python
import STARNet as ST
```

## Troubleshooting

### pip Mirror / Wheel Download Errors

The STARNet environment installs GPU-enabled PyTorch dependencies, so the download can be large. The quick installer uses your active `pip` configuration first. If the active pip mirror fails, it retries once with official PyPI automatically.

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
