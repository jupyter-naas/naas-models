# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from naas_models.pydantic.common_p2p import FieldMask
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
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

    _one_of_dict = {"MessageResponseError._code": {"fields": {"code"}}, "MessageResponseError._message": {"fields": {"message"}}, "MessageResponseError._reason": {"fields": {"reason"}}, "MessageResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: MessageError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class Message(BaseModel):

    _one_of_dict = {"Message._archived_at": {"fields": {"archived_at"}}, "Message._chat_id": {"fields": {"chat_id"}}, "Message._created_at": {"fields": {"created_at"}}, "Message._deleted_at": {"fields": {"deleted_at"}}, "Message._from_user": {"fields": {"from_user"}}, "Message._id": {"fields": {"id"}}, "Message._message": {"fields": {"message"}}, "Message._message_language": {"fields": {"message_language"}}, "Message._message_type": {"fields": {"message_type"}}, "Message._metadata": {"fields": {"metadata"}}, "Message._model_id": {"fields": {"model_id"}}, "Message._selected": {"fields": {"selected"}}, "Message._type": {"fields": {"type"}}, "Message._version": {"fields": {"version"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    version: int = FieldInfo(default=0) 
    created_at: str = FieldInfo(default="") 
    chat_id: int = FieldInfo(default=0) 
    from_user: bool = FieldInfo(default=False) 
    message: str = FieldInfo(default="") 
    message_type: str = FieldInfo(default="") 
    message_language: str = FieldInfo(default="") 
    model_id: str = FieldInfo(default="") 
    type: MessageType = FieldInfo(default=0) 
    metadata: str = FieldInfo(default="") 
    deleted_at: str = FieldInfo(default="") 
    selected: bool = FieldInfo(default=False) 
    archived_at: str = FieldInfo(default="") 




class MessageUpdate(BaseModel):

    _one_of_dict = {"MessageUpdate._archived_at": {"fields": {"archived_at"}}, "MessageUpdate._field_mask": {"fields": {"field_mask"}}, "MessageUpdate._message": {"fields": {"message"}}, "MessageUpdate._message_language": {"fields": {"message_language"}}, "MessageUpdate._message_type": {"fields": {"message_type"}}, "MessageUpdate._metadata": {"fields": {"metadata"}}, "MessageUpdate._selected": {"fields": {"selected"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    message: str = FieldInfo(default="") 
    message_type: str = FieldInfo(default="") 
    message_language: str = FieldInfo(default="") 
    metadata: str = FieldInfo(default="") 
    selected: bool = FieldInfo(default=False) 
    archived_at: str = FieldInfo(default="") 
    field_mask: FieldMask = FieldInfo() 




class Messages(BaseModel):

    messages: typing.List[Message] = FieldInfo(default_factory=list) 




class MessageDeletionRequest(BaseModel):

    _one_of_dict = {"MessageDeletionRequest._id": {"fields": {"id"}}, "MessageDeletionRequest._version": {"fields": {"version"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    version: int = FieldInfo(default=0) 




class MessageDeletionResponse(BaseModel):

    _one_of_dict = {"MessageDeletionResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: MessageError = FieldInfo(default=0) 




class MessageRatinResponseError(BaseModel):

    _one_of_dict = {"MessageRatinResponseError._code": {"fields": {"code"}}, "MessageRatinResponseError._message": {"fields": {"message"}}, "MessageRatinResponseError._reason": {"fields": {"reason"}}, "MessageRatinResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: MessageError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class MessageRating(BaseModel):

    _one_of_dict = {"MessageRating._created_at": {"fields": {"created_at"}}, "MessageRating._message_id": {"fields": {"message_id"}}, "MessageRating._message_version": {"fields": {"message_version"}}, "MessageRating._rating": {"fields": {"rating"}}, "MessageRating._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    message_id: int = FieldInfo(default=0) 
    user_id: str = FieldInfo(default="") 
    message_version: int = FieldInfo(default=0) 
    created_at: str = FieldInfo(default="") 
    rating: str = FieldInfo(default="", regex="^(LIKE|DISLIKE)$") 




class MessageRatingCreationRequest(BaseModel):

    _one_of_dict = {"MessageRatingCreationRequest._message_id": {"fields": {"message_id"}}, "MessageRatingCreationRequest._message_version": {"fields": {"message_version"}}, "MessageRatingCreationRequest._rating": {"fields": {"rating"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    message_id: int = FieldInfo(default=0) 
    message_version: int = FieldInfo(default=0) 
    rating: str = FieldInfo(default="", regex="^(LIKE|DISLIKE)$") 




class MessageRatingCreationResponse(BaseModel):

    _one_of_dict = {"MessageRatingCreationResponse._error": {"fields": {"error"}}, "MessageRatingCreationResponse._message_rating": {"fields": {"message_rating"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: MessageRatinResponseError = FieldInfo() 
    message_rating: MessageRating = FieldInfo() 




class Chat(BaseModel):

    _one_of_dict = {"Chat._created_at": {"fields": {"created_at"}}, "Chat._deleted_at": {"fields": {"deleted_at"}}, "Chat._id": {"fields": {"id"}}, "Chat._is_group": {"fields": {"is_group"}}, "Chat._is_personal_assistant": {"fields": {"is_personal_assistant"}}, "Chat._name": {"fields": {"name"}}, "Chat._starred_at": {"fields": {"starred_at"}}, "Chat._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    created_at: str = FieldInfo(default="") 
    user_id: str = FieldInfo(default="") 
    name: str = FieldInfo(default="") 
    deleted_at: str = FieldInfo(default="") 
    is_group: bool = FieldInfo(default=False) 
    is_personal_assistant: bool = FieldInfo(default=False) 
    starred_at: str = FieldInfo(default="") 




class ChatUpdate(BaseModel):

    _one_of_dict = {"ChatUpdate._field_mask": {"fields": {"field_mask"}}, "ChatUpdate._is_group": {"fields": {"is_group"}}, "ChatUpdate._is_personal_assistant": {"fields": {"is_personal_assistant"}}, "ChatUpdate._name": {"fields": {"name"}}, "ChatUpdate._starred_at": {"fields": {"starred_at"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    is_group: bool = FieldInfo(default=False) 
    is_personal_assistant: bool = FieldInfo(default=False) 
    starred_at: str = FieldInfo(default="") 
    field_mask: FieldMask = FieldInfo() 




class ChatMessages(BaseModel):

    messages: typing.Dict[int, Messages] = FieldInfo(default_factory=dict) 




class ChatResponseError(BaseModel):

    _one_of_dict = {"ChatResponseError._code": {"fields": {"code"}}, "ChatResponseError._message": {"fields": {"message"}}, "ChatResponseError._reason": {"fields": {"reason"}}, "ChatResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: ChatError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class ChatCreationRequest(BaseModel):

    _one_of_dict = {"ChatCreationRequest._is_personal_assistant": {"fields": {"is_personal_assistant"}}, "ChatCreationRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    is_personal_assistant: bool = FieldInfo(default=False) 




class ChatCreationResponse(BaseModel):

    _one_of_dict = {"ChatCreationResponse._chat": {"fields": {"chat"}}, "ChatCreationResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    chat: Chat = FieldInfo() 
    error: ChatResponseError = FieldInfo() 




class ChatGetRequest(BaseModel):

    _one_of_dict = {"ChatGetRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 




class ChatGetResponse(BaseModel):

    _one_of_dict = {"ChatGetResponse._chat": {"fields": {"chat"}}, "ChatGetResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    chat: Chat = FieldInfo() 
    error: ChatResponseError = FieldInfo() 




class ChatMessageGetRequest(BaseModel):

    _one_of_dict = {"ChatMessageGetRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 




class ChatMessageGetResponse(BaseModel):

    _one_of_dict = {"ChatMessageGetResponse._error": {"fields": {"error"}}, "ChatMessageGetResponse._messages": {"fields": {"messages"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ChatResponseError = FieldInfo() 
    messages: ChatMessages = FieldInfo() 




class ChatDeletionRequest(BaseModel):

    _one_of_dict = {"ChatDeletionRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 




class ChatDeletionResponse(BaseModel):

    _one_of_dict = {"ChatDeletionResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ChatResponseError = FieldInfo() 




class ChatUpdateRequest(BaseModel):

    _one_of_dict = {"ChatUpdateRequest._chat_update": {"fields": {"chat_update"}}, "ChatUpdateRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    chat_update: ChatUpdate = FieldInfo() 




class ChatUpdateResponse(BaseModel):

    _one_of_dict = {"ChatUpdateResponse._chat": {"fields": {"chat"}}, "ChatUpdateResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    chat: Chat = FieldInfo() 
    error: ChatResponseError = FieldInfo() 




class ChatListRequest(BaseModel):

    _one_of_dict = {"ChatListRequest._page_number": {"fields": {"page_number"}}, "ChatListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class ChatListResponse(BaseModel):

    _one_of_dict = {"ChatListResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    chat: typing.List[Chat] = FieldInfo(default_factory=list) 
    error: ChatResponseError = FieldInfo() 




class ChatStarRequest(BaseModel):

    _one_of_dict = {"ChatStarRequest._id": {"fields": {"id"}}, "ChatStarRequest._star": {"fields": {"star"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    star: bool = FieldInfo(default=False) 




class ChatStarResponse(BaseModel):

    _one_of_dict = {"ChatStarResponse._chat": {"fields": {"chat"}}, "ChatStarResponse._code": {"fields": {"code"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    chat: Chat = FieldInfo() 
    code: ChatError = FieldInfo(default=0) 




class ChatArchiveRequest(BaseModel):

    _one_of_dict = {"ChatArchiveRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 




class ChatArchiveResponse(BaseModel):

    _one_of_dict = {"ChatArchiveResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ChatResponseError = FieldInfo() 




class CompletionResponse(BaseModel):

    _one_of_dict = {"CompletionResponse._image_resolution": {"fields": {"image_resolution"}}, "CompletionResponse._image_steps": {"fields": {"image_steps"}}, "CompletionResponse._input_tokens": {"fields": {"input_tokens"}}, "CompletionResponse._output_tokens": {"fields": {"output_tokens"}}, "CompletionResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    messages: typing.List[Message] = FieldInfo(default_factory=list) 
    input_tokens: int = FieldInfo(default=0) 
    output_tokens: int = FieldInfo(default=0) 
    image_resolution: str = FieldInfo(default="") 
    image_steps: int = FieldInfo(default=0) 
    status: CompletionStatus = FieldInfo(default=0) 




class BasePayload(BaseModel):

    _one_of_dict = {"BasePayload._name": {"fields": {"name"}}, "BasePayload._prompt": {"fields": {"prompt"}}, "BasePayload._url": {"fields": {"url"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    url: str = FieldInfo(default="") 
    prompt: str = FieldInfo(default="") 




class ChatCompletionRequest(BaseModel):

    _one_of_dict = {"ChatCompletionRequest._id": {"fields": {"id"}}, "ChatCompletionRequest._model_id": {"fields": {"model_id"}}, "ChatCompletionRequest._payload": {"fields": {"payload"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 
    model_id: str = FieldInfo(default="") 
    payload: str = FieldInfo(default="") 




class ChatStopCompletionRequest(BaseModel):

    _one_of_dict = {"ChatStopCompletionRequest._id": {"fields": {"id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    id: int = FieldInfo(default=0) 




class ChatStopCompletionResponse(BaseModel):

    _one_of_dict = {"ChatStopCompletionResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    error: ChatResponseError = FieldInfo() 




class ChatCompletionResponse(BaseModel):

    _one_of_dict = {"ChatCompletionResponse._completion": {"fields": {"completion"}}, "ChatCompletionResponse._error": {"fields": {"error"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    completion: CompletionResponse = FieldInfo() 
    error: ChatResponseError = FieldInfo() 


