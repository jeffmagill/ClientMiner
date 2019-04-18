#!/usr/bin/env bash

docker build -f docker/Dockerfile --tag=unhinged/clientminer .
docker run -v $(pwd):/host unhinged/clientminer python -m clientminer ./data/test.csv
