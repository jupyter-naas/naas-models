# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing





class Archive(BaseModel):

    none: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class ArtifactS3(BaseModel):

    _one_of_dict = {"ArtifactS3._bucket": {"fields": {"bucket"}}, "ArtifactS3._key": {"fields": {"key"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    key: str = FieldInfo(default="") 
    bucket: str = FieldInfo(default="") 




class Artifact(BaseModel):

    _one_of_dict = {"Artifact._archive": {"fields": {"archive"}}, "Artifact._from": {"fields": {"from"}}, "Artifact._mode": {"fields": {"mode"}}, "Artifact._name": {"fields": {"name"}}, "Artifact._path": {"fields": {"path"}}, "Artifact._s3": {"fields": {"s3"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    path: str = FieldInfo(default="") 
    mode: int = FieldInfo(default=0) 
    archive: Archive = FieldInfo() 
    s3: ArtifactS3 = FieldInfo() 




class Inputs(BaseModel):

    parameters: typing.List[Parameter] = FieldInfo(default_factory=list) 
    artifacts: typing.List[Artifact] = FieldInfo(default_factory=list) 




class Outputs(BaseModel):

    parameters: typing.List[Parameter] = FieldInfo(default_factory=list) 
    artifacts: typing.List[Artifact] = FieldInfo(default_factory=list) 




class Parameter(BaseModel):

    _one_of_dict = {"Parameter._default": {"fields": {"default"}}, "Parameter._name": {"fields": {"name"}}, "Parameter._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    value: str = FieldInfo(default="") 
    default: str = FieldInfo(default="") 




class Arguments(BaseModel):

    parameters: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    artifacts: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class DagTasks(BaseModel):

    _one_of_dict = {"DagTasks._arguments": {"fields": {"arguments"}}, "DagTasks._depends": {"fields": {"depends"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    template: str = FieldInfo(default="") 
    depends: str = FieldInfo(default="") 
    arguments: Arguments = FieldInfo() 




class DagTemplate(BaseModel):

    _one_of_dict = {"DagTemplate._target": {"fields": {"target"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    tasks: typing.List[DagTasks] = FieldInfo(default_factory=list) 
    target: str = FieldInfo(default="") 




class ScriptTemplate(BaseModel):

    _one_of_dict = {"ScriptTemplate._image": {"fields": {"image"}}, "ScriptTemplate._source": {"fields": {"source"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    image: str = FieldInfo(default="") 
    command: typing.List[str] = FieldInfo(default_factory=list) 
    resources: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    source: str = FieldInfo(default="") 




class Template(BaseModel):

    _one_of_dict = {"Template._container": {"fields": {"container"}}, "Template._dag": {"fields": {"dag"}}, "Template._inputs": {"fields": {"inputs"}}, "Template._name": {"fields": {"name"}}, "Template._outputs": {"fields": {"outputs"}}, "Template._script": {"fields": {"script"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    container: str = FieldInfo(default="") 
    metadata: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    inputs: Inputs = FieldInfo() 
    outputs: Outputs = FieldInfo() 
    dag: DagTemplate = FieldInfo() 
    script: ScriptTemplate = FieldInfo() 




class Spec(BaseModel):

    _one_of_dict = {"Spec._arguments": {"fields": {"arguments"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    entrypoint: str = FieldInfo(default="") 
    arguments: Arguments = FieldInfo() 
    templates: typing.List[Template] = FieldInfo(default_factory=list) 




class Metadata(BaseModel):

    _one_of_dict = {"Metadata._generateName": {"fields": {"generateName"}}, "Metadata._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    generateName: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    labels: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class Workflow(BaseModel):

    metadata: Metadata = FieldInfo() 
    spec: Spec = FieldInfo() 




class WorkflowCreationRequest(BaseModel):

    _one_of_dict = {"WorkflowCreationRequest._description": {"fields": {"description"}}, "WorkflowCreationRequest._name": {"fields": {"name"}}, "WorkflowCreationRequest._namespace": {"fields": {"namespace"}}, "WorkflowCreationRequest._serverDryRun": {"fields": {"serverDryRun"}}, "WorkflowCreationRequest._user_uid": {"fields": {"user_uid"}}, "WorkflowCreationRequest._workflow": {"fields": {"workflow"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    description: str = FieldInfo(default="") 
    user_uid: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    serverDryRun: bool = FieldInfo(default=False) 
    workflow: Workflow = FieldInfo() 




class WorkflowCreationResponse(BaseModel):

    _one_of_dict = {"WorkflowCreationResponse._message": {"fields": {"message"}}, "WorkflowCreationResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowUpdateRequest(BaseModel):

    _one_of_dict = {"WorkflowUpdateRequest._name": {"fields": {"name"}}, "WorkflowUpdateRequest._namespace": {"fields": {"namespace"}}, "WorkflowUpdateRequest._workflow": {"fields": {"workflow"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    workflow: Workflow = FieldInfo() 




class WorkflowUpdateResponse(BaseModel):

    _one_of_dict = {"WorkflowUpdateResponse._message": {"fields": {"message"}}, "WorkflowUpdateResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowDeleteRequest(BaseModel):

    _one_of_dict = {"WorkflowDeleteRequest._namespace": {"fields": {"namespace"}}, "WorkflowDeleteRequest._workflow_name": {"fields": {"workflow_name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workflow_name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 




class WorkflowDeleteResponse(BaseModel):

    _one_of_dict = {"WorkflowDeleteResponse._message": {"fields": {"message"}}, "WorkflowDeleteResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowGetRequest(BaseModel):

    _one_of_dict = {"WorkflowGetRequest._namespace": {"fields": {"namespace"}}, "WorkflowGetRequest._workflow_name": {"fields": {"workflow_name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    workflow_name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 




class WorkflowGetResponse(BaseModel):

    _one_of_dict = {"WorkflowGetResponse._message": {"fields": {"message"}}, "WorkflowGetResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowListRequest(BaseModel):

    _one_of_dict = {"WorkflowListRequest._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    namespace: str = FieldInfo(default="") 




class WorkflowListResponse(BaseModel):

    workflows: typing.List[WorkflowGetResponse] = FieldInfo(default_factory=list) 




class WorkflowCreationError(BaseModel):

    _one_of_dict = {"WorkflowCreationError._message": {"fields": {"message"}}, "WorkflowCreationError._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowUpdateError(BaseModel):

    _one_of_dict = {"WorkflowUpdateError._message": {"fields": {"message"}}, "WorkflowUpdateError._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowDeleteError(BaseModel):

    _one_of_dict = {"WorkflowDeleteError._message": {"fields": {"message"}}, "WorkflowDeleteError._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowGetError(BaseModel):

    _one_of_dict = {"WorkflowGetError._message": {"fields": {"message"}}, "WorkflowGetError._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowListError(BaseModel):

    _one_of_dict = {"WorkflowListError._message": {"fields": {"message"}}, "WorkflowListError._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 


