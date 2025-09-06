from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import InstagramModel
from schema.schema import InstagramSchema, InstagramSchemaDisplay, UserAuthSchema
from db import db_ig_post
from auth.oauth2 import get_cuurent_user
from typing import List
import string
import random
import shutil


router = APIRouter(prefix='/post', tags=['IG Post'])

image_url_types = ['absolute','relative']

@router.post('/image', response_model=None)
def upload_image(img: UploadFile = File(...), cuurent_user: UserAuthSchema = Depends(get_cuurent_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new_str = f"_{rand_str}."
    filename = new_str.join(img.filename.rsplit(".",1))
    path = f"images/{filename}"
    # return path
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(img.file, buffer)
    #
    return {'filename': path}


### Create New Post...
@router.post('/create', response_model=InstagramSchemaDisplay)
def create_post(request: InstagramSchema, db:Session = Depends(get_db), cuurent_user: UserAuthSchema = Depends(get_cuurent_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=
                            "Parameter image_url_type can only take value 'absolute' or 'relative'. ")

    return db_ig_post.create_post(request, db)

### Retrive New Post...
@router.get('/all', response_model=List[InstagramSchemaDisplay])
def get_ig_post(db: Session = Depends(get_db)):
    return db_ig_post.get_ig_post(db)

### Update New Post...


### Delete Post...
@router.delete('/delete/{id}', response_model=None)
def delete_ig_post(id: int, db:Session=Depends(get_db), cuurent_user: UserAuthSchema = Depends(get_cuurent_user)):
   return db_ig_post.del_ig_post(id, cuurent_user.id, db)

