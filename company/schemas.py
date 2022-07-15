from pydantic import BaseModel
from typing import List

from sqlalchemy import true

 
class UserBase(BaseModel):
    email: str
    name:str
    working_hours:int
    phone_no :str

    class Config:
	    orm_mode=True
  


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_admin:bool

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
   types:str

   class Config:
        orm_mode = True

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id:int

    class config:
        orm_mode=True

class User_role(BaseModel):
    class Config:
        orm_mode = True

    email: str
    name:str
    working_hours:int
    phone_no :str
    is_active: bool
    is_admin:bool
 


class StaffBase(BaseModel):
    user_id:int
    role_id:int


    class Config:
        orm_mode = True
   
class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    id:int
    
    class config:
        orm_mode=True

    