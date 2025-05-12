#!/usr/bin/env bash

DOCKER_BUILDKIT=1 docker build \
  --secret id=env,src=.env \
  -f Dockerfile.ui \
  -t stellar-harvest-ie-ui:latest .
