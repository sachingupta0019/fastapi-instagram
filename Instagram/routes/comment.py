from fastapi import APIRouter, HTTPException, status, Depends
from database.database import get_db
from schema.schema import InstagramCommentSchema, UserAuthSchema
from sqlalchemy.orm import Session
from database import db_comment
from auth.oauth2 import get_cuurent_user
from typing import List


router = APIRouter(prefix='/post', tags=['Post Comment'])

@router.post('/new-comment')
def add_comment(request: InstagramCommentSchema, db:Session=Depends(get_db), current_user: UserAuthSchema = Depends(get_cuurent_user)):
    return db_comment.create_comment(request, db)


@router.get("/all-comment/{post_id}")
def get_all_comments(post_id: int, db:Session=Depends(get_db)):
    post_comment = db_comment.get_all_comment(post_id, db)

    if not post_comment:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=" No Comments")
    return post_comment