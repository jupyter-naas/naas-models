# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.get_desc.from_pb_option.types import UriRefStr
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing

class SpaceError(IntEnum):
    SPACE_NO_ERROR = 0
    SPACE_ALREADY_EXISTS = 1
    SPACE_NOT_FOUND = 2
    SPACE_NOT_UPDATED = 3
    SPACE_MUST_HAVE_ONE_CONTAINER_PORT = 4

class Container(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9-]+)$") 
    image: typing.Optional[str] = Field(default="", min_length=1, pattern="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = Field(default_factory=dict) 
    port: typing.Optional[int] = Field(default=0, ge=0, le=65535) 
    cpu: typing.Optional[str] = Field(default="", pattern="^[1-9]+(.[1-9]+)?[m]?$") 
    memory: typing.Optional[str] = Field(default="", pattern="^[1-9]+(Mi|Gi|Ki)$") 

class ContainerUpdate(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9-]+)$") 
    image: typing.Optional[str] = Field(default="", min_length=1, pattern="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = Field(default_factory=dict) 
    port: typing.Optional[int] = Field(default=0, ge=0, le=65535) 
    cpu: typing.Optional[str] = Field(default="", pattern="^[1-9]+(.[1-9]+)?[m]?$") 
    memory: typing.Optional[str] = Field(default="", pattern="^[1-9]+(Mi|Gi|Ki)$") 

class Space(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: typing.Optional[UUID] = Field(default="") 
    id: typing.Optional[UUID] = Field(default="") 
    domain: typing.Optional[UriRefStr] = Field(default="") 
    containers: typing.List[Container] = Field(default_factory=list, min_length=1) 

class SpaceUpdate(BaseModel):
    domain: typing.Optional[UriRefStr] = Field(default="") 
    containers: typing.List[ContainerUpdate] = Field(default_factory=list, min_length=1) 

class SpaceResponseError(BaseModel):
    code: typing.Optional[SpaceError] = Field(default=0) 
    status: typing.Optional[str] = Field(default="") 
    reason: typing.Optional[str] = Field(default="") 
    message: typing.Optional[str] = Field(default="") 

class SpaceCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    domain: typing.Optional[UriRefStr] = Field(default="") 
    containers: typing.List[Container] = Field(default_factory=list, min_length=1) 

class SpaceCreationResponse(BaseModel):
    space: typing.Optional[Space] = Field(default=None) 
    status: typing.Optional[str] = Field(default="") 

class SpaceGetRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 

class SpaceGetResponse(BaseModel):
    space: typing.Optional[Space] = Field(default=None) 
    status: typing.Optional[str] = Field(default="") 

class SpaceDeletionRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 

class SpaceDeletionResponse(BaseModel):
    status: typing.Optional[str] = Field(default="") 

class SpaceListRequest(BaseModel):
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class SpaceListResponse(BaseModel):
    spaces: typing.List[Space] = Field(default_factory=list) 

class SpaceUpdateRequest(BaseModel):
    name: typing.Optional[str] = Field(default="", min_length=1, max_length=63, pattern="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    space: typing.Optional[SpaceUpdate] = Field(default=None) 

class SpaceUpdateResponse(BaseModel):
    space: typing.Optional[Space] = Field(default=None) 
    status: typing.Optional[str] = Field(default="") 
