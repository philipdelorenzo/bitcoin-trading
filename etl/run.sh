#!/usr/bin/env bash

set -eou pipefail

# Run the ETL process
nohup redis-server --port 6379 &
python3 etl.py
