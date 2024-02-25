# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x07storage\x1a\x0evalidate.proto\"Q\n\x07Storage\x12\x19\n\x0cworkspace_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0f\n\r_workspace_idB\x07\n\x05_name\"$\n\x06Object\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"m\n\x14StorageResponseError\x12)\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x15.storage.StorageErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"k\n\x13ObjectResponseError\x12(\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x14.storage.ObjectErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"J\n\x14StorageCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"T\n\x15StorageCreateResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"/\n\x11StorageGetRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x85\x01\n\x12StorageGetResponse\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_storageB\x08\n\x06_error\"2\n\x14StorageDeleteRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"T\n\x15StorageDeleteResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"@\n\x12StorageListRequest\x12\x19\n\x0cworkspace_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_workspace_id\"t\n\x13StorageListResponse\x12\x14\n\x07storage\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_storageB\x08\n\x06_error\"z\n\x13ObjectCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"S\n\x14ObjectCreateResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"G\n\x11ObjectListRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"s\n\x12ObjectListResponse\x12 \n\x07objects\x18\x01 \x03(\x0b\x32\x0f.storage.Object\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x80\x01\n\x11ObjectGetResponse\x12$\n\x06object\x18\x01 \x01(\x0b\x32\x0f.storage.ObjectH\x00\x88\x01\x01\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x01\x88\x01\x01\x42\t\n\x07_objectB\x08\n\x06_error\"w\n\x10ObjectGetRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object*$\n\x0cStorageError\x12\x14\n\x10STORAGE_NO_ERROR\x10\x00*\"\n\x0bObjectError\x12\x13\n\x0fOBJECT_NO_ERROR\x10\x00\x42\x30Z.github.com/jupyter-naas/naas-models/go/storageb\x06proto3')

_STORAGEERROR = DESCRIPTOR.enum_types_by_name['StorageError']
StorageError = enum_type_wrapper.EnumTypeWrapper(_STORAGEERROR)
_OBJECTERROR = DESCRIPTOR.enum_types_by_name['ObjectError']
ObjectError = enum_type_wrapper.EnumTypeWrapper(_OBJECTERROR)
STORAGE_NO_ERROR = 0
OBJECT_NO_ERROR = 0


_STORAGE = DESCRIPTOR.message_types_by_name['Storage']
_OBJECT = DESCRIPTOR.message_types_by_name['Object']
_STORAGERESPONSEERROR = DESCRIPTOR.message_types_by_name['StorageResponseError']
_OBJECTRESPONSEERROR = DESCRIPTOR.message_types_by_name['ObjectResponseError']
_STORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['StorageCreateRequest']
_STORAGECREATERESPONSE = DESCRIPTOR.message_types_by_name['StorageCreateResponse']
_STORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['StorageGetRequest']
_STORAGEGETRESPONSE = DESCRIPTOR.message_types_by_name['StorageGetResponse']
_STORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['StorageDeleteRequest']
_STORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['StorageDeleteResponse']
_STORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['StorageListRequest']
_STORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['StorageListResponse']
_OBJECTCREATEREQUEST = DESCRIPTOR.message_types_by_name['ObjectCreateRequest']
_OBJECTCREATERESPONSE = DESCRIPTOR.message_types_by_name['ObjectCreateResponse']
_OBJECTLISTREQUEST = DESCRIPTOR.message_types_by_name['ObjectListRequest']
_OBJECTLISTRESPONSE = DESCRIPTOR.message_types_by_name['ObjectListResponse']
_OBJECTGETRESPONSE = DESCRIPTOR.message_types_by_name['ObjectGetResponse']
_OBJECTGETREQUEST = DESCRIPTOR.message_types_by_name['ObjectGetRequest']
Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {
  'DESCRIPTOR' : _STORAGE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.Storage)
  })
_sym_db.RegisterMessage(Storage)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.Object)
  })
_sym_db.RegisterMessage(Object)

StorageResponseError = _reflection.GeneratedProtocolMessageType('StorageResponseError', (_message.Message,), {
  'DESCRIPTOR' : _STORAGERESPONSEERROR,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageResponseError)
  })
_sym_db.RegisterMessage(StorageResponseError)

ObjectResponseError = _reflection.GeneratedProtocolMessageType('ObjectResponseError', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTRESPONSEERROR,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectResponseError)
  })
_sym_db.RegisterMessage(ObjectResponseError)

StorageCreateRequest = _reflection.GeneratedProtocolMessageType('StorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECREATEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageCreateRequest)
  })
_sym_db.RegisterMessage(StorageCreateRequest)

StorageCreateResponse = _reflection.GeneratedProtocolMessageType('StorageCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECREATERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageCreateResponse)
  })
