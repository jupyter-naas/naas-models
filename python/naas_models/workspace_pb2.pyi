import validate_pb2 as _validate_pb2
import errors_pb2 as _errors_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Workspace(_message.Message):
    __slots__ = ("id", "name", "fav_icon", "large_logo", "small_logo", "primary_color", "secondary_color", "tertiary_color", "text_primary_color", "text_secondary_color", "is_personal", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAV_ICON_FIELD_NUMBER: _ClassVar[int]
    LARGE_LOGO_FIELD_NUMBER: _ClassVar[int]
    SMALL_LOGO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TERTIARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    IS_PERSONAL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    fav_icon: str
    large_logo: str
    small_logo: str
    primary_color: str
    secondary_color: str
    tertiary_color: str
    text_primary_color: str
    text_secondary_color: str
    is_personal: bool
    created_at: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., fav_icon: _Optional[str] = ..., large_logo: _Optional[str] = ..., small_logo: _Optional[str] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., tertiary_color: _Optional[str] = ..., text_primary_color: _Optional[str] = ..., text_secondary_color: _Optional[str] = ..., is_personal: bool = ..., created_at: _Optional[str] = ...) -> None: ...

class WorkspaceCreation(_message.Message):
    __slots__ = ("name", "fav_icon", "large_logo", "small_logo", "primary_color", "secondary_color", "tertiary_color", "text_primary_color", "text_secondary_color", "is_personal")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAV_ICON_FIELD_NUMBER: _ClassVar[int]
    LARGE_LOGO_FIELD_NUMBER: _ClassVar[int]
    SMALL_LOGO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TERTIARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    IS_PERSONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    fav_icon: str
    large_logo: str
    small_logo: str
    primary_color: str
    secondary_color: str
    tertiary_color: str
    text_primary_color: str
    text_secondary_color: str
    is_personal: bool
    def __init__(self, name: _Optional[str] = ..., fav_icon: _Optional[str] = ..., large_logo: _Optional[str] = ..., small_logo: _Optional[str] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., tertiary_color: _Optional[str] = ..., text_primary_color: _Optional[str] = ..., text_secondary_color: _Optional[str] = ..., is_personal: bool = ...) -> None: ...

class WorkspaceUpdate(_message.Message):
    __slots__ = ("name", "fav_icon", "large_logo", "small_logo", "primary_color", "secondary_color", "tertiary_color", "text_primary_color", "text_secondary_color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAV_ICON_FIELD_NUMBER: _ClassVar[int]
    LARGE_LOGO_FIELD_NUMBER: _ClassVar[int]
    SMALL_LOGO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TERTIARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    fav_icon: str
    large_logo: str
    small_logo: str
    primary_color: str
    secondary_color: str
    tertiary_color: str
    text_primary_color: str
    text_secondary_color: str
    def __init__(self, name: _Optional[str] = ..., fav_icon: _Optional[str] = ..., large_logo: _Optional[str] = ..., small_logo: _Optional[str] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., tertiary_color: _Optional[str] = ..., text_primary_color: _Optional[str] = ..., text_secondary_color: _Optional[str] = ...) -> None: ...

class WorkspaceUser(_message.Message):
    __slots__ = ("user_id", "workspace_id", "role", "status", "create_at", "update_at", "first_name", "last_name", "email", "profile_picture_url")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    role: str
    status: str
    create_at: str
    update_at: str
    first_name: str
    last_name: str
    email: str
    profile_picture_url: str
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., role: _Optional[str] = ..., status: _Optional[str] = ..., create_at: _Optional[str] = ..., update_at: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., profile_picture_url: _Optional[str] = ...) -> None: ...

class WorkspaceUserUpdate(_message.Message):
    __slots__ = ("role", "status")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    role: str
    status: str
    def __init__(self, role: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class WorkspacePlugin(_message.Message):
    __slots__ = ("id", "workspace_id", "payload", "created_at", "is_public")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    payload: str
    created_at: str
    is_public: bool
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., payload: _Optional[str] = ..., created_at: _Optional[str] = ..., is_public: bool = ...) -> None: ...

class WorkspacePluginUpdate(_message.Message):
    __slots__ = ("payload", "is_public")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    payload: str
    is_public: bool
    def __init__(self, payload: _Optional[str] = ..., is_public: bool = ...) -> None: ...

class WorkspaceListRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class WorkspaceListResponse(_message.Message):
    __slots__ = ("workspaces", "error")
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class InvitedWorkspaceListRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class InvitedWorkspaceListResponse(_message.Message):
    __slots__ = ("workspaces", "error")
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceCreateRequest(_message.Message):
    __slots__ = ("user_id", "workspace")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace: WorkspaceCreation
    def __init__(self, user_id: _Optional[str] = ..., workspace: _Optional[_Union[WorkspaceCreation, _Mapping]] = ...) -> None: ...

