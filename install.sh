#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_DIR="${SCRIPT_DIR}/STARNet"
ENV_NAME="starnet"
MANAGER=""

usage() {
  cat <<'EOF'
Usage: bash install.sh [options]

Create a STARNet conda environment and install all dependencies.

Options:
  --env-name NAME   Environment name (default: starnet)
  --manager NAME    conda or micromamba (default: auto-detect)
  -h, --help        Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --env-name)
      ENV_NAME="$2"; shift 2 ;;
    --manager)
      MANAGER="$2"; shift 2 ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2; exit 1 ;;
  esac
done

# ---- detect manager ----
if [[ -z "${MANAGER}" ]]; then
  if command -v micromamba >/dev/null 2>&1; then
    MANAGER="micromamba"
  elif command -v conda >/dev/null 2>&1; then
    MANAGER="conda"
  else
    echo "Neither conda nor micromamba found. Install one first:" >&2
    echo "  conda: https://github.com/conda-forge/miniforge" >&2
    echo "  micromamba: https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html" >&2
    exit 1
  fi
fi

# ---- validate ----
if [[ ! -d "${PACKAGE_DIR}" ]]; then
  echo "STARNet source not found: ${PACKAGE_DIR}" >&2
  echo "Run: git clone https://github.com/DBinary/STARNet.git" >&2
  exit 1
fi

ENV_FILE="${PACKAGE_DIR}/environment-conda.yml"
REQ_FILE="${PACKAGE_DIR}/requirements-review.txt"

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Missing: ${ENV_FILE}" >&2; exit 1
fi
if [[ ! -f "${REQ_FILE}" ]]; then
  echo "Missing: ${REQ_FILE}" >&2; exit 1
fi

echo "Manager:  ${MANAGER}"
echo "Env name: ${ENV_NAME}"
echo ""

# ---- create environment ----
if "${MANAGER}" run -n "${ENV_NAME}" python -V >/dev/null 2>&1; then
  echo "[1/4] Environment '${ENV_NAME}' exists, updating..."
  "${MANAGER}" env update -n "${ENV_NAME}" -f "${ENV_FILE}" --prune
else
  echo "[1/4] Creating environment '${ENV_NAME}'..."
  "${MANAGER}" env create -n "${ENV_NAME}" -f "${ENV_FILE}"
fi

# ---- pip install dependencies ----
echo "[2/4] Installing Python dependencies (~3 GB, may take 5-20 min)..."
PIP_INDEX_URL=https://pypi.org/simple \
  "${MANAGER}" run -n "${ENV_NAME}" python -m pip install -r "${REQ_FILE}"

# ---- install STARNet ----
echo "[3/4] Installing STARNet (editable mode)..."
PIP_INDEX_URL=https://pypi.org/simple \
  "${MANAGER}" run -n "${ENV_NAME}" python -m pip install --no-deps -e "${PACKAGE_DIR}"

# ---- verify ----
echo "[4/4] Verifying..."
"${MANAGER}" run -n "${ENV_NAME}" python -c "
import STARNet as ST
from STARNet import grn, model, pl, pp
import torch
print('STARNet: OK')
print('CUDA available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('GPU:', torch.cuda.get_device_name(0))
"

echo ""
echo "Done. Activate with:"
echo "  ${MANAGER} activate ${ENV_NAME}"
