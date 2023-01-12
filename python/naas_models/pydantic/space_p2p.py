# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from protobuf_to_pydantic.get_desc.from_pb_option.types import HostNameStr
from protobuf_to_pydantic.get_desc.from_pb_option.types import UriRefStr
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
from pydantic.networks import AnyUrl
from uuid import UUID
import typing



class Protocol(IntEnum):
    HTTP = 0
    HTTPS = 1




class Space(BaseModel):

    _one_of_dict = {"Space._cpu": {"fields": {"cpu"}}, "Space._created_at": {"fields": {"created_at"}}, "Space._domain": {"fields": {"domain"}}, "Space._id": {"fields": {"id"}}, "Space._image": {"fields": {"image"}}, "Space._memory": {"fields": {"memory"}}, "Space._min_count": {"fields": {"min_count"}}, "Space._namespace": {"fields": {"namespace"}}, "Space._url": {"fields": {"url"}}, "Space._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    name: str = FieldInfo(default="", min_length=1, max_length=63, regex="^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$") 
    user_id: UUID = FieldInfo(default="") 
    id: UUID = FieldInfo(default="") 
    created_at: int = FieldInfo(default=0, gt=1673364229281) 
    namespace: HostNameStr = FieldInfo(default="") 
    cpu: float = FieldInfo(default=0.0, gt=0) 
    memory: float = FieldInfo(default=0.0, gt=0) 
    min_count: int = FieldInfo(default=0, ge=0) 
    domain: UriRefStr = FieldInfo(default="") 
    image: str = FieldInfo(default="", regex="^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$") 
    url: AnyUrl = FieldInfo(default="") 
    protocols: typing.List[Protocol] = FieldInfo(default_factory=list) 


