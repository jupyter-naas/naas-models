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



class RegistryError(IntEnum):
    REGISTRY_ALREADY_EXISTS = 0
    REGISTRY_NOT_FOUND = 1
    NOT_AUTHORIZED = 2




class Registry(BaseModel):

    _one_of_dict = {"Registry._name": {"fields": {"name"}}, "Registry._uri": {"fields": {"uri"}}, "Registry._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: str = FieldInfo(default="") 
    uri: str = FieldInfo(default="") 




class RegistryCredentials(BaseModel):

    _one_of_dict = {"RegistryCredentials._password": {"fields": {"password"}}, "RegistryCredentials._username": {"fields": {"username"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    username: str = FieldInfo(default="") 
    password: str = FieldInfo(default="") 




class RegistryCreationRequest(BaseModel):

    _one_of_dict = {"RegistryCreationRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 




class RegistryCreationResponse(BaseModel):

    _one_of_dict = {"RegistryCreationResponse._registry": {"fields": {"registry"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    registry: Registry = FieldInfo() 




class RegistryCreationResponseError(BaseModel):

    _one_of_dict = {"RegistryCreationResponseError._error": {"fields": {"error"}}, "RegistryCreationResponseError._error_message": {"fields": {"error_message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: RegistryError = FieldInfo(default=0) 
    error_message: str = FieldInfo(default="") 




class RegistryListRequest(BaseModel):

    _one_of_dict = {"RegistryListRequest._page_number": {"fields": {"page_number"}}, "RegistryListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class RegistryListResponse(BaseModel):

    registries: typing.List[Registry] = FieldInfo(default_factory=list) 




class RegistryGetRequest(BaseModel):

    _one_of_dict = {"RegistryGetRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 




class RegistryGetResponse(BaseModel):

    _one_of_dict = {"RegistryGetResponse._registry": {"fields": {"registry"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    registry: Registry = FieldInfo() 




class RegistryGetResponseError(BaseModel):

    _one_of_dict = {"RegistryGetResponseError._error": {"fields": {"error"}}, "RegistryGetResponseError._error_message": {"fields": {"error_message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: RegistryError = FieldInfo(default=0) 
    error_message: str = FieldInfo(default="") 




class RegistryDeleteRequest(BaseModel):

    _one_of_dict = {"RegistryDeleteRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 




class RegistryDeleteResponseError(BaseModel):

    _one_of_dict = {"RegistryDeleteResponseError._error": {"fields": {"error"}}, "RegistryDeleteResponseError._error_message": {"fields": {"error_message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: RegistryError = FieldInfo(default=0) 
    error_message: str = FieldInfo(default="") 




class RegistryCredentialsRequest(BaseModel):

    _one_of_dict = {"RegistryCredentialsRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 




class RegistryCredentialsResponse(BaseModel):

    _one_of_dict = {"RegistryCredentialsResponse._credentials": {"fields": {"credentials"}}, "RegistryCredentialsResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    credentials: RegistryCredentials = FieldInfo() 




class RegistryCredentialsResponseError(BaseModel):

    _one_of_dict = {"RegistryCredentialsResponseError._error": {"fields": {"error"}}, "RegistryCredentialsResponseError._error_message": {"fields": {"error_message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: RegistryError = FieldInfo(default=0) 
    error_message: str = FieldInfo(default="") 


