from __future__ import annotations

from collections import defaultdict
from datetime import datetime

from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session, joinedload

from app.models import Criterion, CriterionGroup, ScoreEntry, Semester, Submission, SubmissionStatus, User, UserRole
from app.security import hash_password, verify_password


def authenticate(session: Session, username: str, password: str) -> User | None:
    user = session.scalar(select(User).where(User.username == username.strip()))
    if not user:
        return None
    return user if verify_password(password, user.password_hash) else None


def get_user_by_id(session: Session, user_id: int | None) -> User | None:
    return session.get(User, user_id) if user_id else None


def get_dashboard_stats(session: Session) -> dict[str, int]:
    return {
        "students": session.scalar(select(func.count()).select_from(User).where(User.role == UserRole.STUDENT)) or 0,
        "active_semesters": session.scalar(select(func.count()).select_from(Semester).where(Semester.is_active.is_(True))) or 0,
        "submitted_forms": session.scalar(select(func.count()).select_from(Submission).where(Submission.status == SubmissionStatus.SUBMITTED)) or 0,
        "reviewed_forms": session.scalar(select(func.count()).select_from(Submission).where(Submission.status == SubmissionStatus.REVIEWED)) or 0,
    }


def get_semesters(session: Session) -> list[Semester]:
    return list(session.scalars(select(Semester).order_by(desc(Semester.is_active), desc(Semester.start_date))))


def get_active_semester(session: Session) -> Semester | None:
    return session.scalar(select(Semester).where(Semester.is_active.is_(True)).order_by(desc(Semester.start_date)))


def set_active_semester(session: Session, semester_id: int) -> None:
    for semester in session.scalars(select(Semester)):
        semester.is_active = semester.id == semester_id


def create_semester(session: Session, name: str, academic_year: str, start_date, end_date) -> Semester:
    semester = Semester(name=name.strip(), academic_year=academic_year.strip(), start_date=start_date, end_date=end_date, is_active=False)
    session.add(semester)
    session.flush()
    return semester


def list_students(session: Session) -> list[User]:
    return list(session.scalars(select(User).where(User.role == UserRole.STUDENT).order_by(User.student_code)))


def create_student(session: Session, username: str, password: str, full_name: str, student_code: str, class_name: str, faculty: str, major: str, email: str) -> User:
    student = User(
        username=username.strip(),
        password_hash=hash_password(password),
        full_name=full_name.strip(),
        role=UserRole.STUDENT,
        student_code=student_code.strip(),
        class_name=class_name.strip(),
        faculty=faculty.strip(),
        major=major.strip(),
        email=email.strip(),
    )
    session.add(student)
    session.flush()
    return student


def get_criteria_tree(session: Session) -> list[CriterionGroup]:
    return list(session.scalars(select(CriterionGroup).options(joinedload(CriterionGroup.criteria)).order_by(CriterionGroup.display_order)).unique())


def load_submission(session: Session, submission_id: int) -> Submission | None:
    return session.scalar(
        select(Submission)
        .where(Submission.id == submission_id)
        .options(
            joinedload(Submission.student),
            joinedload(Submission.semester),
            joinedload(Submission.scores).joinedload(ScoreEntry.criterion).joinedload(Criterion.group),
        )
    )


def get_or_create_submission(session: Session, student_id: int, semester_id: int) -> Submission:
    submission = session.scalar(select(Submission).where(Submission.student_id == student_id, Submission.semester_id == semester_id).options(joinedload(Submission.scores)))
    if submission:
        return load_submission(session, submission.id)

    submission = Submission(student_id=student_id, semester_id=semester_id)
    session.add(submission)
    session.flush()
    for criterion in session.scalars(select(Criterion)):
        session.add(ScoreEntry(submission_id=submission.id, criterion_id=criterion.id))
    session.flush()
    return load_submission(session, submission.id)


