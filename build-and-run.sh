#!/usr/bin/env bash

docker build -f docker/Dockerfile --tag=unhinged/clientminer .
./run.sh
