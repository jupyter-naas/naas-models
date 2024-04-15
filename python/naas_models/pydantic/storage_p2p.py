# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing



class StorageError(IntEnum):
    STORAGE_NO_ERROR = 0
    STORAGE_ALREADY_EXIST = 1
    STORAGE_NOT_FOUND = 2


class ObjectError(IntEnum):
    OBJECT_NO_ERROR = 0
    OBJECT_ALREADY_EXIST = 1
    OBJECT_SIZE_ERROR = 2
    OBJECT_NOT_FOUND = 3
    OBJECT_DIR_NOT_EMPTY = 4


class CredentialsError(IntEnum):
    CREDENTIALS_NO_ERROR = 0




class Storage(BaseModel):

    _one_of_dict = {"Storage._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class Object(BaseModel):

    _one_of_dict = {"Object._lastmodified": {"fields": {"lastmodified"}}, "Object._name": {"fields": {"name"}}, "Object._prefix": {"fields": {"prefix"}}, "Object._size": {"fields": {"size"}}, "Object._type": {"fields": {"type"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    type: str = FieldInfo(default="") 
    prefix: str = FieldInfo(default="") 
    size: str = FieldInfo(default="") 
    lastmodified: str = FieldInfo(default="") 




class StorageResponseError(BaseModel):

    _one_of_dict = {"StorageResponseError._error": {"fields": {"error"}}, "StorageResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: StorageError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class ObjectResponseError(BaseModel):

    _one_of_dict = {"ObjectResponseError._error": {"fields": {"error"}}, "ObjectResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ObjectError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class ObjectStorageCredentialsResponseError(BaseModel):

    _one_of_dict = {"ObjectStorageCredentialsResponseError._error": {"fields": {"error"}}, "ObjectStorageCredentialsResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: CredentialsError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class StorageListRequest(BaseModel):

    _one_of_dict = {"StorageListRequest._object": {"fields": {"object"}}, "StorageListRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    object: Object = FieldInfo() 




class StorageListResponse(BaseModel):

    _one_of_dict = {"StorageListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: typing.List[Storage] = FieldInfo(default_factory=list) 
    error: StorageResponseError = FieldInfo() 




class StorageCreateRequest(BaseModel):

    _one_of_dict = {"StorageCreateRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 




class StorageCreateResponse(BaseModel):

    _one_of_dict = {"StorageCreateResponse._error": {"fields": {"error"}}, "StorageCreateResponse._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    error: StorageResponseError = FieldInfo() 




class StorageDeleteRequest(BaseModel):

    _one_of_dict = {"StorageDeleteRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 




class StorageDeleteResponse(BaseModel):

    _one_of_dict = {"StorageDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: StorageResponseError = FieldInfo() 




class StorageListObjectRequest(BaseModel):

    _one_of_dict = {"StorageListObjectRequest._object": {"fields": {"object"}}, "StorageListObjectRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    object: Object = FieldInfo() 




class StorageListObjectResponse(BaseModel):

    _one_of_dict = {"StorageListObjectResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    object: typing.List[Object] = FieldInfo(default_factory=list) 
    error: StorageResponseError = FieldInfo() 




class ObjectCreateRequest(BaseModel):

    _one_of_dict = {"ObjectCreateRequest._object": {"fields": {"object"}}, "ObjectCreateRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    object: Object = FieldInfo() 




class ObjectCreateResponse(BaseModel):

    _one_of_dict = {"ObjectCreateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: StorageResponseError = FieldInfo() 




class ObjectListRequest(BaseModel):

    _one_of_dict = {"ObjectListRequest._object": {"fields": {"object"}}, "ObjectListRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    object: Object = FieldInfo() 




class ObjectListResponse(BaseModel):

    _one_of_dict = {"ObjectListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    object: typing.List[Object] = FieldInfo(default_factory=list) 
    error: ObjectResponseError = FieldInfo() 




class ObjectGetRequest(BaseModel):

    _one_of_dict = {"ObjectGetRequest._object": {"fields": {"object"}}, "ObjectGetRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    object: Object = FieldInfo() 




class ObjectGetResponse(BaseModel):

    _one_of_dict = {"ObjectGetResponse._error": {"fields": {"error"}}, "ObjectGetResponse._object": {"fields": {"object"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    object: Object = FieldInfo() 
    error: ObjectResponseError = FieldInfo() 




class ObjectDeleteRequest(BaseModel):

    _one_of_dict = {"ObjectDeleteRequest._object": {"fields": {"object"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    object: Object = FieldInfo() 




class ObjectDeleteResponse(BaseModel):

    _one_of_dict = {"ObjectDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ObjectResponseError = FieldInfo() 




class ObjectStorageS3Credentials(BaseModel):

    _one_of_dict = {"ObjectStorageS3Credentials._access_key_id": {"fields": {"access_key_id"}}, "ObjectStorageS3Credentials._endpoint_url": {"fields": {"endpoint_url"}}, "ObjectStorageS3Credentials._expiration": {"fields": {"expiration"}}, "ObjectStorageS3Credentials._region_name": {"fields": {"region_name"}}, "ObjectStorageS3Credentials._secret_key": {"fields": {"secret_key"}}, "ObjectStorageS3Credentials._session_token": {"fields": {"session_token"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    endpoint_url: str = FieldInfo(default="") 
    region_name: str = FieldInfo(default="") 
    access_key_id: str = FieldInfo(default="") 
    secret_key: str = FieldInfo(default="") 
    session_token: str = FieldInfo(default="") 
    expiration: str = FieldInfo(default="") 




class ObjectStorageAzureCredentials(BaseModel):

    _one_of_dict = {"ObjectStorageAzureCredentials._access_key_id": {"fields": {"access_key_id"}}, "ObjectStorageAzureCredentials._endpoint_url": {"fields": {"endpoint_url"}}, "ObjectStorageAzureCredentials._secret_key": {"fields": {"secret_key"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    endpoint_url: str = FieldInfo(default="") 
    access_key_id: str = FieldInfo(default="") 
    secret_key: str = FieldInfo(default="") 




class ObjectStorageCredentials(BaseModel):

    s3: ObjectStorageS3Credentials = FieldInfo() 




class ObjectStorageCredentialsRequest(BaseModel):

    _one_of_dict = {"ObjectStorageCredentialsRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 




class ObjectStorageCredentialsResponse(BaseModel):

    _one_of_dict = {"ObjectStorageCredentialsResponse._credentials": {"fields": {"credentials"}}, "ObjectStorageCredentialsResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    credentials: ObjectStorageCredentials = FieldInfo() 
    error: ObjectStorageCredentialsResponseError = FieldInfo() 


