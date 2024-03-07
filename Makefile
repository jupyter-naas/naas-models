d=docker run --rm -it -v `pwd`:/data --workdir /data naas-models-builder:latest
protoc=$(d) protoc

build:
	#@ docker buildx create --name multiarch --driver docker-container --use 2>&1 > /dev/null || true
	#@ docker buildx build -f .docker/Dockerfile -t naas-models-builder --platform=linux/arm64,linux/amd64 .
	@ .docker/load.sh

python: python/naas_models python/naas_models/pydantic

python/naas_models: 
	mkdir -p python/naas_models

python/naas_models/pydantic: python/naas_models
	mkdir -p python/naas_models/pydantic

go:
	mkdir go

clean:
	rm -rf dist go  python/naas_models/*_pb2.py python/naas_models/pydantic/*_p2p.py 

submodules:
	git submodule init && git submodule update

generate: clean python go build submodules
	$(d) python3 -m grpc_tools.protoc \
		-I=protos \
		-I=lib/protoc-gen-validate/validate \
		--protobuf-to-pydantic_out=python/naas_models/pydantic \
		--python_out=python/naas_models \
		--go_out=go \
		--validate_out="lang=go:go" \
		space.proto registry.proto iam.proto aimodel.proto chat.proto credit.proto secret.proto storage.proto workspace.proto validate.proto
		cd python/naas_models && sed -i.bak  's/import validate_pb2/import naas_models.validate_pb2/g' *.py && rm *.bak

bash: 
	$(d) /bin/bash