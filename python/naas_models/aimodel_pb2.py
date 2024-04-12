# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aimodel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raimodel.proto\x12\x07\x61imodel\x1a\x0evalidate.proto\"\xc7\x02\n\x07\x41IModel\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08provider\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05image\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07\x65nabled\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x11\n\x04type\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x17\n\nrestricted\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x17\n\nname_alias\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x1b\n\x0e\x63ontext_window\x18\t \x01(\x05H\x08\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x0b\n\t_providerB\x08\n\x06_imageB\n\n\x08_enabledB\x07\n\x05_typeB\r\n\x0b_restrictedB\r\n\x0b_name_aliasB\x11\n\x0f_context_window\"\x8f\x02\n\x12\x43ompletionResponse\x12\x1f\n\x08model_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x13\n\x0b\x63ompletions\x18\x02 \x03(\t\x12\x19\n\x0cinput_tokens\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x1a\n\routput_tokens\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x1d\n\x10image_resolution\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0bimage_steps\x18\x06 \x01(\x05H\x04\x88\x01\x01\x42\x0b\n\t_model_idB\x0f\n\r_input_tokensB\x10\n\x0e_output_tokensB\x13\n\x11_image_resolutionB\x0e\n\x0c_image_steps\"\xab\x01\n\x14\x41IModelResponseError\x12(\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x15.aimodel.AIModelErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"d\n\x12\x41IModelListRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_page_sizeB\x0e\n\x0c_page_number\"\xa0\x01\n\x13\x41IModelListResponse\x12\"\n\x08\x61imodels\x18\x01 \x03(\x0b\x32\x10.aimodel.AIModel\x12\x18\n\x0bpage_number\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1d.aimodel.AIModelResponseErrorH\x01\x88\x01\x01\x42\x0e\n\x0c_page_numberB\x08\n\x06_error\"5\n\x11\x41IModelGetRequest\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\x05\n\x03_id\"\x85\x01\n\x12\x41IModelGetResponse\x12&\n\x07\x61imodel\x18\x01 \x01(\x0b\x32\x10.aimodel.AIModelH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.aimodel.AIModelResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_aimodelB\x08\n\x06_error\"^\n\x18\x41IModelCompletionRequest\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x14\n\x07payload\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_payload\"\x9d\x01\n\x19\x41IModelCompletionResponse\x12\x34\n\ncompletion\x18\x01 \x01(\x0b\x32\x1b.aimodel.CompletionResponseH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.aimodel.AIModelResponseErrorH\x01\x88\x01\x01\x42\r\n\x0b_completionB\x08\n\x06_error\"\x89\x02\n\x1b\x41IModelAdminCreationRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08provider\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05image\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07\x65nabled\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x11\n\x04type\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nrestricted\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x17\n\nname_alias\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\x07\n\x05_nameB\x0b\n\t_providerB\x08\n\x06_imageB\n\n\x08_enabledB\x07\n\x05_typeB\r\n\x0b_restrictedB\r\n\x0b_name_alias\"\x8f\x01\n\x1c\x41IModelAdminCreationResponse\x12&\n\x07\x61imodel\x18\x01 \x01(\x0b\x32\x10.aimodel.AIModelH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.aimodel.AIModelResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_aimodelB\x08\n\x06_error\"=\n\x19\x41IModelAdminDeleteRequest\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\x05\n\x03_id\"Y\n\x1a\x41IModelAdminDeleteResponse\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.aimodel.AIModelResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error*\xa4\x01\n\x0c\x41IModelError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x12\x0f\n\x0bNOT_UPDATED\x10\x03\x12\x12\n\x0eNOT_AUTHORIZED\x10\x04\x12\x1a\n\x16\x41IMODEL_OUT_OF_CREDITS\x10\x05\x12\"\n\x1e\x41IMODEL_DONT_HANDLE_COMPLETION\x10\x06\x42\x30Z.github.com/jupyter-naas/naas-models/go/aimodelb\x06proto3')

_AIMODELERROR = DESCRIPTOR.enum_types_by_name['AIModelError']
AIModelError = enum_type_wrapper.EnumTypeWrapper(_AIMODELERROR)
NO_ERROR = 0
ALREADY_EXISTS = 1
NOT_FOUND = 2
NOT_UPDATED = 3
NOT_AUTHORIZED = 4
AIMODEL_OUT_OF_CREDITS = 5
AIMODEL_DONT_HANDLE_COMPLETION = 6


_AIMODEL = DESCRIPTOR.message_types_by_name['AIModel']
_COMPLETIONRESPONSE = DESCRIPTOR.message_types_by_name['CompletionResponse']
_AIMODELRESPONSEERROR = DESCRIPTOR.message_types_by_name['AIModelResponseError']
_AIMODELLISTREQUEST = DESCRIPTOR.message_types_by_name['AIModelListRequest']
_AIMODELLISTRESPONSE = DESCRIPTOR.message_types_by_name['AIModelListResponse']
_AIMODELGETREQUEST = DESCRIPTOR.message_types_by_name['AIModelGetRequest']
_AIMODELGETRESPONSE = DESCRIPTOR.message_types_by_name['AIModelGetResponse']
_AIMODELCOMPLETIONREQUEST = DESCRIPTOR.message_types_by_name['AIModelCompletionRequest']
_AIMODELCOMPLETIONRESPONSE = DESCRIPTOR.message_types_by_name['AIModelCompletionResponse']
_AIMODELADMINCREATIONREQUEST = DESCRIPTOR.message_types_by_name['AIModelAdminCreationRequest']
_AIMODELADMINCREATIONRESPONSE = DESCRIPTOR.message_types_by_name['AIModelAdminCreationResponse']
_AIMODELADMINDELETEREQUEST = DESCRIPTOR.message_types_by_name['AIModelAdminDeleteRequest']
_AIMODELADMINDELETERESPONSE = DESCRIPTOR.message_types_by_name['AIModelAdminDeleteResponse']
AIModel = _reflection.GeneratedProtocolMessageType('AIModel', (_message.Message,), {
  'DESCRIPTOR' : _AIMODEL,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModel)
  })
