d=docker run --rm -it -v `pwd`:/data --workdir /data naas-models-builder:latest
protoc=$(d) protoc

generate: clean python go build submodules
	docker compose run --rm -it python
	cd python/naas_models && sed -i.bak  's/import validate_pb2/import naas_models.validate_pb2/g' *.py && rm *.bak
	cd python/naas_models/pydantic && sed -i.bak 's/common_p2p/naas_models.pydantic.common_p2p/g' *.py && rm *.bak
	cd python/naas_models/pydantic && sed -i.bak 's/errors_p2p/naas_models.pydantic.errors_p2p/g' *.py && rm *.bak

build:
	docker compose build

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

bash: 
	$(d) /bin/bash