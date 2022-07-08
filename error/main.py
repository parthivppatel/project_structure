from fastapi import Depends, FastAPI, HTTPException
from requests import session
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

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
    return crud.create_user(db=db, user=user) 


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/roles/",response_model=schemas.Role)
def assign_role(role:schemas.RoleCreate,db:Session=Depends(get_db)):
    return crud.assign_role(db=db,role=role)


@app.post("/staff/",response_model=schemas.Staff)
def manage_staff(staff:schemas.StaffCreate,db:session=Depends(get_db)):
    db_staff=crud.get_user_by_userid(db,user_id=staff.user_id)
    db_check=crud.check(db,user_id=staff.user_id)
    if db_check:
        raise HTTPException(status_code=400, detail="user already assign")
    if not db_staff:
        raise HTTPException(status_code=400, detail="user not exist")
    # db_staff2=crud.get_user_in_staff(db,user_id=staff.user_id)
    # if db_staff2:
    #     raise HTTPException(status_code=400, detail="user is already assign")
    return crud.manage_staff(db=db, staff=staff) 

@app.delete("/users/{user_id}")
def delete_user(user_id:int,db:session=Depends(get_db)):
    db_user=crud.get_user_by_userid(db,user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="user not exist")
    crud.delete_user(db=db,user_id=user_id)
    return {"message":f"succesfully delete user {user_id}"}


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/",response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
