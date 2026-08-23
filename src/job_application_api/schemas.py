from pydantic import BaseModel, EmailStr


class JobApplicationCreate(BaseModel):
    title: str
    description: str


class JobApplicationResponse(BaseModel):
    id: int
    title: str
    description: str


class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    vacancy_id: int


class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    vacancy_id: int