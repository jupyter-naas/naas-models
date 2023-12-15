# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eworkflow.proto\x12\x08workflow\x1a\x0evalidate.proto\"a\n\x07\x41rchive\x12)\n\x04none\x18\x01 \x03(\x0b\x32\x1b.workflow.Archive.NoneEntry\x1a+\n\tNoneEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\nArtifactS3\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x62ucket\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_keyB\t\n\x07_bucket\"\xdd\x01\n\x08\x41rtifact\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04path\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04mode\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x11\n\x04\x66rom\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\'\n\x07\x61rchive\x18\x05 \x01(\x0b\x32\x11.workflow.ArchiveH\x04\x88\x01\x01\x12%\n\x02s3\x18\x06 \x01(\x0b\x32\x14.workflow.ArtifactS3H\x05\x88\x01\x01\x42\x07\n\x05_nameB\x07\n\x05_pathB\x07\n\x05_modeB\x07\n\x05_fromB\n\n\x08_archiveB\x05\n\x03_s3\"X\n\x06Inputs\x12\'\n\nparameters\x18\x01 \x03(\x0b\x32\x13.workflow.Parameter\x12%\n\tartifacts\x18\x02 \x03(\x0b\x32\x12.workflow.Artifact\"Y\n\x07Outputs\x12\'\n\nparameters\x18\x01 \x03(\x0b\x32\x13.workflow.Parameter\x12%\n\tartifacts\x18\x02 \x03(\x0b\x32\x12.workflow.Artifact\"g\n\tParameter\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05value\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_valueB\n\n\x08_default\"\xe0\x01\n\tArguments\x12\x37\n\nparameters\x18\x01 \x03(\x0b\x32#.workflow.Arguments.ParametersEntry\x12\x35\n\tartifacts\x18\x02 \x03(\x0b\x32\".workflow.Arguments.ArtifactsEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x0e\x41rtifactsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x08\x44\x61gTasks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08template\x18\x02 \x01(\t\x12\x14\n\x07\x64\x65pends\x18\x03 \x01(\tH\x00\x88\x01\x01\x12+\n\targuments\x18\x04 \x01(\x0b\x32\x13.workflow.ArgumentsH\x01\x88\x01\x01\x42\n\n\x08_dependsB\x0c\n\n_arguments\"P\n\x0b\x44\x61gTemplate\x12!\n\x05tasks\x18\x01 \x03(\x0b\x32\x12.workflow.DagTasks\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_target\"0\n\x0eScriptTemplate\x12\x13\n\x06source\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_source\"\x9e\x02\n\x08Template\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tcontainer\x18\x02 \x01(\tH\x01\x88\x01\x01\x12%\n\x06inputs\x18\x03 \x01(\x0b\x32\x10.workflow.InputsH\x02\x88\x01\x01\x12\'\n\x07outputs\x18\x04 \x01(\x0b\x32\x11.workflow.OutputsH\x03\x88\x01\x01\x12\'\n\x03\x64\x61g\x18\x05 \x01(\x0b\x32\x15.workflow.DagTemplateH\x04\x88\x01\x01\x12-\n\x06script\x18\x06 \x01(\x0b\x32\x18.workflow.ScriptTemplateH\x05\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_containerB\t\n\x07_inputsB\n\n\x08_outputsB\x06\n\x04_dagB\t\n\x07_script\"|\n\x04Spec\x12\x12\n\nentrypoint\x18\x01 \x01(\t\x12+\n\targuments\x18\x02 \x01(\x0b\x32\x13.workflow.ArgumentsH\x00\x88\x01\x01\x12%\n\ttemplates\x18\x03 \x03(\x0b\x32\x12.workflow.TemplateB\x0c\n\n_arguments\"\xbb\x01\n\x17WorkflowCreationRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10workflowTemplate\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cworkflowSpec\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_namespaceB\x13\n\x11_workflowTemplateB\x0f\n\r_workflowSpec\"X\n\x18WorkflowCreationResponse\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"\xb9\x01\n\x15WorkflowUpdateRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10workflowTemplate\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cworkflowSpec\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_namespaceB\x13\n\x11_workflowTemplateB\x0f\n\r_workflowSpec\"V\n\x16WorkflowUpdateResponse\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"Y\n\x15WorkflowDeleteRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_namespace\"V\n\x16WorkflowDeleteResponse\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"V\n\x12WorkflowGetRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_namespace\"S\n\x13WorkflowGetResponse\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"\x15\n\x13WorkflowListRequest\"H\n\x14WorkflowListResponse\x12\x30\n\tworkflows\x18\x01 \x03(\x0b\x32\x1d.workflow.WorkflowGetResponse\"U\n\x15WorkflowCreationError\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"S\n\x13WorkflowUpdateError\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"S\n\x13WorkflowDeleteError\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"P\n\x10WorkflowGetError\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_message\"Q\n\x11WorkflowListError\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_messageB1Z/github.com/jupyter-naas/naas-models/go/workflowb\x06proto3')



