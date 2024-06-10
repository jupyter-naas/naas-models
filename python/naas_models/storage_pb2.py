# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x07storage\x1a\x0evalidate.proto\"%\n\x07Storage\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\xa8\x01\n\x06Object\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06prefix\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04size\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0clastmodified\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\x07\n\x05_nameB\x07\n\x05_typeB\t\n\x07_prefixB\x07\n\x05_sizeB\x0f\n\r_lastmodified\"m\n\x14StorageResponseError\x12)\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x15.storage.StorageErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"k\n\x13ObjectResponseError\x12(\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x14.storage.ObjectErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"\x82\x01\n%ObjectStorageCredentialsResponseError\x12-\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x19.storage.CredentialsErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"y\n\x12StorageListRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"u\n\x13StorageListResponse\x12!\n\x07storage\x18\x01 \x03(\x0b\x32\x10.storage.Storage\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"J\n\x14StorageCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"\x88\x01\n\x15StorageCreateResponse\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_storageB\x08\n\x06_error\"J\n\x14StorageDeleteRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"T\n\x15StorageDeleteResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x7f\n\x18StorageListObjectRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"y\n\x19StorageListObjectResponse\x12\x1f\n\x06object\x18\x01 \x03(\x0b\x32\x0f.storage.Object\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"z\n\x13ObjectCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"R\n\x14ObjectCreateResponse\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"x\n\x11ObjectListRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"q\n\x12ObjectListResponse\x12\x1f\n\x06object\x18\x01 \x03(\x0b\x32\x0f.storage.Object\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"w\n\x10ObjectGetRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"\x80\x01\n\x11ObjectGetResponse\x12$\n\x06object\x18\x01 \x01(\x0b\x32\x0f.storage.ObjectH\x00\x88\x01\x01\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x01\x88\x01\x01\x42\t\n\x07_objectB\x08\n\x06_error\"F\n\x13ObjectDeleteRequest\x12$\n\x06object\x18\x01 \x01(\x0b\x32\x0f.storage.ObjectH\x00\x88\x01\x01\x42\t\n\x07_object\"R\n\x14ObjectDeleteResponse\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x9e\x02\n\x1aObjectStorageS3Credentials\x12\x19\n\x0c\x65ndpoint_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bregion_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\raccess_key_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nsecret_key\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rsession_token\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nexpiration\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x0f\n\r_endpoint_urlB\x0e\n\x0c_region_nameB\x10\n\x0e_access_key_idB\r\n\x0b_secret_keyB\x10\n\x0e_session_tokenB\r\n\x0b_expiration\"\xa1\x01\n\x1dObjectStorageAzureCredentials\x12\x19\n\x0c\x65ndpoint_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\raccess_key_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nsecret_key\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0f\n\r_endpoint_urlB\x10\n\x0e_access_key_idB\r\n\x0b_secret_key\"K\n\x18ObjectStorageCredentials\x12/\n\x02s3\x18\x01 \x01(\x0b\x32#.storage.ObjectStorageS3Credentials\"U\n\x1fObjectStorageCredentialsRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"\xbd\x01\n ObjectStorageCredentialsResponse\x12;\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32!.storage.ObjectStorageCredentialsH\x00\x88\x01\x01\x12\x42\n\x05\x65rror\x18\x02 \x01(\x0b\x32..storage.ObjectStorageCredentialsResponseErrorH\x01\x88\x01\x01\x42\x0e\n\x0c_credentialsB\x08\n\x06_error*V\n\x0cStorageError\x12\x14\n\x10STORAGE_NO_ERROR\x10\x00\x12\x19\n\x15STORAGE_ALREADY_EXIST\x10\x01\x12\x15\n\x11STORAGE_NOT_FOUND\x10\x02*\x83\x01\n\x0bObjectError\x12\x13\n\x0fOBJECT_NO_ERROR\x10\x00\x12\x18\n\x14OBJECT_ALREADY_EXIST\x10\x01\x12\x15\n\x11OBJECT_SIZE_ERROR\x10\x02\x12\x14\n\x10OBJECT_NOT_FOUND\x10\x03\x12\x18\n\x14OBJECT_DIR_NOT_EMPTY\x10\x04*,\n\x10\x43redentialsError\x12\x18\n\x14\x43REDENTIALS_NO_ERROR\x10\x00\x42\x30Z.github.com/jupyter-naas/naas-models/go/storageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/jupyter-naas/naas-models/go/storage'
  _globals['_STORAGEERROR']._serialized_start=3138
  _globals['_STORAGEERROR']._serialized_end=3224
  _globals['_OBJECTERROR']._serialized_start=3227
  _globals['_OBJECTERROR']._serialized_end=3358
  _globals['_CREDENTIALSERROR']._serialized_start=3360
  _globals['_CREDENTIALSERROR']._serialized_end=3404
  _globals['_STORAGE']._serialized_start=42
  _globals['_STORAGE']._serialized_end=79
  _globals['_OBJECT']._serialized_start=82
  _globals['_OBJECT']._serialized_end=250
  _globals['_STORAGERESPONSEERROR']._serialized_start=252
  _globals['_STORAGERESPONSEERROR']._serialized_end=361
  _globals['_OBJECTRESPONSEERROR']._serialized_start=363
  _globals['_OBJECTRESPONSEERROR']._serialized_end=470
  _globals['_OBJECTSTORAGECREDENTIALSRESPONSEERROR']._serialized_start=473
  _globals['_OBJECTSTORAGECREDENTIALSRESPONSEERROR']._serialized_end=603
  _globals['_STORAGELISTREQUEST']._serialized_start=605
  _globals['_STORAGELISTREQUEST']._serialized_end=726
  _globals['_STORAGELISTRESPONSE']._serialized_start=728
  _globals['_STORAGELISTRESPONSE']._serialized_end=845
  _globals['_STORAGECREATEREQUEST']._serialized_start=847
  _globals['_STORAGECREATEREQUEST']._serialized_end=921
  _globals['_STORAGECREATERESPONSE']._serialized_start=924
  _globals['_STORAGECREATERESPONSE']._serialized_end=1060
  _globals['_STORAGEDELETEREQUEST']._serialized_start=1062
  _globals['_STORAGEDELETEREQUEST']._serialized_end=1136
  _globals['_STORAGEDELETERESPONSE']._serialized_start=1138
  _globals['_STORAGEDELETERESPONSE']._serialized_end=1222
  _globals['_STORAGELISTOBJECTREQUEST']._serialized_start=1224
  _globals['_STORAGELISTOBJECTREQUEST']._serialized_end=1351
  _globals['_STORAGELISTOBJECTRESPONSE']._serialized_start=1353
  _globals['_STORAGELISTOBJECTRESPONSE']._serialized_end=1474
  _globals['_OBJECTCREATEREQUEST']._serialized_start=1476
  _globals['_OBJECTCREATEREQUEST']._serialized_end=1598
  _globals['_OBJECTCREATERESPONSE']._serialized_start=1600
  _globals['_OBJECTCREATERESPONSE']._serialized_end=1682
  _globals['_OBJECTLISTREQUEST']._serialized_start=1684
  _globals['_OBJECTLISTREQUEST']._serialized_end=1804
  _globals['_OBJECTLISTRESPONSE']._serialized_start=1806
  _globals['_OBJECTLISTRESPONSE']._serialized_end=1919
  _globals['_OBJECTGETREQUEST']._serialized_start=1921
  _globals['_OBJECTGETREQUEST']._serialized_end=2040
  _globals['_OBJECTGETRESPONSE']._serialized_start=2043
  _globals['_OBJECTGETRESPONSE']._serialized_end=2171
  _globals['_OBJECTDELETEREQUEST']._serialized_start=2173
  _globals['_OBJECTDELETEREQUEST']._serialized_end=2243
  _globals['_OBJECTDELETERESPONSE']._serialized_start=2245
  _globals['_OBJECTDELETERESPONSE']._serialized_end=2327
  _globals['_OBJECTSTORAGES3CREDENTIALS']._serialized_start=2330
  _globals['_OBJECTSTORAGES3CREDENTIALS']._serialized_end=2616
  _globals['_OBJECTSTORAGEAZURECREDENTIALS']._serialized_start=2619
  _globals['_OBJECTSTORAGEAZURECREDENTIALS']._serialized_end=2780
  _globals['_OBJECTSTORAGECREDENTIALS']._serialized_start=2782
  _globals['_OBJECTSTORAGECREDENTIALS']._serialized_end=2857
  _globals['_OBJECTSTORAGECREDENTIALSREQUEST']._serialized_start=2859
  _globals['_OBJECTSTORAGECREDENTIALSREQUEST']._serialized_end=2944
  _globals['_OBJECTSTORAGECREDENTIALSRESPONSE']._serialized_start=2947
  _globals['_OBJECTSTORAGECREDENTIALSRESPONSE']._serialized_end=3136
# @@protoc_insertion_point(module_scope)
