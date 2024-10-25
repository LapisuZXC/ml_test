from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserSchema(BaseModel):
    id: int
    gender: str
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str

    class Config:
        orm_mode = True
        from_attributes = True
 

class PostSchema(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True
        from_attributes = True


class FeedSchema(BaseModel):
    user_id: int
    post_id: int
    action: str
    time: datetime
    user: Optional[UserSchema]
    post: Optional[PostSchema]

    class Config:
        orm_mode = True
        from_attributes = True


class FeedRecomendationSchema(BaseModel):
    post_id: int
    likes: int

    class Config:
        orm_mode = True
        from_attributes = True
