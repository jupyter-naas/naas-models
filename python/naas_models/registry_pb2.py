# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registry.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregistry.proto\x12\x08registry\x1a\x0evalidate.proto\"\x8f\x01\n\x08Registry\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03uri\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_user_idB\x06\n\x04_uri\"]\n\x13RegistryCredentials\x12\x15\n\x08username\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08password\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_usernameB\x0b\n\t_password\"b\n\x17RegistryCreationRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"R\n\x18RegistryCreationResponse\x12)\n\x08registry\x18\x01 \x01(\x0b\x32\x12.registry.RegistryH\x00\x88\x01\x01\x42\x0b\n\t_registry\"\x84\x01\n\x1dRegistryCreationResponseError\x12+\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x17.registry.RegistryErrorH\x00\x88\x01\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x10\n\x0e_error_message\"e\n\x13RegistryListRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_page_sizeB\x0e\n\x0c_page_number\">\n\x14RegistryListResponse\x12&\n\nregistries\x18\x01 \x03(\x0b\x32\x12.registry.Registry\"]\n\x12RegistryGetRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"M\n\x13RegistryGetResponse\x12)\n\x08registry\x18\x01 \x01(\x0b\x32\x12.registry.RegistryH\x00\x88\x01\x01\x42\x0b\n\t_registry\"\x7f\n\x18RegistryGetResponseError\x12+\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x17.registry.RegistryErrorH\x00\x88\x01\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x10\n\x0e_error_message\"3\n\x15RegistryDeleteRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x82\x01\n\x1bRegistryDeleteResponseError\x12+\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x17.registry.RegistryErrorH\x00\x88\x01\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x10\n\x0e_error_message\"e\n\x1aRegistryCredentialsRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"\xaf\x01\n\x1bRegistryCredentialsResponse\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x37\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x1d.registry.RegistryCredentialsH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_credentials\"\x87\x01\n RegistryCredentialsResponseError\x12+\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x17.registry.RegistryErrorH\x00\x88\x01\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x10\n\x0e_error_message*X\n\rRegistryError\x12\x1b\n\x17REGISTRY_ALREADY_EXISTS\x10\x00\x12\x16\n\x12REGISTRY_NOT_FOUND\x10\x01\x12\x12\n\x0eNOT_AUTHORIZED\x10\x02\x42\x31Z/github.com/jupyter-naas/naas-models/go/registryb\x06proto3')

_REGISTRYERROR = DESCRIPTOR.enum_types_by_name['RegistryError']
RegistryError = enum_type_wrapper.EnumTypeWrapper(_REGISTRYERROR)
REGISTRY_ALREADY_EXISTS = 0
REGISTRY_NOT_FOUND = 1
NOT_AUTHORIZED = 2


_REGISTRY = DESCRIPTOR.message_types_by_name['Registry']
_REGISTRYCREDENTIALS = DESCRIPTOR.message_types_by_name['RegistryCredentials']
_REGISTRYCREATIONREQUEST = DESCRIPTOR.message_types_by_name['RegistryCreationRequest']
_REGISTRYCREATIONRESPONSE = DESCRIPTOR.message_types_by_name['RegistryCreationResponse']
_REGISTRYCREATIONRESPONSEERROR = DESCRIPTOR.message_types_by_name['RegistryCreationResponseError']
_REGISTRYLISTREQUEST = DESCRIPTOR.message_types_by_name['RegistryListRequest']
_REGISTRYLISTRESPONSE = DESCRIPTOR.message_types_by_name['RegistryListResponse']
_REGISTRYGETREQUEST = DESCRIPTOR.message_types_by_name['RegistryGetRequest']
_REGISTRYGETRESPONSE = DESCRIPTOR.message_types_by_name['RegistryGetResponse']
_REGISTRYGETRESPONSEERROR = DESCRIPTOR.message_types_by_name['RegistryGetResponseError']
_REGISTRYDELETEREQUEST = DESCRIPTOR.message_types_by_name['RegistryDeleteRequest']
_REGISTRYDELETERESPONSEERROR = DESCRIPTOR.message_types_by_name['RegistryDeleteResponseError']
_REGISTRYCREDENTIALSREQUEST = DESCRIPTOR.message_types_by_name['RegistryCredentialsRequest']
_REGISTRYCREDENTIALSRESPONSE = DESCRIPTOR.message_types_by_name['RegistryCredentialsResponse']
_REGISTRYCREDENTIALSRESPONSEERROR = DESCRIPTOR.message_types_by_name['RegistryCredentialsResponseError']
Registry = _reflection.GeneratedProtocolMessageType('Registry', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRY,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.Registry)
  })
_sym_db.RegisterMessage(Registry)

RegistryCredentials = _reflection.GeneratedProtocolMessageType('RegistryCredentials', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREDENTIALS,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCredentials)
  })
_sym_db.RegisterMessage(RegistryCredentials)

RegistryCreationRequest = _reflection.GeneratedProtocolMessageType('RegistryCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREATIONREQUEST,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCreationRequest)
  })
_sym_db.RegisterMessage(RegistryCreationRequest)

RegistryCreationResponse = _reflection.GeneratedProtocolMessageType('RegistryCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREATIONRESPONSE,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCreationResponse)
  })
_sym_db.RegisterMessage(RegistryCreationResponse)

