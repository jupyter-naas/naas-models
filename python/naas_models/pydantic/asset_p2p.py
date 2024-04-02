# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

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
    INTERNAL_SERVER_ERROR = 1000




class Asset(BaseModel):

    _one_of_dict = {"Asset._content_disposition": {"fields": {"content_disposition"}}, "Asset._content_type": {"fields": {"content_type"}}, "Asset._created_at": {"fields": {"created_at"}}, "Asset._id": {"fields": {"id"}}, "Asset._prefix": {"fields": {"prefix"}}, "Asset._updated_at": {"fields": {"updated_at"}}, "Asset._user_id": {"fields": {"user_id"}}, "Asset._version_id": {"fields": {"version_id"}}, "Asset._visibility": {"fields": {"visibility"}}, "Asset._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: str = FieldInfo(default="") 
    workspace_id: str = FieldInfo(default="") 
    user_id: str = FieldInfo(default="") 
    prefix: str = FieldInfo(default="") 
    version_id: str = FieldInfo(default="") 
    visibility: str = FieldInfo(default="") 
    content_type: str = FieldInfo(default="") 
    content_disposition: str = FieldInfo(default="") 
    created_at: str = FieldInfo(default="") 
    updated_at: str = FieldInfo(default="") 




class AssetCreation(BaseModel):

    _one_of_dict = {"AssetCreation._object": {"fields": {"object"}}, "AssetCreation._storage_name": {"fields": {"storage_name"}}, "AssetCreation._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    storage_name: str = FieldInfo(default="") 
    object: str = FieldInfo(default="") 




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


