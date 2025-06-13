import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end():
    # create
    resp = client.post("/bookmarks/", json={
        "user_id": 1,
        "url": "http://test",
        "title": "T",
        "description": "",
        "tags": ["x","y"]
    })
    assert resp.status_code == 200
    bid = resp.json()["id"]

    # list
    resp = client.get("/bookmarks/", params={"user_id":1, "tags":["x"]})
    assert resp.status_code == 200
    assert len(resp.json()) == 1

    # delete
    resp = client.delete(f"/bookmarks/{bid}")
    assert resp.status_code == 200
    # confirm gone
    resp = client.get("/bookmarks/", params={"user_id":1})
    assert resp.json() == []