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



class WorkspaceError(IntEnum):
    WORKSPACE_NO_ERROR = 0
    WORKSPACE_NOT_FOUND = 1
    WORKSPACE_USER_ALREADY_EXISTS = 2
    WORKSPACE_USER_NOT_FOUND = 3
    WORKSPACE_USER_ALREADY_ACTIVE = 4
    USER_ALREADY_HAVE_PERSONAL_WORKSPACE = 5
    INTERNAL_SERVER_ERROR = 1000




class Workspace(BaseModel):

    _one_of_dict = {"Workspace._create_at": {"fields": {"create_at"}}, "Workspace._id": {"fields": {"id"}}, "Workspace._is_personal": {"fields": {"is_personal"}}, "Workspace._logo": {"fields": {"logo"}}, "Workspace._name": {"fields": {"name"}}, "Workspace._primary_color": {"fields": {"primary_color"}}, "Workspace._secondary_color": {"fields": {"secondary_color"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    name: str = FieldInfo(default="") 
    logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 
    is_personal: bool = FieldInfo(default=False) 
    create_at: str = FieldInfo(default="") 




class WorkspaceUpdate(BaseModel):

    _one_of_dict = {"WorkspaceUpdate._logo": {"fields": {"logo"}}, "WorkspaceUpdate._name": {"fields": {"name"}}, "WorkspaceUpdate._primary_color": {"fields": {"primary_color"}}, "WorkspaceUpdate._secondary_color": {"fields": {"secondary_color"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 




class WorkspaceUser(BaseModel):

    _one_of_dict = {"WorkspaceUser._create_at": {"fields": {"create_at"}}, "WorkspaceUser._role": {"fields": {"role"}}, "WorkspaceUser._status": {"fields": {"status"}}, "WorkspaceUser._update_at": {"fields": {"update_at"}}, "WorkspaceUser._user_id": {"fields": {"user_id"}}, "WorkspaceUser._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 
    role: str = FieldInfo(default="") 
    status: str = FieldInfo(default="") 
    create_at: str = FieldInfo(default="") 
    update_at: str = FieldInfo(default="") 




class WorkspaceUserUpdate(BaseModel):

    _one_of_dict = {"WorkspaceUserUpdate._role": {"fields": {"role"}}, "WorkspaceUserUpdate._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    role: str = FieldInfo(default="") 
    status: str = FieldInfo(default="") 




class WorkspacePlugin(BaseModel):

    _one_of_dict = {"WorkspacePlugin._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 




class WorkspaceResponseError(BaseModel):

    _one_of_dict = {"WorkspaceResponseError._code": {"fields": {"code"}}, "WorkspaceResponseError._message": {"fields": {"message"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: WorkspaceError = FieldInfo(default=0) 
    message: str = FieldInfo(default="") 




class WorkspaceListRequest(BaseModel):

    _one_of_dict = {"WorkspaceListRequest._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 




class WorkspaceListResponse(BaseModel):

    _one_of_dict = {"WorkspaceListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspaces: typing.List[Workspace] = FieldInfo(default_factory=list) 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceCreateRequest(BaseModel):

    _one_of_dict = {"WorkspaceCreateRequest._is_personal": {"fields": {"is_personal"}}, "WorkspaceCreateRequest._logo": {"fields": {"logo"}}, "WorkspaceCreateRequest._name": {"fields": {"name"}}, "WorkspaceCreateRequest._primary_color": {"fields": {"primary_color"}}, "WorkspaceCreateRequest._secondary_color": {"fields": {"secondary_color"}}, "WorkspaceCreateRequest._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    name: str = FieldInfo(default="") 
    logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 
    is_personal: bool = FieldInfo(default=False) 




class WorkspaceCreateResponse(BaseModel):

    _one_of_dict = {"WorkspaceCreateResponse._error": {"fields": {"error"}}, "WorkspaceCreateResponse._workspace": {"fields": {"workspace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace: Workspace = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceGetRequest(BaseModel):

    _one_of_dict = {"WorkspaceGetRequest._user_id": {"fields": {"user_id"}}, "WorkspaceGetRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 




class WorkspaceGetResponse(BaseModel):

    _one_of_dict = {"WorkspaceGetResponse._error": {"fields": {"error"}}, "WorkspaceGetResponse._workspace": {"fields": {"workspace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace: Workspace = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceUpdateRequest(BaseModel):

    _one_of_dict = {"WorkspaceUpdateRequest._workspace": {"fields": {"workspace"}}, "WorkspaceUpdateRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    workspace: WorkspaceUpdate = FieldInfo() 




class WorkspaceUpdateResponse(BaseModel):

    _one_of_dict = {"WorkspaceUpdateResponse._error": {"fields": {"error"}}, "WorkspaceUpdateResponse._workspace": {"fields": {"workspace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace: Workspace = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceDeleteRequest(BaseModel):

    _one_of_dict = {"WorkspaceDeleteRequest._user_id": {"fields": {"user_id"}}, "WorkspaceDeleteRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 




class WorkspaceDeleteResponse(BaseModel):

    _one_of_dict = {"WorkspaceDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: WorkspaceResponseError = FieldInfo() 

