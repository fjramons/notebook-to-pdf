#!/bin/bash

export CONTAINER_NAME=fjramons/notebook2pdf

# Builds and tags the container image
docker rmi "${CONTAINER_NAME}" || true
docker build -t "${CONTAINER_NAME}" .
