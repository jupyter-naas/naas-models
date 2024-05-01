# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing

class AssetError(IntEnum):
    ASSET_NO_ERROR = 0
    ASSET_NOT_FOUND = 1
    ASSET_ALREADY_EXISTS = 2
    ASSET_REQUEST_ERROR = 3
    INTERNAL_SERVER_ERROR = 1000

class ObjectMetadata(BaseModel):
    provider: typing.Optional[str] = Field(default="") 
    provider_bucket_name: typing.Optional[str] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    storage_name: typing.Optional[str] = Field(default="") 
    prefix: typing.Optional[str] = Field(default="") 
    object_name: typing.Optional[str] = Field(default="") 
    content_type: typing.Optional[str] = Field(default="") 
    content_length: typing.Optional[str] = Field(default="") 
    object_updated_at: typing.Optional[datetime] = Field(default_factory=datetime.now) 
    object_version: typing.Optional[str] = Field(default="") 
    metadata: typing.Optional[str] = Field(default="") 

class Asset(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    object_name: typing.Optional[str] = Field(default="") 
    visibility: typing.Optional[str] = Field(default="") 
    content_disposition: typing.Optional[str] = Field(default="") 
    password: typing.Optional[str] = Field(default="") 
    url: typing.Optional[str] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    storage_name: typing.Optional[str] = Field(default="") 
    prefix: typing.Optional[str] = Field(default="") 
    object_version: typing.Optional[str] = Field(default="") 
    content_type: typing.Optional[str] = Field(default="") 
    object_updated_at: typing.Optional[datetime] = Field(default_factory=datetime.now) 
    asset_created_at: typing.Optional[datetime] = Field(default_factory=datetime.now) 
    user_id: typing.Optional[UUID] = Field(default="") 
    provider: typing.Optional[str] = Field(default="") 
    provider_bucket_name: typing.Optional[str] = Field(default="") 

class AssetCreation(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    storage_name: typing.Optional[str] = Field(default="") 
    object_name: typing.Optional[str] = Field(default="") 
    object_version: typing.Optional[str] = Field(default="") 
    visibility: typing.Optional[str] = Field(default="") 
    content_disposition: typing.Optional[str] = Field(default="") 
    password: typing.Optional[str] = Field(default="") 

class AssetUpdate(BaseModel):
    visibility: typing.Optional[str] = Field(default="") 
    content_disposition: typing.Optional[str] = Field(default="") 

class AssetResponseError(BaseModel):
    code: typing.Optional[AssetError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class AssetCreateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    asset_creation: typing.Optional[AssetCreation] = Field(default=None) 

class AssetCreateResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default=None) 
    error: typing.Optional[AssetResponseError] = Field(default=None) 

class AssetGetRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    asset_id: typing.Optional[UUID] = Field(default="") 

class AssetGetResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default=None) 
    error: typing.Optional[AssetResponseError] = Field(default=None) 

class AssetGetObjectRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    asset_id: typing.Optional[UUID] = Field(default="") 

class AssetGetObjectResponse(BaseModel):
    url: typing.Optional[str] = Field(default="") 
    error: typing.Optional[AssetResponseError] = Field(default=None) 

class AssetUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    asset_update: typing.Optional[AssetUpdate] = Field(default=None) 

class AssetUpdateResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default=None) 
    error: typing.Optional[AssetResponseError] = Field(default=None) 

class AssetDeleteRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    asset_id: typing.Optional[UUID] = Field(default="") 

class AssetDeleteResponse(BaseModel):
    error: typing.Optional[AssetResponseError] = Field(default=None) 
