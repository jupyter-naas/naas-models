# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class SecretError(IntEnum):
    SECRET_NO_ERROR = 0
    SECRET_ALREADY_EXISTS = 1
    SECRET_NOT_FOUND = 2
    SECRET_MARKED_FOR_DELETION = 3

class Secret(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    value: typing.Optional[str] = Field(default="") 

class SecretResponseError(BaseModel):
    error: typing.Optional[SecretError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class SecretCreateRequest(BaseModel):
    secret: typing.Optional[Secret] = Field(default=None) 

class SecretCreateResponse(BaseModel):
    error: typing.Optional[SecretResponseError] = Field(default=None) 

class SecretGetRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 

class SecretGetResponse(BaseModel):
    secret: typing.Optional[Secret] = Field(default=None) 
    error: typing.Optional[SecretResponseError] = Field(default=None) 

class SecretDeleteRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 

class SecretDeleteResponse(BaseModel):
    error: typing.Optional[SecretResponseError] = Field(default=None) 

class SecretListRequest(BaseModel):
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class SecretListResponse(BaseModel):
    secrets: typing.List[Secret] = Field(default_factory=list) 
    error: typing.Optional[SecretResponseError] = Field(default=None) 

class SecretBulkCreateRequest(BaseModel):
    secrets: typing.List[Secret] = Field(default_factory=list) 

class SecretBulkCreateResponse(BaseModel):
    error: typing.List[SecretResponseError] = Field(default_factory=list) 
