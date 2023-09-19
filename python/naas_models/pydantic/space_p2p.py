# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from protobuf_to_pydantic.get_desc.from_pb_option.types import UriRefStr
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
from uuid import UUID
import typing



class SpaceError(IntEnum):
    SPACE_NO_ERROR = 0
    SPACE_ALREADY_EXISTS = 1
    SPACE_NOT_FOUND = 2
    SPACE_NOT_UPDATED = 3
    SPACE_MUST_HAVE_ONE_CONTAINER_PORT = 4




class Container(BaseModel):

    _one_of_dict = {"Container._cpu": {"fields": {"cpu"}}, "Container._image": {"fields": {"image"}}, "Container._memory": {"fields": {"memory"}}, "Container._name": {"fields": {"name"}}, "Container._port": {"fields": {"port"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9-]+)$") 
    image: str = FieldInfo(default="", min_length=1, regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    port: int = FieldInfo(default=0, ge=0, le=65535) 
    cpu: str = FieldInfo(default="", regex="^[0-9]+(.[0-9]+)?[m]?$") 
    memory: str = FieldInfo(default="", regex="^[0-9]+(Mi|Gi|Ki)$") 




class ContainerUpdate(BaseModel):

    _one_of_dict = {"ContainerUpdate._cpu": {"fields": {"cpu"}}, "ContainerUpdate._image": {"fields": {"image"}}, "ContainerUpdate._memory": {"fields": {"memory"}}, "ContainerUpdate._name": {"fields": {"name"}}, "ContainerUpdate._port": {"fields": {"port"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9-]+)$") 
    image: str = FieldInfo(default="", min_length=1, regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    port: int = FieldInfo(default=0, ge=0, le=65535) 
    cpu: str = FieldInfo(default="", regex="^[0-9]+(.[0-9]+)?[m]?$") 
    memory: str = FieldInfo(default="", regex="^[0-9]+(Mi|Gi|Ki)$") 




class Space(BaseModel):

    _one_of_dict = {"Space._domain": {"fields": {"domain"}}, "Space._id": {"fields": {"id"}}, "Space._name": {"fields": {"name"}}, "Space._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: UUID = FieldInfo(default="") 
    id: UUID = FieldInfo(default="") 
    domain: UriRefStr = FieldInfo(default="") 
    containers: typing.List[Container] = FieldInfo(default_factory=list, min_items=1) 




class SpaceUpdate(BaseModel):

    _one_of_dict = {"SpaceUpdate._domain": {"fields": {"domain"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    domain: UriRefStr = FieldInfo(default="") 
    containers: typing.List[ContainerUpdate] = FieldInfo(default_factory=list, min_items=1) 




class SpaceResponseError(BaseModel):

    _one_of_dict = {"SpaceResponseError._code": {"fields": {"code"}}, "SpaceResponseError._message": {"fields": {"message"}}, "SpaceResponseError._reason": {"fields": {"reason"}}, "SpaceResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: SpaceError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class SpaceCreationRequest(BaseModel):

    _one_of_dict = {"SpaceCreationRequest._domain": {"fields": {"domain"}}, "SpaceCreationRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    domain: UriRefStr = FieldInfo(default="") 
    containers: typing.List[Container] = FieldInfo(default_factory=list, min_items=1) 




class SpaceCreationResponse(BaseModel):

    _one_of_dict = {"SpaceCreationResponse._space": {"fields": {"space"}}, "SpaceCreationResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 




class SpaceGetRequest(BaseModel):

    _one_of_dict = {"SpaceGetRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 




class SpaceGetResponse(BaseModel):

    _one_of_dict = {"SpaceGetResponse._space": {"fields": {"space"}}, "SpaceGetResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 




class SpaceDeletionRequest(BaseModel):

    _one_of_dict = {"SpaceDeletionRequest._name": {"fields": {"name"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 




class SpaceDeletionResponse(BaseModel):

    _one_of_dict = {"SpaceDeletionResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    status: str = FieldInfo(default="") 




class SpaceListRequest(BaseModel):

    _one_of_dict = {"SpaceListRequest._page_number": {"fields": {"page_number"}}, "SpaceListRequest._page_size": {"fields": {"page_size"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    page_size: int = FieldInfo(default=0) 
    page_number: int = FieldInfo(default=0) 




class SpaceListResponse(BaseModel):

    spaces: typing.List[Space] = FieldInfo(default_factory=list) 




class SpaceUpdateRequest(BaseModel):

    _one_of_dict = {"SpaceUpdateRequest._name": {"fields": {"name"}}, "SpaceUpdateRequest._space": {"fields": {"space"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    space: SpaceUpdate = FieldInfo() 




class SpaceUpdateResponse(BaseModel):

    _one_of_dict = {"SpaceUpdateResponse._space": {"fields": {"space"}}, "SpaceUpdateResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 


