FROM --platform=$TARGETPLATFORM ubuntu:latest

ARG TARGETARCH
ARG TARGETOS

RUN apt-get update && apt-get install --yes wget unzip python3 python3-pip golang-go 

ENV PROTOC_VERSION=21.12
ADD .docker/install-protoc.sh /tmp/
RUN chmod +x /tmp/install-protoc.sh
RUN /tmp/install-protoc.sh

ENV PROTOC_GEN_VALIDATE_VERSION=0.9.1
ADD .docker/install-protoc-gen-validate.sh /tmp/
RUN chmod +x /tmp/install-protoc-gen-validate.sh
RUN /tmp/install-protoc-gen-validate.sh

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/go/bin"

ADD .docker/requirements.txt /tmp/requirements.txt
RUN pip --default-timeout=100 install -r /tmp/requirements.txt

#ENTRYPOINT ["/usr/local/bin/protoc"]