# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from naas_models.pydantic.common_p2p import FieldMask
from enum import IntEnum
from naas_models.pydantic.errors_p2p import ErrorResponse
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing

class MessageType(IntEnum):
    UNDEFINED = 0
    SYSTEM = 1
    AI = 2
    HUMAN = 3
    TOOL_USAGE = 5
    TOOL_ANSWER = 6


class MessageStatus(IntEnum):
    MESSAGE_STATUS_UNSPECIFIED = 0
    MESSAGE_STATUS_PENDING = 1
    MESSAGE_STATUS_COMPLETED = 2
    MESSAGE_STATUS_FAILED = 3
    MESSAGE_STATUS_CANCELLED = 4


class CompletionStatus(IntEnum):
    COMPLETED = 0
    FAILED = 1
    TIMEOUT = 2

class Message(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    version: typing.Optional[int] = Field(default=0) 
    created_at: typing.Optional[str] = Field(default="") 
    chat_id: typing.Optional[int] = Field(default=0) 
    from_user: typing.Optional[bool] = Field(default=False) 
    message: typing.Optional[str] = Field(default="") 
    message_type: typing.Optional[str] = Field(default="") 
    message_language: typing.Optional[str] = Field(default="") 
    model_id: typing.Optional[str] = Field(default="") 
    type: typing.Optional[MessageType] = Field(default=0) 
    metadata: typing.Optional[str] = Field(default="") 
    deleted_at: typing.Optional[str] = Field(default="") 
    selected: typing.Optional[bool] = Field(default=False) 
    archived_at: typing.Optional[str] = Field(default="") 
    status: typing.Optional[MessageStatus] = Field(default=0) 

class MessageUpdate(BaseModel):
    message: typing.Optional[str] = Field(default="") 
    message_type: typing.Optional[str] = Field(default="") 
    message_language: typing.Optional[str] = Field(default="") 
    metadata: typing.Optional[str] = Field(default="") 
    selected: typing.Optional[bool] = Field(default=False) 
    archived_at: typing.Optional[str] = Field(default="") 
    field_mask: typing.Optional[FieldMask] = Field(default=None) 

class Messages(BaseModel):
    messages: typing.List[Message] = Field(default_factory=list) 

class MessageDeletionRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    version: typing.Optional[int] = Field(default=0) 

class MessageDeletionResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class MessageRating(BaseModel):
    message_id: typing.Optional[int] = Field(default=0) 
    user_id: typing.Optional[str] = Field(default="") 
    message_version: typing.Optional[int] = Field(default=0) 
    created_at: typing.Optional[str] = Field(default="") 
    rating: typing.Optional[str] = Field(default="", pattern="^(LIKE|DISLIKE)$") 

class MessageRatingCreationRequest(BaseModel):
    message_id: typing.Optional[int] = Field(default=0) 
    message_version: typing.Optional[int] = Field(default=0) 
    rating: typing.Optional[str] = Field(default="", pattern="^(LIKE|DISLIKE)$") 

class MessageRatingCreationResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    message_rating: typing.Optional[MessageRating] = Field(default=None) 

class Chat(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    created_at: typing.Optional[str] = Field(default="") 
    user_id: typing.Optional[str] = Field(default="") 
    name: typing.Optional[str] = Field(default="") 
    deleted_at: typing.Optional[str] = Field(default="") 
    is_group: typing.Optional[bool] = Field(default=False) 
    starred_at: typing.Optional[str] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class ChatUpdate(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    is_group: typing.Optional[bool] = Field(default=False) 
    starred_at: typing.Optional[str] = Field(default="") 
    field_mask: typing.Optional[FieldMask] = Field(default=None) 

class ChatMessages(BaseModel):
    messages: typing.Dict[int, Messages] = Field(default_factory=dict) 

class ChatCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    workspace_id: typing.Optional[UUID] = Field(default="") 

class ChatCreationResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatGetRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatGetResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatMessageGetRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatMessageGetResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    messages: typing.Optional[ChatMessages] = Field(default=None) 

class ChatDeletionRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatDeletionResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatUpdateRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    chat_update: typing.Optional[ChatUpdate] = Field(default=None) 

class ChatUpdateResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class ChatListResponse(BaseModel):
    chat: typing.List[Chat] = Field(default_factory=list) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatStarRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    star: typing.Optional[bool] = Field(default=False) 

class ChatStarResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatArchiveRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatArchiveResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class CompletionResponse(BaseModel):
    messages: typing.List[Message] = Field(default_factory=list) 
    input_tokens: typing.Optional[int] = Field(default=0) 
    output_tokens: typing.Optional[int] = Field(default=0) 
    image_resolution: typing.Optional[str] = Field(default="") 
    image_steps: typing.Optional[int] = Field(default=0) 
    status: typing.Optional[CompletionStatus] = Field(default=0) 

class BasePayload(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    url: typing.Optional[str] = Field(default="") 
    prompt: typing.Optional[str] = Field(default="") 

class ChatCompletionRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    model_id: typing.Optional[str] = Field(default="") 
    payload: typing.Optional[str] = Field(default="") 
    plugin_id: typing.Optional[UUID] = Field(default="") 

class ChatStopCompletionRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatStopCompletionResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 

class ChatCompletionResponse(BaseModel):
    completion: typing.Optional[CompletionResponse] = Field(default=None) 
    error: typing.Optional[ErrorResponse] = Field(default=None) 
