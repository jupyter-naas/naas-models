# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: errors.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65rrors.proto\x12\x06\x65rrors\x1a\x0evalidate.proto*\x95\x03\n\x05\x45rror\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\xc7\x01\x12\x17\n\x12IAM_USER_NOT_FOUND\x10\xc8\x01\x12\x18\n\x13WORKSPACE_NOT_FOUND\x10\xac\x02\x12\"\n\x1dWORKSPACE_USER_ALREADY_EXISTS\x10\xae\x02\x12\x1d\n\x18WORKSPACE_USER_NOT_FOUND\x10\xaf\x02\x12\"\n\x1dWORKSPACE_USER_ALREADY_ACTIVE\x10\xb0\x02\x12\x33\n.WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE\x10\xb1\x02\x12\x1f\n\x1aWORKSPACE_PLUGIN_NOT_FOUND\x10\xb2\x02\x12\x1d\n\x18WORKSPACE_INVITE_INVALID\x10\xb3\x02\x12\x32\n-WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE\x10\xb4\x02\x12\x1f\n\x1a\x43REDITS_USER_HAS_NO_PARENT\x10\x90\x03\x42/Z-github.com/jupyter-naas/naas-models/go/errorsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/jupyter-naas/naas-models/go/errors'
  _globals['_ERROR']._serialized_start=41
  _globals['_ERROR']._serialized_end=446
# @@protoc_insertion_point(module_scope)