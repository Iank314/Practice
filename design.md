taggable-bookmark-service/
├── README.md
├── design.md         # architecture and data model
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py       # FastAPI application entrypoint
│   ├── database.py   # SQLite setup
│   ├── models.py     # SQLAlchemy ORM models
│   ├── schemas.py    # Pydantic request/response schemas
│   └── crud.py       # CRUD operations
└── tests/
    ├── test_crud.py  # unit tests for CRUD logic
    └── test_api.py   # end-to-end tests via TestClient


