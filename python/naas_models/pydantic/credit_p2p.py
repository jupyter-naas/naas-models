# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.26.1 
# Pydantic Version: 2.7.1 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class CreditTransaction(BaseModel):
    scenario: typing.Optional[str] = Field(default="") 
    user: typing.Optional[str] = Field(default="") 
    plan: typing.Optional[str] = Field(default="") 
    type: typing.Optional[str] = Field(default="") 
    meta_1_desc: typing.Optional[str] = Field(default="") 
    meta_1: typing.Optional[str] = Field(default="") 
    meta_2_desc: typing.Optional[str] = Field(default="") 
    meta_2: typing.Optional[str] = Field(default="") 
    meta_3_desc: typing.Optional[str] = Field(default="") 
    meta_3: typing.Optional[str] = Field(default="") 
    quantity: typing.Optional[float] = Field(default=0.0) 
    unit: typing.Optional[str] = Field(default="") 
    unit_price: typing.Optional[float] = Field(default=0.0) 
    credit: typing.Optional[float] = Field(default=0.0) 
    credit_dollar: typing.Optional[float] = Field(default=0.0) 
    date_extract: typing.Optional[str] = Field(default="") 

class Balance(BaseModel):
    balance: typing.Optional[float] = Field(default=0.0) 
    balance_dollar: typing.Optional[float] = Field(default=0.0) 
