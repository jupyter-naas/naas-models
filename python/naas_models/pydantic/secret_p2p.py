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



class SecretError(IntEnum):
    SECRET_NO_ERROR = 0
    SECRET_ALREADY_EXISTS = 1
    SECRET_NOT_FOUND = 2
    SECRET_MARKED_FOR_DELETION = 3




class Secret(BaseModel):

    _one_of_dict = {"Secret._name": {"fields": {"name"}}, "Secret._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    value: str = FieldInfo(default="") 




class SecretResponseError(BaseModel):

    _one_of_dict = {"SecretResponseError._error": {"fields": {"error"}}, "SecretResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: SecretError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class SecretCreateRequest(BaseModel):

    _one_of_dict = {"SecretCreateRequest._secret": {"fields": {"secret"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    secret: Secret = FieldInfo() 




class SecretCreateResponse(BaseModel):

    _one_of_dict = {"SecretCreateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: SecretResponseError = FieldInfo() 




class SecretGetRequest(BaseModel):

    _one_of_dict = {"SecretGetRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class SecretGetResponse(BaseModel):

    _one_of_dict = {"SecretGetResponse._error": {"fields": {"error"}}, "SecretGetResponse._secret": {"fields": {"secret"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    secret: Secret = FieldInfo() 
    error: SecretResponseError = FieldInfo() 




class SecretDeleteRequest(BaseModel):

    _one_of_dict = {"SecretDeleteRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class SecretDeleteResponse(BaseModel):

    _one_of_dict = {"SecretDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: SecretResponseError = FieldInfo() 




class SecretListRequest(BaseModel):

    _one_of_dict = {"SecretListRequest._page_number": {"fields": {"page_number"}}, "SecretListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class SecretListResponse(BaseModel):

    _one_of_dict = {"SecretListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    secrets: typing.List[Secret] = FieldInfo(default_factory=list) 
    error: SecretResponseError = FieldInfo() 




class SecretBulkCreateRequest(BaseModel):

    secrets: typing.List[Secret] = FieldInfo(default_factory=list) 




class SecretBulkCreateResponse(BaseModel):

    error: typing.List[SecretResponseError] = FieldInfo(default_factory=list) 


