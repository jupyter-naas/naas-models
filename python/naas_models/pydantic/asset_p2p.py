# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.12.3 
from .errors_p2p import ErrorResponse
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

class AssetListRequest(BaseModel):
    """
     Asset List
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    page_size: typing.Optional[int] = Field(default=0)
    page_number: typing.Optional[int] = Field(default=0)

class AssetListResponse(BaseModel):
    assets: typing.List[Asset] = Field(default_factory=list)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class AssetCreateRequest(BaseModel):
    """
      Asset Create
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    asset_creation: typing.Optional[AssetCreation] = Field(default_factory=AssetCreation)

class AssetCreateResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default_factory=Asset)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class AssetGetRequest(BaseModel):
    """
     Asset Get
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    asset_id: typing.Optional[UUID] = Field(default="")

class AssetGetResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default_factory=Asset)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class AssetGetObjectRequest(BaseModel):
    """
     Asset Get Object
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    asset_id: typing.Optional[UUID] = Field(default="")

class AssetGetObjectResponse(BaseModel):
    url: typing.Optional[str] = Field(default="")
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class AssetUpdateRequest(BaseModel):
    """
     Asset Update
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    asset_update: typing.Optional[AssetUpdate] = Field(default_factory=AssetUpdate)

class AssetUpdateResponse(BaseModel):
    asset: typing.Optional[Asset] = Field(default_factory=Asset)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class AssetDeleteRequest(BaseModel):
    """
     Asset Delete
    """

    workspace_id: typing.Optional[UUID] = Field(default="")
    asset_id: typing.Optional[UUID] = Field(default="")

class AssetDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)