RegistryCreationResponseError = _reflection.GeneratedProtocolMessageType('RegistryCreationResponseError', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREATIONRESPONSEERROR,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCreationResponseError)
  })
_sym_db.RegisterMessage(RegistryCreationResponseError)

RegistryListRequest = _reflection.GeneratedProtocolMessageType('RegistryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYLISTREQUEST,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryListRequest)
  })
_sym_db.RegisterMessage(RegistryListRequest)

RegistryListResponse = _reflection.GeneratedProtocolMessageType('RegistryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYLISTRESPONSE,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryListResponse)
  })
_sym_db.RegisterMessage(RegistryListResponse)

RegistryGetRequest = _reflection.GeneratedProtocolMessageType('RegistryGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYGETREQUEST,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryGetRequest)
  })
_sym_db.RegisterMessage(RegistryGetRequest)

RegistryGetResponse = _reflection.GeneratedProtocolMessageType('RegistryGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYGETRESPONSE,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryGetResponse)
  })
_sym_db.RegisterMessage(RegistryGetResponse)

RegistryGetResponseError = _reflection.GeneratedProtocolMessageType('RegistryGetResponseError', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYGETRESPONSEERROR,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryGetResponseError)
  })
_sym_db.RegisterMessage(RegistryGetResponseError)

RegistryDeleteRequest = _reflection.GeneratedProtocolMessageType('RegistryDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYDELETEREQUEST,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryDeleteRequest)
  })
_sym_db.RegisterMessage(RegistryDeleteRequest)

RegistryDeleteResponseError = _reflection.GeneratedProtocolMessageType('RegistryDeleteResponseError', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYDELETERESPONSEERROR,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryDeleteResponseError)
  })
_sym_db.RegisterMessage(RegistryDeleteResponseError)

RegistryCredentialsRequest = _reflection.GeneratedProtocolMessageType('RegistryCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREDENTIALSREQUEST,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCredentialsRequest)
  })
_sym_db.RegisterMessage(RegistryCredentialsRequest)

RegistryCredentialsResponse = _reflection.GeneratedProtocolMessageType('RegistryCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREDENTIALSRESPONSE,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCredentialsResponse)
  })
_sym_db.RegisterMessage(RegistryCredentialsResponse)

RegistryCredentialsResponseError = _reflection.GeneratedProtocolMessageType('RegistryCredentialsResponseError', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRYCREDENTIALSRESPONSEERROR,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.RegistryCredentialsResponseError)
  })
_sym_db.RegisterMessage(RegistryCredentialsResponseError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/jupyter-naas/naas-models/go/registry'
  _REGISTRY.fields_by_name['name']._options = None
  _REGISTRY.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _REGISTRYCREATIONREQUEST.fields_by_name['name']._options = None
  _REGISTRYCREATIONREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _REGISTRYGETREQUEST.fields_by_name['name']._options = None
  _REGISTRYGETREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _REGISTRYCREDENTIALSREQUEST.fields_by_name['name']._options = None
  _REGISTRYCREDENTIALSREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _REGISTRYCREDENTIALSRESPONSE.fields_by_name['name']._options = None
  _REGISTRYCREDENTIALSRESPONSE.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _REGISTRYERROR._serialized_start=1679
  _REGISTRYERROR._serialized_end=1767
  _REGISTRY._serialized_start=45
  _REGISTRY._serialized_end=188
  _REGISTRYCREDENTIALS._serialized_start=190
  _REGISTRYCREDENTIALS._serialized_end=283
  _REGISTRYCREATIONREQUEST._serialized_start=285
  _REGISTRYCREATIONREQUEST._serialized_end=383
  _REGISTRYCREATIONRESPONSE._serialized_start=385
  _REGISTRYCREATIONRESPONSE._serialized_end=467
  _REGISTRYCREATIONRESPONSEERROR._serialized_start=470
  _REGISTRYCREATIONRESPONSEERROR._serialized_end=602
  _REGISTRYLISTREQUEST._serialized_start=604
  _REGISTRYLISTREQUEST._serialized_end=705
  _REGISTRYLISTRESPONSE._serialized_start=707
  _REGISTRYLISTRESPONSE._serialized_end=769
  _REGISTRYGETREQUEST._serialized_start=771
  _REGISTRYGETREQUEST._serialized_end=864
  _REGISTRYGETRESPONSE._serialized_start=866
  _REGISTRYGETRESPONSE._serialized_end=943
  _REGISTRYGETRESPONSEERROR._serialized_start=945
  _REGISTRYGETRESPONSEERROR._serialized_end=1072
  _REGISTRYDELETEREQUEST._serialized_start=1074
  _REGISTRYDELETEREQUEST._serialized_end=1125
  _REGISTRYDELETERESPONSEERROR._serialized_start=1128
  _REGISTRYDELETERESPONSEERROR._serialized_end=1258
  _REGISTRYCREDENTIALSREQUEST._serialized_start=1260
  _REGISTRYCREDENTIALSREQUEST._serialized_end=1361
  _REGISTRYCREDENTIALSRESPONSE._serialized_start=1364
  _REGISTRYCREDENTIALSRESPONSE._serialized_end=1539
  _REGISTRYCREDENTIALSRESPONSEERROR._serialized_start=1542
  _REGISTRYCREDENTIALSRESPONSEERROR._serialized_end=1677
# @@protoc_insertion_point(module_scope)