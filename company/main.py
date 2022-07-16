from fastapi import Depends, FastAPI, HTTPException
from requests import session
from sqlalchemy.orm import Session
from typing import List

import crud, models, schemas
from database import SessionLocal, engine
from models import User,Role

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_check=crud.check_phone(db,phone_no=user.phone_no)
    if db_check:
        raise HTTPException(status_code=400, detail="phone no already registered")
    return crud.create_user(db=db, user=user) 


@app.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/user_Role/")
def roles_of_users(db: Session = Depends(get_db)):
    db_query=db.query(User.id,User.name,User.email,User.is_admin,User.role_id,Role.types)\
    .join(Role,Role.id == User.role_id, isouter=True)\
    .all()
    return db_query


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/roles/",response_model=schemas.Role)
def assign_role(role:schemas.RoleCreate,db:Session=Depends(get_db)):
    check_role=db.query(models.Role).filter(models.Role.types==role.types).first()
    if check_role:
        raise HTTPException(status_code=404, detail="role already assign")
    return crud.assign_role(db=db,role=role)


@app.post("/staff/",response_model=schemas.Staff)
def manage_staff(staff:schemas.StaffCreate,db:session=Depends(get_db)):
    db_staff=crud.get_user(db,user_id=staff.user_id)
    db_check=crud.check(db,user_id=staff.user_id)
    if db_check:
        raise HTTPException(status_code=400, detail="user already assign")
    if not db_staff:
        raise HTTPException(status_code=400, detail="user not exist")
    return crud.manage_staff(db=db, staff=staff) 

@app.delete("/users/{user_id}")
def delete_user(user_id:int,db:session=Depends(get_db)):
    db_user=crud.get_user(db,user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="user not exist")
    crud.delete_user_from_staff(db,user_id=user_id)
    crud.delete_user(db=db,user_id=user_id)
    return {"message":f"succesfully delete user {user_id}"}

@app.put("/users/{user_id}",response_model=schemas.User)
def update_user(user_id:int,user:schemas.UserCreate,db:session=Depends(get_db)):
    db_user=crud.get_user(db,user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="user not exist")
    db_update=crud.update_user(db=db,user=user,user_id=user_id)
    return db_update