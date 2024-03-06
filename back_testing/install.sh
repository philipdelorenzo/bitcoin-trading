#!/bin/bash

arch -arm64 brew install ta-lib

export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"

pip install -r requirements.txt
