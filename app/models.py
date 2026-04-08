from __future__ import annotations

from datetime import date, datetime
from enum import Enum

from sqlalchemy import Date, DateTime, Enum as SqlEnum, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    ADVISOR = "advisor"
    STUDENT = "student"


class SubmissionStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(512))
    full_name: Mapped[str] = mapped_column(String(120))
    role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole))
    student_code: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)
    email: Mapped[str | None] = mapped_column(String(120), unique=True, nullable=True)
    class_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    faculty: Mapped[str | None] = mapped_column(String(120), nullable=True)
    major: Mapped[str | None] = mapped_column(String(120), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    submissions: Mapped[list["Submission"]] = relationship(back_populates="student")


class Semester(Base):
    __tablename__ = "semesters"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    academic_year: Mapped[str] = mapped_column(String(20))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    submissions: Mapped[list["Submission"]] = relationship(back_populates="semester")


class CriterionGroup(Base):
    __tablename__ = "criterion_groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    max_points: Mapped[float] = mapped_column(Float, default=0.0)

    criteria: Mapped[list["Criterion"]] = relationship(
        back_populates="group", order_by="Criterion.display_order", cascade="all, delete-orphan"
    )


class Criterion(Base):
    __tablename__ = "criteria"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("criterion_groups.id"))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    max_points: Mapped[float] = mapped_column(Float, default=0.0)
    display_order: Mapped[int] = mapped_column(Integer, default=0)

    group: Mapped["CriterionGroup"] = relationship(back_populates="criteria")
    scores: Mapped[list["ScoreEntry"]] = relationship(back_populates="criterion")


class Submission(Base):
    __tablename__ = "submissions"
    __table_args__ = (UniqueConstraint("student_id", "semester_id", name="uq_student_semester"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    status: Mapped[SubmissionStatus] = mapped_column(SqlEnum(SubmissionStatus), default=SubmissionStatus.DRAFT)
    self_total: Mapped[float] = mapped_column(Float, default=0.0)
    advisor_total: Mapped[float] = mapped_column(Float, default=0.0)
    student_note: Mapped[str] = mapped_column(Text, default="")
    advisor_note: Mapped[str] = mapped_column(Text, default="")
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student: Mapped["User"] = relationship(back_populates="submissions")
    semester: Mapped["Semester"] = relationship(back_populates="submissions")
    scores: Mapped[list["ScoreEntry"]] = relationship(
        back_populates="submission", cascade="all, delete-orphan", order_by="ScoreEntry.id"
    )


class ScoreEntry(Base):
    __tablename__ = "score_entries"
    __table_args__ = (UniqueConstraint("submission_id", "criterion_id", name="uq_submission_criterion"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(ForeignKey("submissions.id"))
    criterion_id: Mapped[int] = mapped_column(ForeignKey("criteria.id"))
    self_score: Mapped[float] = mapped_column(Float, default=0.0)
    advisor_score: Mapped[float] = mapped_column(Float, default=0.0)
    evidence: Mapped[str] = mapped_column(Text, default="")
    advisor_feedback: Mapped[str] = mapped_column(Text, default="")

    submission: Mapped["Submission"] = relationship(back_populates="scores")
    criterion: Mapped["Criterion"] = relationship(back_populates="scores")
