# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: space.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bspace.proto\x12\x05space\x1a\x0evalidate.proto\"\xcc\x04\n\x05Space\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x1e\n\x07user_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x12\x19\n\x02id\x18\x03 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x02\x88\x01\x01\x12R\n\ncreated_at\x18\x04 \x01(\tB9\xfa\x42\x36r422^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d{1,6})?Z$H\x03\x88\x01\x01\x12.\n\tresources\x18\x06 \x03(\x0b\x32\x1b.space.Space.ResourcesEntry\x12\x16\n\tnamespace\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x06\x64omain\x18\t \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01H\x05\x88\x01\x01\x12\x45\n\x05image\x18\n \x01(\tB1\xfa\x42.r,2*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$H\x06\x88\x01\x01\x12\x1a\n\x03url\x18\x0b \x01(\tB\x08\xfa\x42\x05r\x03\x88\x01\x01H\x07\x88\x01\x01\x12\"\n\tprotocols\x18\x0c \x03(\x0e\x32\x0f.space.Protocol\x1a\x30\n\x0eResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_nameB\n\n\x08_user_idB\x05\n\x03_idB\r\n\x0b_created_atB\x0c\n\n_namespaceB\t\n\x07_domainB\x08\n\x06_imageB\x06\n\x04_url\"\xa5\x01\n\x12SpaceResponseError\x12$\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x11.space.SpaceErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"\x82\x02\n\x14SpaceCreationRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x1e\n\x07user_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x12\x16\n\tnamespace\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x45\n\x05image\x18\x04 \x01(\tB1\xfa\x42.r,2*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$H\x03\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_user_idB\x0c\n\n_namespaceB\x08\n\x06_image\"c\n\x15SpaceCreationResponse\x12 \n\x05space\x18\x01 \x01(\x0b\x32\x0c.space.SpaceH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_spaceB\t\n\x07_status\"Z\n\x0fSpaceGetRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"^\n\x10SpaceGetResponse\x12 \n\x05space\x18\x01 \x01(\x0b\x32\x0c.space.SpaceH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_spaceB\t\n\x07_status\"_\n\x14SpaceDeletionRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"7\n\x15SpaceDeletionResponse\x12\x13\n\x06status\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_status\">\n\x10SpaceListRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\n\n\x08_user_id\"1\n\x11SpaceListResponse\x12\x1c\n\x06spaces\x18\x01 \x03(\x0b\x32\x0c.space.Space*\x1f\n\x08Protocol\x12\x08\n\x04HTTP\x10\x00\x12\t\n\x05HTTPS\x10\x01*;\n\nSpaceError\x12\x18\n\x14SPACE_ALREADY_EXISTS\x10\x00\x12\x13\n\x0fSPACE_NOT_FOUND\x10\x01\x42.Z,github.com/jupyter-naas/naas-models/go/spaceb\x06proto3')

_PROTOCOL = DESCRIPTOR.enum_types_by_name['Protocol']
Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
_SPACEERROR = DESCRIPTOR.enum_types_by_name['SpaceError']
SpaceError = enum_type_wrapper.EnumTypeWrapper(_SPACEERROR)
HTTP = 0
HTTPS = 1
SPACE_ALREADY_EXISTS = 0
SPACE_NOT_FOUND = 1


_SPACE = DESCRIPTOR.message_types_by_name['Space']
_SPACE_RESOURCESENTRY = _SPACE.nested_types_by_name['ResourcesEntry']
_SPACERESPONSEERROR = DESCRIPTOR.message_types_by_name['SpaceResponseError']
_SPACECREATIONREQUEST = DESCRIPTOR.message_types_by_name['SpaceCreationRequest']
_SPACECREATIONRESPONSE = DESCRIPTOR.message_types_by_name['SpaceCreationResponse']
_SPACEGETREQUEST = DESCRIPTOR.message_types_by_name['SpaceGetRequest']
_SPACEGETRESPONSE = DESCRIPTOR.message_types_by_name['SpaceGetResponse']
_SPACEDELETIONREQUEST = DESCRIPTOR.message_types_by_name['SpaceDeletionRequest']
_SPACEDELETIONRESPONSE = DESCRIPTOR.message_types_by_name['SpaceDeletionResponse']
_SPACELISTREQUEST = DESCRIPTOR.message_types_by_name['SpaceListRequest']
_SPACELISTRESPONSE = DESCRIPTOR.message_types_by_name['SpaceListResponse']
Space = _reflection.GeneratedProtocolMessageType('Space', (_message.Message,), {

  'ResourcesEntry' : _reflection.GeneratedProtocolMessageType('ResourcesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SPACE_RESOURCESENTRY,
    '__module__' : 'space_pb2'
    # @@protoc_insertion_point(class_scope:space.Space.ResourcesEntry)
    })
  ,
  'DESCRIPTOR' : _SPACE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.Space)
  })
_sym_db.RegisterMessage(Space)
_sym_db.RegisterMessage(Space.ResourcesEntry)

