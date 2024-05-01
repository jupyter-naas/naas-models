# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from naas_models.pydantic.common_p2p import FieldMask
from enum import IntEnum
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


class MessageError(IntEnum):
    MESSAGE_NO_ERROR = 0
    MESSAGE_ALREADY_EXISTS = 1
    MESSAGE_NOT_FOUND = 2
    MESSAGE_NOT_UPDATED = 3
    MESSAGE_NOT_AUTHORIZED = 4
    MESSAGE_INTERNAL_SERVER_ERROR = 1000


class CompletionStatus(IntEnum):
    COMPLETED = 0
    FAILED = 1
    TIMEOUT = 2


class ChatError(IntEnum):
    CHAT_NO_ERROR = 0
    CHAT_ALREADY_EXISTS = 1
    CHAT_NOT_FOUND = 2
    CHAT_NOT_UPDATED = 3
    CHAT_NOT_AUTHORIZED = 4
    CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXISTS = 5
    CHAT_AIMODEL_NOT_FOUND = 6
    CHAT_OUT_OF_CREDIT = 7
    CHAT_CONTEXT_LENGTH_EXCEEDED = 8
    CHAT_INTERNAL_SERVER_ERROR = 1000

class MessageResponseError(BaseModel):
    code: typing.Optional[MessageError] = Field(default=0) 
    status: typing.Optional[str] = Field(default="") 
    reason: typing.Optional[str] = Field(default="") 
    message: typing.Optional[str] = Field(default="") 

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
    error: typing.Optional[MessageError] = Field(default=0) 

class MessageRatinResponseError(BaseModel):
    code: typing.Optional[MessageError] = Field(default=0) 
    status: typing.Optional[str] = Field(default="") 
    reason: typing.Optional[str] = Field(default="") 
    message: typing.Optional[str] = Field(default="") 

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
    error: typing.Optional[MessageRatinResponseError] = Field(default=None) 
    message_rating: typing.Optional[MessageRating] = Field(default=None) 

class Chat(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    created_at: typing.Optional[str] = Field(default="") 
    user_id: typing.Optional[str] = Field(default="") 
    name: typing.Optional[str] = Field(default="") 
    deleted_at: typing.Optional[str] = Field(default="") 
    is_group: typing.Optional[bool] = Field(default=False) 
    is_personal_assistant: typing.Optional[bool] = Field(default=False) 
    starred_at: typing.Optional[str] = Field(default="") 

class ChatUpdate(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    is_group: typing.Optional[bool] = Field(default=False) 
    is_personal_assistant: typing.Optional[bool] = Field(default=False) 
    starred_at: typing.Optional[str] = Field(default="") 
    field_mask: typing.Optional[FieldMask] = Field(default=None) 

class ChatMessages(BaseModel):
    messages: typing.Dict[int, Messages] = Field(default_factory=dict) 

class ChatResponseError(BaseModel):
    code: typing.Optional[ChatError] = Field(default=0) 
    status: typing.Optional[str] = Field(default="") 
    reason: typing.Optional[str] = Field(default="") 
    message: typing.Optional[str] = Field(default="") 

class ChatCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    is_personal_assistant: typing.Optional[bool] = Field(default=False) 

class ChatCreationResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatGetRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatGetResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatMessageGetRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatMessageGetResponse(BaseModel):
    error: typing.Optional[ChatResponseError] = Field(default=None) 
    messages: typing.Optional[ChatMessages] = Field(default=None) 

class ChatDeletionRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatDeletionResponse(BaseModel):
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatUpdateRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    chat_update: typing.Optional[ChatUpdate] = Field(default=None) 

class ChatUpdateResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatListRequest(BaseModel):
    page_size: typing.Optional[int] = Field(default=0) 
    page_number: typing.Optional[int] = Field(default=0) 

class ChatListResponse(BaseModel):
    chat: typing.List[Chat] = Field(default_factory=list) 
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatStarRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 
    star: typing.Optional[bool] = Field(default=False) 

class ChatStarResponse(BaseModel):
    chat: typing.Optional[Chat] = Field(default=None) 
    code: typing.Optional[ChatError] = Field(default=0) 

class ChatArchiveRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0) 

class ChatArchiveResponse(BaseModel):
    error: typing.Optional[ChatResponseError] = Field(default=None) 

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
    error: typing.Optional[ChatResponseError] = Field(default=None) 

class ChatCompletionResponse(BaseModel):
    completion: typing.Optional[CompletionResponse] = Field(default=None) 
    error: typing.Optional[ChatResponseError] = Field(default=None) 
