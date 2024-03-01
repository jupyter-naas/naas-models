# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workspace.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworkspace.proto\x12\tworkspace\x1a\x0evalidate.proto\"\x95\x02\n\tWorkspace\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04logo\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rprimary_color\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1c\n\x0fsecondary_color\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0bis_personal\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x16\n\tcreate_at\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x07\n\x05_logoB\x10\n\x0e_primary_colorB\x12\n\x10_secondary_colorB\x0e\n\x0c_is_personalB\x0c\n\n_create_at\"\xa9\x01\n\x0fWorkspaceUpdate\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04logo\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rprimary_color\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0fsecondary_color\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_nameB\x07\n\x05_logoB\x10\n\x0e_primary_colorB\x12\n\x10_secondary_color\"\xf9\x01\n\rWorkspaceUser\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12#\n\x0cworkspace_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x12\x11\n\x04role\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06status\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x16\n\tcreate_at\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x16\n\tupdate_at\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\n\n\x08_user_idB\x0f\n\r_workspace_idB\x07\n\x05_roleB\t\n\x07_statusB\x0c\n\n_create_atB\x0c\n\n_update_at\"Q\n\x13WorkspaceUserUpdate\x12\x11\n\x04role\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_roleB\t\n\x07_status\"3\n\x0fWorkspacePlugin\x12\x19\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\x05\n\x03_id\"q\n\x16WorkspaceResponseError\x12,\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.workspace.WorkspaceErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_codeB\n\n\x08_message\"B\n\x14WorkspaceListRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\n\n\x08_user_id\"\x82\x01\n\x15WorkspaceListResponse\x12(\n\nworkspaces\x18\x01 \x03(\x0b\x32\x14.workspace.Workspace\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.workspace.WorkspaceResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x86\x02\n\x16WorkspaceCreateRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04logo\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rprimary_color\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1c\n\x0fsecondary_color\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0bis_personal\x18\x06 \x01(\x08H\x05\x88\x01\x01\x42\n\n\x08_user_idB\x07\n\x05_nameB\x07\n\x05_logoB\x10\n\x0e_primary_colorB\x12\n\x10_secondary_colorB\x0e\n\x0c_is_personal\"\x96\x01\n\x17WorkspaceCreateResponse\x12,\n\tworkspace\x18\x01 \x01(\x0b\x32\x14.workspace.WorkspaceH\x00\x88\x01\x01\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.workspace.WorkspaceResponseErrorH\x01\x88\x01\x01\x42\x0c\n\n_workspaceB\x08\n\x06_error\"w\n\x13WorkspaceGetRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12#\n\x0cworkspace_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x42\n\n\x08_user_idB\x0f\n\r_workspace_id\"\x93\x01\n\x14WorkspaceGetResponse\x12,\n\tworkspace\x18\x01 \x01(\x0b\x32\x14.workspace.WorkspaceH\x00\x88\x01\x01\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.workspace.WorkspaceResponseErrorH\x01\x88\x01\x01\x42\x0c\n\n_workspaceB\x08\n\x06_error\"\x90\x01\n\x16WorkspaceUpdateRequest\x12#\n\x0cworkspace_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x32\n\tworkspace\x18\x02 \x01(\x0b\x32\x1a.workspace.WorkspaceUpdateH\x01\x88\x01\x01\x42\x0f\n\r_workspace_idB\x0c\n\n_workspace\"\x96\x01\n\x17WorkspaceUpdateResponse\x12,\n\tworkspace\x18\x01 \x01(\x0b\x32\x14.workspace.WorkspaceH\x00\x88\x01\x01\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32!.workspace.WorkspaceResponseErrorH\x01\x88\x01\x01\x42\x0c\n\n_workspaceB\x08\n\x06_error\"z\n\x16WorkspaceDeleteRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12#\n\x0cworkspace_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x42\n\n\x08_user_idB\x0f\n\r_workspace_id\"Z\n\x17WorkspaceDeleteResponse\x12\x35\n\x05\x65rror\x18\x01 \x01(\x0b\x32!.workspace.WorkspaceResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error*\xeb\x01\n\x0eWorkspaceError\x12\x16\n\x12WORKSPACE_NO_ERROR\x10\x00\x12\x17\n\x13WORKSPACE_NOT_FOUND\x10\x01\x12!\n\x1dWORKSPACE_USER_ALREADY_EXISTS\x10\x02\x12\x1c\n\x18WORKSPACE_USER_NOT_FOUND\x10\x03\x12!\n\x1dWORKSPACE_USER_ALREADY_ACTIVE\x10\x04\x12(\n$USER_ALREADY_HAVE_PERSONAL_WORKSPACE\x10\x05\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\xe8\x07\x42\x32Z0github.com/jupyter-naas/naas-models/go/workspaceb\x06proto3')

