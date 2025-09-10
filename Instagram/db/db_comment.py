from Instagram.db.models import InstagramCommentModel
from Instagram.schema.schema import InstagramCommentSchema
from sqlalchemy.orm import Session
from datetime import datetime



###
def create_comment(request: InstagramCommentSchema, db:Session):
    new_comment = InstagramCommentModel(
        text = request.text,
        likes = request.likes if request.likes is not None else 0,
        username = request.username,
        timestamp = datetime.now(),
        post_id = request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


###
def get_all_comment(post_id: int, db:Session):
    return db.query(InstagramCommentModel).filter(InstagramCommentModel.post_id == post_id).all()
                    