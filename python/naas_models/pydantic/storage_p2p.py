# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
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
    code: typing.Optional[StorageError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class ObjectResponseError(BaseModel):
    code: typing.Optional[ObjectError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class ObjectStorageCredentialsResponseError(BaseModel):
    code: typing.Optional[CredentialsError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class StorageListRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    object: typing.Optional[Object] = Field(default=None) 

class StorageListResponse(BaseModel):
    storage: typing.List[Storage] = Field(default_factory=list) 
    error: typing.Optional[StorageResponseError] = Field(default=None) 

class StorageCreateRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 

class StorageCreateResponse(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    error: typing.Optional[StorageResponseError] = Field(default=None) 

class StorageDeleteRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 

class StorageDeleteResponse(BaseModel):
    error: typing.Optional[StorageResponseError] = Field(default=None) 

class StorageListObjectRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    object: typing.Optional[Object] = Field(default=None) 

class StorageListObjectResponse(BaseModel):
    object: typing.List[Object] = Field(default_factory=list) 
    error: typing.Optional[StorageResponseError] = Field(default=None) 

class ObjectCreateRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    object: typing.Optional[Object] = Field(default=None) 

class ObjectCreateResponse(BaseModel):
    error: typing.Optional[ObjectResponseError] = Field(default=None) 

class ObjectListRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    object: typing.Optional[Object] = Field(default=None) 

class ObjectListResponse(BaseModel):
    object: typing.List[Object] = Field(default_factory=list) 
    error: typing.Optional[ObjectResponseError] = Field(default=None) 

class ObjectGetRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 
    object: typing.Optional[Object] = Field(default=None) 

class ObjectGetResponse(BaseModel):
    object: typing.Optional[Object] = Field(default=None) 
    error: typing.Optional[ObjectResponseError] = Field(default=None) 

class ObjectDeleteRequest(BaseModel):
    object: typing.Optional[Object] = Field(default=None) 

class ObjectDeleteResponse(BaseModel):
    error: typing.Optional[ObjectResponseError] = Field(default=None) 

class ObjectStorageS3Credentials(BaseModel):
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
    s3: ObjectStorageS3Credentials = Field() 

class ObjectStorageCredentialsRequest(BaseModel):
    storage: typing.Optional[Storage] = Field(default=None) 

class ObjectStorageCredentialsResponse(BaseModel):
    credentials: typing.Optional[ObjectStorageCredentials] = Field(default=None) 
    error: typing.Optional[ObjectStorageCredentialsResponseError] = Field(default=None) 
