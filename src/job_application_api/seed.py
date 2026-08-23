from job_application_api.database import SessionLocal
from job_application_api.models import Candidate, JobApplication

python_job = JobApplication(
    title="Python Backend Engineer",
    description="Build and maintain backend APIs with Python and FastAPI.",
)

data_job = JobApplication(
    title="Data Analyst",
    description="Analyze business data and create reports and dashboards.",
)

michael_candidate = Candidate(
    name="Michael",
    email="michael@example.com",
    vacancyrec=python_job,
)

john_candidate = Candidate(
    name="John",
    email="john@example.com",
    vacancyrec=python_job,
)

sarah_candidate = Candidate(
    name="Sarah",
    email="sarah@example.com",
    vacancyrec=data_job,
)

def main():
    with SessionLocal.begin() as database_session:
        database_session.add_all(
            [
                python_job,
                data_job,
                michael_candidate,
                john_candidate,
                sarah_candidate,
            ]
        )


if __name__ == "__main__":
    main()