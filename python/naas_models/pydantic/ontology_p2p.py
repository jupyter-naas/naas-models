# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from naas_models.pydantic.common_p2p import FieldMask
from naas_models.pydantic.errors_p2p import ErrorResponse
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing


class Ontology(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    label: typing.Optional[str] = Field(default="") 
    source: typing.Optional[str] = Field(default="") 
    download_url: typing.Optional[str] = Field(default="") 

class OntologySummary(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    label: typing.Optional[str] = Field(default="") 
    download_url: typing.Optional[str] = Field(default="") 

class OntologyCreation(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    label: typing.Optional[str] = Field(default="", min_length=1, max_length=255) 
    source: typing.Optional[str] = Field(default="", min_length=1) 
    download_url: typing.Optional[str] = Field(default="") 

class OntologyUpdate(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    label: typing.Optional[str] = Field(default="") 
    source: typing.Optional[str] = Field(default="") 
    download_url: typing.Optional[str] = Field(default="") 
    field_mask: typing.Optional[FieldMask] = Field(default=None) 

class OntologyListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class OntologyListResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    ontologies: typing.List[OntologySummary] = Field(default_factory=list) 

class OntologyGetRequest(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class OntologyGetResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    ontology: typing.Optional[Ontology] = Field(default=None) 

class OntologyCreationRequest(BaseModel):
    ontology: OntologyCreation = Field() 

class OntologyCreationResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    ontology: typing.Optional[Ontology] = Field(default=None) 

class OntologyUpdateRequest(BaseModel):
    ontology: typing.Optional[OntologyUpdate] = Field(default=None) 

class OntologyUpdateResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    ontology: typing.Optional[Ontology] = Field(default=None) 

class OntologyDeletionRequest(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class OntologyDeletionResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