_WORKSPACEERROR = DESCRIPTOR.enum_types_by_name['WorkspaceError']
WorkspaceError = enum_type_wrapper.EnumTypeWrapper(_WORKSPACEERROR)
WORKSPACE_NO_ERROR = 0
WORKSPACE_NOT_FOUND = 1
WORKSPACE_USER_ALREADY_EXISTS = 2
WORKSPACE_USER_NOT_FOUND = 3
WORKSPACE_USER_ALREADY_ACTIVE = 4
USER_ALREADY_HAVE_PERSONAL_WORKSPACE = 5
INTERNAL_SERVER_ERROR = 1000


_WORKSPACE = DESCRIPTOR.message_types_by_name['Workspace']
_WORKSPACEUPDATE = DESCRIPTOR.message_types_by_name['WorkspaceUpdate']
_WORKSPACEUSER = DESCRIPTOR.message_types_by_name['WorkspaceUser']
_WORKSPACEUSERUPDATE = DESCRIPTOR.message_types_by_name['WorkspaceUserUpdate']
_WORKSPACEPLUGIN = DESCRIPTOR.message_types_by_name['WorkspacePlugin']
_WORKSPACERESPONSEERROR = DESCRIPTOR.message_types_by_name['WorkspaceResponseError']
_WORKSPACELISTREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceListRequest']
_WORKSPACELISTRESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceListResponse']
_WORKSPACECREATEREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceCreateRequest']
_WORKSPACECREATERESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceCreateResponse']
_WORKSPACEGETREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceGetRequest']
_WORKSPACEGETRESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceGetResponse']
_WORKSPACEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceUpdateRequest']
_WORKSPACEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceUpdateResponse']
_WORKSPACEDELETEREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceDeleteRequest']
_WORKSPACEDELETERESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceDeleteResponse']
Workspace = _reflection.GeneratedProtocolMessageType('Workspace', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.Workspace)
  })
_sym_db.RegisterMessage(Workspace)

WorkspaceUpdate = _reflection.GeneratedProtocolMessageType('WorkspaceUpdate', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUPDATE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceUpdate)
  })
_sym_db.RegisterMessage(WorkspaceUpdate)

WorkspaceUser = _reflection.GeneratedProtocolMessageType('WorkspaceUser', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUSER,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceUser)
  })
_sym_db.RegisterMessage(WorkspaceUser)

WorkspaceUserUpdate = _reflection.GeneratedProtocolMessageType('WorkspaceUserUpdate', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUSERUPDATE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceUserUpdate)
  })
_sym_db.RegisterMessage(WorkspaceUserUpdate)

WorkspacePlugin = _reflection.GeneratedProtocolMessageType('WorkspacePlugin', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEPLUGIN,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspacePlugin)
  })
_sym_db.RegisterMessage(WorkspacePlugin)

WorkspaceResponseError = _reflection.GeneratedProtocolMessageType('WorkspaceResponseError', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACERESPONSEERROR,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceResponseError)
  })
_sym_db.RegisterMessage(WorkspaceResponseError)

WorkspaceListRequest = _reflection.GeneratedProtocolMessageType('WorkspaceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACELISTREQUEST,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceListRequest)
  })
_sym_db.RegisterMessage(WorkspaceListRequest)

WorkspaceListResponse = _reflection.GeneratedProtocolMessageType('WorkspaceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACELISTRESPONSE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceListResponse)
  })
_sym_db.RegisterMessage(WorkspaceListResponse)

WorkspaceCreateRequest = _reflection.GeneratedProtocolMessageType('WorkspaceCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACECREATEREQUEST,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceCreateRequest)
  })
_sym_db.RegisterMessage(WorkspaceCreateRequest)

WorkspaceCreateResponse = _reflection.GeneratedProtocolMessageType('WorkspaceCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACECREATERESPONSE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceCreateResponse)
  })
_sym_db.RegisterMessage(WorkspaceCreateResponse)

WorkspaceGetRequest = _reflection.GeneratedProtocolMessageType('WorkspaceGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEGETREQUEST,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceGetRequest)
  })
_sym_db.RegisterMessage(WorkspaceGetRequest)