_ARCHIVE = DESCRIPTOR.message_types_by_name['Archive']
_ARCHIVE_NONEENTRY = _ARCHIVE.nested_types_by_name['NoneEntry']
_ARTIFACTS3 = DESCRIPTOR.message_types_by_name['ArtifactS3']
_ARTIFACT = DESCRIPTOR.message_types_by_name['Artifact']
_INPUTS = DESCRIPTOR.message_types_by_name['Inputs']
_OUTPUTS = DESCRIPTOR.message_types_by_name['Outputs']
_PARAMETER = DESCRIPTOR.message_types_by_name['Parameter']
_ARGUMENTS = DESCRIPTOR.message_types_by_name['Arguments']
_ARGUMENTS_PARAMETERSENTRY = _ARGUMENTS.nested_types_by_name['ParametersEntry']
_ARGUMENTS_ARTIFACTSENTRY = _ARGUMENTS.nested_types_by_name['ArtifactsEntry']
_DAGTASKS = DESCRIPTOR.message_types_by_name['DagTasks']
_DAGTEMPLATE = DESCRIPTOR.message_types_by_name['DagTemplate']
_SCRIPTTEMPLATE = DESCRIPTOR.message_types_by_name['ScriptTemplate']
_TEMPLATE = DESCRIPTOR.message_types_by_name['Template']
_SPEC = DESCRIPTOR.message_types_by_name['Spec']
_WORKFLOWCREATIONREQUEST = DESCRIPTOR.message_types_by_name['WorkflowCreationRequest']
_WORKFLOWCREATIONRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowCreationResponse']
_WORKFLOWUPDATEREQUEST = DESCRIPTOR.message_types_by_name['WorkflowUpdateRequest']
_WORKFLOWUPDATERESPONSE = DESCRIPTOR.message_types_by_name['WorkflowUpdateResponse']
_WORKFLOWDELETEREQUEST = DESCRIPTOR.message_types_by_name['WorkflowDeleteRequest']
_WORKFLOWDELETERESPONSE = DESCRIPTOR.message_types_by_name['WorkflowDeleteResponse']
_WORKFLOWGETREQUEST = DESCRIPTOR.message_types_by_name['WorkflowGetRequest']
_WORKFLOWGETRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowGetResponse']
_WORKFLOWLISTREQUEST = DESCRIPTOR.message_types_by_name['WorkflowListRequest']
_WORKFLOWLISTRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowListResponse']
_WORKFLOWCREATIONERROR = DESCRIPTOR.message_types_by_name['WorkflowCreationError']
_WORKFLOWUPDATEERROR = DESCRIPTOR.message_types_by_name['WorkflowUpdateError']
_WORKFLOWDELETEERROR = DESCRIPTOR.message_types_by_name['WorkflowDeleteError']
_WORKFLOWGETERROR = DESCRIPTOR.message_types_by_name['WorkflowGetError']
_WORKFLOWLISTERROR = DESCRIPTOR.message_types_by_name['WorkflowListError']
Archive = _reflection.GeneratedProtocolMessageType('Archive', (_message.Message,), {

  'NoneEntry' : _reflection.GeneratedProtocolMessageType('NoneEntry', (_message.Message,), {
    'DESCRIPTOR' : _ARCHIVE_NONEENTRY,
    '__module__' : 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.Archive.NoneEntry)
    })
  ,
  'DESCRIPTOR' : _ARCHIVE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Archive)
  })
_sym_db.RegisterMessage(Archive)
_sym_db.RegisterMessage(Archive.NoneEntry)

ArtifactS3 = _reflection.GeneratedProtocolMessageType('ArtifactS3', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACTS3,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.ArtifactS3)
  })
_sym_db.RegisterMessage(ArtifactS3)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Artifact)
  })
_sym_db.RegisterMessage(Artifact)

Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
  'DESCRIPTOR' : _INPUTS,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Inputs)
  })
_sym_db.RegisterMessage(Inputs)

Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTS,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Outputs)
  })
_sym_db.RegisterMessage(Outputs)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETER,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Parameter)
  })
_sym_db.RegisterMessage(Parameter)

