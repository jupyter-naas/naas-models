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

    _one_of_dict = {"ScriptTemplate._source": {"fields": {"source"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    source: str = FieldInfo(default="") 




class Template(BaseModel):

    _one_of_dict = {"Template._container": {"fields": {"container"}}, "Template._dag": {"fields": {"dag"}}, "Template._inputs": {"fields": {"inputs"}}, "Template._name": {"fields": {"name"}}, "Template._outputs": {"fields": {"outputs"}}, "Template._script": {"fields": {"script"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    container: str = FieldInfo(default="") 
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




class WorkflowCreationRequest(BaseModel):

    _one_of_dict = {"WorkflowCreationRequest._name": {"fields": {"name"}}, "WorkflowCreationRequest._namespace": {"fields": {"namespace"}}, "WorkflowCreationRequest._workflowSpec": {"fields": {"workflowSpec"}}, "WorkflowCreationRequest._workflowTemplate": {"fields": {"workflowTemplate"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    workflowTemplate: str = FieldInfo(default="") 
    workflowSpec: str = FieldInfo(default="") 




class WorkflowCreationResponse(BaseModel):

    _one_of_dict = {"WorkflowCreationResponse._message": {"fields": {"message"}}, "WorkflowCreationResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowUpdateRequest(BaseModel):

    _one_of_dict = {"WorkflowUpdateRequest._name": {"fields": {"name"}}, "WorkflowUpdateRequest._namespace": {"fields": {"namespace"}}, "WorkflowUpdateRequest._workflowSpec": {"fields": {"workflowSpec"}}, "WorkflowUpdateRequest._workflowTemplate": {"fields": {"workflowTemplate"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    workflowTemplate: str = FieldInfo(default="") 
    workflowSpec: str = FieldInfo(default="") 




class WorkflowUpdateResponse(BaseModel):

    _one_of_dict = {"WorkflowUpdateResponse._message": {"fields": {"message"}}, "WorkflowUpdateResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowDeleteRequest(BaseModel):

    _one_of_dict = {"WorkflowDeleteRequest._name": {"fields": {"name"}}, "WorkflowDeleteRequest._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 




class WorkflowDeleteResponse(BaseModel):

    _one_of_dict = {"WorkflowDeleteResponse._message": {"fields": {"message"}}, "WorkflowDeleteResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowGetRequest(BaseModel):

    _one_of_dict = {"WorkflowGetRequest._name": {"fields": {"name"}}, "WorkflowGetRequest._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 




class WorkflowGetResponse(BaseModel):

    _one_of_dict = {"WorkflowGetResponse._message": {"fields": {"message"}}, "WorkflowGetResponse._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class WorkflowListRequest(BaseModel):




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


