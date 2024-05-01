# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator.v2 import in_validator
from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator
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
    id: typing.Optional[UUID] = Field(default="") 
    name: typing.Optional[str] = Field(default="") 
    fav_icon: typing.Optional[str] = Field(default="") 
    large_logo: typing.Optional[str] = Field(default="") 
    small_logo: typing.Optional[str] = Field(default="") 
    primary_color: typing.Optional[str] = Field(default="") 
    secondary_color: typing.Optional[str] = Field(default="") 
    tertiary_color: typing.Optional[str] = Field(default="") 
    text_primary_color: typing.Optional[str] = Field(default="") 
    text_secondary_color: typing.Optional[str] = Field(default="") 
    is_personal: typing.Optional[bool] = Field(default=False) 
    created_at: typing.Optional[str] = Field(default="") 

class WorkspaceCreation(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    fav_icon: typing.Optional[str] = Field(default="") 
    large_logo: typing.Optional[str] = Field(default="") 
    small_logo: typing.Optional[str] = Field(default="") 
    primary_color: typing.Optional[str] = Field(default="") 
    secondary_color: typing.Optional[str] = Field(default="") 
    tertiary_color: typing.Optional[str] = Field(default="") 
    text_primary_color: typing.Optional[str] = Field(default="") 
    text_secondary_color: typing.Optional[str] = Field(default="") 
    is_personal: typing.Optional[bool] = Field(default=False) 

class WorkspaceUpdate(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    fav_icon: typing.Optional[str] = Field(default="") 
    large_logo: typing.Optional[str] = Field(default="") 
    small_logo: typing.Optional[str] = Field(default="") 
    primary_color: typing.Optional[str] = Field(default="") 
    secondary_color: typing.Optional[str] = Field(default="") 
    tertiary_color: typing.Optional[str] = Field(default="") 
    text_primary_color: typing.Optional[str] = Field(default="") 
    text_secondary_color: typing.Optional[str] = Field(default="") 

class WorkspaceUser(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    role: typing.Optional[str] = Field(default="", in_=["owner", "admin", "member"]) 
    status: typing.Optional[str] = Field(default="", in_=["active", "invited", "declined"]) 
    create_at: typing.Optional[str] = Field(default="") 
    update_at: typing.Optional[str] = Field(default="") 

    role_in_validator = field_validator("role", mode="after",check_fields=None)(in_validator)
    status_in_validator = field_validator("status", mode="after",check_fields=None)(in_validator)

class WorkspaceUserUpdate(BaseModel):
    role: typing.Optional[str] = Field(default="", in_=["owner", "admin", "member"]) 
    status: typing.Optional[str] = Field(default="", in_=["active", "invited", "declined"]) 

    role_in_validator = field_validator("role", mode="after",check_fields=None)(in_validator)
    status_in_validator = field_validator("status", mode="after",check_fields=None)(in_validator)

class WorkspacePlugin(BaseModel):
    id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    payload: typing.Optional[str] = Field(default="") 
    create_at: typing.Optional[str] = Field(default="") 

class WorkspacePluginUpdate(BaseModel):
    payload: typing.Optional[str] = Field(default="") 

class WorkspaceResponseError(BaseModel):
    code: typing.Optional[WorkspaceError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class WorkspaceListRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceListResponse(BaseModel):
    workspaces: typing.List[Workspace] = Field(default_factory=list) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceCreateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace: typing.Optional[WorkspaceCreation] = Field(default=None) 

class WorkspaceCreateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceGetResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workspace: typing.Optional[WorkspaceUpdate] = Field(default=None) 

class WorkspaceUpdateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceDeleteResponse(BaseModel):
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceUserListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserListResponse(BaseModel):
    workspace_users: typing.List[WorkspaceUser] = Field(default_factory=list) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceUserGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserGetResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceUserUpdateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workspace_user: typing.Optional[WorkspaceUserUpdate] = Field(default=None) 

class WorkspaceUserUpdateResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspaceUserDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserDeleteResponse(BaseModel):
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspacePluginCreateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    payload: typing.Optional[str] = Field(default="") 

class WorkspacePluginCreateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspacePluginGetRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginGetResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspacePluginListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginListResponse(BaseModel):
    workspace_plugins: typing.List[WorkspacePlugin] = Field(default_factory=list) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspacePluginUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 
    workspace_plugin: typing.Optional[WorkspacePluginUpdate] = Field(default=None) 

class WorkspacePluginUpdateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 

class WorkspacePluginDeleteRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginDeleteResponse(BaseModel):
    error: typing.Optional[WorkspaceResponseError] = Field(default=None) 
