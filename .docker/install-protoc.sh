#!/usr/bin/env bash

if [[ "$TARGETOS" == "linux" ]]; then

    if [[ "$TARGETARCH" == "amd64" ]]; then
        ARCH="x86_64"
    elif [[ "$TARGETARCH" == "arm64" ]]; then
        ARCH="aarch_64"
    else
        echo "Arch $BUILDARCH not supported. aborting"
        exit 1
    fi

else
    echo "Platform $TARGETOS not supported. aborting."
    exit 1
fi

cd /tmp \
    && wget https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-${ARCH}.zip \
    && unzip protoc-${PROTOC_VERSION}-linux-${ARCH}.zip \
    && mv include /usr/local/include \
    && mv bin/protoc /usr/local/bin/protoc
