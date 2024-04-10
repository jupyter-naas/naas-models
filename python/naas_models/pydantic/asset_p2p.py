# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
from uuid import UUID



class AssetError(IntEnum):
    ASSET_NO_ERROR = 0
    ASSET_NOT_FOUND = 1
    ASSET_ALREADY_EXISTS = 2
    INTERNAL_SERVER_ERROR = 1000




class Asset(BaseModel):

    _one_of_dict = {"Asset._asset_created_at": {"fields": {"asset_created_at"}}, "Asset._content_disposition": {"fields": {"content_disposition"}}, "Asset._content_type": {"fields": {"content_type"}}, "Asset._id": {"fields": {"id"}}, "Asset._object_name": {"fields": {"object_name"}}, "Asset._object_updated_at": {"fields": {"object_updated_at"}}, "Asset._object_version": {"fields": {"object_version"}}, "Asset._password": {"fields": {"password"}}, "Asset._prefix": {"fields": {"prefix"}}, "Asset._provider": {"fields": {"provider"}}, "Asset._provider_bucket_name": {"fields": {"provider_bucket_name"}}, "Asset._storage_name": {"fields": {"storage_name"}}, "Asset._url": {"fields": {"url"}}, "Asset._user_id": {"fields": {"user_id"}}, "Asset._visibility": {"fields": {"visibility"}}, "Asset._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    object_name: str = FieldInfo(default="") 
    visibility: str = FieldInfo(default="") 
    content_disposition: str = FieldInfo(default="") 
    password: str = FieldInfo(default="") 
    url: str = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 
    storage_name: str = FieldInfo(default="") 
    prefix: str = FieldInfo(default="") 
    object_version: str = FieldInfo(default="") 
    content_type: str = FieldInfo(default="") 
    object_updated_at: datetime = FieldInfo(default_factory=datetime.now) 
    asset_created_at: datetime = FieldInfo(default_factory=datetime.now) 
    user_id: UUID = FieldInfo(default="") 
    provider: str = FieldInfo(default="") 
    provider_bucket_name: str = FieldInfo(default="") 




class AssetCreation(BaseModel):

    _one_of_dict = {"AssetCreation._content_disposition": {"fields": {"content_disposition"}}, "AssetCreation._object_name": {"fields": {"object_name"}}, "AssetCreation._object_version": {"fields": {"object_version"}}, "AssetCreation._password": {"fields": {"password"}}, "AssetCreation._storage_name": {"fields": {"storage_name"}}, "AssetCreation._visibility": {"fields": {"visibility"}}, "AssetCreation._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    storage_name: str = FieldInfo(default="") 
    object_name: str = FieldInfo(default="") 
    object_version: str = FieldInfo(default="") 
    visibility: str = FieldInfo(default="") 
    content_disposition: str = FieldInfo(default="") 
    password: str = FieldInfo(default="") 




class AssetUpdate(BaseModel):

    _one_of_dict = {"AssetUpdate._content_disposition": {"fields": {"content_disposition"}}, "AssetUpdate._visibility": {"fields": {"visibility"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    visibility: str = FieldInfo(default="") 
    content_disposition: str = FieldInfo(default="") 




class AssetResponseError(BaseModel):

    _one_of_dict = {"AssetResponseError._code": {"fields": {"code"}}, "AssetResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: AssetError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class AssetCreateRequest(BaseModel):

    _one_of_dict = {"AssetCreateRequest._asset": {"fields": {"asset"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    asset: AssetCreation = FieldInfo() 




class AssetCreateResponse(BaseModel):

    _one_of_dict = {"AssetCreateResponse._asset": {"fields": {"asset"}}, "AssetCreateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    asset: Asset = FieldInfo() 
    error: AssetResponseError = FieldInfo() 




class AssetGetRequest(BaseModel):

    _one_of_dict = {"AssetGetRequest._asset_id": {"fields": {"asset_id"}}, "AssetGetRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    asset_id: UUID = FieldInfo(default="") 




class AssetGetResponse(BaseModel):

    _one_of_dict = {"AssetGetResponse._asset": {"fields": {"asset"}}, "AssetGetResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    asset: Asset = FieldInfo() 
    error: AssetResponseError = FieldInfo() 




class AssetGetObjectRequest(BaseModel):

    _one_of_dict = {"AssetGetObjectRequest._asset_id": {"fields": {"asset_id"}}, "AssetGetObjectRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    asset_id: UUID = FieldInfo(default="") 




class AssetGetObjectResponse(BaseModel):

    _one_of_dict = {"AssetGetObjectResponse._error": {"fields": {"error"}}, "AssetGetObjectResponse._url": {"fields": {"url"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    url: str = FieldInfo(default="") 
    error: AssetResponseError = FieldInfo() 




class AssetUpdateRequest(BaseModel):

    _one_of_dict = {"AssetUpdateRequest._asset_update": {"fields": {"asset_update"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    asset_update: AssetUpdate = FieldInfo() 




class AssetUpdateResponse(BaseModel):

    _one_of_dict = {"AssetUpdateResponse._asset": {"fields": {"asset"}}, "AssetUpdateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    asset: Asset = FieldInfo() 
    error: AssetResponseError = FieldInfo() 




class AssetDeleteRequest(BaseModel):

    _one_of_dict = {"AssetDeleteRequest._asset_id": {"fields": {"asset_id"}}, "AssetDeleteRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    asset_id: UUID = FieldInfo(default="") 




class AssetDeleteResponse(BaseModel):

    _one_of_dict = {"AssetDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: AssetResponseError = FieldInfo() 


