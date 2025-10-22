# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.12.3 
from .errors_p2p import ErrorResponse
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
    first_name: typing.Optional[str] = Field(default="")
    last_name: typing.Optional[str] = Field(default="")
    email: typing.Optional[str] = Field(default="")
    profile_picture_url: typing.Optional[str] = Field(default="")

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
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class InvitedWorkspaceListRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")

class InvitedWorkspaceListResponse(BaseModel):
    workspaces: typing.List[Workspace] = Field(default_factory=list)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceCreateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace: typing.Optional[WorkspaceCreation] = Field(default_factory=WorkspaceCreation)

class WorkspaceCreateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default_factory=Workspace)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceGetResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default_factory=Workspace)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    workspace: typing.Optional[WorkspaceUpdate] = Field(default_factory=WorkspaceUpdate)

class WorkspaceUpdateResponse(BaseModel):
    workspace: typing.Optional[Workspace] = Field(default_factory=Workspace)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceInviteUserRequest(BaseModel):
    _one_of_dict = {"WorkspaceInviteUserRequest.user": {"fields": {"email", "user_id"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    workspace_id: typing.Optional[UUID] = Field(default="")
    user_id: UUID = Field(default="")
    email: EmailStr = Field(default="")
    role: typing.Optional[str] = Field(default="", in_=["owner", "admin", "member"])

    role_in_validator = field_validator("role", mode="after",check_fields=None)(in_validator)

class WorkspaceInviteUserResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default_factory=WorkspaceUser)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceUserListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceUserListResponse(BaseModel):
    workspace_users: typing.List[WorkspaceUser] = Field(default_factory=list)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceUserGetRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceUserGetResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default_factory=WorkspaceUser)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceUserUpdateRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace_id: typing.Optional[UUID] = Field(default="")
    workspace_user: typing.Optional[WorkspaceUserUpdate] = Field(default_factory=WorkspaceUserUpdate)

class WorkspaceUserUpdateResponse(BaseModel):
    workspace_user: typing.Optional[WorkspaceUser] = Field(default_factory=WorkspaceUser)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceUserDeleteRequest(BaseModel):
    user_id: typing.Optional[UUID] = Field(default="")
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceUserDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspacePluginCreateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    payload: typing.Optional[str] = Field(default="")
    is_public: typing.Optional[bool] = Field(default=False)

class WorkspacePluginCreateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default_factory=WorkspacePlugin)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspacePluginGetRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    plugin_id: typing.Optional[UUID] = Field(default="")

class WorkspacePluginGetResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default_factory=WorkspacePlugin)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspacePluginListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspacePluginListResponse(BaseModel):
    workspace_plugins: typing.List[WorkspacePlugin] = Field(default_factory=list)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspacePluginUpdateRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    plugin_id: typing.Optional[UUID] = Field(default="")
    workspace_plugin: typing.Optional[WorkspacePluginUpdate] = Field(default_factory=WorkspacePluginUpdate)

class WorkspacePluginUpdateResponse(BaseModel):
    workspace_plugin: typing.Optional[WorkspacePlugin] = Field(default_factory=WorkspacePlugin)
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspacePluginDeleteRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")
    plugin_id: typing.Optional[UUID] = Field(default="")

class WorkspacePluginDeleteResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)

class WorkspaceWipeRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="")

class WorkspaceWipeResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default_factory=ErrorResponse)
