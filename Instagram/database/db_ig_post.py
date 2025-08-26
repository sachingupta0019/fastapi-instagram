from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from schema.schema import InstagramSchema
from database.models import InstagramModel
from datetime import datetime


### Create New IG Post
def create_post(request: InstagramSchema, db: Session):
    new_post = InstagramModel(
        post_title = request.post_title,
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        created_at = datetime.now(),
        user_id = request.user_id

    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


### Get All IG Post...
def get_ig_post(db: Session):
    ig_post = db.query(InstagramModel).all()

    if not ig_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not Found.")
    return ig_post

### Edit IG Post
def edit_ig_post(request: InstagramSchema, id: int, db: Session):
    pass

### Delete IG Post...

def del_ig_post(id: int, user_d: int, db: Session):
    ig_post = db.query(InstagramModel).filter(InstagramModel.id == id).first()

    if not ig_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found.")

    if ig_post.user_id != user_d:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Post creator can delete the post")
    
    db.delete(ig_post)
    db.commit()

    return {'Message' : f'IG Post with id {id} is deleted.'}