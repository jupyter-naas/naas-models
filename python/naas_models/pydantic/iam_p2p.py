# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing





class TokenData(BaseModel):

    _one_of_dict = {"TokenData._user_id": {"fields": {"user_id"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: str = FieldInfo(default="") 
    scopes: typing.List[str] = FieldInfo(default_factory=list) 




class Profile(BaseModel):

    _one_of_dict = {"Profile._company": {"fields": {"company"}}, "Profile._first_name": {"fields": {"first_name"}}, "Profile._last_name": {"fields": {"last_name"}}, "Profile._phone": {"fields": {"phone"}}, "Profile._product_updates": {"fields": {"product_updates"}}, "Profile._profile_picture_url": {"fields": {"profile_picture_url"}}, "Profile._role": {"fields": {"role"}}, "Profile._targeted_use": {"fields": {"targeted_use"}}, "Profile._timezone": {"fields": {"timezone"}}, "Profile._user_id": {"fields": {"user_id"}}, "Profile._user_presentation": {"fields": {"user_presentation"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    user_id: str = FieldInfo(default="") 
    first_name: str = FieldInfo(default="") 
    last_name: str = FieldInfo(default="") 
    company: str = FieldInfo(default="") 
    role: str = FieldInfo(default="") 
    timezone: str = FieldInfo(default="") 
    profile_picture_url: str = FieldInfo(default="") 
    user_presentation: str = FieldInfo(default="") 
    targeted_use: str = FieldInfo(default="") 
    product_updates: bool = FieldInfo(default=False) 
    phone: str = FieldInfo(default="") 


