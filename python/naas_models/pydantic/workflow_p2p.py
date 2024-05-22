# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
import typing

class WorkflowError(IntEnum):
    WORKFLOW_NO_ERROR = 0
    INTERNAL_SERVER_ERROR = 1000

class WorkflowResponseError(BaseModel):
    code: typing.Optional[WorkflowError] = Field(default=0) 
    message: typing.Optional[str] = Field(default="") 

class Archive(BaseModel):
    none: typing.Dict[str, str] = Field(default_factory=dict) 

class ArtifactS3(BaseModel):
    key: typing.Optional[str] = Field(default="") 
    bucket: typing.Optional[str] = Field(default="") 

class Artifact(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    path: typing.Optional[str] = Field(default="") 
    mode: typing.Optional[int] = Field(default=0) 
    archive: typing.Optional[Archive] = Field(default=None) 
    s3: typing.Optional[ArtifactS3] = Field(default=None) 

class Parameter(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    value: typing.Optional[str] = Field(default="") 
    default: typing.Optional[str] = Field(default="") 

class Inputs(BaseModel):
    parameters: typing.List[Parameter] = Field(default_factory=list) 
    artifacts: typing.List[Artifact] = Field(default_factory=list) 

class Outputs(BaseModel):
    parameters: typing.List[Parameter] = Field(default_factory=list) 
    artifacts: typing.List[Artifact] = Field(default_factory=list) 

class Arguments(BaseModel):
    parameters: typing.List[Parameter] = Field(default_factory=list) 
    artifacts: typing.List[Artifact] = Field(default_factory=list) 

class DagTasks(BaseModel):
    name: str = Field(default="") 
    template: str = Field(default="") 
    depends: typing.Optional[str] = Field(default="") 
    arguments: typing.Optional[Arguments] = Field(default=None) 

class DagTemplate(BaseModel):
    tasks: typing.List[DagTasks] = Field(default_factory=list) 
    target: typing.Optional[str] = Field(default="") 

class ScriptTemplate(BaseModel):
    image: typing.Optional[str] = Field(default="") 
    command: typing.List[str] = Field(default_factory=list) 
    resources: typing.Dict[str, str] = Field(default_factory=dict) 
    source: typing.Optional[str] = Field(default="") 

class ContainerTemplate(BaseModel):
    name: str = Field(default="") 
    image: str = Field(default="") 
    command: typing.List[str] = Field(default_factory=list) 
    args: typing.List[str] = Field(default_factory=list) 

class Template(BaseModel):
    name: str = Field(default="") 
    inputs: typing.Optional[Inputs] = Field(default=None) 
    outputs: typing.Optional[Outputs] = Field(default=None) 
    dag: typing.Optional[DagTemplate] = Field(default=None) 
    script: typing.Optional[ScriptTemplate] = Field(default=None) 
    ttlStrategy: typing.Optional[str] = Field(default="") 
    container: typing.Optional[ContainerTemplate] = Field(default=None) 
    podGC: typing.Optional[str] = Field(default="") 
    metadata: typing.Dict[str, str] = Field(default_factory=dict) 

class Spec(BaseModel):
    arguments: typing.Optional[Arguments] = Field(default=None) 
    entrypoint: typing.Optional[str] = Field(default="") 
    templates: typing.List[Template] = Field(default_factory=list) 

class Metadata(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    generateName: typing.Optional[str] = Field(default="") 
    namespace: typing.Optional[str] = Field(default="") 
    labels: typing.Dict[str, str] = Field(default_factory=dict) 

class WorkflowStatus(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    phase: typing.Optional[str] = Field(default="") 
    startedAt: typing.Optional[str] = Field(default="") 
    finishedAt: typing.Optional[str] = Field(default="") 
    progress: typing.Optional[str] = Field(default="") 
    outputs: typing.Optional[str] = Field(default="") 

class Workflow(BaseModel):
    metadata: Metadata = Field() 
    spec: Spec = Field() 

class CronSpec(BaseModel):
    schedule: str = Field(default="") 
    timezone: str = Field(default="") 
    startingDeadlineSeconds: typing.Optional[str] = Field(default="") 
    concurrencyPolicy: typing.Optional[str] = Field(default="") 
    successfulJobsHistoryLimit: typing.Optional[str] = Field(default="") 
    failedJobsHistoryLimit: typing.Optional[str] = Field(default="") 
    suspend: typing.Optional[str] = Field(default="") 
    workflowSpec: Spec = Field() 

class CronWorkflow(BaseModel):
    metadata: Metadata = Field() 
    spec: CronSpec = Field() 

class WorkflowCreationRequest(BaseModel):
    name: typing.Optional[str] = Field(default="") 
    description: typing.Optional[str] = Field(default="") 
    user_uid: typing.Optional[UUID] = Field(default="") 
    namespace: typing.Optional[str] = Field(default="") 
    serverDryRun: typing.Optional[bool] = Field(default=False) 
    token: typing.Optional[str] = Field(default="") 
    workflow: typing.Optional[Workflow] = Field(default=None) 

class WorkflowCreationResponse(BaseModel):
    workflow: typing.Optional[WorkflowStatus] = Field(default=None) 
    error: typing.Optional[WorkflowError] = Field(default=0) 

class WorkflowDeleteRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workflow_name: typing.Optional[str] = Field(default="") 

class WorkflowDeleteResponse(BaseModel):
    workflow: typing.Optional[WorkflowStatus] = Field(default=None) 
    error: typing.Optional[WorkflowError] = Field(default=0) 

class WorkflowGetRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 
    workflow_name: typing.Optional[str] = Field(default="") 

class WorkflowGetResponse(BaseModel):
    workflow: typing.Optional[WorkflowStatus] = Field(default=None) 
    error: typing.Optional[WorkflowResponseError] = Field(default=None) 

class WorkflowListRequest(BaseModel):
    workspace_id: typing.Optional[UUID] = Field(default="") 

class WorkflowListResponse(BaseModel):
    workflows: typing.List[WorkflowStatus] = Field(default_factory=list) 
    error: typing.Optional[WorkflowResponseError] = Field(default=None) 
