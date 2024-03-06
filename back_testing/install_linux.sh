#!/bin/bash

apt update
apt install gcc build-essential wget -y
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --build=aarch64-unknown-linux-gnu
make
make install

export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