class WorkspaceCreateResponse(_message.Message):
    __slots__ = ("workspace", "error")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceGetRequest(_message.Message):
    __slots__ = ("user_id", "workspace_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceGetResponse(_message.Message):
    __slots__ = ("workspace", "error")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceUpdateRequest(_message.Message):
    __slots__ = ("workspace_id", "workspace")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    workspace: WorkspaceUpdate
    def __init__(self, workspace_id: _Optional[str] = ..., workspace: _Optional[_Union[WorkspaceUpdate, _Mapping]] = ...) -> None: ...

class WorkspaceUpdateResponse(_message.Message):
    __slots__ = ("workspace", "error")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceDeleteRequest(_message.Message):
    __slots__ = ("user_id", "workspace_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _errors_pb2.ErrorResponse
    def __init__(self, error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceInviteUserRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id", "email", "role")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    email: str
    role: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class WorkspaceInviteUserResponse(_message.Message):
    __slots__ = ("workspace_user", "error")
    WORKSPACE_USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_user: WorkspaceUser
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_user: _Optional[_Union[WorkspaceUser, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceUserListRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceUserListResponse(_message.Message):
    __slots__ = ("workspace_users", "error")
    WORKSPACE_USERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_users: _containers.RepeatedCompositeFieldContainer[WorkspaceUser]
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_users: _Optional[_Iterable[_Union[WorkspaceUser, _Mapping]]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceUserGetRequest(_message.Message):
    __slots__ = ("user_id", "workspace_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceUserGetResponse(_message.Message):
    __slots__ = ("workspace_user", "error")
    WORKSPACE_USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_user: WorkspaceUser
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_user: _Optional[_Union[WorkspaceUser, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceUserUpdateRequest(_message.Message):
    __slots__ = ("user_id", "workspace_id", "workspace_user")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_USER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    workspace_user: WorkspaceUserUpdate
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., workspace_user: _Optional[_Union[WorkspaceUserUpdate, _Mapping]] = ...) -> None: ...

class WorkspaceUserUpdateResponse(_message.Message):
    __slots__ = ("workspace_user", "error")
    WORKSPACE_USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_user: WorkspaceUser
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_user: _Optional[_Union[WorkspaceUser, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceUserDeleteRequest(_message.Message):
    __slots__ = ("user_id", "workspace_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    workspace_id: str
    def __init__(self, user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceUserDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _errors_pb2.ErrorResponse
    def __init__(self, error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspacePluginCreateRequest(_message.Message):
    __slots__ = ("workspace_id", "payload", "is_public")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    payload: str
    is_public: bool
    def __init__(self, workspace_id: _Optional[str] = ..., payload: _Optional[str] = ..., is_public: bool = ...) -> None: ...

class WorkspacePluginCreateResponse(_message.Message):
    __slots__ = ("workspace_plugin", "error")
    WORKSPACE_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_plugin: WorkspacePlugin
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_plugin: _Optional[_Union[WorkspacePlugin, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspacePluginGetRequest(_message.Message):
    __slots__ = ("workspace_id", "plugin_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    plugin_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., plugin_id: _Optional[str] = ...) -> None: ...

class WorkspacePluginGetResponse(_message.Message):
    __slots__ = ("workspace_plugin", "error")
    WORKSPACE_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_plugin: WorkspacePlugin
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_plugin: _Optional[_Union[WorkspacePlugin, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspacePluginListRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class WorkspacePluginListResponse(_message.Message):
    __slots__ = ("workspace_plugins", "error")
    WORKSPACE_PLUGINS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_plugins: _containers.RepeatedCompositeFieldContainer[WorkspacePlugin]
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_plugins: _Optional[_Iterable[_Union[WorkspacePlugin, _Mapping]]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspacePluginUpdateRequest(_message.Message):
    __slots__ = ("workspace_id", "plugin_id", "workspace_plugin")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    plugin_id: str
    workspace_plugin: WorkspacePluginUpdate
    def __init__(self, workspace_id: _Optional[str] = ..., plugin_id: _Optional[str] = ..., workspace_plugin: _Optional[_Union[WorkspacePluginUpdate, _Mapping]] = ...) -> None: ...

class WorkspacePluginUpdateResponse(_message.Message):
    __slots__ = ("workspace_plugin", "error")
    WORKSPACE_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    workspace_plugin: WorkspacePlugin
    error: _errors_pb2.ErrorResponse
    def __init__(self, workspace_plugin: _Optional[_Union[WorkspacePlugin, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspacePluginDeleteRequest(_message.Message):
    __slots__ = ("workspace_id", "plugin_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    plugin_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., plugin_id: _Optional[str] = ...) -> None: ...

class WorkspacePluginDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _errors_pb2.ErrorResponse
    def __init__(self, error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...

class WorkspaceWipeRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class WorkspaceWipeResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _errors_pb2.ErrorResponse
    def __init__(self, error: _Optional[_Union[_errors_pb2.ErrorResponse, _Mapping]] = ...) -> None: ...
