# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from pydantic import BaseModel

class Error(IntEnum):
    NO_ERROR = 0
    INTERNAL_SERVER_ERROR = 199
    IAM_USER_NOT_FOUND = 200
    WORKSPACE_NOT_FOUND = 300
    WORKSPACE_USER_ALREADY_EXISTS = 302
    WORKSPACE_USER_NOT_FOUND = 303
    WORKSPACE_USER_ALREADY_ACTIVE = 304
    WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE = 305
    WORKSPACE_PLUGIN_NOT_FOUND = 306
    WORKSPACE_INVITE_INVALID = 307
    WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE = 308
    CREDITS_USER_HAS_NO_PARENT = 400
