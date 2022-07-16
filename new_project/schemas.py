from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    id : int
    email : str
    name : str
    working_hours : int
    phone_no : str
    is_active : bool
    is_admin : bool
    
    class Config:
        orm_mode = True

class Role(BaseModel):
    id : int
    types : str

    class config:
        orm_mode=True