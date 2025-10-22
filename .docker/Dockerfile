FROM --platform=$TARGETPLATFORM ubuntu:latest

ARG TARGETARCH
ARG TARGETOS

RUN apt-get update && apt-get install --yes wget unzip python3 python3-pip golang-go python3-dev

ENV PROTOC_VERSION=21.12
ADD .docker/install-protoc.sh /tmp/
RUN chmod +x /tmp/install-protoc.sh
RUN /tmp/install-protoc.sh

ENV PROTOC_GEN_VALIDATE_VERSION=1.2.1
ADD .docker/install-protoc-gen-validate.sh /tmp/
RUN chmod +x /tmp/install-protoc-gen-validate.sh
RUN /tmp/install-protoc-gen-validate.sh

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/go/bin"

RUN python3 -m pip install poetry --break-system-packages

# Removing version pining to try to follow new versions.
# RUN bash -c 'virtualenv venv \
#     && source venv/bin/activate \
#     && python3 -m pip install --upgrade pip \
#     && pip install protobuf-to-pydantic[mypy-protobuf]=="0.2.6.2" protobuf grpcio-tools'
# #    && pip install protobuf-to-pydantic=="0.1.7.4" protobuf-to-pydantic[mypy-protobuf]=="0.1.7.4" protobuf protobuf2pydantic grpcio-tools'


#ENTRYPOINT ["/usr/local/bin/protoc"]