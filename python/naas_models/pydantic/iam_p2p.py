# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from naas_models.pydantic.errors_p2p import ErrorResponse
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
from pydantic.networks import EmailStr
from uuid import UUID
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

class ImpersonateUserRequest(BaseModel):
    _one_of_dict = {"ImpersonateUserRequest.user": {"fields": {"email", "user_id"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    user_id: UUID = Field(default="") 
    email: EmailStr = Field(default="") 

class ImpersonateUserResponse(BaseModel):
    error: typing.Optional[ErrorResponse] = Field(default=None) 
    token: typing.Optional[str] = Field(default="") 
