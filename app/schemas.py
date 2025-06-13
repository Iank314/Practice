from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    class Config:
        orm_mode = True

class BookmarkBase(BaseModel):
    url: HttpUrl
    title: str
    description: Optional[str] = None
    tags: List[str] = []

class BookmarkCreate(BookmarkBase):
    user_id: int

class Bookmark(BookmarkBase):
    id: int
    user_id: int
    created: datetime
    tags: List[Tag]
    class Config:
        orm_mode = True