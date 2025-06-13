from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

bookmark_tags = Table(
    'bookmark_tags', Base.metadata,
    Column('bookmark_id', Integer, ForeignKey('bookmarks.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    tags = relationship('Tag', secondary=bookmark_tags, back_populates='bookmarks')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    bookmarks = relationship('Bookmark', secondary=bookmark_tags, back_populates='tags')