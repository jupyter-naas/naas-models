# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class RegistryError(IntEnum):
    REGISTRY_ALREADY_EXISTS = 0
    REGISTRY_NOT_FOUND = 1
    NOT_AUTHORIZED = 2

class Registry(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: typing.Optional[str] = Field(default="") 
    uri: typing.Optional[str] = Field(default="") 

class RegistryCredentials(BaseModel):
    username: typing.Optional[str] = Field(default="") 
    password: typing.Optional[str] = Field(default="") 

class RegistryCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 

class RegistryCreationResponse(BaseModel):
    registry: typing.Optional[Registry] = Field(default=None) 

class RegistryCreationResponseError(BaseModel):
    error: typing.Optional[RegistryError] = Field(default=0) 
    error_message: typing.Optional[str] = Field(default="") 

class RegistryListRequest(BaseModel):
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class RegistryListResponse(BaseModel):
    registries: typing.List[Registry] = Field(default_factory=list) 

class RegistryGetRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 

class RegistryGetResponse(BaseModel):
    registry: typing.Optional[Registry] = Field(default=None) 

class RegistryGetResponseError(BaseModel):
    error: typing.Optional[RegistryError] = Field(default=0) 
    error_message: typing.Optional[str] = Field(default="") 

class RegistryDeleteRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 

class RegistryDeleteResponseError(BaseModel):
    error: typing.Optional[RegistryError] = Field(default=0) 
    error_message: typing.Optional[str] = Field(default="") 

class RegistryCredentialsRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 

class RegistryCredentialsResponse(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    credentials: typing.Optional[RegistryCredentials] = Field(default=None) 

class RegistryCredentialsResponseError(BaseModel):
    error: typing.Optional[RegistryError] = Field(default=0) 
    error_message: typing.Optional[str] = Field(default="") 
