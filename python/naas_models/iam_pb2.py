# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iam.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tiam.proto\x12\x03iam\x1a\x0evalidate.proto\"=\n\tTokenData\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06scopes\x18\x02 \x03(\tB\n\n\x08_user_id\"\xc7\x03\n\x07Profile\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nfirst_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tlast_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07\x63ompany\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x11\n\x04role\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08timezone\x18\x06 \x01(\tH\x05\x88\x01\x01\x12 \n\x13profile_picture_url\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1e\n\x11user_presentation\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x19\n\x0ctargeted_use\x18\t \x01(\tH\x08\x88\x01\x01\x12\x1c\n\x0fproduct_updates\x18\n \x01(\x08H\t\x88\x01\x01\x12\x12\n\x05phone\x18\x0b \x01(\tH\n\x88\x01\x01\x42\n\n\x08_user_idB\r\n\x0b_first_nameB\x0c\n\n_last_nameB\n\n\x08_companyB\x07\n\x05_roleB\x0b\n\t_timezoneB\x16\n\x14_profile_picture_urlB\x14\n\x12_user_presentationB\x0f\n\r_targeted_useB\x12\n\x10_product_updatesB\x08\n\x06_phoneB,Z*github.com/jupyter-naas/naas-models/go/iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iam_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/jupyter-naas/naas-models/go/iam'
  _globals['_TOKENDATA']._serialized_start=34
  _globals['_TOKENDATA']._serialized_end=95
  _globals['_PROFILE']._serialized_start=98
  _globals['_PROFILE']._serialized_end=553
# @@protoc_insertion_point(module_scope)
