# Job Application API

A FastAPI application that manages job vacancies and candidates using PostgreSQL, SQLAlchemy ORM, and Alembic migrations.

---

## Project Structure

The application uses two related database tables:

- `vacancy` - Stores job vacancy information.
- `applicant` - Stores candidate information for vacancy applications.

### Relationship

- One vacancy can have many applicants.
- Each applicant belongs to one vacancy.
- Candidate email addresses must be unique.

---

## Technologies

- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Psycopg
- Docker Compose
- uv
- Pytest

---

## Setup

### 1. Install Dependencies

```bash
uv sync
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/job_application_db
```

### 3. Start PostgreSQL

Start the PostgreSQL container using Docker Compose:

```bash
docker compose up -d
```

Verify that the container is running:

```bash
docker compose ps
```

### 4. Run Database Migrations

Apply all pending database migrations:

```bash
uv run alembic upgrade head
```

### 5. Seed Sample Data

Populate the database with sample records:

```bash
uv run python -m job_application_api.seed
```

### 6. Start the API

Run the FastAPI development server:

```bash
uv run fastapi dev src/job_application_api/main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Database Migrations

### Create a New Migration

After making changes to your SQLAlchemy models, generate a migration:

```bash
uv run alembic revision --autogenerate -m "describe the change"
```

### Apply Migrations

```bash
uv run alembic upgrade head
```

### Check Current Migration Version

```bash
uv run alembic current
```

---

## Testing

Run the test suite:

```bash
uv run pytest
```

---

## Docker Compose

The local PostgreSQL database is defined in `docker-compose.yml`.

### Database Configuration

```text
Database   : job_application_db
User       : postgres
Port       : 5432
Container  : job_application_postgres
```

PostgreSQL data is stored in a Docker named volume, allowing data to persist even when the container is stopped or restarted.

### Stop the Database

```bash
docker compose down
```

### Remove the Database and Persistent Volume

```bash
docker compose down -v
```

---

## API Endpoints

### Health Check

```http
GET /
```

Returns the API health status.

### Database Connection Test

```http
GET /database-test
```

Tests the database connection.

### Candidates

#### Create Candidate

```http
POST /candidates
```

#### Get Candidate

```http
GET /candidates/{candidate_id}
```

### Job Applications

#### Create Job Application

```http
POST /job-applications
```

#### Get Job Application

```http
GET /job-applications/{application_id}
```

#### Get Candidates for a Vacancy

```http
GET /job-applications/{application_id}/candidates
```

---

## Data Rules

- Candidate email addresses must be unique.
- A candidate must belong to a vacancy.
- A vacancy can have multiple candidates.
- A candidate cannot apply to multiple vacancies.

---