from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ----- Author Schemas -----
class AuthorBase(BaseModel):
    name: str
    email: EmailStr

class AuthorCreate(AuthorBase):
    pass

class AuthorRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class AuthorResponse(AuthorRead):
    posts: List["PostRead"] = []  # forward reference to PostRead

    class Config:
        from_attributes = True

# ----- Post Schemas -----
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    author_id: int

class PostRead(PostBase):
    id: int
    author: AuthorRead  # nested author info

    class Config:
        from_attributes = True

class PostResponse(PostRead):
    author_id: int  # include author_id in addition to nested author

# ----- Resolve forward references -----
AuthorResponse.model_rebuild()
