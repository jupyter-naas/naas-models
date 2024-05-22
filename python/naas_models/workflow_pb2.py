# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflow.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eworkflow.proto\x12\x08workflow\x1a\x0evalidate.proto\"n\n\x15WorkflowResponseError\x12*\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.workflow.WorkflowErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_codeB\n\n\x08_message\"a\n\x07\x41rchive\x12)\n\x04none\x18\x01 \x03(\x0b\x32\x1b.workflow.Archive.NoneEntry\x1a+\n\tNoneEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\nArtifactS3\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x62ucket\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_keyB\t\n\x07_bucket\"\xdd\x01\n\x08\x41rtifact\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04path\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04mode\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x11\n\x04\x66rom\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\'\n\x07\x61rchive\x18\x05 \x01(\x0b\x32\x11.workflow.ArchiveH\x04\x88\x01\x01\x12%\n\x02s3\x18\x06 \x01(\x0b\x32\x14.workflow.ArtifactS3H\x05\x88\x01\x01\x42\x07\n\x05_nameB\x07\n\x05_pathB\x07\n\x05_modeB\x07\n\x05_fromB\n\n\x08_archiveB\x05\n\x03_s3\"X\n\x06Inputs\x12\'\n\nparameters\x18\x01 \x03(\x0b\x32\x13.workflow.Parameter\x12%\n\tartifacts\x18\x02 \x03(\x0b\x32\x12.workflow.Artifact\"Y\n\x07Outputs\x12\'\n\nparameters\x18\x01 \x03(\x0b\x32\x13.workflow.Parameter\x12%\n\tartifacts\x18\x02 \x03(\x0b\x32\x12.workflow.Artifact\"g\n\tParameter\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05value\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_valueB\n\n\x08_default\"[\n\tArguments\x12\'\n\nparameters\x18\x01 \x03(\x0b\x32\x13.workflow.Parameter\x12%\n\tartifacts\x18\x02 \x03(\x0b\x32\x12.workflow.Artifact\"\x87\x01\n\x08\x44\x61gTasks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08template\x18\x02 \x01(\t\x12\x14\n\x07\x64\x65pends\x18\x03 \x01(\tH\x00\x88\x01\x01\x12+\n\targuments\x18\x04 \x01(\x0b\x32\x13.workflow.ArgumentsH\x01\x88\x01\x01\x42\n\n\x08_dependsB\x0c\n\n_arguments\"P\n\x0b\x44\x61gTemplate\x12!\n\x05tasks\x18\x01 \x03(\x0b\x32\x12.workflow.DagTasks\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_target\"\xcd\x01\n\x0eScriptTemplate\x12\x12\n\x05image\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07\x63ommand\x18\x02 \x03(\t\x12:\n\tresources\x18\x03 \x03(\x0b\x32\'.workflow.ScriptTemplate.ResourcesEntry\x12\x13\n\x06source\x18\x04 \x01(\tH\x01\x88\x01\x01\x1a\x30\n\x0eResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06_imageB\t\n\x07_source\"O\n\x11\x43ontainerTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x03 \x03(\t\x12\x0c\n\x04\x61rgs\x18\x04 \x03(\t\"\xda\x03\n\x08Template\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x06inputs\x18\x02 \x01(\x0b\x32\x10.workflow.InputsH\x00\x88\x01\x01\x12\'\n\x07outputs\x18\x03 \x01(\x0b\x32\x11.workflow.OutputsH\x01\x88\x01\x01\x12\'\n\x03\x64\x61g\x18\x04 \x01(\x0b\x32\x15.workflow.DagTemplateH\x02\x88\x01\x01\x12-\n\x06script\x18\x05 \x01(\x0b\x32\x18.workflow.ScriptTemplateH\x03\x88\x01\x01\x12\x18\n\x0bttlStrategy\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x33\n\tcontainer\x18\x07 \x01(\x0b\x32\x1b.workflow.ContainerTemplateH\x05\x88\x01\x01\x12\x12\n\x05podGC\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x32\n\x08metadata\x18\t \x03(\x0b\x32 .workflow.Template.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07_inputsB\n\n\x08_outputsB\x06\n\x04_dagB\t\n\x07_scriptB\x0e\n\x0c_ttlStrategyB\x0c\n\n_containerB\x08\n\x06_podGC\"\x90\x01\n\x04Spec\x12+\n\targuments\x18\x01 \x01(\x0b\x32\x13.workflow.ArgumentsH\x00\x88\x01\x01\x12\x17\n\nentrypoint\x18\x02 \x01(\tH\x01\x88\x01\x01\x12%\n\ttemplates\x18\x03 \x03(\x0b\x32\x12.workflow.TemplateB\x0c\n\n_argumentsB\r\n\x0b_entrypoint\"\xd7\x01\n\x08Metadata\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cgenerateName\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tnamespace\x18\x03 \x01(\tH\x02\x88\x01\x01\x12.\n\x06labels\x18\x04 \x03(\x0b\x32\x1e.workflow.Metadata.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_nameB\x0f\n\r_generateNameB\x0c\n\n_namespace\"\xde\x01\n\x0eWorkflowStatus\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05phase\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tstartedAt\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nfinishedAt\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08progress\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07outputs\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_phaseB\x0c\n\n_startedAtB\r\n\x0b_finishedAtB\x0b\n\t_progressB\n\n\x08_outputs\"N\n\x08Workflow\x12$\n\x08metadata\x18\x01 \x01(\x0b\x32\x12.workflow.Metadata\x12\x1c\n\x04spec\x18\x02 \x01(\x0b\x32\x0e.workflow.Spec\"\xf6\x02\n\x08\x43ronSpec\x12\x10\n\x08schedule\x18\x01 \x01(\t\x12\x10\n\x08timezone\x18\x02 \x01(\t\x12$\n\x17startingDeadlineSeconds\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11\x63oncurrencyPolicy\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\'\n\x1asuccessfulJobsHistoryLimit\x18\x05 \x01(\tH\x02\x88\x01\x01\x12#\n\x16\x66\x61iledJobsHistoryLimit\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07suspend\x18\x07 \x01(\tH\x04\x88\x01\x01\x12$\n\x0cworkflowSpec\x18\x08 \x01(\x0b\x32\x0e.workflow.SpecB\x1a\n\x18_startingDeadlineSecondsB\x14\n\x12_concurrencyPolicyB\x1d\n\x1b_successfulJobsHistoryLimitB\x19\n\x17_failedJobsHistoryLimitB\n\n\x08_suspend\"V\n\x0c\x43ronWorkflow\x12$\n\x08metadata\x18\x01 \x01(\x0b\x32\x12.workflow.Metadata\x12 \n\x04spec\x18\x02 \x01(\x0b\x32\x12.workflow.CronSpec\"\xb5\x02\n\x17WorkflowCreationRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x08user_uid\x18\x03 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x02\x88\x01\x01\x12\x16\n\tnamespace\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0cserverDryRun\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x12\n\x05token\x18\x06 \x01(\tH\x05\x88\x01\x01\x12)\n\x08workflow\x18\x07 \x01(\x0b\x32\x12.workflow.WorkflowH\x06\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x0b\n\t_user_uidB\x0c\n\n_namespaceB\x0f\n\r_serverDryRunB\x08\n\x06_tokenB\x0b\n\t_workflow\"\x8f\x01\n\x18WorkflowCreationResponse\x12/\n\x08workflow\x18\x01 \x01(\x0b\x32\x18.workflow.WorkflowStatusH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x17.workflow.WorkflowErrorH\x01\x88\x01\x01\x42\x0b\n\t_workflowB\x08\n\x06_error\"{\n\x15WorkflowDeleteRequest\x12#\n\x0cworkspace_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x1a\n\rworkflow_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0f\n\r_workspace_idB\x10\n\x0e_workflow_name\"\x8d\x01\n\x16WorkflowDeleteResponse\x12/\n\x08workflow\x18\x01 \x01(\x0b\x32\x18.workflow.WorkflowStatusH\x00\x88\x01\x01\x12+\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x17.workflow.WorkflowErrorH\x01\x88\x01\x01\x42\x0b\n\t_workflowB\x08\n\x06_error\"x\n\x12WorkflowGetRequest\x12#\n\x0cworkspace_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x12\x1a\n\rworkflow_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0f\n\r_workspace_idB\x10\n\x0e_workflow_name\"\x92\x01\n\x13WorkflowGetResponse\x12/\n\x08workflow\x18\x01 \x01(\x0b\x32\x18.workflow.WorkflowStatusH\x00\x88\x01\x01\x12\x33\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1f.workflow.WorkflowResponseErrorH\x01\x88\x01\x01\x42\x0b\n\t_workflowB\x08\n\x06_error\"K\n\x13WorkflowListRequest\x12#\n\x0cworkspace_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x00\x88\x01\x01\x42\x0f\n\r_workspace_id\"\x82\x01\n\x14WorkflowListResponse\x12+\n\tworkflows\x18\x01 \x03(\x0b\x32\x18.workflow.WorkflowStatus\x12\x33\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1f.workflow.WorkflowResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error*B\n\rWorkflowError\x12\x15\n\x11WORKFLOW_NO_ERROR\x10\x00\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\xe8\x07\x42\x31Z/github.com/jupyter-naas/naas-models/go/workflowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workflow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/github.com/jupyter-naas/naas-models/go/workflow'
  _globals['_ARCHIVE_NONEENTRY']._loaded_options = None
  _globals['_ARCHIVE_NONEENTRY']._serialized_options = b'8\001'
  _globals['_SCRIPTTEMPLATE_RESOURCESENTRY']._loaded_options = None
  _globals['_SCRIPTTEMPLATE_RESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_TEMPLATE_METADATAENTRY']._loaded_options = None
  _globals['_TEMPLATE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_METADATA_LABELSENTRY']._loaded_options = None
  _globals['_METADATA_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_WORKFLOWCREATIONREQUEST'].fields_by_name['user_uid']._loaded_options = None
  _globals['_WORKFLOWCREATIONREQUEST'].fields_by_name['user_uid']._serialized_options = b'\372B\005r\003\260\001\001'
  _globals['_WORKFLOWDELETEREQUEST'].fields_by_name['workspace_id']._loaded_options = None
  _globals['_WORKFLOWDELETEREQUEST'].fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _globals['_WORKFLOWGETREQUEST'].fields_by_name['workspace_id']._loaded_options = None
  _globals['_WORKFLOWGETREQUEST'].fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _globals['_WORKFLOWLISTREQUEST'].fields_by_name['workspace_id']._loaded_options = None
  _globals['_WORKFLOWLISTREQUEST'].fields_by_name['workspace_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _globals['_WORKFLOWERROR']._serialized_start=4259
  _globals['_WORKFLOWERROR']._serialized_end=4325
  _globals['_WORKFLOWRESPONSEERROR']._serialized_start=44
  _globals['_WORKFLOWRESPONSEERROR']._serialized_end=154
  _globals['_ARCHIVE']._serialized_start=156
  _globals['_ARCHIVE']._serialized_end=253
  _globals['_ARCHIVE_NONEENTRY']._serialized_start=210
  _globals['_ARCHIVE_NONEENTRY']._serialized_end=253
  _globals['_ARTIFACTS3']._serialized_start=255
  _globals['_ARTIFACTS3']._serialized_end=325
  _globals['_ARTIFACT']._serialized_start=328
  _globals['_ARTIFACT']._serialized_end=549
  _globals['_INPUTS']._serialized_start=551
  _globals['_INPUTS']._serialized_end=639
  _globals['_OUTPUTS']._serialized_start=641
  _globals['_OUTPUTS']._serialized_end=730
  _globals['_PARAMETER']._serialized_start=732
  _globals['_PARAMETER']._serialized_end=835
  _globals['_ARGUMENTS']._serialized_start=837
  _globals['_ARGUMENTS']._serialized_end=928
  _globals['_DAGTASKS']._serialized_start=931
  _globals['_DAGTASKS']._serialized_end=1066
  _globals['_DAGTEMPLATE']._serialized_start=1068
  _globals['_DAGTEMPLATE']._serialized_end=1148
  _globals['_SCRIPTTEMPLATE']._serialized_start=1151
  _globals['_SCRIPTTEMPLATE']._serialized_end=1356
  _globals['_SCRIPTTEMPLATE_RESOURCESENTRY']._serialized_start=1287
  _globals['_SCRIPTTEMPLATE_RESOURCESENTRY']._serialized_end=1335
  _globals['_CONTAINERTEMPLATE']._serialized_start=1358
  _globals['_CONTAINERTEMPLATE']._serialized_end=1437
  _globals['_TEMPLATE']._serialized_start=1440
  _globals['_TEMPLATE']._serialized_end=1914
  _globals['_TEMPLATE_METADATAENTRY']._serialized_start=1785
  _globals['_TEMPLATE_METADATAENTRY']._serialized_end=1832
  _globals['_SPEC']._serialized_start=1917
  _globals['_SPEC']._serialized_end=2061
  _globals['_METADATA']._serialized_start=2064
  _globals['_METADATA']._serialized_end=2279
  _globals['_METADATA_LABELSENTRY']._serialized_start=2194
  _globals['_METADATA_LABELSENTRY']._serialized_end=2239
  _globals['_WORKFLOWSTATUS']._serialized_start=2282
  _globals['_WORKFLOWSTATUS']._serialized_end=2504
  _globals['_WORKFLOW']._serialized_start=2506
  _globals['_WORKFLOW']._serialized_end=2584
  _globals['_CRONSPEC']._serialized_start=2587
  _globals['_CRONSPEC']._serialized_end=2961
  _globals['_CRONWORKFLOW']._serialized_start=2963
  _globals['_CRONWORKFLOW']._serialized_end=3049
  _globals['_WORKFLOWCREATIONREQUEST']._serialized_start=3052
  _globals['_WORKFLOWCREATIONREQUEST']._serialized_end=3361
  _globals['_WORKFLOWCREATIONRESPONSE']._serialized_start=3364
  _globals['_WORKFLOWCREATIONRESPONSE']._serialized_end=3507
  _globals['_WORKFLOWDELETEREQUEST']._serialized_start=3509
  _globals['_WORKFLOWDELETEREQUEST']._serialized_end=3632
  _globals['_WORKFLOWDELETERESPONSE']._serialized_start=3635
  _globals['_WORKFLOWDELETERESPONSE']._serialized_end=3776
  _globals['_WORKFLOWGETREQUEST']._serialized_start=3778
  _globals['_WORKFLOWGETREQUEST']._serialized_end=3898
  _globals['_WORKFLOWGETRESPONSE']._serialized_start=3901
  _globals['_WORKFLOWGETRESPONSE']._serialized_end=4047
  _globals['_WORKFLOWLISTREQUEST']._serialized_start=4049
  _globals['_WORKFLOWLISTREQUEST']._serialized_end=4124
  _globals['_WORKFLOWLISTRESPONSE']._serialized_start=4127
  _globals['_WORKFLOWLISTRESPONSE']._serialized_end=4257
# @@protoc_insertion_point(module_scope)
