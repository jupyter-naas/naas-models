# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import common_pb2 as common__pb2
import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0c\x63ommon.proto\x1a\x0evalidate.proto\"\xa8\x01\n\x14MessageResponseError\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x12.chat.MessageErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"\xd4\x04\n\x07Message\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07version\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12!\n\ncreated_at\x18\x03 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x02\x88\x01\x01\x12\x14\n\x07\x63hat_id\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x16\n\tfrom_user\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x14\n\x07message\x18\x06 \x01(\tH\x05\x88\x01\x01\x12#\n\x0cmessage_type\x18\x07 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x06\x88\x01\x01\x12\'\n\x10message_language\x18\x08 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x07\x88\x01\x01\x12\x15\n\x08model_id\x18\t \x01(\tH\x08\x88\x01\x01\x12$\n\x04type\x18\n \x01(\x0e\x32\x11.chat.MessageTypeH\t\x88\x01\x01\x12\x15\n\x08metadata\x18\x0b \x01(\tH\n\x88\x01\x01\x12!\n\ndeleted_at\x18\x0c \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x0b\x88\x01\x01\x12\x15\n\x08selected\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\"\n\x0b\x61rchived_at\x18\x0e \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\r\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_versionB\r\n\x0b_created_atB\n\n\x08_chat_idB\x0c\n\n_from_userB\n\n\x08_messageB\x0f\n\r_message_typeB\x13\n\x11_message_languageB\x0b\n\t_model_idB\x07\n\x05_typeB\x0b\n\t_metadataB\r\n\x0b_deleted_atB\x0b\n\t_selectedB\x0e\n\x0c_archived_at\"\xdc\x02\n\rMessageUpdate\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12#\n\x0cmessage_type\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x01\x88\x01\x01\x12\'\n\x10message_language\x18\x03 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x02\x88\x01\x01\x12\x15\n\x08metadata\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08selected\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\"\n\x0b\x61rchived_at\x18\x06 \x01(\tB\x08\xfa\x42\x05r\x03\xd0\x01\x01H\x05\x88\x01\x01\x12*\n\nfield_mask\x18\x64 \x01(\x0b\x32\x11.common.FieldMaskH\x06\x88\x01\x01\x42\n\n\x08_messageB\x0f\n\r_message_typeB\x13\n\x11_message_languageB\x0b\n\t_metadataB\x0b\n\t_selectedB\x0e\n\x0c_archived_atB\r\n\x0b_field_mask\"+\n\x08Messages\x12\x1f\n\x08messages\x18\x01 \x03(\x0b\x32\r.chat.Message\"R\n\x16MessageDeletionRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07version\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_version\"K\n\x17MessageDeletionResponse\x12&\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x12.chat.MessageErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xad\x01\n\x19MessageRatinResponseError\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x12.chat.MessageErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"\xef\x01\n\rMessageRating\x12\x17\n\nmessage_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1c\n\x0fmessage_version\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x17\n\ncreated_at\x18\x04 \x01(\tH\x03\x88\x01\x01\x12/\n\x06rating\x18\x05 \x01(\tB\x1a\xfa\x42\x17r\x15\x32\x10^(LIKE|DISLIKE)$\xd0\x01\x00H\x04\x88\x01\x01\x42\r\n\x0b_message_idB\n\n\x08_user_idB\x12\n\x10_message_versionB\r\n\x0b_created_atB\t\n\x07_rating\"\xb4\x01\n\x1cMessageRatingCreationRequest\x12\x17\n\nmessage_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0fmessage_version\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12/\n\x06rating\x18\x03 \x01(\tB\x1a\xfa\x42\x17r\x15\x32\x10^(LIKE|DISLIKE)$\xd0\x01\x00H\x02\x88\x01\x01\x42\r\n\x0b_message_idB\x12\n\x10_message_versionB\t\n\x07_rating\"\xa3\x01\n\x1dMessageRatingCreationResponse\x12\x33\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1f.chat.MessageRatinResponseErrorH\x00\x88\x01\x01\x12\x30\n\x0emessage_rating\x18\x02 \x01(\x0b\x32\x13.chat.MessageRatingH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x11\n\x0f_message_rating\"\xb6\x02\n\x04\x43hat\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x17\n\ncreated_at\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07user_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04name\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x17\n\ndeleted_at\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08is_group\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\"\n\x15is_personal_assistant\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x17\n\nstarred_at\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x05\n\x03_idB\r\n\x0b_created_atB\n\n\x08_user_idB\x07\n\x05_nameB\r\n\x0b_deleted_atB\x0b\n\t_is_groupB\x18\n\x16_is_personal_assistantB\r\n\x0b_starred_at\"\xed\x01\n\nChatUpdate\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08is_group\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\"\n\x15is_personal_assistant\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x17\n\nstarred_at\x18\x04 \x01(\tH\x03\x88\x01\x01\x12*\n\nfield_mask\x18\x64 \x01(\x0b\x32\x11.common.FieldMaskH\x04\x88\x01\x01\x42\x07\n\x05_nameB\x0b\n\t_is_groupB\x18\n\x16_is_personal_assistantB\r\n\x0b_starred_atB\r\n\x0b_field_mask\"\x83\x01\n\x0c\x43hatMessages\x12\x32\n\x08messages\x18\x01 \x03(\x0b\x32 .chat.ChatMessages.MessagesEntry\x1a?\n\rMessagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.chat.Messages:\x02\x38\x01\"\xa2\x01\n\x11\x43hatResponseError\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0f.chat.ChatErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"o\n\x13\x43hatCreationRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\"\n\x15is_personal_assistant\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x07\n\x05_nameB\x18\n\x16_is_personal_assistant\"u\n\x14\x43hatCreationResponse\x12\x1d\n\x04\x63hat\x18\x01 \x01(\x0b\x32\n.chat.ChatH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x01\x88\x01\x01\x42\x07\n\x05_chatB\x08\n\x06_error\"(\n\x0e\x43hatGetRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id\"p\n\x0f\x43hatGetResponse\x12\x1d\n\x04\x63hat\x18\x01 \x01(\x0b\x32\n.chat.ChatH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x01\x88\x01\x01\x42\x07\n\x05_chatB\x08\n\x06_error\"/\n\x15\x43hatMessageGetRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id\"\x87\x01\n\x16\x43hatMessageGetResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x00\x88\x01\x01\x12)\n\x08messages\x18\x02 \x01(\x0b\x32\x12.chat.ChatMessagesH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x0b\n\t_messages\"-\n\x13\x43hatDeletionRequest\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x42\x05\n\x03_id\"M\n\x14\x43hatDeletionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"g\n\x11\x43hatUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12*\n\x0b\x63hat_update\x18\x02 \x01(\x0b\x32\x10.chat.ChatUpdateH\x01\x88\x01\x01\x42\x05\n\x03_idB\x0e\n\x0c_chat_update\"s\n\x12\x43hatUpdateResponse\x12\x1d\n\x04\x63hat\x18\x01 \x01(\x0b\x32\n.chat.ChatH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x01\x88\x01\x01\x42\x07\n\x05_chatB\x08\n\x06_error\"a\n\x0f\x43hatListRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_page_sizeB\x0e\n\x0c_page_number\"c\n\x10\x43hatListResponse\x12\x18\n\x04\x63hat\x18\x01 \x03(\x0b\x32\n.chat.Chat\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"E\n\x0f\x43hatStarRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04star\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_star\"g\n\x10\x43hatStarResponse\x12\x1d\n\x04\x63hat\x18\x01 \x01(\x0b\x32\n.chat.ChatH\x00\x88\x01\x01\x12\"\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x0f.chat.ChatErrorH\x01\x88\x01\x01\x42\x07\n\x05_chatB\x07\n\x05_code\",\n\x12\x43hatArchiveRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id\"L\n\x13\x43hatArchiveResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xa5\x02\n\x12\x43ompletionResponse\x12\x1f\n\x08messages\x18\x01 \x03(\x0b\x32\r.chat.Message\x12\x19\n\x0cinput_tokens\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x1a\n\routput_tokens\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x1d\n\x10image_resolution\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bimage_steps\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12+\n\x06status\x18\x06 \x01(\x0e\x32\x16.chat.CompletionStatusH\x04\x88\x01\x01\x42\x0f\n\r_input_tokensB\x10\n\x0e_output_tokensB\x13\n\x11_image_resolutionB\x0e\n\x0c_image_stepsB\t\n\x07_status\"c\n\x0b\x42\x61sePayload\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03url\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06prompt\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_nameB\x06\n\x04_urlB\t\n\x07_prompt\"\xa5\x01\n\x15\x43hatCompletionRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08model_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07payload\x18\x03 \x01(\tH\x02\x88\x01\x01\x12 \n\tplugin_id\x18\x04 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x03\x88\x01\x01\x42\x05\n\x03_idB\x0b\n\t_model_idB\n\n\x08_payloadB\x0c\n\n_plugin_id\"3\n\x19\x43hatStopCompletionRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id\"S\n\x1a\x43hatStopCompletionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x91\x01\n\x16\x43hatCompletionResponse\x12\x31\n\ncompletion\x18\x01 \x01(\x0b\x32\x18.chat.CompletionResponseH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.chat.ChatResponseErrorH\x01\x88\x01\x01\x42\r\n\x0b_completionB\x08\n\x06_error*;\n\x0bMessageType\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x06\n\x02\x41I\x10\x02\x12\t\n\x05HUMAN\x10\x03*\xb0\x01\n\x0cMessageError\x12\x14\n\x10MESSAGE_NO_ERROR\x10\x00\x12\x1a\n\x16MESSAGE_ALREADY_EXISTS\x10\x01\x12\x15\n\x11MESSAGE_NOT_FOUND\x10\x02\x12\x17\n\x13MESSAGE_NOT_UPDATED\x10\x03\x12\x1a\n\x16MESSAGE_NOT_AUTHORIZED\x10\x04\x12\"\n\x1dMESSAGE_INTERNAL_SERVER_ERROR\x10\xe8\x07*:\n\x10\x43ompletionStatus\x12\r\n\tCOMPLETED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02*\x9e\x02\n\tChatError\x12\x11\n\rCHAT_NO_ERROR\x10\x00\x12\x17\n\x13\x43HAT_ALREADY_EXISTS\x10\x01\x12\x12\n\x0e\x43HAT_NOT_FOUND\x10\x02\x12\x14\n\x10\x43HAT_NOT_UPDATED\x10\x03\x12\x17\n\x13\x43HAT_NOT_AUTHORIZED\x10\x04\x12+\n\'CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXISTS\x10\x05\x12\x1a\n\x16\x43HAT_AIMODEL_NOT_FOUND\x10\x06\x12\x16\n\x12\x43HAT_OUT_OF_CREDIT\x10\x07\x12 \n\x1c\x43HAT_CONTEXT_LENGTH_EXCEEDED\x10\x08\x12\x1f\n\x1a\x43HAT_INTERNAL_SERVER_ERROR\x10\xe8\x07\x32\xfa\x02\n\x0b\x43hatService\x12\x41\n\x06\x43reate\x12\x19.chat.ChatCreationRequest\x1a\x1a.chat.ChatCreationResponse\"\x00\x12\x34\n\x03Get\x12\x14.chat.ChatGetRequest\x1a\x15.chat.ChatGetResponse\"\x00\x12\x37\n\x04List\x12\x15.chat.ChatListRequest\x1a\x16.chat.ChatListResponse\"\x00\x12\x41\n\x06\x44\x65lete\x12\x19.chat.ChatDeletionRequest\x1a\x1a.chat.ChatDeletionResponse\"\x00\x12=\n\x06Update\x12\x17.chat.ChatUpdateRequest\x1a\x18.chat.ChatUpdateResponse\"\x00\x12\x37\n\x04Star\x12\x15.chat.ChatStarRequest\x1a\x16.chat.ChatStarResponse\"\x00\x42-Z+github.com/jupyter-naas/naas-models/go/chatb\x06proto3')

_MESSAGETYPE = DESCRIPTOR.enum_types_by_name['MessageType']
MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
_MESSAGEERROR = DESCRIPTOR.enum_types_by_name['MessageError']
MessageError = enum_type_wrapper.EnumTypeWrapper(_MESSAGEERROR)
_COMPLETIONSTATUS = DESCRIPTOR.enum_types_by_name['CompletionStatus']
CompletionStatus = enum_type_wrapper.EnumTypeWrapper(_COMPLETIONSTATUS)
_CHATERROR = DESCRIPTOR.enum_types_by_name['ChatError']
ChatError = enum_type_wrapper.EnumTypeWrapper(_CHATERROR)
UNDEFINED = 0
SYSTEM = 1
AI = 2
HUMAN = 3
MESSAGE_NO_ERROR = 0
MESSAGE_ALREADY_EXISTS = 1
MESSAGE_NOT_FOUND = 2
MESSAGE_NOT_UPDATED = 3
MESSAGE_NOT_AUTHORIZED = 4
MESSAGE_INTERNAL_SERVER_ERROR = 1000
COMPLETED = 0
FAILED = 1
TIMEOUT = 2
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


_MESSAGERESPONSEERROR = DESCRIPTOR.message_types_by_name['MessageResponseError']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_MESSAGEUPDATE = DESCRIPTOR.message_types_by_name['MessageUpdate']
_MESSAGES = DESCRIPTOR.message_types_by_name['Messages']
_MESSAGEDELETIONREQUEST = DESCRIPTOR.message_types_by_name['MessageDeletionRequest']
_MESSAGEDELETIONRESPONSE = DESCRIPTOR.message_types_by_name['MessageDeletionResponse']
_MESSAGERATINRESPONSEERROR = DESCRIPTOR.message_types_by_name['MessageRatinResponseError']
_MESSAGERATING = DESCRIPTOR.message_types_by_name['MessageRating']
_MESSAGERATINGCREATIONREQUEST = DESCRIPTOR.message_types_by_name['MessageRatingCreationRequest']
_MESSAGERATINGCREATIONRESPONSE = DESCRIPTOR.message_types_by_name['MessageRatingCreationResponse']
_CHAT = DESCRIPTOR.message_types_by_name['Chat']
_CHATUPDATE = DESCRIPTOR.message_types_by_name['ChatUpdate']
_CHATMESSAGES = DESCRIPTOR.message_types_by_name['ChatMessages']
_CHATMESSAGES_MESSAGESENTRY = _CHATMESSAGES.nested_types_by_name['MessagesEntry']
_CHATRESPONSEERROR = DESCRIPTOR.message_types_by_name['ChatResponseError']
_CHATCREATIONREQUEST = DESCRIPTOR.message_types_by_name['ChatCreationRequest']
_CHATCREATIONRESPONSE = DESCRIPTOR.message_types_by_name['ChatCreationResponse']
_CHATGETREQUEST = DESCRIPTOR.message_types_by_name['ChatGetRequest']
_CHATGETRESPONSE = DESCRIPTOR.message_types_by_name['ChatGetResponse']
_CHATMESSAGEGETREQUEST = DESCRIPTOR.message_types_by_name['ChatMessageGetRequest']
_CHATMESSAGEGETRESPONSE = DESCRIPTOR.message_types_by_name['ChatMessageGetResponse']
_CHATDELETIONREQUEST = DESCRIPTOR.message_types_by_name['ChatDeletionRequest']
_CHATDELETIONRESPONSE = DESCRIPTOR.message_types_by_name['ChatDeletionResponse']
_CHATUPDATEREQUEST = DESCRIPTOR.message_types_by_name['ChatUpdateRequest']
_CHATUPDATERESPONSE = DESCRIPTOR.message_types_by_name['ChatUpdateResponse']
_CHATLISTREQUEST = DESCRIPTOR.message_types_by_name['ChatListRequest']
_CHATLISTRESPONSE = DESCRIPTOR.message_types_by_name['ChatListResponse']
_CHATSTARREQUEST = DESCRIPTOR.message_types_by_name['ChatStarRequest']
_CHATSTARRESPONSE = DESCRIPTOR.message_types_by_name['ChatStarResponse']
_CHATARCHIVEREQUEST = DESCRIPTOR.message_types_by_name['ChatArchiveRequest']
_CHATARCHIVERESPONSE = DESCRIPTOR.message_types_by_name['ChatArchiveResponse']
_COMPLETIONRESPONSE = DESCRIPTOR.message_types_by_name['CompletionResponse']
_BASEPAYLOAD = DESCRIPTOR.message_types_by_name['BasePayload']
_CHATCOMPLETIONREQUEST = DESCRIPTOR.message_types_by_name['ChatCompletionRequest']
_CHATSTOPCOMPLETIONREQUEST = DESCRIPTOR.message_types_by_name['ChatStopCompletionRequest']
_CHATSTOPCOMPLETIONRESPONSE = DESCRIPTOR.message_types_by_name['ChatStopCompletionResponse']
_CHATCOMPLETIONRESPONSE = DESCRIPTOR.message_types_by_name['ChatCompletionResponse']
MessageResponseError = _reflection.GeneratedProtocolMessageType('MessageResponseError', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSEERROR,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageResponseError)
  })