_sym_db.RegisterMessage(AIModel)

CompletionResponse = _reflection.GeneratedProtocolMessageType('CompletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONRESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.CompletionResponse)
  })
_sym_db.RegisterMessage(CompletionResponse)

AIModelResponseError = _reflection.GeneratedProtocolMessageType('AIModelResponseError', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELRESPONSEERROR,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelResponseError)
  })
_sym_db.RegisterMessage(AIModelResponseError)

AIModelListRequest = _reflection.GeneratedProtocolMessageType('AIModelListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELLISTREQUEST,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelListRequest)
  })
_sym_db.RegisterMessage(AIModelListRequest)

AIModelListResponse = _reflection.GeneratedProtocolMessageType('AIModelListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELLISTRESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelListResponse)
  })
_sym_db.RegisterMessage(AIModelListResponse)

AIModelGetRequest = _reflection.GeneratedProtocolMessageType('AIModelGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELGETREQUEST,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelGetRequest)
  })
_sym_db.RegisterMessage(AIModelGetRequest)

AIModelGetResponse = _reflection.GeneratedProtocolMessageType('AIModelGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELGETRESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelGetResponse)
  })
_sym_db.RegisterMessage(AIModelGetResponse)

AIModelCompletionRequest = _reflection.GeneratedProtocolMessageType('AIModelCompletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELCOMPLETIONREQUEST,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelCompletionRequest)
  })
_sym_db.RegisterMessage(AIModelCompletionRequest)

AIModelCompletionResponse = _reflection.GeneratedProtocolMessageType('AIModelCompletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELCOMPLETIONRESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelCompletionResponse)
  })
_sym_db.RegisterMessage(AIModelCompletionResponse)

AIModelAdminCreationRequest = _reflection.GeneratedProtocolMessageType('AIModelAdminCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELADMINCREATIONREQUEST,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelAdminCreationRequest)
  })
_sym_db.RegisterMessage(AIModelAdminCreationRequest)

AIModelAdminCreationResponse = _reflection.GeneratedProtocolMessageType('AIModelAdminCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELADMINCREATIONRESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelAdminCreationResponse)
  })
_sym_db.RegisterMessage(AIModelAdminCreationResponse)

AIModelAdminDeleteRequest = _reflection.GeneratedProtocolMessageType('AIModelAdminDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELADMINDELETEREQUEST,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelAdminDeleteRequest)
  })
_sym_db.RegisterMessage(AIModelAdminDeleteRequest)

AIModelAdminDeleteResponse = _reflection.GeneratedProtocolMessageType('AIModelAdminDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _AIMODELADMINDELETERESPONSE,
  '__module__' : 'aimodel_pb2'
  # @@protoc_insertion_point(class_scope:aimodel.AIModelAdminDeleteResponse)
  })
_sym_db.RegisterMessage(AIModelAdminDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/jupyter-naas/naas-models/go/aimodel'
  _AIMODEL.fields_by_name['id']._options = None
  _AIMODEL.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _COMPLETIONRESPONSE.fields_by_name['model_id']._options = None
  _COMPLETIONRESPONSE.fields_by_name['model_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _AIMODELGETREQUEST.fields_by_name['id']._options = None
  _AIMODELGETREQUEST.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _AIMODELCOMPLETIONREQUEST.fields_by_name['id']._options = None
  _AIMODELCOMPLETIONREQUEST.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _AIMODELADMINDELETEREQUEST.fields_by_name['id']._options = None
  _AIMODELADMINDELETEREQUEST.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _AIMODELERROR._serialized_start=2101
  _AIMODELERROR._serialized_end=2265
  _AIMODEL._serialized_start=43
  _AIMODEL._serialized_end=370
  _COMPLETIONRESPONSE._serialized_start=373
  _COMPLETIONRESPONSE._serialized_end=644
  _AIMODELRESPONSEERROR._serialized_start=647
  _AIMODELRESPONSEERROR._serialized_end=818
  _AIMODELLISTREQUEST._serialized_start=820
  _AIMODELLISTREQUEST._serialized_end=920
  _AIMODELLISTRESPONSE._serialized_start=923
  _AIMODELLISTRESPONSE._serialized_end=1083
  _AIMODELGETREQUEST._serialized_start=1085
  _AIMODELGETREQUEST._serialized_end=1138
  _AIMODELGETRESPONSE._serialized_start=1141
  _AIMODELGETRESPONSE._serialized_end=1274
  _AIMODELCOMPLETIONREQUEST._serialized_start=1276
  _AIMODELCOMPLETIONREQUEST._serialized_end=1370
  _AIMODELCOMPLETIONRESPONSE._serialized_start=1373
  _AIMODELCOMPLETIONRESPONSE._serialized_end=1530
  _AIMODELADMINCREATIONREQUEST._serialized_start=1533
  _AIMODELADMINCREATIONREQUEST._serialized_end=1798
  _AIMODELADMINCREATIONRESPONSE._serialized_start=1801
  _AIMODELADMINCREATIONRESPONSE._serialized_end=1944
  _AIMODELADMINDELETEREQUEST._serialized_start=1946
  _AIMODELADMINDELETEREQUEST._serialized_end=2007
  _AIMODELADMINDELETERESPONSE._serialized_start=2009
  _AIMODELADMINDELETERESPONSE._serialized_end=2098
# @@protoc_insertion_point(module_scope)
