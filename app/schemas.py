from pydantic import BaseModel, EmailStr
from  datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    date: datetime

    class Config:
        orm_mode = True  # to work with sqlalchemy models



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True # optional field with default value True


class PostCreate(PostBase):
    pass

### This is used to shape the response of the post created more clearly we can deicide what to show and what not to show
class PostResponse(PostBase):
    id: int
    date: datetime 
    user_id: int
    user_info: UserResponse


    class Config:
        orm_mode = True  # to work with sqlalchemy models

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True



class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None   
    # Optional field jodi token e id na thake tahole None thakbe


class VoteBase(BaseModel):
    post_id: int
    dir: int # direction 1 means upvote and 0 means remove upvote



        
