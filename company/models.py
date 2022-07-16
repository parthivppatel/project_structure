from email.policy import default
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from database import *


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    working_hours=Column(Integer)
    name=Column(String)
    phone_no=Column(String,unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin=Column(Boolean,default=False)
    role_id= Column(Integer,ForeignKey("roles.id"))
    roles = relationship("Role", back_populates="owner_role")

class Role(Base):
   __tablename__="roles"
   
   id = Column(Integer, primary_key=True, index=True)
   types=Column(String)

 
   owner_role=relationship("User",back_populates="roles")
    
# class Staff(Base):
#     __tablename__="staff"

#     id = Column(Integer,primary_key=True, index=True)
#     user_id=Column(Integer,ForeignKey("users.id"))
#     role_id=Column(Integer,ForeignKey("roles.id"))

#     owner = relationship("User", back_populates="staff")
#     back_role = relationship("Role", back_populates="staff_role")