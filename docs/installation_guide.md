# STARNet Installation Guide

## Prerequisites

STARNet requires **Python 3.11**. Other Python versions are not claimed as supported unless separately validated.

We recommend installing STARNet within a `conda` environment to avoid dependency conflicts.

### Platform Requirements

STARNet is developed and tested on Linux. macOS and Windows (WSL) may work but are not actively validated.

## Installation Methods

### Source Installation (Recommended)

Currently, STARNet is not available on PyPI. Install directly from the GitHub repository:

**1. Clone the Repository**

```bash
git clone https://github.com/DBinary/STARNet.git
```

**2. Create and Activate a Conda Environment**

```bash
conda create -n starnet python=3.11
conda activate starnet
```

**3. Install STARNet**

```bash
cd STARNet
pip install -e .
```

### Unified Environment Installation

For a validated, reproducible environment with pinned dependencies:

```bash
conda env create -f environment-review.yml
conda activate starnet-review
python -m pip install -e .
```

This method uses the `environment-review.yml` file bundled in the repository and is the preferred workflow for reproducing manuscript results.

## Usage

After installation, verify that STARNet imports correctly:

```python
import STARNet as ST
```

## Troubleshooting

### libstdc++ / CXXABI Errors

On some systems, the system `libstdc++` may be picked before the active conda environment, causing errors for optional genomics tooling. If this happens, export the active environment library path before running GRN inference:

```bash
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
```

### GPU Support

For GPU acceleration, install the appropriate CuPy build for your CUDA toolkit after installing STARNet.