_sym_db.RegisterMessage(MessageResponseError)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Message)
  })
_sym_db.RegisterMessage(Message)

MessageUpdate = _reflection.GeneratedProtocolMessageType('MessageUpdate', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEUPDATE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageUpdate)
  })
_sym_db.RegisterMessage(MessageUpdate)

Messages = _reflection.GeneratedProtocolMessageType('Messages', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGES,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Messages)
  })
_sym_db.RegisterMessage(Messages)

MessageDeletionRequest = _reflection.GeneratedProtocolMessageType('MessageDeletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDELETIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageDeletionRequest)
  })
_sym_db.RegisterMessage(MessageDeletionRequest)

MessageDeletionResponse = _reflection.GeneratedProtocolMessageType('MessageDeletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDELETIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageDeletionResponse)
  })
_sym_db.RegisterMessage(MessageDeletionResponse)

MessageRatinResponseError = _reflection.GeneratedProtocolMessageType('MessageRatinResponseError', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERATINRESPONSEERROR,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageRatinResponseError)
  })
_sym_db.RegisterMessage(MessageRatinResponseError)

MessageRating = _reflection.GeneratedProtocolMessageType('MessageRating', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERATING,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageRating)
  })
_sym_db.RegisterMessage(MessageRating)

