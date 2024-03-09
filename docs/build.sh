#!/usr/bin/env bash

set -euo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
MAIN_DIR="$(realpath ${BASEDIR}/..)"

# Build the documentation
# We need to pull the documentation from the separate applications.
# - back_testing
# - btc_app
# - etl

# Remove the existing documentation
echo "[INFO] - Resetting existing documentation"
[[ -d "${MAIN_DIR}/docs/back_testing" ]] && rm -rf "${MAIN_DIR}/docs/back_testing" && mkdir -p "${MAIN_DIR}/docs/back_testing" || mkdir -p "${MAIN_DIR}/docs/back_testing"
[[ -d "${MAIN_DIR}/docs/btc_app" ]] && rm -rf "${MAIN_DIR}/docs/btc_app" && mkdir -p "${MAIN_DIR}/docs/btc_app" || mkdir -p "${MAIN_DIR}/docs/btc_app"
[[ -d "${MAIN_DIR}/docs/etl" ]] && rm -rf "${MAIN_DIR}/docs/etl" && mkdir -p "${MAIN_DIR}/docs/etl" || mkdir -p "${MAIN_DIR}/docs/etl"

# back_testing
echo "[INFO] - Building back_testing documentation"

[[ -f "${MAIN_DIR}/back_testing/index.md" ]] && cp -R "${MAIN_DIR}/back_testing/index.md" "${MAIN_DIR}/docs/back_testing/"
[[ -d "${MAIN_DIR}/back_testing/docs" ]] && cp -R "${MAIN_DIR}/back_testing/docs" "${MAIN_DIR}/docs/back_testing"

# btc_app
echo "[INFO] - Building btc_app documentation"

[[ -f "${MAIN_DIR}/btc_app/index.md" ]] && cp -R "${MAIN_DIR}/btc_app/index.md" "${MAIN_DIR}/docs/btc_app/index.md"
[[ -d "${MAIN_DIR}/btc_app/docs" ]] && cp -R "${MAIN_DIR}/btc_app/docs" "${MAIN_DIR}/docs/btc_app"

# etl
echo "[INFO] - Building etl documentation"

[[ -f "${MAIN_DIR}/etl/index.md" ]] && cp -R "${MAIN_DIR}/etl/index.md" "${MAIN_DIR}/docs/etl/index.md"
[[ -d "${MAIN_DIR}/etl/docs" ]] && cp -R "${MAIN_DIR}/etl/docs" "${MAIN_DIR}/docs/etl"

# Build the diagrams
echo "[INFO] - Building diagrams"
poetry run python "${MAIN_DIR}/docs/create_diagrams.py"

exit 0