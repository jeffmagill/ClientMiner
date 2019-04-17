#!/usr/bin/env bash

docker build --tag=unhinged/clientmining .
docker run -v $(pwd):/host unhinged/clientmining python app.py ./data/test.csv
