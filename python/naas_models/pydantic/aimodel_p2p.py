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
import typing



class AIModelError(IntEnum):
    NO_ERROR = 0
    ALREADY_EXISTS = 1
    NOT_FOUND = 2
    NOT_UPDATED = 3
    NOT_AUTHORIZED = 4
    AIMODEL_OUT_OF_CREDITS = 5
    AIMODEL_DONT_HANDLE_COMPLETION = 6




class AIModel(BaseModel):

    _one_of_dict = {"AIModel._enabled": {"fields": {"enabled"}}, "AIModel._id": {"fields": {"id"}}, "AIModel._image": {"fields": {"image"}}, "AIModel._name": {"fields": {"name"}}, "AIModel._name_alias": {"fields": {"name_alias"}}, "AIModel._provider": {"fields": {"provider"}}, "AIModel._restricted": {"fields": {"restricted"}}, "AIModel._type": {"fields": {"type"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    name: str = FieldInfo(default="") 
    provider: str = FieldInfo(default="") 
    image: str = FieldInfo(default="") 
    enabled: bool = FieldInfo(default=False) 
    type: str = FieldInfo(default="") 
    restricted: bool = FieldInfo(default=False) 
    name_alias: str = FieldInfo(default="") 




class CompletionResponse(BaseModel):

    _one_of_dict = {"CompletionResponse._image_resolution": {"fields": {"image_resolution"}}, "CompletionResponse._image_steps": {"fields": {"image_steps"}}, "CompletionResponse._input_tokens": {"fields": {"input_tokens"}}, "CompletionResponse._model_id": {"fields": {"model_id"}}, "CompletionResponse._output_tokens": {"fields": {"output_tokens"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    model_id: UUID = FieldInfo(default="") 
    completions: typing.List[str] = FieldInfo(default_factory=list) 
    input_tokens: int = FieldInfo(default=0) 
    output_tokens: int = FieldInfo(default=0) 
    image_resolution: str = FieldInfo(default="") 
    image_steps: int = FieldInfo(default=0) 




class AIModelResponseError(BaseModel):

    _one_of_dict = {"AIModelResponseError._code": {"fields": {"code"}}, "AIModelResponseError._message": {"fields": {"message"}}, "AIModelResponseError._reason": {"fields": {"reason"}}, "AIModelResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: AIModelError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class AIModelListRequest(BaseModel):

    _one_of_dict = {"AIModelListRequest._page_number": {"fields": {"page_number"}}, "AIModelListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class AIModelListResponse(BaseModel):

    _one_of_dict = {"AIModelListResponse._error": {"fields": {"error"}}, "AIModelListResponse._page_number": {"fields": {"page_number"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    aimodels: typing.List[AIModel] = FieldInfo(default_factory=list) 
    page_number: int = FieldInfo(default=0) 
    error: AIModelResponseError = FieldInfo() 




class AIModelGetRequest(BaseModel):

    _one_of_dict = {"AIModelGetRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 




class AIModelGetResponse(BaseModel):

    _one_of_dict = {"AIModelGetResponse._aimodel": {"fields": {"aimodel"}}, "AIModelGetResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    aimodel: AIModel = FieldInfo() 
    error: AIModelResponseError = FieldInfo() 




class AIModelCompletionRequest(BaseModel):

    _one_of_dict = {"AIModelCompletionRequest._id": {"fields": {"id"}}, "AIModelCompletionRequest._payload": {"fields": {"payload"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    payload: str = FieldInfo(default="") 




class AIModelCompletionResponse(BaseModel):

    _one_of_dict = {"AIModelCompletionResponse._completion": {"fields": {"completion"}}, "AIModelCompletionResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    completion: CompletionResponse = FieldInfo() 
    error: AIModelResponseError = FieldInfo() 




class AIModelAdminCreationRequest(BaseModel):

    _one_of_dict = {"AIModelAdminCreationRequest._enabled": {"fields": {"enabled"}}, "AIModelAdminCreationRequest._image": {"fields": {"image"}}, "AIModelAdminCreationRequest._name": {"fields": {"name"}}, "AIModelAdminCreationRequest._name_alias": {"fields": {"name_alias"}}, "AIModelAdminCreationRequest._provider": {"fields": {"provider"}}, "AIModelAdminCreationRequest._restricted": {"fields": {"restricted"}}, "AIModelAdminCreationRequest._type": {"fields": {"type"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    provider: str = FieldInfo(default="") 
    image: str = FieldInfo(default="") 
    enabled: bool = FieldInfo(default=False) 
    type: str = FieldInfo(default="") 
    restricted: bool = FieldInfo(default=False) 
    name_alias: str = FieldInfo(default="") 




class AIModelAdminCreationResponse(BaseModel):

    _one_of_dict = {"AIModelAdminCreationResponse._aimodel": {"fields": {"aimodel"}}, "AIModelAdminCreationResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    aimodel: AIModel = FieldInfo() 
    error: AIModelResponseError = FieldInfo() 




class AIModelAdminDeleteRequest(BaseModel):

    _one_of_dict = {"AIModelAdminDeleteRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 




class AIModelAdminDeleteResponse(BaseModel):

    _one_of_dict = {"AIModelAdminDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: AIModelResponseError = FieldInfo() 


