# STARNet
STARNet (**S**pa**T**i**A**l RNA-ATAC-seq gene **R**egulatory **Net**work) is a computational framework designed to decipher spatially specific gene regulatory networks (GRNs) from spatial RNA-ATAC-seq data.

## STARNet Tutorials
Please refer to the official [STARNet tutorials](https://starnet-tutorials.readthedocs.io/) for detailed guides and documentation.

## STARNet Installation

Currently, `STARNet` is not available for direct installation from PyPI (the Python Package Index). To use the package, you must clone the source code from its Git repository and install it locally.

### Installation Steps

Follow these steps in your terminal to get `STARNet` set up in your local environment.

**1. Clone the Repository**

First, use `git` to clone the `STARNet` repository to your local machine.

```bash
git clone https://github.com/DBinary/STARNet.git
```


**2. Navigate to the Directory**

Once the repository is cloned, change your current directory to the newly created `STARNet` folder.

```bash
cd STARNet
```

**3. Install the Package**

Now, you can install the package using `pip`.

```bash
pip install -e .
```

### Usage

After the installation is complete, you can import and use `STARNet` in your Python scripts or interactive sessions like this:

```python
import STARNet as ST
```