MessageRatingCreationRequest = _reflection.GeneratedProtocolMessageType('MessageRatingCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERATINGCREATIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageRatingCreationRequest)
  })
_sym_db.RegisterMessage(MessageRatingCreationRequest)

MessageRatingCreationResponse = _reflection.GeneratedProtocolMessageType('MessageRatingCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERATINGCREATIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.MessageRatingCreationResponse)
  })
_sym_db.RegisterMessage(MessageRatingCreationResponse)

Chat = _reflection.GeneratedProtocolMessageType('Chat', (_message.Message,), {
  'DESCRIPTOR' : _CHAT,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Chat)
  })
_sym_db.RegisterMessage(Chat)

ChatUpdate = _reflection.GeneratedProtocolMessageType('ChatUpdate', (_message.Message,), {
  'DESCRIPTOR' : _CHATUPDATE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatUpdate)
  })
_sym_db.RegisterMessage(ChatUpdate)

ChatMessages = _reflection.GeneratedProtocolMessageType('ChatMessages', (_message.Message,), {

  'MessagesEntry' : _reflection.GeneratedProtocolMessageType('MessagesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CHATMESSAGES_MESSAGESENTRY,
    '__module__' : 'chat_pb2'
    # @@protoc_insertion_point(class_scope:chat.ChatMessages.MessagesEntry)
    })
  ,
  'DESCRIPTOR' : _CHATMESSAGES,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatMessages)
  })
