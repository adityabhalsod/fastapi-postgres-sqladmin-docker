# FastAPI + PostgreSQL + SQLAdmin + Docker

This project is a starter template for building modern web APIs using FastAPI, async SQLAlchemy, PostgreSQL, an admin panel with SQLAdmin, and Docker.

## Features

- Async FastAPI application
- PostgreSQL database (via Docker)
- SQLAlchemy ORM (async)
- Admin panel at `/admin/` with SQLAdmin
- Dockerized for easy local and production deployment


## Quick Start

### 1. Clone \& Go to Folder

```bash
git clone https://github.com/adityabhalsod/fastapi-postgres-sqladmin-docker.git
cd fastapi-postgres-sqladmin-docker
```


### 2. Create `.env` File

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_db
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/fastapi_db
```


### 3. Build and Run with Docker Compose

```bash
docker-compose up --build
```

- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)

## FAQ

- Browse and edit `/items/` via API or use the `/admin` panel.
- For production, secure `/admin` with authentication.

**Enjoy!** 🚀