SpaceResponseError = _reflection.GeneratedProtocolMessageType('SpaceResponseError', (_message.Message,), {
  'DESCRIPTOR' : _SPACERESPONSEERROR,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceResponseError)
  })
_sym_db.RegisterMessage(SpaceResponseError)

SpaceCreationRequest = _reflection.GeneratedProtocolMessageType('SpaceCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACECREATIONREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceCreationRequest)
  })
_sym_db.RegisterMessage(SpaceCreationRequest)

SpaceCreationResponse = _reflection.GeneratedProtocolMessageType('SpaceCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACECREATIONRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceCreationResponse)
  })
_sym_db.RegisterMessage(SpaceCreationResponse)

SpaceGetRequest = _reflection.GeneratedProtocolMessageType('SpaceGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACEGETREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceGetRequest)
  })
_sym_db.RegisterMessage(SpaceGetRequest)

SpaceGetResponse = _reflection.GeneratedProtocolMessageType('SpaceGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACEGETRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceGetResponse)
  })
_sym_db.RegisterMessage(SpaceGetResponse)

SpaceDeletionRequest = _reflection.GeneratedProtocolMessageType('SpaceDeletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDELETIONREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceDeletionRequest)
  })
_sym_db.RegisterMessage(SpaceDeletionRequest)

SpaceDeletionResponse = _reflection.GeneratedProtocolMessageType('SpaceDeletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDELETIONRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceDeletionResponse)
  })
_sym_db.RegisterMessage(SpaceDeletionResponse)

SpaceListRequest = _reflection.GeneratedProtocolMessageType('SpaceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACELISTREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceListRequest)
  })
_sym_db.RegisterMessage(SpaceListRequest)

SpaceListResponse = _reflection.GeneratedProtocolMessageType('SpaceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACELISTRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceListResponse)
  })
_sym_db.RegisterMessage(SpaceListResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/jupyter-naas/naas-models/go/space'
  _SPACE_RESOURCESENTRY._options = None
  _SPACE_RESOURCESENTRY._serialized_options = b'8\001'
  _SPACE.fields_by_name['name']._options = None
  _SPACE.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACE.fields_by_name['user_id']._options = None
  _SPACE.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _SPACE.fields_by_name['id']._options = None
  _SPACE.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _SPACE.fields_by_name['created_at']._options = None
  _SPACE.fields_by_name['created_at']._serialized_options = b'\372B6r422^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d{1,6})?Z$'
  _SPACE.fields_by_name['domain']._options = None
  _SPACE.fields_by_name['domain']._serialized_options = b'\372B\005r\003\220\001\001'
  _SPACE.fields_by_name['image']._options = None
  _SPACE.fields_by_name['image']._serialized_options = b'\372B.r,2*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$'
  _SPACE.fields_by_name['url']._options = None
  _SPACE.fields_by_name['url']._serialized_options = b'\372B\005r\003\210\001\001'
  _SPACECREATIONREQUEST.fields_by_name['name']._options = None
  _SPACECREATIONREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACECREATIONREQUEST.fields_by_name['user_id']._options = None
  _SPACECREATIONREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _SPACECREATIONREQUEST.fields_by_name['image']._options = None
  _SPACECREATIONREQUEST.fields_by_name['image']._serialized_options = b'\372B.r,2*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$'
  _SPACEGETREQUEST.fields_by_name['name']._options = None
  _SPACEGETREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACEDELETIONREQUEST.fields_by_name['name']._options = None
  _SPACEDELETIONREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACELISTREQUEST.fields_by_name['user_id']._options = None
  _SPACELISTREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _PROTOCOL._serialized_start=1616
  _PROTOCOL._serialized_end=1647
  _SPACEERROR._serialized_start=1649
  _SPACEERROR._serialized_end=1708
  _SPACE._serialized_start=39
  _SPACE._serialized_end=627
  _SPACE_RESOURCESENTRY._serialized_start=493
  _SPACE_RESOURCESENTRY._serialized_end=541
  _SPACERESPONSEERROR._serialized_start=630
  _SPACERESPONSEERROR._serialized_end=795
  _SPACECREATIONREQUEST._serialized_start=798
  _SPACECREATIONREQUEST._serialized_end=1056
  _SPACECREATIONRESPONSE._serialized_start=1058
  _SPACECREATIONRESPONSE._serialized_end=1157
  _SPACEGETREQUEST._serialized_start=1159
  _SPACEGETREQUEST._serialized_end=1249
  _SPACEGETRESPONSE._serialized_start=1251
  _SPACEGETRESPONSE._serialized_end=1345
  _SPACEDELETIONREQUEST._serialized_start=1347
  _SPACEDELETIONREQUEST._serialized_end=1442
  _SPACEDELETIONRESPONSE._serialized_start=1444
  _SPACEDELETIONRESPONSE._serialized_end=1499
  _SPACELISTREQUEST._serialized_start=1501
  _SPACELISTREQUEST._serialized_end=1563
  _SPACELISTRESPONSE._serialized_start=1565
  _SPACELISTRESPONSE._serialized_end=1614
# @@protoc_insertion_point(module_scope)
