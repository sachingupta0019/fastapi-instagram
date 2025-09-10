from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from Instagram.db.database import get_db
from Instagram.db import db_user
from sqlalchemy.orm import Session
from Instagram.schema.schema import InstagramUserSchema,InstagramUserSchemaDisplay, UserAuthSchema
from Instagram.auth.oauth2 import get_cuurent_user
from typing import List
# import shutil

router = APIRouter(prefix="/user", tags=['User profile'])

## Create New User
@router.post("/create", response_model=InstagramUserSchemaDisplay)
def create_user(request: InstagramUserSchema, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)

## User Profile Photo
# @router.post("/profile-photo", response_model=[])
# def user_profile_photo(img: UploadFile = File(...), current_user: UserAuthSchema = Depends(get_cuurent_user) ):
#     filename = img.filename
#     path = f"images/profile_photo/{filename}"
#     with open(path, 'w+b') as buffer:
#         shutil.copyfileobj(img.file, buffer)
#     return {"path":path, "filename":filename}

## Get All Users
@router.get('/all-users', response_model=List[InstagramUserSchemaDisplay])
def get_user(db: Session = Depends(get_db)):
    return db_user.get_user(db)