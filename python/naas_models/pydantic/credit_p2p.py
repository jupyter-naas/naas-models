# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo





class CreditTransaction(BaseModel):

    _one_of_dict = {"CreditTransaction._credit": {"fields": {"credit"}}, "CreditTransaction._credit_dollar": {"fields": {"credit_dollar"}}, "CreditTransaction._date_extract": {"fields": {"date_extract"}}, "CreditTransaction._meta_1": {"fields": {"meta_1"}}, "CreditTransaction._meta_1_desc": {"fields": {"meta_1_desc"}}, "CreditTransaction._meta_2": {"fields": {"meta_2"}}, "CreditTransaction._meta_2_desc": {"fields": {"meta_2_desc"}}, "CreditTransaction._meta_3": {"fields": {"meta_3"}}, "CreditTransaction._meta_3_desc": {"fields": {"meta_3_desc"}}, "CreditTransaction._plan": {"fields": {"plan"}}, "CreditTransaction._quantity": {"fields": {"quantity"}}, "CreditTransaction._scenario": {"fields": {"scenario"}}, "CreditTransaction._type": {"fields": {"type"}}, "CreditTransaction._unit": {"fields": {"unit"}}, "CreditTransaction._unit_price": {"fields": {"unit_price"}}, "CreditTransaction._user": {"fields": {"user"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    scenario: str = FieldInfo(default="") 
    user: str = FieldInfo(default="") 
    plan: str = FieldInfo(default="") 
    type: str = FieldInfo(default="") 
    meta_1_desc: str = FieldInfo(default="") 
    meta_1: str = FieldInfo(default="") 
    meta_2_desc: str = FieldInfo(default="") 
    meta_2: str = FieldInfo(default="") 
    meta_3_desc: str = FieldInfo(default="") 
    meta_3: str = FieldInfo(default="") 
    quantity: float = FieldInfo(default=0.0) 
    unit: str = FieldInfo(default="") 
    unit_price: float = FieldInfo(default=0.0) 
    credit: float = FieldInfo(default=0.0) 
    credit_dollar: float = FieldInfo(default=0.0) 
    date_extract: str = FieldInfo(default="") 




class Balance(BaseModel):

    _one_of_dict = {"Balance._balance": {"fields": {"balance"}}, "Balance._balance_dollar": {"fields": {"balance_dollar"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    balance: float = FieldInfo(default=0.0) 
    balance_dollar: float = FieldInfo(default=0.0) 


