import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app import crud, models, schemas

@pytest.fixture(scope="module")
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal()


def test_create_and_query(db):
    b = schemas.BookmarkCreate(user_id=1, url="http://example.com", title="Ex", description=None, tags=["foo"])
    created = crud.create_bookmark(db, b)
    assert created.id == 1
    results = crud.get_bookmarks(db, 1, tags=["foo"])
    assert len(results) == 1


def test_delete(db):
    assert crud.delete_bookmark(db, 1)
    assert not crud.get_bookmarks(db, 1)