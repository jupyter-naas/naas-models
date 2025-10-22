# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.12.3 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from uuid import UUID
import typing

class StorageError(IntEnum):
    STORAGE_NO_ERROR = 0
    STORAGE_ALREADY_EXIST = 1
    STORAGE_NOT_FOUND = 2
    INTERNAL_SERVER_ERROR = 1000


class ObjectError(IntEnum):
    OBJECT_NO_ERROR = 0
    OBJECT_ALREADY_EXIST = 1
    OBJECT_SIZE_ERROR = 2
    OBJECT_NOT_FOUND = 3
    OBJECT_DIR_NOT_EMPTY = 4


class CredentialsError(IntEnum):
    CREDENTIALS_NO_ERROR = 0

class Storage(BaseModel):
    name: typing.Optional[str] = Field(default="")

class Object(BaseModel):
    name: typing.Optional[str] = Field(default="")
    type: typing.Optional[str] = Field(default="")
    prefix: typing.Optional[str] = Field(default="")
    size: typing.Optional[str] = Field(default="")
    lastmodified: typing.Optional[str] = Field(default="")

class StorageResponseError(BaseModel):
    model_config = ConfigDict(validate_default=True)
    code: typing.Optional[StorageError] = Field(default=0)
    message: typing.Optional[str] = Field(default="")

class ObjectResponseError(BaseModel):
    model_config = ConfigDict(validate_default=True)
    code: typing.Optional[ObjectError] = Field(default=0)
    message: typing.Optional[str] = Field(default="")

class ObjectStorageCredentialsResponseError(BaseModel):
    model_config = ConfigDict(validate_default=True)
    code: typing.Optional[CredentialsError] = Field(default=0)
    message: typing.Optional[str] = Field(default="")

class StorageListRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    object: typing.Optional[Object] = Field(default_factory=Object)

class StorageListResponse(BaseModel):
    storage: typing.List[Storage] = Field(default_factory=list)
    error: typing.Optional[StorageResponseError] = Field(default_factory=StorageResponseError)

class StorageCreateRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)

class StorageCreateResponse(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    error: typing.Optional[StorageResponseError] = Field(default_factory=StorageResponseError)

class StorageDeleteRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)

class StorageDeleteResponse(BaseModel):
    error: typing.Optional[StorageResponseError] = Field(default_factory=StorageResponseError)

class StorageListObjectRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    object: typing.Optional[Object] = Field(default_factory=Object)

class StorageListObjectResponse(BaseModel):
    object: typing.List[Object] = Field(default_factory=list)
    error: typing.Optional[StorageResponseError] = Field(default_factory=StorageResponseError)

class ObjectCreateRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    object: typing.Optional[Object] = Field(default_factory=Object)

class ObjectCreateResponse(BaseModel):
    error: typing.Optional[ObjectResponseError] = Field(default_factory=ObjectResponseError)

class ObjectListRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    object: typing.Optional[Object] = Field(default_factory=Object)

class ObjectListResponse(BaseModel):
    object: typing.List[Object] = Field(default_factory=list)
    error: typing.Optional[ObjectResponseError] = Field(default_factory=ObjectResponseError)

class ObjectGetRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default_factory=Storage)
    object: typing.Optional[Object] = Field(default_factory=Object)

class ObjectGetResponse(BaseModel):
    object: typing.Optional[Object] = Field(default_factory=Object)
    error: typing.Optional[ObjectResponseError] = Field(default_factory=ObjectResponseError)

class ObjectDeleteRequest(BaseModel):
    object: typing.Optional[Object] = Field(default_factory=Object)

class ObjectDeleteResponse(BaseModel):
    error: typing.Optional[ObjectResponseError] = Field(default_factory=ObjectResponseError)

class ObjectStorageS3Credentials(BaseModel):
    """
     Credentials
    """

    endpoint_url: typing.Optional[str] = Field(default="")
    region_name: typing.Optional[str] = Field(default="")
    access_key_id: typing.Optional[str] = Field(default="")
    secret_key: typing.Optional[str] = Field(default="")
    session_token: typing.Optional[str] = Field(default="")
    expiration: typing.Optional[str] = Field(default="")

class ObjectStorageAzureCredentials(BaseModel):
    endpoint_url: typing.Optional[str] = Field(default="")
    access_key_id: typing.Optional[str] = Field(default="")
    secret_key: typing.Optional[str] = Field(default="")

class ObjectStorageCredentials(BaseModel):
    s3: ObjectStorageS3Credentials = Field(default_factory=ObjectStorageS3Credentials)

class ObjectStorageCredentialsRequest(BaseModel):
#optional string workspace_id = 1;
    storage: typing.Optional[Storage] = Field(default_factory=Storage)

class ObjectStorageCredentialsResponse(BaseModel):
    credentials: typing.Optional[ObjectStorageCredentials] = Field(default_factory=ObjectStorageCredentials)
    error: typing.Optional[ObjectStorageCredentialsResponseError] = Field(default_factory=ObjectStorageCredentialsResponseError)

class StorageObjectPublicUrlRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    storage_name: typing.Optional[str] = Field(default="")
    prefix: typing.Optional[str] = Field(default="")
    object_name: typing.Optional[str] = Field(default="")

class StorageObjectPublicUrlResponse(BaseModel):
    url: typing.Optional[str] = Field(default="")
    error: typing.Optional[ObjectStorageCredentialsResponseError] = Field(default_factory=ObjectStorageCredentialsResponseError)
