from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


class UserBase(BaseModel):
    email: str
    working_hours:float


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
  
    class Config:
        orm_mode = True



# class RoleBase(BaseModel):
#    types:str

# class RoleCreate(RoleBase):
#     pass

# class Role(RoleBase):
#     id:int

#     class config:
#         orm_mode=True



# class StaffBase(BaseModel):
#     user_id:int
#     role_id:int

# class StaffCreate(StaffBase):
#     pass

# class Staff(StaffBase):
#     id:int

#     class config:
#         orm_mode=True