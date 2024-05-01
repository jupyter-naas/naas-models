# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing

class AIModelError(IntEnum):
    NO_ERROR = 0
    ALREADY_EXISTS = 1
    NOT_FOUND = 2
    NOT_UPDATED = 3
    NOT_AUTHORIZED = 4
    AIMODEL_OUT_OF_CREDITS = 5
    AIMODEL_DONT_HANDLE_COMPLETION = 6

class AIModel(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    name: typing.Optional[str] = Field(default="") 
    provider: typing.Optional[str] = Field(default="") 
    image: typing.Optional[str] = Field(default="") 
    enabled: typing.Optional[bool] = Field(default=False) 
    type: typing.Optional[str] = Field(default="") 
    restricted: typing.Optional[bool] = Field(default=False) 
    name_alias: typing.Optional[str] = Field(default="") 
    context_window: typing.Optional[int] = Field(default=0) 

class CompletionResponse(BaseModel):
    model_id: typing.Optional[UUID] = Field(default="") 
    completions: typing.List[str] = Field(default_factory=list) 
    input_tokens: typing.Optional[int] = Field(default=0) 
    output_tokens: typing.Optional[int] = Field(default=0) 
    image_resolution: typing.Optional[str] = Field(default="") 
    image_steps: typing.Optional[int] = Field(default=0) 

class AIModelResponseError(BaseModel):
    code: typing.Optional[AIModelError] = Field(default=0) 
    status: typing.Optional[str] = Field(default="") 
    reason: typing.Optional[str] = Field(default="") 
    message: typing.Optional[str] = Field(default="") 

class AIModelListRequest(BaseModel):
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class AIModelListResponse(BaseModel):
    aimodels: typing.List[AIModel] = Field(default_factory=list) 
    page_number: typing.Optional[int] = Field(default=0) 
    error: typing.Optional[AIModelResponseError] = Field(default=None) 

class AIModelGetRequest(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 

class AIModelGetResponse(BaseModel):
    aimodel: typing.Optional[AIModel] = Field(default=None) 
    error: typing.Optional[AIModelResponseError] = Field(default=None) 

class AIModelCompletionRequest(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    payload: typing.Optional[str] = Field(default="") 

class AIModelCompletionResponse(BaseModel):
    completion: typing.Optional[CompletionResponse] = Field(default=None) 
    error: typing.Optional[AIModelResponseError] = Field(default=None) 

class AIModelAdminCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    provider: typing.Optional[str] = Field(default="") 
    image: typing.Optional[str] = Field(default="") 
    enabled: typing.Optional[bool] = Field(default=False) 
    type: typing.Optional[str] = Field(default="") 
    restricted: typing.Optional[bool] = Field(default=False) 
    name_alias: typing.Optional[str] = Field(default="") 

class AIModelAdminCreationResponse(BaseModel):
    aimodel: typing.Optional[AIModel] = Field(default=None) 
    error: typing.Optional[AIModelResponseError] = Field(default=None) 

class AIModelAdminDeleteRequest(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 

class AIModelAdminDeleteResponse(BaseModel):
    error: typing.Optional[AIModelResponseError] = Field(default=None) 
