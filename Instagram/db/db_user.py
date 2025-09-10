from Instagram.db.models import InstgramUserModel
from Instagram.schema.schema import InstagramUserSchema, InstagramUserSchemaDisplay
from sqlalchemy.orm import Session
from Instagram.db.hash import Hash
from fastapi import HTTPException, status


### Register a New User...
def create_user(request: InstagramUserSchema, db: Session):
    new_user = InstgramUserModel(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password),
        # profile_photo = request.profile_photo,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


### Get All Users.
def get_user(db: Session):
    users = db.query(InstgramUserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not exists.')
    return users

###  Get User by Username..
def get_user_by_username(db: Session, username: str):
    user = db.query(InstgramUserModel).filter(InstgramUserModel.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found.")
    
    return user