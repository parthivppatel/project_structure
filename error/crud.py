from statistics import mode
from requests import session
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first() 


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email,hashed_password=fake_hashed_password,working_hours=user.working_hours,name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def assign_role(db:Session,role:schemas.RoleCreate):
    db_role=models.Role(types=role.types)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
    
def manage_staff(db:Session,staff:schemas.StaffCreate):
    db_staff=models.Staff(user_id=staff.user_id,role_id=staff.role_id)
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_user_by_userid(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first() 

def delete_user(db:Session,user_id:int):
    db.query(models.User).filter(models.User.id==user_id).delete()
    db.commit()

def check(db:session,user_id:int):
    return db.query(models.Staff).filter(models.Staff.user_id==user_id).first()

# def get_user_in_staff(db:session,user_id:int):
#     return db.query(models.Staff).filter(models.Staff.user_id == user_id) 

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
