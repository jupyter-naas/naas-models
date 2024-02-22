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


class ObjectError(IntEnum):
    OBJECT_NO_ERROR = 0




class Storage(BaseModel):

    _one_of_dict = {"Storage._name": {"fields": {"name"}}, "Storage._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: str = FieldInfo(default="") 
    name: str = FieldInfo(default="") 




class Object(BaseModel):

    _one_of_dict = {"Object._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




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




class StorageCreateRequest(BaseModel):

    _one_of_dict = {"StorageCreateRequest._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 




class StorageCreateResponse(BaseModel):

    _one_of_dict = {"StorageCreateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: StorageResponseError = FieldInfo() 




class StorageGetRequest(BaseModel):

    _one_of_dict = {"StorageGetRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class StorageGetResponse(BaseModel):

    _one_of_dict = {"StorageGetResponse._error": {"fields": {"error"}}, "StorageGetResponse._storage": {"fields": {"storage"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    storage: Storage = FieldInfo() 
    error: StorageResponseError = FieldInfo() 




class StorageDeleteRequest(BaseModel):

    _one_of_dict = {"StorageDeleteRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class StorageDeleteResponse(BaseModel):

    _one_of_dict = {"StorageDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: StorageResponseError = FieldInfo() 




class StorageListRequest(BaseModel):

    _one_of_dict = {"StorageListRequest._page_number": {"fields": {"page_number"}}, "StorageListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class StorageListResponse(BaseModel):

    _one_of_dict = {"StorageListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    directories: typing.List[Storage] = FieldInfo(default_factory=list) 
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


