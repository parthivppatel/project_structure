from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
import database as databaseutils
from models.users import User, Role


router = APIRouter(prefix="/users",tags=["Users"])

# Users
@router.get("/list")
def get_user_list(db: Session = Depends(databaseutils.get_db)):
    
    db_query = db.query(User.id,User.name,User.email,User.is_admin,User.role_id,Role.types)\
        .join(Role,Role.id == User.role_id, isouter=True)\
        .all()
    
    return db_query

@router.post("/create")
def create_users(db: Session = Depends(databaseutils.get_db)):
    # db_query = db.query()
    pass

@router.put("/update")
def update_users(db: Session = Depends(databaseutils.get_db)):
    # db_query = db.query()
    pass

@router.delete("/delete")
def delete_users(db: Session = Depends(databaseutils.get_db)):
    # db_query = db.query()
    pass


# Role
@router.get("/role_list")
def get_role_list(db: Session = Depends(databaseutils.get_db)):
    
    db_query = db.query(Role).all()
    
    return db_query