_sym_db.RegisterMessage(StorageCreateResponse)

StorageGetRequest = _reflection.GeneratedProtocolMessageType('StorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEGETREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageGetRequest)
  })
_sym_db.RegisterMessage(StorageGetRequest)

StorageGetResponse = _reflection.GeneratedProtocolMessageType('StorageGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEGETRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageGetResponse)
  })
_sym_db.RegisterMessage(StorageGetResponse)

StorageDeleteRequest = _reflection.GeneratedProtocolMessageType('StorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDELETEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageDeleteRequest)
  })
_sym_db.RegisterMessage(StorageDeleteRequest)

StorageDeleteResponse = _reflection.GeneratedProtocolMessageType('StorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDELETERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageDeleteResponse)
  })
_sym_db.RegisterMessage(StorageDeleteResponse)

StorageListRequest = _reflection.GeneratedProtocolMessageType('StorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListRequest)
  })
_sym_db.RegisterMessage(StorageListRequest)

StorageListResponse = _reflection.GeneratedProtocolMessageType('StorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListResponse)
  })
_sym_db.RegisterMessage(StorageListResponse)

ObjectCreateRequest = _reflection.GeneratedProtocolMessageType('ObjectCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTCREATEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectCreateRequest)
  })
_sym_db.RegisterMessage(ObjectCreateRequest)

ObjectCreateResponse = _reflection.GeneratedProtocolMessageType('ObjectCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTCREATERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectCreateResponse)
  })
_sym_db.RegisterMessage(ObjectCreateResponse)

ObjectListRequest = _reflection.GeneratedProtocolMessageType('ObjectListRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTLISTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectListRequest)
  })
_sym_db.RegisterMessage(ObjectListRequest)

ObjectListResponse = _reflection.GeneratedProtocolMessageType('ObjectListResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTLISTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectListResponse)
  })
_sym_db.RegisterMessage(ObjectListResponse)

ObjectGetResponse = _reflection.GeneratedProtocolMessageType('ObjectGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTGETRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectGetResponse)
  })
_sym_db.RegisterMessage(ObjectGetResponse)

ObjectGetRequest = _reflection.GeneratedProtocolMessageType('ObjectGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTGETREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectGetRequest)
  })
_sym_db.RegisterMessage(ObjectGetRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/jupyter-naas/naas-models/go/storage'
  _STORAGEERROR._serialized_start=1703
  _STORAGEERROR._serialized_end=1739
  _OBJECTERROR._serialized_start=1741
  _OBJECTERROR._serialized_end=1775
  _STORAGE._serialized_start=42
  _STORAGE._serialized_end=123
  _OBJECT._serialized_start=125
  _OBJECT._serialized_end=161
  _STORAGERESPONSEERROR._serialized_start=163
  _STORAGERESPONSEERROR._serialized_end=272
  _OBJECTRESPONSEERROR._serialized_start=274
  _OBJECTRESPONSEERROR._serialized_end=381
  _STORAGECREATEREQUEST._serialized_start=383
  _STORAGECREATEREQUEST._serialized_end=457
  _STORAGECREATERESPONSE._serialized_start=459
  _STORAGECREATERESPONSE._serialized_end=543
  _STORAGEGETREQUEST._serialized_start=545
  _STORAGEGETREQUEST._serialized_end=592
  _STORAGEGETRESPONSE._serialized_start=595
  _STORAGEGETRESPONSE._serialized_end=728
  _STORAGEDELETEREQUEST._serialized_start=730
  _STORAGEDELETEREQUEST._serialized_end=780
  _STORAGEDELETERESPONSE._serialized_start=782
  _STORAGEDELETERESPONSE._serialized_end=866
  _STORAGELISTREQUEST._serialized_start=868
  _STORAGELISTREQUEST._serialized_end=932
  _STORAGELISTRESPONSE._serialized_start=934
  _STORAGELISTRESPONSE._serialized_end=1050
  _OBJECTCREATEREQUEST._serialized_start=1052
  _OBJECTCREATEREQUEST._serialized_end=1174
  _OBJECTCREATERESPONSE._serialized_start=1176
  _OBJECTCREATERESPONSE._serialized_end=1259
  _OBJECTLISTREQUEST._serialized_start=1261
  _OBJECTLISTREQUEST._serialized_end=1332
  _OBJECTLISTRESPONSE._serialized_start=1334
  _OBJECTLISTRESPONSE._serialized_end=1449
  _OBJECTGETRESPONSE._serialized_start=1452
  _OBJECTGETRESPONSE._serialized_end=1580
  _OBJECTGETREQUEST._serialized_start=1582
  _OBJECTGETREQUEST._serialized_end=1701
# @@protoc_insertion_point(module_scope)
