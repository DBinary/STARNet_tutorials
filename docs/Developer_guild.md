# Developer Guide

!!! Note
    To better understand STARNet, you may check out our [preprint](https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2) first to learn about the general idea.

Below we describe the main components of the framework, and how to extend the existing implementations.

## Framework

The STARNet code is stored in the [`src/STARNet`](https://github.com/DBinary/STARNet/tree/master/src/STARNet) folder in the GitHub repository, with the `__init__.py` file taking care of lazy module loading.

A STARNet framework is primarily composed of 5 components:

- `grn`: Gene Regulatory Network inference, including peak-to-gene linking, motif scanning, and GRN construction.
- `pp`: Preprocessing and downstream analysis, including peak-gene association extraction, GRN scoring, TF module scoring, and GWAS utilities.
- `pl`: Plotting utilities for GRN, GWAS, and spatial visualization.
- `model`: The STARNet deep-learning model (PyTorch Geometric-based) for integrating spatial RNA and ATAC data.
- `external`: Vendored third-party packages (e.g., scglue, SEACells, scdrs, palantir, epiverse) to avoid installation conflicts.

All public functions are exposed through the top-level `STARNet` namespace via lazy loading in `__init__.py`.

## For Developers

### External Module

In most cases, integrating an existing package is preferable to re-implementing it. We can directly clone the entire package from GitHub and move the folder into the `external` directory. During this process, pay attention to:

1. **License compatibility** with STARNet's MIT license.
2. **Import hygiene**: Change top-level imports of packages that are not STARNet dependencies to function-level imports.

This is incorrect because `dgl` is not in STARNet's default requirements:

```python
import dgl

def calculate():
    dgl.run()
```

The correct approach:

```python
def calculate():
    import dgl
    dgl.run()
```

We recommend using `try/except` to detect import errors and guide users to the correct installation page:

```python
def calculate():
    try:
        import dgl
    except ImportError:
        raise ImportError(
            'Please install dgl from https://www.dgl.ai/pages/start.html'
        )
    dgl.run()
```

### Main Module

If you want to contribute a new feature, identify which module it belongs to:

- `grn` → algorithms for GRN inference
- `pp` → preprocessing and downstream analysis utilities
- `pl` → plotting functions
- `model` → neural network components

Add a new file (e.g., `_newfeature.py`) inside the appropriate module folder and expose it in that module's `__init__.py`.

All functions require parameter descriptions in the following format:

```python
def infer_grn(rna: ad.AnnData,
              adata_atac: ad.AnnData = None,
              genomic_data_pathway: str = None,
              n_genes: int = 500) -> pd.DataFrame:
    """
    Infer Gene Regulatory Network from multi-omics data.

    Parameters
    ----------
    rna : ad.AnnData
        The AnnData object of spatial RNA-seq data.
    adata_atac : ad.AnnData, optional
        The AnnData object of spatial ATAC-seq data.
    genomic_data_pathway : str, optional
        Path to the genomic data.
    n_genes : int, optional
        Number of genes to consider. Default is 500.

    Returns
    -------
    pd.DataFrame
        Inferred gene regulatory network.
    """
```

## Pull Request

1. Fork STARNet on GitHub and clone your fork.
2. Create a feature branch.
3. Make your changes with clear commit messages.
4. Open a Pull Request and wait for review.
