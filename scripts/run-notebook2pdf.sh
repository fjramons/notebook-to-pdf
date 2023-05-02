#!/bin/bash

export IMAGE_NAME=fjramons/notebook2pdf
export CONTAINER_NAME=notebook2pdf
export WORKDIR_CONTAINER=/workdir

docker run \
--name "${CONTAINER_NAME}" \
-it \
--rm \
-v "${PWD}":"${WORKDIR_CONTAINER}" \
"${IMAGE_NAME}" ${@}
