from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List, Union
from app.utils.custom_types import PyObjectId





class IgBase(BaseModel):
    username: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "ig": "",
            }
        }


class IgInput(IgBase):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "",
                "password": "",
            }
        }


class Ig(IgBase):
    username: str = Field(...)
    password: str = Field(...)
    is_expired: Union[bool, None] = None
    ig_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "",
                "password": "",
                "is_expired":False,
                'ig_id':''
            }
        }

class IgViewModel(IgBase):
    username: str = Field(...)
    is_expired: Union[bool, None] = None
    ig_id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    schema_extra = {
            "example": {
                "username": "",
                "is_expired":False,
                'ig_id':''
            }
        }
