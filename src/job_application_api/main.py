from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from job_application_api.dependencies import get_database_session
from job_application_api.models import Candidate, JobApplication
from job_application_api.schemas import (
    CandidateCreate,
    CandidateResponse,
    JobApplicationCreate,
    JobApplicationResponse,
)

app = FastAPI(title="Job Application API")


@app.get("/")
def read_root():
    return {"message": "Job Application API is running"}


@app.get("/database-test")
def database_test(
    database_session: Session = Depends(get_database_session),
):
    return {"message": "Database session dependency is working"}


@app.post("/candidates", response_model=CandidateResponse, status_code=201)
def create_candidate(
    candidate_data: CandidateCreate,
    database_session: Session = Depends(get_database_session),
):
    candidate_record = Candidate(
        name=candidate_data.name,
        email=candidate_data.email,
        vacancy_id=candidate_data.vacancy_id,
    )

    database_session.add(candidate_record)

    try:
        database_session.commit()
    except IntegrityError:
        database_session.rollback()

        raise HTTPException(
            status_code=409,
            detail="A candidate with this email already exists.",
        )

    database_session.refresh(candidate_record)

    return candidate_record


@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(
    candidate_id: int,
    database_session: Session = Depends(get_database_session),
):
    candidate_record = database_session.get(Candidate, candidate_id)

    if candidate_record is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found",
        )

    return candidate_record


@app.post(
    "/job-applications",
    response_model=JobApplicationResponse,
    status_code=201,
)
def create_job_application(
    application_data: JobApplicationCreate,
    database_session: Session = Depends(get_database_session),
):
    application_record = JobApplication(
        title=application_data.title,
        description=application_data.description,
    )

    database_session.add(application_record)
    database_session.commit()
    database_session.refresh(application_record)

    return application_record


@app.get(
    "/job-applications/{application_id}",
    response_model=JobApplicationResponse,
)
def get_job_application(
    application_id: int,
    database_session: Session = Depends(get_database_session),
):
    application_record = database_session.get(
        JobApplication,
        application_id,
    )

    if application_record is None:
        raise HTTPException(
            status_code=404,
            detail="Job application not found",
        )

    return application_record


@app.get(
    "/job-applications/{application_id}/candidates",
    response_model=list[CandidateResponse],
)
def get_job_application_candidates(
    application_id: int,
    database_session: Session = Depends(get_database_session),
):
    application_record = database_session.get(
        JobApplication,
        application_id,
    )

    if application_record is None:
        raise HTTPException(
            status_code=404,
            detail="Job application not found",
        )

    return application_record.applicantsapp