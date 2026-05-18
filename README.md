<p align="center">
  <img src="docs/img/figure1_tutorials.png" alt="STARNet Overview" width="800">
</p>

<p align="center">
  <strong>Spatially resolved inference of gene regulatory networks from spatial multi-omics data</strong>
</p>

<p align="center">
  <a href="https://starnet-tutorials.readthedocs.io/"><img src="https://img.shields.io/badge/Docs-ReadTheDocs-1f6feb"></a>
  <a href="https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2"><img src="https://img.shields.io/badge/Preprint-bioRxiv-b31b1b"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ea44f"></a>
  <a href="#installation"><img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776ab"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Spatial%20RNA--ATAC--seq-6f42c1">
  <img src="https://img.shields.io/badge/Spatial%20Multi--Omics-f78166">
  <img src="https://img.shields.io/badge/GRN%20Inference-0e8a16">
  <img src="https://img.shields.io/badge/Domain%20Fate%20Driver-a371f7">
  <img src="https://img.shields.io/badge/GWAS%20Analysis-9a6700">
  <img src="https://img.shields.io/badge/Drug%20Response-0969da">
</p>

[Documentation](https://starnet-tutorials.readthedocs.io/) | [Preprint](https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2) | [GitHub](https://github.com/DBinary/STARNet)

STARNet (**S**pa**T**i**A**l RNA-ATAC-seq gene **R**egulatory **Net**work) is a computational framework designed to decipher spatially specific gene regulatory networks (GRNs) from spatial RNA-ATAC-seq and other spatial multi-omics data.

> [!IMPORTANT]
>
> STARNet is not currently distributed on PyPI. Please install it from source.

## Key Features

- Spatially resolved GRN inference from spatial RNA-ATAC-seq and spatial multi-omics data.
- Core workflows centered on `ST.model.STARNet(...).preprocess()` and `ST.grn.infer_grn_from_multiomics()`.
- Downstream analysis utilities including `ST.pp.extract_peak_gene_associations()`, `ST.pp.score_all_grn()`, and `ST.pp.score_TF_module()`.
- GWAS-related utilities such as `ST.pp.process_gwas_sumstats()` and SNP / GRN association functions.
- Online documentation and tutorial notebooks for GRN inference across datasets, GWAS analysis, and drug response workflows.

## Documentation and Tutorials

- Online documentation: [starnet-tutorials.readthedocs.io](https://starnet-tutorials.readthedocs.io/)
- Installation guide: [STARNet_guide/docs/installation_guide.md](STARNet_guide/docs/installation_guide.md)
- Tutorial index: [docs/tutorials/index.md](docs/tutorials/index.md)
- GRN inference example: [P21 Mouse Brain](docs/tutorials/GRN_Inference_P21_Mouse_Brain.ipynb)
- Application example: [GWAS Analysis](docs/tutorials/Application_GWAS_Analysis.ipynb)
- Application example: [Drug Response](docs/tutorials/Application_Drug_Response.ipynb)

## Installation

### Standard source installation

Clone the repository and install STARNet into a fresh Python 3.10 or 3.11 environment. For standard user and developer installation, prefer `uv`.

```bash
git clone https://github.com/DBinary/STARNet.git
cd STARNet
micromamba create -n starnet python=3.11
micromamba activate starnet
micromamba install uv
uv pip install -e .
```

### Runtime note for GRN inference

On some systems, the system `libstdc++` may still be picked before the active conda environment and trigger `CXXABI` / `libstdc++` errors for optional genomics tooling.

If that happens, export the active environment library path before running `ST.grn.infer_grn_from_multiomics(...)`:

```bash
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
```

## Quick Start

After installation, import STARNet as:

```python
import STARNet as ST
```

The current release is organized around the following entry points:

```python
# Model preprocessing
model = ST.model.STARNet(...)
model.preprocess()

# Spatial GRN inference
grn = ST.grn.infer_grn_from_multiomics(...)

# Downstream analysis
peak_gene = ST.pp.extract_peak_gene_associations(...)
grn_scores = ST.pp.score_all_grn(...)
tf_module_scores = ST.pp.score_TF_module(...)

# GWAS utilities
gwas = ST.pp.process_gwas_sumstats(...)
```

See the tutorial notebooks and online documentation for complete datasets, parameters, and end-to-end examples.

## Repository Structure

```text
.
├── STARNet/                 # Main Python package
├── STARNet_guide/           # Documentation source and tutorials
├── Resource/                # Reference resources bundled with the project
├── environment-review.yml   # Validated reproduction environment
├── pyproject.toml           # Package metadata
├── README.md
└── LICENSE
```

## Citation

If you use STARNet in your work, please cite:

> Hu L, Zhang S, Zhang X, Luo Y, Gu H, Liu P, Mao S, Chen L, Xia Y, Yang M, Zhang S, Min Y, Li H, Wang P, Yu H, Zeng J. STARNet enables spatially resolved inference of gene regulatory networks from spatial multi-omics data. bioRxiv. 2025. doi: 10.1101/2025.08.21.671434.

Preprint: [https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2](https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2)

```bibtex
@article{hu2025starnet,
  title = {STARNet enables spatially resolved inference of gene regulatory networks from spatial multi-omics data},
  author = {Hu, Lei and Zhang, Shichen and Zhang, Xuting and Luo, Yihai and Gu, Haoteng and Liu, Peng and Mao, Sheng and Chen, Li and Xia, Yuhao and Yang, Minghao and Zhang, Sai and Min, Yaosen and Li, Han and Wang, Peizhuo and Yu, Hongtao and Zeng, Jianyang},
  journal = {bioRxiv},
  year = {2025},
  doi = {10.1101/2025.08.21.671434},
  url = {https://www.biorxiv.org/content/10.1101/2025.08.21.671434v2}
}
```

## Contact

- Lei Hu ([hulei@westlake.edu.cn](mailto:hulei@westlake.edu.cn))
- Shichen Zhang ([zhangshichen@westlake.edu.cn](mailto:zhangshichen@westlake.edu.cn))
- Xuting Zhang ([zhangxuting@westlake.edu.cn](mailto:zhangxuting@westlake.edu.cn))
- Yihai Luo ([luoyihai@westlake.edu.cn](mailto:luoyihai@westlake.edu.cn))

## License

STARNet is released under the [MIT License](LICENSE).