_sym_db.RegisterMessage(ChatMessages)
_sym_db.RegisterMessage(ChatMessages.MessagesEntry)

ChatResponseError = _reflection.GeneratedProtocolMessageType('ChatResponseError', (_message.Message,), {
  'DESCRIPTOR' : _CHATRESPONSEERROR,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatResponseError)
  })
_sym_db.RegisterMessage(ChatResponseError)

ChatCreationRequest = _reflection.GeneratedProtocolMessageType('ChatCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATCREATIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatCreationRequest)
  })
_sym_db.RegisterMessage(ChatCreationRequest)

ChatCreationResponse = _reflection.GeneratedProtocolMessageType('ChatCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATCREATIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatCreationResponse)
  })
_sym_db.RegisterMessage(ChatCreationResponse)

ChatGetRequest = _reflection.GeneratedProtocolMessageType('ChatGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATGETREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatGetRequest)
  })
_sym_db.RegisterMessage(ChatGetRequest)

ChatGetResponse = _reflection.GeneratedProtocolMessageType('ChatGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATGETRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatGetResponse)
  })
_sym_db.RegisterMessage(ChatGetResponse)

ChatMessageGetRequest = _reflection.GeneratedProtocolMessageType('ChatMessageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGEGETREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatMessageGetRequest)
  })
