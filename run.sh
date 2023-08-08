#!/bin/bash

set -euo pipefail

# Build the Docker image
docker build -t transcribe-podcast .

# Run the Docker container
docker run --rm --quiet -it -v "$PWD:/usr/src/app" transcribe-podcast