Arguments = _reflection.GeneratedProtocolMessageType('Arguments', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _ARGUMENTS_PARAMETERSENTRY,
    '__module__' : 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.Arguments.ParametersEntry)
    })
  ,

  'ArtifactsEntry' : _reflection.GeneratedProtocolMessageType('ArtifactsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ARGUMENTS_ARTIFACTSENTRY,
    '__module__' : 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.Arguments.ArtifactsEntry)
    })
  ,
  'DESCRIPTOR' : _ARGUMENTS,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Arguments)
  })
_sym_db.RegisterMessage(Arguments)
_sym_db.RegisterMessage(Arguments.ParametersEntry)
_sym_db.RegisterMessage(Arguments.ArtifactsEntry)

DagTasks = _reflection.GeneratedProtocolMessageType('DagTasks', (_message.Message,), {
  'DESCRIPTOR' : _DAGTASKS,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.DagTasks)
  })
_sym_db.RegisterMessage(DagTasks)

DagTemplate = _reflection.GeneratedProtocolMessageType('DagTemplate', (_message.Message,), {
  'DESCRIPTOR' : _DAGTEMPLATE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.DagTemplate)
  })
_sym_db.RegisterMessage(DagTemplate)

ScriptTemplate = _reflection.GeneratedProtocolMessageType('ScriptTemplate', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTTEMPLATE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.ScriptTemplate)
  })
_sym_db.RegisterMessage(ScriptTemplate)

Template = _reflection.GeneratedProtocolMessageType('Template', (_message.Message,), {
  'DESCRIPTOR' : _TEMPLATE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Template)
  })
_sym_db.RegisterMessage(Template)

Spec = _reflection.GeneratedProtocolMessageType('Spec', (_message.Message,), {
  'DESCRIPTOR' : _SPEC,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Spec)
  })
_sym_db.RegisterMessage(Spec)

WorkflowCreationRequest = _reflection.GeneratedProtocolMessageType('WorkflowCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWCREATIONREQUEST,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowCreationRequest)
  })
_sym_db.RegisterMessage(WorkflowCreationRequest)

WorkflowCreationResponse = _reflection.GeneratedProtocolMessageType('WorkflowCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWCREATIONRESPONSE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowCreationResponse)
  })
_sym_db.RegisterMessage(WorkflowCreationResponse)

WorkflowUpdateRequest = _reflection.GeneratedProtocolMessageType('WorkflowUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWUPDATEREQUEST,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowUpdateRequest)
  })
_sym_db.RegisterMessage(WorkflowUpdateRequest)

WorkflowUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkflowUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWUPDATERESPONSE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowUpdateResponse)
  })
_sym_db.RegisterMessage(WorkflowUpdateResponse)

WorkflowDeleteRequest = _reflection.GeneratedProtocolMessageType('WorkflowDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWDELETEREQUEST,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowDeleteRequest)
  })
_sym_db.RegisterMessage(WorkflowDeleteRequest)

WorkflowDeleteResponse = _reflection.GeneratedProtocolMessageType('WorkflowDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWDELETERESPONSE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowDeleteResponse)
  })
_sym_db.RegisterMessage(WorkflowDeleteResponse)

WorkflowGetRequest = _reflection.GeneratedProtocolMessageType('WorkflowGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWGETREQUEST,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowGetRequest)
  })
_sym_db.RegisterMessage(WorkflowGetRequest)

WorkflowGetResponse = _reflection.GeneratedProtocolMessageType('WorkflowGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWGETRESPONSE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowGetResponse)
  })
_sym_db.RegisterMessage(WorkflowGetResponse)

WorkflowListRequest = _reflection.GeneratedProtocolMessageType('WorkflowListRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWLISTREQUEST,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowListRequest)
  })
_sym_db.RegisterMessage(WorkflowListRequest)

WorkflowListResponse = _reflection.GeneratedProtocolMessageType('WorkflowListResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWLISTRESPONSE,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowListResponse)
  })
_sym_db.RegisterMessage(WorkflowListResponse)

WorkflowCreationError = _reflection.GeneratedProtocolMessageType('WorkflowCreationError', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWCREATIONERROR,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowCreationError)
  })
_sym_db.RegisterMessage(WorkflowCreationError)

WorkflowUpdateError = _reflection.GeneratedProtocolMessageType('WorkflowUpdateError', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWUPDATEERROR,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowUpdateError)
  })
_sym_db.RegisterMessage(WorkflowUpdateError)

WorkflowDeleteError = _reflection.GeneratedProtocolMessageType('WorkflowDeleteError', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWDELETEERROR,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowDeleteError)
  })
_sym_db.RegisterMessage(WorkflowDeleteError)

