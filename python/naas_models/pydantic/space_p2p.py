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



class Protocol(IntEnum):
    HTTP = 0
    HTTPS = 1


class SpaceError(IntEnum):
    SPACE_ALREADY_EXISTS = 0
    SPACE_NOT_FOUND = 1
    SPACE_NOT_UPDATED = 2




class Space(BaseModel):

    _one_of_dict = {"Space._created_at": {"fields": {"created_at"}}, "Space._domain": {"fields": {"domain"}}, "Space._id": {"fields": {"id"}}, "Space._image": {"fields": {"image"}}, "Space._name": {"fields": {"name"}}, "Space._namespace": {"fields": {"namespace"}}, "Space._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: UUID = FieldInfo(default="") 
    id: UUID = FieldInfo(default="") 
    created_at: str = FieldInfo(default="", regex="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d{1,6})?Z$") 
    resources: typing.Dict[str, str] = FieldInfo(default_factory=dict) 
    namespace: str = FieldInfo(default="") 
    domain: UriRefStr = FieldInfo(default="") 
    image: str = FieldInfo(default="", regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    protocols: typing.List[Protocol] = FieldInfo(default_factory=list) 
    env: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class SpaceResponseError(BaseModel):

    _one_of_dict = {"SpaceResponseError._code": {"fields": {"code"}}, "SpaceResponseError._message": {"fields": {"message"}}, "SpaceResponseError._reason": {"fields": {"reason"}}, "SpaceResponseError._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    code: SpaceError = FieldInfo(default=0) 
    status: str = FieldInfo(default="") 
    reason: str = FieldInfo(default="") 
    message: str = FieldInfo(default="") 




class SpaceCreationRequest(BaseModel):

    _one_of_dict = {"SpaceCreationRequest._image": {"fields": {"image"}}, "SpaceCreationRequest._name": {"fields": {"name"}}, "SpaceCreationRequest._namespace": {"fields": {"namespace"}}, "SpaceCreationRequest._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: UUID = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 
    image: str = FieldInfo(default="", regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class SpaceCreationResponse(BaseModel):

    _one_of_dict = {"SpaceCreationResponse._space": {"fields": {"space"}}, "SpaceCreationResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 




class SpaceGetRequest(BaseModel):

    _one_of_dict = {"SpaceGetRequest._name": {"fields": {"name"}}, "SpaceGetRequest._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    namespace: str = FieldInfo(default="") 




class SpaceGetResponse(BaseModel):

    _one_of_dict = {"SpaceGetResponse._space": {"fields": {"space"}}, "SpaceGetResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 




class SpaceDeletionRequest(BaseModel):

    _one_of_dict = {"SpaceDeletionRequest._name": {"fields": {"name"}}, "SpaceDeletionRequest._namespace": {"fields": {"namespace"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    namespace: str = FieldInfo(default="") 




class SpaceDeletionResponse(BaseModel):

    _one_of_dict = {"SpaceDeletionResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    status: str = FieldInfo(default="") 




class SpaceListRequest(BaseModel):

    _one_of_dict = {"SpaceListRequest._namespace": {"fields": {"namespace"}}, "SpaceListRequest._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: UUID = FieldInfo(default="") 
    namespace: str = FieldInfo(default="") 




class SpaceListResponse(BaseModel):

    spaces: typing.List[Space] = FieldInfo(default_factory=list) 




class SpaceUpdatePatch(BaseModel):

    _one_of_dict = {"SpaceUpdatePatch._image": {"fields": {"image"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    image: str = FieldInfo(default="", regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    env: typing.Dict[str, str] = FieldInfo(default_factory=dict) 




class SpaceUpdateRequest(BaseModel):

    _one_of_dict = {"SpaceUpdateRequest._name": {"fields": {"name"}}, "SpaceUpdateRequest._namespace": {"fields": {"namespace"}}, "SpaceUpdateRequest._update_patch": {"fields": {"update_patch"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    namespace: str = FieldInfo(default="") 
    update_patch: SpaceUpdatePatch = FieldInfo() 




class SpaceUpdateResponse(BaseModel):

    _one_of_dict = {"SpaceUpdateResponse._space": {"fields": {"space"}}, "SpaceUpdateResponse._status": {"fields": {"status"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    space: Space = FieldInfo() 
    status: str = FieldInfo(default="") 


