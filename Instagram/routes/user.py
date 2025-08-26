from fastapi import APIRouter, HTTPException, Depends
from database.database import get_db
from database import db_user
from sqlalchemy.orm import Session
from schema.schema import InstagramUserSchema,InstagramUserSchemaDisplay
from typing import List

router = APIRouter(prefix="/user", tags=['User profile'])

## Create New User
@router.post("/create", response_model=InstagramUserSchemaDisplay)
def create_user(request: InstagramUserSchema, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)


## Get All Users
@router.get('/all-users', response_model=List[InstagramUserSchemaDisplay])
def get_user(db: Session = Depends(get_db)):
    return db_user.get_user(db)