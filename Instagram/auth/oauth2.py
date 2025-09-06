from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_user
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')




def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta is not None:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

        
def get_cuurent_user(token: str = Depends(oauth2_schema), db:Session=Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers= {'WWW-Authenticate':'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
    except JWTError:
        raise credential_exception
    
    user = db_user.get_user_by_username(db, username)
    if user is None:
        raise credential_exception
    return user