WorkspaceGetResponse = _reflection.GeneratedProtocolMessageType('WorkspaceGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEGETRESPONSE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceGetResponse)
  })
_sym_db.RegisterMessage(WorkspaceGetResponse)

WorkspaceUpdateRequest = _reflection.GeneratedProtocolMessageType('WorkspaceUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUPDATEREQUEST,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceUpdateRequest)
  })
_sym_db.RegisterMessage(WorkspaceUpdateRequest)

WorkspaceUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkspaceUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUPDATERESPONSE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceUpdateResponse)
  })
_sym_db.RegisterMessage(WorkspaceUpdateResponse)

WorkspaceDeleteRequest = _reflection.GeneratedProtocolMessageType('WorkspaceDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEDELETEREQUEST,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceDeleteRequest)
  })
_sym_db.RegisterMessage(WorkspaceDeleteRequest)

WorkspaceDeleteResponse = _reflection.GeneratedProtocolMessageType('WorkspaceDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEDELETERESPONSE,
  '__module__' : 'workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceDeleteResponse)
  })
_sym_db.RegisterMessage(WorkspaceDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/jupyter-naas/naas-models/go/workspace'
  _WORKSPACE.fields_by_name['id']._options = None
  _WORKSPACE.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEUSER.fields_by_name['user_id']._options = None
  _WORKSPACEUSER.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEUSER.fields_by_name['workspace_id']._options = None
  _WORKSPACEUSER.fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEPLUGIN.fields_by_name['id']._options = None
  _WORKSPACEPLUGIN.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACELISTREQUEST.fields_by_name['user_id']._options = None
  _WORKSPACELISTREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACECREATEREQUEST.fields_by_name['user_id']._options = None
  _WORKSPACECREATEREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEGETREQUEST.fields_by_name['user_id']._options = None
  _WORKSPACEGETREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEGETREQUEST.fields_by_name['workspace_id']._options = None
  _WORKSPACEGETREQUEST.fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEUPDATEREQUEST.fields_by_name['workspace_id']._options = None
  _WORKSPACEUPDATEREQUEST.fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEDELETEREQUEST.fields_by_name['user_id']._options = None
  _WORKSPACEDELETEREQUEST.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEDELETEREQUEST.fields_by_name['workspace_id']._options = None
  _WORKSPACEDELETEREQUEST.fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _WORKSPACEERROR._serialized_start=2408
  _WORKSPACEERROR._serialized_end=2643
  _WORKSPACE._serialized_start=47
  _WORKSPACE._serialized_end=324
  _WORKSPACEUPDATE._serialized_start=327
  _WORKSPACEUPDATE._serialized_end=496
  _WORKSPACEUSER._serialized_start=499
  _WORKSPACEUSER._serialized_end=748
  _WORKSPACEUSERUPDATE._serialized_start=750
  _WORKSPACEUSERUPDATE._serialized_end=831
  _WORKSPACEPLUGIN._serialized_start=833
  _WORKSPACEPLUGIN._serialized_end=884
  _WORKSPACERESPONSEERROR._serialized_start=886
  _WORKSPACERESPONSEERROR._serialized_end=999
  _WORKSPACELISTREQUEST._serialized_start=1001
  _WORKSPACELISTREQUEST._serialized_end=1067
  _WORKSPACELISTRESPONSE._serialized_start=1070
  _WORKSPACELISTRESPONSE._serialized_end=1200
  _WORKSPACECREATEREQUEST._serialized_start=1203
  _WORKSPACECREATEREQUEST._serialized_end=1465
  _WORKSPACECREATERESPONSE._serialized_start=1468
  _WORKSPACECREATERESPONSE._serialized_end=1618
  _WORKSPACEGETREQUEST._serialized_start=1620
  _WORKSPACEGETREQUEST._serialized_end=1739
  _WORKSPACEGETRESPONSE._serialized_start=1742
  _WORKSPACEGETRESPONSE._serialized_end=1889
  _WORKSPACEUPDATEREQUEST._serialized_start=1892
  _WORKSPACEUPDATEREQUEST._serialized_end=2036
  _WORKSPACEUPDATERESPONSE._serialized_start=2039
  _WORKSPACEUPDATERESPONSE._serialized_end=2189
  _WORKSPACEDELETEREQUEST._serialized_start=2191
  _WORKSPACEDELETEREQUEST._serialized_end=2313
  _WORKSPACEDELETERESPONSE._serialized_start=2315
  _WORKSPACEDELETERESPONSE._serialized_end=2405
# @@protoc_insertion_point(module_scope)
