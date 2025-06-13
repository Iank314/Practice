from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/bookmarks/", response_model=schemas.Bookmark)
def create(b: schemas.BookmarkCreate, db: Session=Depends(get_db)):
    return crud.create_bookmark(db, b)

@app.get("/bookmarks/", response_model=List[schemas.Bookmark])
def read(user_id: int, tags: List[str] = Query(None), start: str=None, end: str=None, db: Session=Depends(get_db)):
    return crud.get_bookmarks(db, user_id, tags, start, end)

@app.delete("/bookmarks/{bookmark_id}")
def delete(bookmark_id: int, db: Session=Depends(get_db)):
    if not crud.delete_bookmark(db, bookmark_id):
        raise HTTPException(status_code=404, detail="Bookmark not found")

@app.put("/bookmarks/{bookmark_id}", response_model=schemas.Bookmark)
def update(bookmark_id: int, data: schemas.BookmarkBase, db: Session=Depends(get_db)):
    updated = crud.update_bookmark(db, bookmark_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return updated