_sym_db.RegisterMessage(ChatMessageGetRequest)

ChatMessageGetResponse = _reflection.GeneratedProtocolMessageType('ChatMessageGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGEGETRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatMessageGetResponse)
  })
_sym_db.RegisterMessage(ChatMessageGetResponse)

ChatDeletionRequest = _reflection.GeneratedProtocolMessageType('ChatDeletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATDELETIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatDeletionRequest)
  })
_sym_db.RegisterMessage(ChatDeletionRequest)

ChatDeletionResponse = _reflection.GeneratedProtocolMessageType('ChatDeletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATDELETIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatDeletionResponse)
  })
_sym_db.RegisterMessage(ChatDeletionResponse)

ChatUpdateRequest = _reflection.GeneratedProtocolMessageType('ChatUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATUPDATEREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatUpdateRequest)
  })
_sym_db.RegisterMessage(ChatUpdateRequest)

ChatUpdateResponse = _reflection.GeneratedProtocolMessageType('ChatUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATUPDATERESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatUpdateResponse)
  })
_sym_db.RegisterMessage(ChatUpdateResponse)

ChatListRequest = _reflection.GeneratedProtocolMessageType('ChatListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATLISTREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatListRequest)
  })
_sym_db.RegisterMessage(ChatListRequest)