def get_student_submissions(session: Session, student_id: int) -> list[Submission]:
    return list(session.scalars(select(Submission).where(Submission.student_id == student_id).options(joinedload(Submission.semester)).order_by(desc(Submission.updated_at))))


def get_pending_submissions(session: Session) -> list[Submission]:
    return list(
        session.scalars(
            select(Submission)
            .where(Submission.status.in_([SubmissionStatus.SUBMITTED, SubmissionStatus.REVIEWED]))
            .options(joinedload(Submission.student), joinedload(Submission.semester))
            .order_by(desc(Submission.updated_at))
        )
    )


def update_student_scores(session: Session, submission_id: int, score_payload: dict[int, dict[str, str | float]], student_note: str, submit: bool) -> Submission:
    submission = load_submission(session, submission_id)
    if not submission:
        raise ValueError("Khong tim thay phieu danh gia.")
    if submission.status == SubmissionStatus.REVIEWED:
        raise ValueError("Phieu da duoc duyet.")

    for score in submission.scores:
        payload = score_payload.get(score.criterion_id, {})
        max_points = score.criterion.max_points if score.criterion else 0
        score.self_score = _clamp_score(float(payload.get("self_score", 0) or 0), max_points)
        score.evidence = str(payload.get("evidence", "") or "").strip()
        if score.advisor_score == 0:
            score.advisor_score = score.self_score

    submission.self_total = round(sum(item.self_score for item in submission.scores), 2)
    submission.student_note = student_note.strip()
    submission.status = SubmissionStatus.SUBMITTED if submit else SubmissionStatus.DRAFT
    submission.submitted_at = datetime.utcnow() if submit else None
    submission.updated_at = datetime.utcnow()
    return submission


def update_advisor_scores(session: Session, submission_id: int, score_payload: dict[int, dict[str, str | float]], advisor_note: str) -> Submission:
    submission = load_submission(session, submission_id)
    if not submission:
        raise ValueError("Khong tim thay phieu danh gia.")

    for score in submission.scores:
        payload = score_payload.get(score.criterion_id, {})
        max_points = score.criterion.max_points if score.criterion else 0
        score.advisor_score = _clamp_score(float(payload.get("advisor_score", 0) or 0), max_points)
        score.advisor_feedback = str(payload.get("advisor_feedback", "") or "").strip()

    submission.advisor_total = round(sum(item.advisor_score for item in submission.scores), 2)
    submission.advisor_note = advisor_note.strip()
    submission.status = SubmissionStatus.REVIEWED
    submission.reviewed_at = datetime.utcnow()
    submission.updated_at = datetime.utcnow()
    return submission


def group_totals(submission: Submission) -> list[dict]:
    grouped: dict[int, dict] = defaultdict(lambda: {"title": "", "max_points": 0.0, "self_total": 0.0, "advisor_total": 0.0})
    for score in submission.scores:
        criterion = score.criterion
        if not criterion or not criterion.group:
            continue
        item = grouped[criterion.group.id]
        item["title"] = criterion.group.title
        item["max_points"] = criterion.group.max_points
        item["self_total"] += score.self_score
        item["advisor_total"] += score.advisor_score
    return list(grouped.values())


def serialize_submission(submission: Submission) -> dict:
    return {
        "id": submission.id,
        "student": submission.student.full_name if submission.student else "",
        "student_code": submission.student.student_code if submission.student else "",
        "semester": submission.semester.name if submission.semester else "",
        "status": submission.status.value,
        "self_total": submission.self_total,
        "advisor_total": submission.advisor_total,
        "scores": [
            {
                "criterion": score.criterion.title if score.criterion else "",
                "group": score.criterion.group.title if score.criterion and score.criterion.group else "",
                "self_score": score.self_score,
                "advisor_score": score.advisor_score,
                "evidence": score.evidence,
            }
            for score in submission.scores
        ],
    }


def _clamp_score(value: float, max_points: float) -> float:
    return round(max(0.0, min(value, max_points)), 2)
