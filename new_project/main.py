from fastapi import Depends, FastAPI, HTTPException
from requests import session
from sqlalchemy.orm import Session
from typing import List
from database import Base, engine
from routers import users

root_path = "/"

Base.metadata.create_all(bind=engine)

app =FastAPI(debug=True, root_path=root_path)


app.include_router(users.router) # User Route Call

@app.get("/", tags=["Default"])
def main():
    return {"hello" : "hi"}
