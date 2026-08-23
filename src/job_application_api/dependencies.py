from collections.abc import Generator

from sqlalchemy.orm import Session

from job_application_api.database import SessionLocal


def get_database_session() -> Generator[Session, None, None]:
    database_session = SessionLocal()

    try:
        yield database_session
    finally:
        database_session.close()