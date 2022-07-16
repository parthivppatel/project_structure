from email.policy import default
from operator import index
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import Base

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
    role_id = Column(Integer, ForeignKey("roles.id"), index=False,default=2)

class Role(Base):
   __tablename__="roles"
   
   id = Column(Integer, primary_key=True, index=True)
   types=Column(String)
