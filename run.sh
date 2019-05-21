#!/usr/bin/env bash

docker run -v $(pwd):/host unhinged/clientminer python -m clientminer ./data/test.csv
