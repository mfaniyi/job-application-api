from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class JobApplication(Base):
    __tablename__ = "vacancy"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200),nullable=False)
    description: Mapped[str] = mapped_column(String(1000),nullable=False)
    applicantsapp: Mapped[list["Candidate"]] = relationship(back_populates="vacancyrec")

class Candidate(Base):
    __tablename__ = "applicant"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    email: Mapped[str] = mapped_column(String(255),unique=True,nullable=False)
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancy.id"),nullable=False)
    vacancyrec: Mapped["JobApplication"] = relationship(back_populates="applicantsapp")