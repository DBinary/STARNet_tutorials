import importlib.util
import inspect
import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE / "extensions")]

# Try to locate the STARNet package.
# Layout: HERE.parent.parent is the repo root,
#   which contains the STARNet/ package directory under STARNet/src/.
_repo_root = HERE.parent.parent
_starnet_src = _repo_root / "STARNet" / "src"
if _starnet_src.is_dir():
    sys.path.insert(0, str(_starnet_src))

# -- Project information -------------------------------------------------------
project = "STARNet"
author = "Lei Hu, Shichen Zhang, Xuting Zhang, Yihai Luo, and others"
copyright = f"{datetime.now():%Y}, AICB Lab, Westlake University"
release = "1.0.0"
version = release
repository_url = "https://github.com/DBinary/STARNet"
default_github_ref = "main"


def _fallback_github_ref() -> str:
    for key in ("READTHEDOCS_GIT_IDENTIFIER", "GITHUB_REF_NAME", "READTHEDOCS_VERSION_NAME"):
        value = os.environ.get(key)
        if value and value not in {"latest", "stable"}:
            return value
    return default_github_ref


try:
    from importlib.metadata import metadata as _pkg_meta
    _info = _pkg_meta("STARNet")
    _ver = _info.get("Version")
    if _ver:
        release = version = _ver
    _author = _info.get("Author")
    if _author:
        author = _author
except Exception:
    pass

html_context = {
    "display_github": True,
    "github_user": "DBinary",
    "github_repo": project,
    "github_version": _fallback_github_ref(),
    "conf_py_path": "/docs/",
}

# -- Extensions ---------------------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxext.opengraph",
]

# Load custom extensions from docs/extensions/
_ext_dir = HERE / "extensions"
if _ext_dir.exists():
    sys.path.insert(0, str(_ext_dir))
    for _p in sorted(_ext_dir.glob("*.py")):
        extensions.append(_p.stem)

# -- Autodoc / Napoleon -------------------------------------------------------
autosummary_generate = True
autodoc_member_order = "bysource"

autodoc_mock_imports = [
    "torch",
    "torch_geometric",
    "lightning",
    "scanpy",
    "anndata",
    "numpy",
    "pandas",
    "scipy",
    "sklearn",
    "snapatac2",
    "pyfaidx",
    "joblib",
    "tqdm",
    "pyranges",
    "statsmodels",
]
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_rtype = True
napoleon_use_param = True
napoleon_custom_sections = [("Params", "Parameters")]
todo_include_todos = False

# -- MyST / myst-nb -----------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "html_admonition",
    "substitution",
    "linkify",
]
myst_url_schemes = ("http", "https", "mailto")
nb_output_stderr = "remove"
nb_execution_mode = "off"
nb_merge_streams = True
typehints_defaults = "braces"

# -- Source files -------------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
    ".md": "myst-nb",
}
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "overrides",
    "site",
]
needs_sphinx = "4.0"
nitpicky = False

# -- extlinks / intersphinx ---------------------------------------------------
extlinks = {
    "issue": (f"{repository_url}/issues/%s", "#%s"),
    "pr": (f"{repository_url}/pull/%s", "#%s"),
    "ghuser": ("https://github.com/%s", "@%s"),
}

intersphinx_mapping = {
    "anndata": ("https://anndata.readthedocs.io/en/stable/", None),
    "ipython": ("https://ipython.readthedocs.io/en/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
    "scanpy": ("https://scanpy.readthedocs.io/en/stable/", None),
}

# -- HTML / Furo --------------------------------------------------------------
html_theme = "furo"
html_title = project
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#00897b",
        "color-brand-content": "#00897b",
    },
    "dark_css_variables": {
        "color-brand-primary": "#4db6ac",
        "color-brand-content": "#4db6ac",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": repository_url,
            "html": "",
            "class": "fab fa-github fa-2x",
        }
    ],
}

pygments_style = "tango"
pygments_dark_style = "monokai"

html_static_path = ["_static"]
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
    "css/override.css",
]
html_show_sphinx = False

# -- Linkcode -----------------------------------------------------------------
def _git(*args):
    return subprocess.check_output(["git", *args]).strip().decode()

_git_ref = None
try:
    _git_ref = _git("name-rev", "--name-only", "--no-undefined", "HEAD")
    _git_ref = re.sub(r"^(remotes/[^/]+|tags)/", "", _git_ref)
except Exception:
    pass
if not _git_ref or re.search(r"[\^~]", _git_ref):
    try:
        _git_ref = _git("rev-parse", "HEAD")
    except Exception:
        _git_ref = _fallback_github_ref()

_starnet_module_path = None
try:
    _spec = importlib.util.find_spec("STARNet")
    if _spec and _spec.origin:
        _starnet_module_path = os.path.dirname(_spec.origin)
except Exception:
    pass


def linkcode_resolve(domain, info):
    """Resolve a Python object to its GitHub source URL."""
    if domain != "py":
        return None
    if not _starnet_module_path:
        return None
    try:
        obj = sys.modules[info["module"]]
        for part in info["fullname"].split("."):
            obj = getattr(obj, part)
        obj = inspect.unwrap(obj)
        if isinstance(obj, property):
            obj = inspect.unwrap(obj.fget)
        path = os.path.relpath(inspect.getsourcefile(obj), start=_starnet_module_path)
        src, lineno = inspect.getsourcelines(obj)
    except Exception:
        return None
    path = f"{path}#{lineno}-{lineno + len(src) - 1}"
    return f"{repository_url}/blob/{_git_ref}/STARNet/src/STARNet/{path}"
