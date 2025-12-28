# To-Do List — Fullstack (React + FastAPI)

Classic full-stack ToDo application built with **React** (frontend) and **FastAPI** (backend).  
The project focuses on **clean architecture**, **JWT authentication**, and **scalable backend structure**.

---

## Features

### Authentication
- JWT-based authentication
- Login using **email OR username**
- Password hashing (Argon2 / Passlib)
- Protected API routes
- Architecture ready for:
  - email activation
  - refresh tokens
  - OAuth (Google / GitHub) — optional, not required

### Backend
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2 validation
- Modular structure (`auth`, `core`, `todos`)
- Database configured via `.env`
- PostgreSQL / SQLite support

### Frontend
- React
- Tailwind CSS
- Modular components
- Responsive UI

---

## Project Structure (Backend)

```
back/
├── app/
│ ├── auth/
│ │ ├── router.py
│ │ ├── schemas.py
│ │ ├── crud.py
│ │ ├── models.py
│ │ └── security.py
│ ├── core/
│ │ ├── config.py
│ │ ├── database.py
│ │ └── security.py
│ ├── todos/
│ └── main.py
├── alembic/
├── alembic.ini
├── requirements.txt
├── .env
└── .gitignore
```

## Requirements

- Python **3.11+**
- Node.js **18+**
- PostgreSQL *(optional – SQLite supported)*

---

## Environment Variables

Create a `.env` file in the `back/` directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
SECRET_KEY=super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

⚠️ .env is ignored by git and must not be committed.

## Backend Setup

```
cd back
python -m venv venv
source venv/bin/activate   # Linux 

pip install -r requirements.txt
```

Run backend

```
uvicorn app.main:app --reload
```

API will be available at:
👉 http://localhost:8000

Swagger docs:
👉 http://localhost:8000/docs

## Database & Migrations

The project uses SQLAlchemy + Alembic.

Important notes:

Database must exist before running migrations (PostgreSQL does NOT create it automatically)

Tables are created via Alembic migrations


PostgreSQL example:

```
sudo -i -u postgres
psql
CREATE DATABASE auth_db;
```

## Frontend Setup

```
cd front
npm install
npm run dev
```

Frontend will be available at:
👉 http://localhost:5173

