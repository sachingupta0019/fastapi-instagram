from fastapi import Depends, HTTPException, status, APIRouter
from Instagram.auth import oauth2
from sqlalchemy.orm import Session
from Instagram.db import models
from Instagram.db.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from Instagram.db.hash import Hash

router = APIRouter(tags=['Authentication'])

# @router.post('/token')
# def get_access_token(request: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
#     user = db.query(models.InstgramUserModel).filter(models.InstgramUserModel.username == request.username).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found.")
    
#     if not Hash.verify(request.password, user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password.")
    
#     access_token = oauth2.create_access_token({'sub': user.username})

#     return {
#         "access_token": access_token,
#         "token_type" : 'bearer',
#         "header" : "WWW-Authenticate",
#         "user" : user.username,
#     }


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = db.query(models.InstgramUserModel).filter(models.InstgramUserModel.username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found.")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password.")
    
    access_token = oauth2.create_access_token(data = {'username' : user.username})

    return {
        'access_token' : access_token,
        'token_type'  : 'bearer',
        'username' : user.username,
        'user_id' : user.id,
    }