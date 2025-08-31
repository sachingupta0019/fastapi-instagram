from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated, Optional, List


### Instagram User Schema
class InstagramUserSchema(BaseModel):
    # id: Annotated[str, Field(title="User ID")]
    username: Annotated[str, Field(title="User Name")]
    email: Annotated[str, Field(title="User Email")]
    password: Annotated[str, Field("User Password")]
    # profile_photo_url: Annotated[str, Field("Profile Photo")]


class InstagramUserSchemaDisplay(BaseModel):
    id: Annotated[int, Field(title="User ID")]
    username: Annotated[str, Field(title="User Name")]
    email: Annotated[str, Field(title="User Email")]
    # profile_photo_url: Annotated[str, Field("Profile Photo")]
    class config():
        orm_mode = True

### User Authorization schema
class UserAuthSchema(BaseModel):
    id: int
    username: Annotated[str, Field(title="Username")]
    email: Annotated[str, Field(title="Email ID")]


### Instagram Post Schema
class InstagramSchema(BaseModel):
    post_title: Annotated[str, Field(title="Post Title")]
    #description: Annotated[str, Field(title="Post description")]
    image_url: Annotated[str, Field(title="Post Image Url")]
    image_url_type: Annotated[str, Field(title="Type of Image URL.")]
    caption: Annotated[str, Field(title=" Image Caption.")]
    # created_at: Annotated[datetime, Field(title="created at")]
    user_id: Annotated[int, Field("user Id")]
    #updated_at: Annotated[datetime, Field(title="updated at")]


## For InstagramSchemaDisplay Display
class User(BaseModel):
    username: str
    # profile_photo_url: str
    class config():
        orm_mode = True

## For InstagramSchemaDisplay Display
class Comment(BaseModel):
    text: str
    likes: bool
    username: str
    timestamp: datetime
    class config():
        orm_mode = True


##
class InstagramSchemaDisplay(BaseModel):
    id: int
    post_title: Annotated[str, Field(title="Post Title")]
    #description: Annotated[str, Field(title="Post description")]
    image_url: Annotated[str, Field(title="Post Image Url")]
    image_url_type: Annotated[str, Field(title="Type of Image URL.")]
    caption: Annotated[str, Field(title=" Image Caption.")]
    created_at: Annotated[datetime, Field(title="created at")]
    #updated_at: Annotated[datetime, Field(title="updated at")]
    user: User
    comments: List[Comment]
    class config():
        orm_mode = True
        

class InstagramCommentSchema(BaseModel):
    username: str
    text: Annotated[Optional[str], Field(title="Post Comments")]
    likes: Optional[bool] = Field(title="Post Like Status")
    post_id: Annotated[int, Field(title="Post ID")]