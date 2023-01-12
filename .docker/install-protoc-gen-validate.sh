#!/usr/bin/env bash

if [[ "$TARGETOS" == "linux" ]]; then

    if [[ "$TARGETARCH" == "amd64" ]]; then
        ARCH="amd64"
    elif [[ "$TARGETARCH" == "arm64" ]]; then
        ARCH="arm64"
    else
        echo "Arch $BUILDARCH not supported. aborting"
        exit 1
    fi

else
    echo "Platform $TARGETOS not supported. aborting."
    exit 1
fi


cd /tmp \
    && wget https://github.com/bufbuild/protoc-gen-validate/releases/download/v${PROTOC_GEN_VALIDATE_VERSION}/protoc-gen-validate_${PROTOC_GEN_VALIDATE_VERSION}_linux_${ARCH}.tar.gz \
    && tar zxvf protoc-gen-validate_${PROTOC_GEN_VALIDATE_VERSION}_linux_${ARCH}.tar.gz \
    && mv protoc-gen-* /usr/local/bin/
