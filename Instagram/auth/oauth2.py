from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_user
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError




oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY = '202c3153cb5bc22345860bdaedaf6619b3061ce129a197c5bf02cbbf47d7a715' ### import secrets; print(secrets.token_hex(32))
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 15

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