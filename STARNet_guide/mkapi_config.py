from __future__ import annotations

import os
from pathlib import Path
import sys


def before_on_config(config, _plugin) -> None:
    root = Path(__file__).resolve().parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    # Add STARNet src directory so mkapi can import the package.
    # mkapi_config.py lives at STARNet_guide/STARNet_guide/mkapi_config.py
    # STARNet src is at repo_root/src/, so relative path is ../../src
    starnet_src = root / ".." / ".." / "src"
    starnet_src = starnet_src.resolve()
    if starnet_src.exists() and str(starnet_src) not in sys.path:
        sys.path.insert(0, str(starnet_src))


def page_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]


def section_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]


def toc_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]