WorkflowGetError = _reflection.GeneratedProtocolMessageType('WorkflowGetError', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWGETERROR,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowGetError)
  })
_sym_db.RegisterMessage(WorkflowGetError)

WorkflowListError = _reflection.GeneratedProtocolMessageType('WorkflowListError', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWLISTERROR,
  '__module__' : 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowListError)
  })
_sym_db.RegisterMessage(WorkflowListError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/jupyter-naas/naas-models/go/workflow'
  _ARCHIVE_NONEENTRY._options = None
  _ARCHIVE_NONEENTRY._serialized_options = b'8\001'
  _ARGUMENTS_PARAMETERSENTRY._options = None
  _ARGUMENTS_PARAMETERSENTRY._serialized_options = b'8\001'
  _ARGUMENTS_ARTIFACTSENTRY._options = None
  _ARGUMENTS_ARTIFACTSENTRY._serialized_options = b'8\001'
  _ARCHIVE._serialized_start=44
  _ARCHIVE._serialized_end=141
  _ARCHIVE_NONEENTRY._serialized_start=98
  _ARCHIVE_NONEENTRY._serialized_end=141
  _ARTIFACTS3._serialized_start=143
  _ARTIFACTS3._serialized_end=213
  _ARTIFACT._serialized_start=216
  _ARTIFACT._serialized_end=437
  _INPUTS._serialized_start=439
  _INPUTS._serialized_end=527
  _OUTPUTS._serialized_start=529
  _OUTPUTS._serialized_end=618
  _PARAMETER._serialized_start=620
  _PARAMETER._serialized_end=723
  _ARGUMENTS._serialized_start=726
  _ARGUMENTS._serialized_end=950
  _ARGUMENTS_PARAMETERSENTRY._serialized_start=851
  _ARGUMENTS_PARAMETERSENTRY._serialized_end=900
  _ARGUMENTS_ARTIFACTSENTRY._serialized_start=902
  _ARGUMENTS_ARTIFACTSENTRY._serialized_end=950
  _DAGTASKS._serialized_start=953
  _DAGTASKS._serialized_end=1088
  _DAGTEMPLATE._serialized_start=1090
  _DAGTEMPLATE._serialized_end=1170
  _SCRIPTTEMPLATE._serialized_start=1172
  _SCRIPTTEMPLATE._serialized_end=1220
  _TEMPLATE._serialized_start=1223
  _TEMPLATE._serialized_end=1509
  _SPEC._serialized_start=1511
  _SPEC._serialized_end=1635
  _WORKFLOWCREATIONREQUEST._serialized_start=1638
  _WORKFLOWCREATIONREQUEST._serialized_end=1825
  _WORKFLOWCREATIONRESPONSE._serialized_start=1827
  _WORKFLOWCREATIONRESPONSE._serialized_end=1915
  _WORKFLOWUPDATEREQUEST._serialized_start=1918
  _WORKFLOWUPDATEREQUEST._serialized_end=2103
  _WORKFLOWUPDATERESPONSE._serialized_start=2105
  _WORKFLOWUPDATERESPONSE._serialized_end=2191
  _WORKFLOWDELETEREQUEST._serialized_start=2193
  _WORKFLOWDELETEREQUEST._serialized_end=2282
  _WORKFLOWDELETERESPONSE._serialized_start=2284
  _WORKFLOWDELETERESPONSE._serialized_end=2370
  _WORKFLOWGETREQUEST._serialized_start=2372
  _WORKFLOWGETREQUEST._serialized_end=2458
  _WORKFLOWGETRESPONSE._serialized_start=2460
  _WORKFLOWGETRESPONSE._serialized_end=2543
  _WORKFLOWLISTREQUEST._serialized_start=2545
  _WORKFLOWLISTREQUEST._serialized_end=2566
  _WORKFLOWLISTRESPONSE._serialized_start=2568
  _WORKFLOWLISTRESPONSE._serialized_end=2640
  _WORKFLOWCREATIONERROR._serialized_start=2642
  _WORKFLOWCREATIONERROR._serialized_end=2727
  _WORKFLOWUPDATEERROR._serialized_start=2729
  _WORKFLOWUPDATEERROR._serialized_end=2812
  _WORKFLOWDELETEERROR._serialized_start=2814
  _WORKFLOWDELETEERROR._serialized_end=2897
  _WORKFLOWGETERROR._serialized_start=2899
  _WORKFLOWGETERROR._serialized_end=2979
  _WORKFLOWLISTERROR._serialized_start=2981
  _WORKFLOWLISTERROR._serialized_end=3062
# @@protoc_insertion_point(module_scope)
