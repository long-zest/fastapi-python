from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class BlogUser(Blog):
    id: int
    class Config():
        orm_mode = True

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    class Config():
        orm_mode = True

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    # blogs: List[BlogUser] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    id: Optional[str] = None