ChatListResponse = _reflection.GeneratedProtocolMessageType('ChatListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATLISTRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatListResponse)
  })
_sym_db.RegisterMessage(ChatListResponse)

ChatStarRequest = _reflection.GeneratedProtocolMessageType('ChatStarRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATSTARREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatStarRequest)
  })
_sym_db.RegisterMessage(ChatStarRequest)

ChatStarResponse = _reflection.GeneratedProtocolMessageType('ChatStarResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATSTARRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatStarResponse)
  })
_sym_db.RegisterMessage(ChatStarResponse)

ChatArchiveRequest = _reflection.GeneratedProtocolMessageType('ChatArchiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATARCHIVEREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatArchiveRequest)
  })
_sym_db.RegisterMessage(ChatArchiveRequest)

ChatArchiveResponse = _reflection.GeneratedProtocolMessageType('ChatArchiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATARCHIVERESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatArchiveResponse)
  })
_sym_db.RegisterMessage(ChatArchiveResponse)

CompletionResponse = _reflection.GeneratedProtocolMessageType('CompletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.CompletionResponse)
  })
_sym_db.RegisterMessage(CompletionResponse)

BasePayload = _reflection.GeneratedProtocolMessageType('BasePayload', (_message.Message,), {
  'DESCRIPTOR' : _BASEPAYLOAD,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.BasePayload)
  })
_sym_db.RegisterMessage(BasePayload)

