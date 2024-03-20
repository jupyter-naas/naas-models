# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from protobuf_to_pydantic.customer_validator import in_validator
from pydantic import BaseModel
from pydantic import root_validator
from pydantic import validator
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
    WORKSPACE_PLUGIN_NOT_FOUND = 6
    INTERNAL_SERVER_ERROR = 1000




class Workspace(BaseModel):

    _one_of_dict = {"Workspace._created_at": {"fields": {"created_at"}}, "Workspace._fav_icon": {"fields": {"fav_icon"}}, "Workspace._id": {"fields": {"id"}}, "Workspace._is_personal": {"fields": {"is_personal"}}, "Workspace._large_logo": {"fields": {"large_logo"}}, "Workspace._name": {"fields": {"name"}}, "Workspace._primary_color": {"fields": {"primary_color"}}, "Workspace._secondary_color": {"fields": {"secondary_color"}}, "Workspace._small_logo": {"fields": {"small_logo"}}, "Workspace._tertiary_color": {"fields": {"tertiary_color"}}, "Workspace._text_primary_color": {"fields": {"text_primary_color"}}, "Workspace._text_secondary_color": {"fields": {"text_secondary_color"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    name: str = FieldInfo(default="") 
    fav_icon: str = FieldInfo(default="") 
    large_logo: str = FieldInfo(default="") 
    small_logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 
    tertiary_color: str = FieldInfo(default="") 
    text_primary_color: str = FieldInfo(default="") 
    text_secondary_color: str = FieldInfo(default="") 
    is_personal: bool = FieldInfo(default=False) 
    created_at: str = FieldInfo(default="") 




class WorkspaceCreation(BaseModel):

    _one_of_dict = {"WorkspaceCreation._fav_icon": {"fields": {"fav_icon"}}, "WorkspaceCreation._is_personal": {"fields": {"is_personal"}}, "WorkspaceCreation._large_logo": {"fields": {"large_logo"}}, "WorkspaceCreation._name": {"fields": {"name"}}, "WorkspaceCreation._primary_color": {"fields": {"primary_color"}}, "WorkspaceCreation._secondary_color": {"fields": {"secondary_color"}}, "WorkspaceCreation._small_logo": {"fields": {"small_logo"}}, "WorkspaceCreation._tertiary_color": {"fields": {"tertiary_color"}}, "WorkspaceCreation._text_primary_color": {"fields": {"text_primary_color"}}, "WorkspaceCreation._text_secondary_color": {"fields": {"text_secondary_color"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    fav_icon: str = FieldInfo(default="") 
    large_logo: str = FieldInfo(default="") 
    small_logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 
    tertiary_color: str = FieldInfo(default="") 
    text_primary_color: str = FieldInfo(default="") 
    text_secondary_color: str = FieldInfo(default="") 
    is_personal: bool = FieldInfo(default=False) 




class WorkspaceUpdate(BaseModel):

    _one_of_dict = {"WorkspaceUpdate._fav_icon": {"fields": {"fav_icon"}}, "WorkspaceUpdate._large_logo": {"fields": {"large_logo"}}, "WorkspaceUpdate._name": {"fields": {"name"}}, "WorkspaceUpdate._primary_color": {"fields": {"primary_color"}}, "WorkspaceUpdate._secondary_color": {"fields": {"secondary_color"}}, "WorkspaceUpdate._small_logo": {"fields": {"small_logo"}}, "WorkspaceUpdate._tertiary_color": {"fields": {"tertiary_color"}}, "WorkspaceUpdate._text_primary_color": {"fields": {"text_primary_color"}}, "WorkspaceUpdate._text_secondary_color": {"fields": {"text_secondary_color"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    fav_icon: str = FieldInfo(default="") 
    large_logo: str = FieldInfo(default="") 
    small_logo: str = FieldInfo(default="") 
    primary_color: str = FieldInfo(default="") 
    secondary_color: str = FieldInfo(default="") 
    tertiary_color: str = FieldInfo(default="") 
    text_primary_color: str = FieldInfo(default="") 
    text_secondary_color: str = FieldInfo(default="") 




class WorkspaceUser(BaseModel):

    role_in_validator = validator("role",  allow_reuse=True)(in_validator)
    status_in_validator = validator("status",  allow_reuse=True)(in_validator)
    _one_of_dict = {"WorkspaceUser._create_at": {"fields": {"create_at"}}, "WorkspaceUser._role": {"fields": {"role"}}, "WorkspaceUser._status": {"fields": {"status"}}, "WorkspaceUser._update_at": {"fields": {"update_at"}}, "WorkspaceUser._user_id": {"fields": {"user_id"}}, "WorkspaceUser._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 
    role: str = FieldInfo(default="", in_=["admin", "member", "owner"]) 
    status: str = FieldInfo(default="", in_=["active", "declined", "invited"]) 
    create_at: str = FieldInfo(default="") 
    update_at: str = FieldInfo(default="") 




class WorkspaceUserUpdate(BaseModel):

    role_in_validator = validator("role",  allow_reuse=True)(in_validator)
    status_in_validator = validator("status",  allow_reuse=True)(in_validator)
    _one_of_dict = {"WorkspaceUserUpdate._role": {"fields": {"role"}}, "WorkspaceUserUpdate._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    role: str = FieldInfo(default="", in_=["admin", "member", "owner"]) 
    status: str = FieldInfo(default="", in_=["active", "declined", "invited"]) 




class WorkspacePlugin(BaseModel):

    _one_of_dict = {"WorkspacePlugin._create_at": {"fields": {"create_at"}}, "WorkspacePlugin._id": {"fields": {"id"}}, "WorkspacePlugin._payload": {"fields": {"payload"}}, "WorkspacePlugin._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 
    payload: str = FieldInfo(default="") 
    create_at: str = FieldInfo(default="") 




class WorkspacePluginUpdate(BaseModel):

    _one_of_dict = {"WorkspacePluginUpdate._payload": {"fields": {"payload"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    payload: str = FieldInfo(default="") 




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

    _one_of_dict = {"WorkspaceCreateRequest._user_id": {"fields": {"user_id"}}, "WorkspaceCreateRequest._workspace": {"fields": {"workspace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace: WorkspaceCreation = FieldInfo() 




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




class WorkspaceUserListRequest(BaseModel):

    _one_of_dict = {"WorkspaceUserListRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 




class WorkspaceUserListResponse(BaseModel):

    _one_of_dict = {"WorkspaceUserListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_users: typing.List[WorkspaceUser] = FieldInfo(default_factory=list) 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceUserGetRequest(BaseModel):

    _one_of_dict = {"WorkspaceUserGetRequest._user_id": {"fields": {"user_id"}}, "WorkspaceUserGetRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 




class WorkspaceUserGetResponse(BaseModel):

    _one_of_dict = {"WorkspaceUserGetResponse._error": {"fields": {"error"}}, "WorkspaceUserGetResponse._workspace_user": {"fields": {"workspace_user"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_user: WorkspaceUser = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceUserUpdateRequest(BaseModel):

    _one_of_dict = {"WorkspaceUserUpdateRequest._user_id": {"fields": {"user_id"}}, "WorkspaceUserUpdateRequest._workspace_id": {"fields": {"workspace_id"}}, "WorkspaceUserUpdateRequest._workspace_user": {"fields": {"workspace_user"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 
    workspace_user: WorkspaceUserUpdate = FieldInfo() 




class WorkspaceUserUpdateResponse(BaseModel):

    _one_of_dict = {"WorkspaceUserUpdateResponse._error": {"fields": {"error"}}, "WorkspaceUserUpdateResponse._workspace_user": {"fields": {"workspace_user"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_user: WorkspaceUser = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspaceUserDeleteRequest(BaseModel):

    _one_of_dict = {"WorkspaceUserDeleteRequest._user_id": {"fields": {"user_id"}}, "WorkspaceUserDeleteRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    workspace_id: UUID = FieldInfo(default="") 




class WorkspaceUserDeleteResponse(BaseModel):

    _one_of_dict = {"WorkspaceUserDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: WorkspaceResponseError = FieldInfo() 




class WorkspacePluginCreateRequest(BaseModel):

    _one_of_dict = {"WorkspacePluginCreateRequest._payload": {"fields": {"payload"}}, "WorkspacePluginCreateRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    payload: str = FieldInfo(default="") 




class WorkspacePluginCreateResponse(BaseModel):

    _one_of_dict = {"WorkspacePluginCreateResponse._error": {"fields": {"error"}}, "WorkspacePluginCreateResponse._workspace_plugin": {"fields": {"workspace_plugin"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_plugin: WorkspacePlugin = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspacePluginGetRequest(BaseModel):

    _one_of_dict = {"WorkspacePluginGetRequest._plugin_id": {"fields": {"plugin_id"}}, "WorkspacePluginGetRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    plugin_id: UUID = FieldInfo(default="") 




class WorkspacePluginGetResponse(BaseModel):

    _one_of_dict = {"WorkspacePluginGetResponse._error": {"fields": {"error"}}, "WorkspacePluginGetResponse._workspace_plugin": {"fields": {"workspace_plugin"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_plugin: WorkspacePlugin = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspacePluginListRequest(BaseModel):

    _one_of_dict = {"WorkspacePluginListRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 




class WorkspacePluginListResponse(BaseModel):

    _one_of_dict = {"WorkspacePluginListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_plugins: typing.List[WorkspacePlugin] = FieldInfo(default_factory=list) 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspacePluginUpdateRequest(BaseModel):

    _one_of_dict = {"WorkspacePluginUpdateRequest._plugin_id": {"fields": {"plugin_id"}}, "WorkspacePluginUpdateRequest._workspace_id": {"fields": {"workspace_id"}}, "WorkspacePluginUpdateRequest._workspace_plugin": {"fields": {"workspace_plugin"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    plugin_id: UUID = FieldInfo(default="") 
    workspace_plugin: WorkspacePluginUpdate = FieldInfo() 




class WorkspacePluginUpdateResponse(BaseModel):

    _one_of_dict = {"WorkspacePluginUpdateResponse._error": {"fields": {"error"}}, "WorkspacePluginUpdateResponse._workspace_plugin": {"fields": {"workspace_plugin"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_plugin: WorkspacePlugin = FieldInfo() 
    error: WorkspaceResponseError = FieldInfo() 




class WorkspacePluginDeleteRequest(BaseModel):

    _one_of_dict = {"WorkspacePluginDeleteRequest._plugin_id": {"fields": {"plugin_id"}}, "WorkspacePluginDeleteRequest._workspace_id": {"fields": {"workspace_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workspace_id: UUID = FieldInfo(default="") 
    plugin_id: UUID = FieldInfo(default="") 




class WorkspacePluginDeleteResponse(BaseModel):

    _one_of_dict = {"WorkspacePluginDeleteResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: WorkspaceResponseError = FieldInfo() 


