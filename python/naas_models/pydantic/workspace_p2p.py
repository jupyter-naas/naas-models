# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from naas_models.pydantic.errors_p2p import ErrorResponse
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from protobuf_to_pydantic.customer_validator.v2 import in_validator
from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator
from pydantic.networks import EmailStr
from uuid import UUID
import typing


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
    created_at: typing.Optional[str] = Field(default="") 
    is_public: typing.Optional[bool] = Field(default=False) 

class WorkspacePluginUpdate(BaseModel):
    payload: typing.Optional[str] = Field(default="") 
    is_public: typing.Optional[bool] = Field(default=False) 

class WorkspaceListRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceListResponse(BaseModel):
    workspaces: typing.List[Workspace] = Field(default_factory=list) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class InvitedWorkspaceListRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 

class InvitedWorkspaceListResponse(BaseModel):
    workspaces: typing.List[Workspace] = Field(default_factory=list) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceCreateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace: typing.Optional[WorkspaceCreation] = Field(default=None) 

class WorkspaceCreateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceGetResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workspace: typing.Optional[WorkspaceUpdate] = Field(default=None) 

class WorkspaceUpdateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceInviteUserRequest(BaseModel):
    _one_of_dict = {"WorkspaceInviteUserRequest.user": {"fields": {"email", "user_id"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    workspace_id: typing.Optional[UUID] = Field(default="") 
    user_id: UUID = Field(default="") 
    email: EmailStr = Field(default="") 
    role: typing.Optional[str] = Field(default="", in_=["owner", "admin", "member"]) 

    role_in_validator = field_validator("role", mode="after",check_fields=None)(in_validator)

class WorkspaceInviteUserResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceUserListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserListResponse(BaseModel):
    workspace_users: typing.List[WorkspaceUser] = Field(default_factory=list) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceUserGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserGetResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceUserUpdateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workspace_user: typing.Optional[WorkspaceUserUpdate] = Field(default=None) 

class WorkspaceUserUpdateResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceUserDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceUserDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspacePluginCreateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    payload: typing.Optional[str] = Field(default="") 
    is_public: typing.Optional[bool] = Field(default=False) 

class WorkspacePluginCreateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspacePluginGetRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginGetResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspacePluginListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginListResponse(BaseModel):
    workspace_plugins: typing.List[WorkspacePlugin] = Field(default_factory=list) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspacePluginUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 
    workspace_plugin: typing.Optional[WorkspacePluginUpdate] = Field(default=None) 

class WorkspacePluginUpdateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspacePluginDeleteRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 

class WorkspacePluginDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class WorkspaceWipeRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkspaceWipeResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
