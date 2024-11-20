# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class Error(IntEnum):
    NO_ERROR = 0
    INTERNAL_SERVER_ERROR = 199
    IAM_USER_NOT_FOUND = 200
    IAM_USER_NOT_AUTHORIZED = 201
    IAM_API_KEY_ALREADY_EXISTS = 202
    WORKSPACE_NOT_FOUND = 300
    WORKSPACE_USER_ALREADY_EXISTS = 302
    WORKSPACE_USER_NOT_FOUND = 303
    WORKSPACE_USER_ALREADY_ACTIVE = 304
    WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE = 305
    WORKSPACE_PLUGIN_NOT_FOUND = 306
    WORKSPACE_INVITE_INVALID = 307
    WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE = 308
    CREDITS_USER_HAS_NO_PARENT = 400
    CREDITS_OUT_OF_CREDITS = 401
    ONTOLOGY_NOT_FOUND = 500
    CHAT_NOT_FOUND = 600
    CHAT_NOT_AUTHORIZED = 601
    CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXIST = 602
    CHAT_CONTEXT_LENGTH_EXCEEDED = 603
    CHAT_MESSAGE_ALREADY_EXISTS = 604
    CHAT_MESSAGE_NOT_FOUND = 605
    CHAT_INTERNAL_SERVER_ERROR = 699
    AIMODEL_NOT_FOUND = 700
    ASSET_NOT_FOUND = 800
    ASSET_ALREADY_EXISTS = 801
    ASSET_REQUEST_ERROR = 802

class ErrorResponse(BaseModel):
    code: typing.Optional[Error] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 
