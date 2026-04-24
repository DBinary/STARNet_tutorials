from __future__ import annotations

import os
from pathlib import Path
import sys


def before_on_config(config, _plugin) -> None:
    root = Path(__file__).resolve().parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    # Add STARNet src directory so mkapi can import the package
    starnet_src = Path("/data/hulei/STARNet_first_revision/STARNet/src")
    if str(starnet_src) not in sys.path:
        sys.path.insert(0, str(starnet_src))


def page_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]


def section_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]


def toc_title(name: str, _depth: int) -> str:
    return name.split(".")[-1]
