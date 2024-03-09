#!/usr/bin/env bash

set -euo pipefail

python -m mkdocs build && python -m mkdocs serve --dev-addr=0.0.0.0:8100
