# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class TokenData(BaseModel):
    user_id: typing.Optional[str] = Field(default="") 
    scopes: typing.List[str] = Field(default_factory=list) 

class Profile(BaseModel):
    user_id: typing.Optional[str] = Field(default="") 
    first_name: typing.Optional[str] = Field(default="") 
    last_name: typing.Optional[str] = Field(default="") 
    company: typing.Optional[str] = Field(default="") 
    role: typing.Optional[str] = Field(default="") 
    timezone: typing.Optional[str] = Field(default="") 
    profile_picture_url: typing.Optional[str] = Field(default="") 
    user_presentation: typing.Optional[str] = Field(default="") 
    targeted_use: typing.Optional[str] = Field(default="") 
    product_updates: typing.Optional[bool] = Field(default=False) 
    phone: typing.Optional[str] = Field(default="") 
