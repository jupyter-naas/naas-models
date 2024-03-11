# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic.fields import FieldInfo
import typing





class FieldMask(BaseModel):

    paths: typing.List[str] = FieldInfo(default_factory=list, min_items=1) 