ChatCompletionRequest = _reflection.GeneratedProtocolMessageType('ChatCompletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATCOMPLETIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatCompletionRequest)
  })
_sym_db.RegisterMessage(ChatCompletionRequest)

ChatStopCompletionRequest = _reflection.GeneratedProtocolMessageType('ChatStopCompletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATSTOPCOMPLETIONREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatStopCompletionRequest)
  })
_sym_db.RegisterMessage(ChatStopCompletionRequest)

ChatStopCompletionResponse = _reflection.GeneratedProtocolMessageType('ChatStopCompletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATSTOPCOMPLETIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatStopCompletionResponse)
  })
_sym_db.RegisterMessage(ChatStopCompletionResponse)

ChatCompletionResponse = _reflection.GeneratedProtocolMessageType('ChatCompletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHATCOMPLETIONRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatCompletionResponse)
  })
_sym_db.RegisterMessage(ChatCompletionResponse)

_CHATSERVICE = DESCRIPTOR.services_by_name['ChatService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/jupyter-naas/naas-models/go/chat'
  _MESSAGE.fields_by_name['created_at']._options = None
  _MESSAGE.fields_by_name['created_at']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGE.fields_by_name['message_type']._options = None
  _MESSAGE.fields_by_name['message_type']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGE.fields_by_name['message_language']._options = None
  _MESSAGE.fields_by_name['message_language']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGE.fields_by_name['deleted_at']._options = None
  _MESSAGE.fields_by_name['deleted_at']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGE.fields_by_name['archived_at']._options = None
  _MESSAGE.fields_by_name['archived_at']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGEUPDATE.fields_by_name['message_type']._options = None
  _MESSAGEUPDATE.fields_by_name['message_type']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGEUPDATE.fields_by_name['message_language']._options = None
  _MESSAGEUPDATE.fields_by_name['message_language']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGEUPDATE.fields_by_name['archived_at']._options = None
  _MESSAGEUPDATE.fields_by_name['archived_at']._serialized_options = b'\372B\005r\003\320\001\001'
  _MESSAGERATING.fields_by_name['rating']._options = None
  _MESSAGERATING.fields_by_name['rating']._serialized_options = b'\372B\027r\0252\020^(LIKE|DISLIKE)$\320\001\000'
  _MESSAGERATINGCREATIONREQUEST.fields_by_name['rating']._options = None
  _MESSAGERATINGCREATIONREQUEST.fields_by_name['rating']._serialized_options = b'\372B\027r\0252\020^(LIKE|DISLIKE)$\320\001\000'
  _CHATMESSAGES_MESSAGESENTRY._options = None
  _CHATMESSAGES_MESSAGESENTRY._serialized_options = b'8\001'
  _CHATCOMPLETIONREQUEST.fields_by_name['plugin_id']._options = None
  _CHATCOMPLETIONREQUEST.fields_by_name['plugin_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _MESSAGETYPE._serialized_start=5300
  _MESSAGETYPE._serialized_end=5359
  _MESSAGEERROR._serialized_start=5362
  _MESSAGEERROR._serialized_end=5538
  _COMPLETIONSTATUS._serialized_start=5540
  _COMPLETIONSTATUS._serialized_end=5598
  _CHATERROR._serialized_start=5601
  _CHATERROR._serialized_end=5887
  _MESSAGERESPONSEERROR._serialized_start=81
  _MESSAGERESPONSEERROR._serialized_end=249
  _MESSAGE._serialized_start=252
  _MESSAGE._serialized_end=848
  _MESSAGEUPDATE._serialized_start=851
  _MESSAGEUPDATE._serialized_end=1199
  _MESSAGES._serialized_start=1201
  _MESSAGES._serialized_end=1244
  _MESSAGEDELETIONREQUEST._serialized_start=1246
  _MESSAGEDELETIONREQUEST._serialized_end=1328
  _MESSAGEDELETIONRESPONSE._serialized_start=1330
  _MESSAGEDELETIONRESPONSE._serialized_end=1405
  _MESSAGERATINRESPONSEERROR._serialized_start=1408
  _MESSAGERATINRESPONSEERROR._serialized_end=1581
  _MESSAGERATING._serialized_start=1584
  _MESSAGERATING._serialized_end=1823
  _MESSAGERATINGCREATIONREQUEST._serialized_start=1826
  _MESSAGERATINGCREATIONREQUEST._serialized_end=2006
  _MESSAGERATINGCREATIONRESPONSE._serialized_start=2009
  _MESSAGERATINGCREATIONRESPONSE._serialized_end=2172
  _CHAT._serialized_start=2175
  _CHAT._serialized_end=2485
  _CHATUPDATE._serialized_start=2488
  _CHATUPDATE._serialized_end=2725
  _CHATMESSAGES._serialized_start=2728
  _CHATMESSAGES._serialized_end=2859
  _CHATMESSAGES_MESSAGESENTRY._serialized_start=2796
  _CHATMESSAGES_MESSAGESENTRY._serialized_end=2859
  _CHATRESPONSEERROR._serialized_start=2862
  _CHATRESPONSEERROR._serialized_end=3024
  _CHATCREATIONREQUEST._serialized_start=3026
  _CHATCREATIONREQUEST._serialized_end=3137
  _CHATCREATIONRESPONSE._serialized_start=3139
  _CHATCREATIONRESPONSE._serialized_end=3256
  _CHATGETREQUEST._serialized_start=3258
  _CHATGETREQUEST._serialized_end=3298
  _CHATGETRESPONSE._serialized_start=3300
  _CHATGETRESPONSE._serialized_end=3412
  _CHATMESSAGEGETREQUEST._serialized_start=3414
  _CHATMESSAGEGETREQUEST._serialized_end=3461
  _CHATMESSAGEGETRESPONSE._serialized_start=3464
  _CHATMESSAGEGETRESPONSE._serialized_end=3599
  _CHATDELETIONREQUEST._serialized_start=3601
  _CHATDELETIONREQUEST._serialized_end=3646
  _CHATDELETIONRESPONSE._serialized_start=3648
  _CHATDELETIONRESPONSE._serialized_end=3725
  _CHATUPDATEREQUEST._serialized_start=3727
  _CHATUPDATEREQUEST._serialized_end=3830
  _CHATUPDATERESPONSE._serialized_start=3832
  _CHATUPDATERESPONSE._serialized_end=3947
  _CHATLISTREQUEST._serialized_start=3949
  _CHATLISTREQUEST._serialized_end=4046
  _CHATLISTRESPONSE._serialized_start=4048
  _CHATLISTRESPONSE._serialized_end=4147
  _CHATSTARREQUEST._serialized_start=4149
  _CHATSTARREQUEST._serialized_end=4218
  _CHATSTARRESPONSE._serialized_start=4220
  _CHATSTARRESPONSE._serialized_end=4323
  _CHATARCHIVEREQUEST._serialized_start=4325
  _CHATARCHIVEREQUEST._serialized_end=4369
  _CHATARCHIVERESPONSE._serialized_start=4371
  _CHATARCHIVERESPONSE._serialized_end=4447
  _COMPLETIONRESPONSE._serialized_start=4450
  _COMPLETIONRESPONSE._serialized_end=4743
  _BASEPAYLOAD._serialized_start=4745
  _BASEPAYLOAD._serialized_end=4844
  _CHATCOMPLETIONREQUEST._serialized_start=4847
  _CHATCOMPLETIONREQUEST._serialized_end=5012
  _CHATSTOPCOMPLETIONREQUEST._serialized_start=5014
  _CHATSTOPCOMPLETIONREQUEST._serialized_end=5065
  _CHATSTOPCOMPLETIONRESPONSE._serialized_start=5067
  _CHATSTOPCOMPLETIONRESPONSE._serialized_end=5150
  _CHATCOMPLETIONRESPONSE._serialized_start=5153
  _CHATCOMPLETIONRESPONSE._serialized_end=5298
  _CHATSERVICE._serialized_start=5890
  _CHATSERVICE._serialized_end=6268
# @@protoc_insertion_point(module_scope)
