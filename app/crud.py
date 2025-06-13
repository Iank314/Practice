from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

# -------- Bookmarks --------
def create_bookmark(db: Session, b: schemas.BookmarkCreate):
    tag_objs = []
    for name in b.tags:
        tag = db.query(models.Tag).filter(models.Tag.name==name).first()
        if not tag:
            tag = models.Tag(name=name)
            db.add(tag)
        tag_objs.append(tag)
    db_book = models.Bookmark(
        user_id=b.user_id,
        url=str(b.url),
        title=b.title,
        description=b.description,
        tags=tag_objs
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_bookmarks(db: Session, user_id: int, tags: List[str]=None, start: str=None, end: str=None):
    query = db.query(models.Bookmark).filter(models.Bookmark.user_id==user_id)
    if tags:
        for name in tags:
            query = query.filter(models.Bookmark.tags.any(models.Tag.name==name))
    if start:
        query = query.filter(models.Bookmark.created >= start)
    if end:
        query = query.filter(models.Bookmark.created <= end)
    return query.all()


def delete_bookmark(db: Session, bookmark_id: int):
    db_book = db.query(models.Bookmark).get(bookmark_id)
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True


def update_bookmark(db: Session, bookmark_id: int, data: schemas.BookmarkBase):
    db_book = db.query(models.Bookmark).get(bookmark_id)
    if not db_book:
        return None

    # Update simple fields
    db_book.url = str(data.url)
    db_book.title = data.title
    db_book.description = data.description

    # Rebuild the tag list
    tag_objs = []
    for name in data.tags:
        tag = db.query(models.Tag).filter(models.Tag.name == name).first()
        if not tag:
            tag = models.Tag(name=name)
            db.add(tag)
        tag_objs.append(tag)

    db_book.tags = tag_objs

    db.commit()
    db.refresh(db_book)
    return db_book
