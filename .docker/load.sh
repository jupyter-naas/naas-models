#!/usr/bin/env bash

OS=`uname`
PLATFORM=`uname -m`

[ "$OS" == "Darwin" ] && [ "$PLATFORM" == "arm64" ] && docker buildx build -f .docker/Dockerfile --load --platform linux/arm64 -t naas-models-builder:latest . && exit 0
[ "$OS" == "Darwin" ] && [ "$PLATFORM" == "amd64" ] && docker buildx build -f .docker/Dockerfile --load --platform linux/amd64 -t naas-models-builder:latest . && exit 0

echo "os '${OS}' and platform '${PLATFORM}' are not supported" && exit 1
