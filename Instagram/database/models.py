from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from database.database import Base
from datetime import datetime


class InstgramUserModel(Base):
    __tablename__ = "instagram_user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(120))
    # profile_photo_url = Column(String(512))
    ### Relationship
    post = relationship("InstagramModel", back_populates="user")



class InstagramModel(Base):
    __tablename__ = "instagram"

    id = Column(Integer, primary_key=True, index=True)
    post_title = Column(String(256))
    #description = Column(String(512))
    image_url = Column(String(512))
    image_url_type = Column(String(512))
    caption = Column(String(512))
    
    created_at = Column(DateTime, default=datetime.now())
    #updated_at = Column(DateTime, default=datetime.now())
    ### Relationship
    user_id = Column(Integer, ForeignKey('instagram_user.id'))

    user = relationship("InstgramUserModel", back_populates="post")
    comments = relationship("InstagramCommentModel", back_populates="post")
   

class InstagramCommentModel(Base):
    __tablename__ = 'post_comment'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String(255))
    likes = Column(Boolean, nullable=True) 
    username = Column(String(255))
    timestamp = Column(DateTime)
    ##
    post_id = Column(Integer, ForeignKey('instagram.id'))
    post = relationship("InstagramModel", back_populates='comments')