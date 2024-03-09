#!/usr/bin/env bash

set -euo pipefail

BASEDIR=$(dirname "$0")
MAIN_DIR=$(dirname "$BASEDIR")

# Build the documentation
# We need to pull the documentation from the separate applications.
# - back_testing
# - btc_app
# - etl


# back_testing
echo "Building back_testing documentation"

[[ -f "${MAIN_DIR}/back_testing/index.md" ]] && cp -r "${MAIN_DIR}/back_testing/index.md" "${MAIN_DIR}/docs/back_testing"
[[ -d "${MAIN_DIR}/back_testing/docs" ]] && cp -r "${MAIN_DIR}/back_testing/docs" "${MAIN_DIR}/docs/back_testing"

# btc_app
echo "Building btc_app documentation"

[[ -f "${MAIN_DIR}/btc_app/index.md" ]] && cp -r "${MAIN_DIR}/btc_app/index.md" "${MAIN_DIR}/docs/btc_app"
[[ -d "${MAIN_DIR}/btc_app/docs" ]] && cp -r "${MAIN_DIR}/btc_app/docs" "${MAIN_DIR}/docs/btc_app"

# etl
echo "Building etl documentation"

[[ -f "${MAIN_DIR}/etl/index.md" ]] && cp -r "${MAIN_DIR}/etl/index.md" "${MAIN_DIR}/docs/etl"
[[ -d "${MAIN_DIR}/etl/docs" ]] && cp -r "${MAIN_DIR}/etl/docs" "${MAIN_DIR}/docs/etl"

