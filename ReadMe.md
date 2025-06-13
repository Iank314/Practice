# Taggable Bookmark Service

A simple RESTful API for saving, tagging, and querying bookmarks. Built with FastAPI, SQLAlchemy, and SQLite, it lets users create, list, update, and delete bookmarks with free‑form tags.

## 📦 Features

* **Create** bookmarks with URL, title, description, and tags
* **List** bookmarks filtered by user, tags (AND logic), and date range
* **Update** bookmark metadata and tags
* **Delete** bookmarks
* **In‑memory** or **SQLite** persistence

## ⚙️ Prerequisites

* Python 3.8+
* pip (Python package manager)

## 🚀 Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/taggable-bookmark-service.git
   cd taggable-bookmark-service
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .\.venv\Scripts\activate    # Windows PowerShell
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

* The API will be available at `http://127.0.0.1:8000`
* Swagger UI documentation at `http://127.0.0.1:8000/docs`

## 🗂 File Layout

```
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
```

## 📝 API Endpoints

* **POST** `/bookmarks/`
  Create a new bookmark.
  **Body**: JSON with `user_id`, `url`, `title`, `description`, `tags` (list of strings).

* **GET** `/bookmarks/`
  List bookmarks for a user.
  **Query Params**: `user_id` (int, required), `tags` (list, optional, AND filter), `start` (ISO date, optional), `end` (ISO date, optional).

* **PUT** `/bookmarks/{bookmark_id}`
  Update title/description/tags of a bookmark.
  **Body**: same as create minus `user_id`.

* **DELETE** `/bookmarks/{bookmark_id}`
  Delete a bookmark by its ID.

## 🧪 Running Tests

Use pytest to run both unit and end-to-end tests:

```bash
pytest -v
```


