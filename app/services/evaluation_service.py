from __future__ import annotations

from collections import defaultdict
from datetime import datetime

from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session, joinedload

from app.models import Criterion, CriterionGroup, ScoreEntry, Semester, Submission, SubmissionStatus, User, UserRole, Event, EventParticipation, ParticipationStatus
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
        min_points = score.criterion.min_points if score.criterion else 0
        previous_evidence = score.evidence
        previous_evidence_type = score.evidence_type or ""
        previous_evidence_file = score.evidence_file or ""
        score.self_score = _clamp_score(float(payload.get("self_score", 0) or 0), min_points, max_points)
        score.evidence = str(payload.get("evidence", "") or "").strip()
        if "evidence_type" in payload:
            score.evidence_type = str(payload["evidence_type"]).strip()
        if "evidence_file" in payload:
            score.evidence_file = str(payload["evidence_file"]).strip()
        if "evidence_status" in payload:
            score.evidence_status = str(payload["evidence_status"]).strip() or "pending"
        elif (
            score.evidence != previous_evidence
            or (score.evidence_type or "") != previous_evidence_type
            or (score.evidence_file or "") != previous_evidence_file
        ):
            score.evidence_status = "pending"
            if not score.evidence:
                score.advisor_feedback = ""
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
        min_points = score.criterion.min_points if score.criterion else 0
        score.advisor_score = _clamp_score(float(payload.get("advisor_score", 0) or 0), min_points, max_points)
        score.advisor_feedback = str(payload.get("advisor_feedback", "") or "").strip()

    submission.advisor_total = round(sum(item.advisor_score for item in submission.scores), 2)
    submission.advisor_note = advisor_note.strip()
    submission.status = SubmissionStatus.REVIEWED
    submission.reviewed_at = datetime.utcnow()
    submission.updated_at = datetime.utcnow()
    return submission


def get_submissions_for_semester(session: Session, semester_id: int) -> list[Submission]:
    return list(
        session.scalars(
            select(Submission)
            .where(Submission.semester_id == semester_id)
            .options(
                joinedload(Submission.student),
                joinedload(Submission.semester),
                joinedload(Submission.scores).joinedload(ScoreEntry.criterion).joinedload(Criterion.group),
            )
            .order_by(desc(Submission.updated_at))
        ).unique()
    )


def review_evidence(session: Session, submission_id: int, criterion_id: int, approved: bool, feedback: str = "") -> Submission:
    submission = load_submission(session, submission_id)
    if not submission:
        raise ValueError("Khong tim thay phieu danh gia.")

    score = next((item for item in submission.scores if item.criterion_id == criterion_id), None)
    if not score:
        raise ValueError("Khong tim thay minh chung.")

    score.evidence_status = "approved" if approved else "rejected"
    score.advisor_feedback = feedback.strip() or ("Đã duyệt minh chứng." if approved else "Minh chứng chưa hợp lệ.")
    score.advisor_score = score.self_score if approved else 0.0
    submission.advisor_total = round(sum(item.advisor_score for item in submission.scores), 2)
    submission.updated_at = datetime.utcnow()
    if submission.status == SubmissionStatus.DRAFT:
        submission.status = SubmissionStatus.SUBMITTED
    return submission


def admin_update_submission(
    session: Session,
    submission_id: int,
    score_payload: dict[int, dict[str, str | float]],
    student_note: str,
    advisor_note: str,
    status: str,
    submitted_at: datetime | None,
    reviewed_at: datetime | None,
) -> Submission:
    submission = load_submission(session, submission_id)
    if not submission:
        raise ValueError("Khong tim thay phieu danh gia.")

    for score in submission.scores:
        payload = score_payload.get(score.criterion_id, {})
        max_points = score.criterion.max_points if score.criterion else 0
        min_points = score.criterion.min_points if score.criterion else 0
        score.self_score = _clamp_score(float(payload.get("self_score", score.self_score) or 0), min_points, max_points)
        score.advisor_score = _clamp_score(float(payload.get("advisor_score", score.advisor_score) or 0), min_points, max_points)
        score.evidence = str(payload.get("evidence", score.evidence) or "").strip()
        score.evidence_type = str(payload.get("evidence_type", score.evidence_type or "") or "").strip()
        score.evidence_file = str(payload.get("evidence_file", score.evidence_file or "") or "").strip()
        score.evidence_status = str(payload.get("evidence_status", score.evidence_status or "pending") or "pending").strip()
        score.advisor_feedback = str(payload.get("advisor_feedback", score.advisor_feedback) or "").strip()

    submission.self_total = round(sum(item.self_score for item in submission.scores), 2)
    submission.advisor_total = round(sum(item.advisor_score for item in submission.scores), 2)
    submission.student_note = student_note.strip()
    submission.advisor_note = advisor_note.strip()
    submission.status = SubmissionStatus(status)
    submission.submitted_at = submitted_at
    submission.reviewed_at = reviewed_at
    submission.updated_at = datetime.utcnow()
    return submission


def admin_update_semester(session: Session, semester_id: int, start_date, end_date, is_active: bool) -> Semester:
    semester = session.get(Semester, semester_id)
    if not semester:
        raise ValueError("Khong tim thay hoc ky.")

    semester.start_date = start_date
    semester.end_date = end_date
    if is_active:
        set_active_semester(session, semester_id)
    else:
        semester.is_active = False
    return semester


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


def _clamp_score(value: float, min_points: float, max_points: float) -> float:
    return round(max(min_points, min(value, max_points)), 2)


def get_active_events(session: Session, semester_id: int) -> list[Event]:
    return list(session.scalars(select(Event).where(Event.semester_id == semester_id, Event.is_active.is_(True)).order_by(Event.name)))


def get_student_event_participations(session: Session, student_id: int) -> list[EventParticipation]:
    return list(session.scalars(select(EventParticipation).where(EventParticipation.student_id == student_id).options(joinedload(EventParticipation.event)).order_by(desc(EventParticipation.submitted_at))))


def submit_event_participation(session: Session, student_id: int, event_id: int, evidence_path: str | None = None) -> EventParticipation:
    existing = session.scalar(select(EventParticipation).where(EventParticipation.student_id == student_id, EventParticipation.event_id == event_id))
    if existing:
        raise ValueError("Ban da dang ky hoac tham gia su kien nay roi.")
    participation = EventParticipation(student_id=student_id, event_id=event_id, evidence_path=evidence_path)
    session.add(participation)
    session.flush()
    return participation


def get_pending_event_participations(session: Session) -> list[EventParticipation]:
    return list(session.scalars(select(EventParticipation).where(EventParticipation.status == ParticipationStatus.PENDING).options(joinedload(EventParticipation.event), joinedload(EventParticipation.student)).order_by(EventParticipation.submitted_at)))


def approve_event_participation(session: Session, participation_id: int) -> EventParticipation:
    participation = session.get(EventParticipation, participation_id)
    if not participation:
        raise ValueError("Khong tim thay ban ghi tham gia.")
    if participation.status != ParticipationStatus.PENDING:
        raise ValueError("Ban ghi da duoc xu ly truoc do.")

    participation.status = ParticipationStatus.APPROVED
    participation.reviewed_at = datetime.utcnow()

    # Apply points to student's submission for that semester
    event = participation.event
    submission = session.scalar(select(Submission).where(Submission.student_id == participation.student_id, Submission.semester_id == event.semester_id).options(joinedload(Submission.scores).joinedload(ScoreEntry.criterion)))
    if not submission:
        # Create submission if not exists
        submission = get_or_create_submission(session, participation.student_id, event.semester_id)

    # Find score entry for the event's criterion
    for score in submission.scores:
        if score.criterion_id == event.criterion_id:
            max_p = score.criterion.max_points if score.criterion else 0
            min_p = score.criterion.min_points if score.criterion else 0
            # Increase score by event points strictly
            score.self_score = _clamp_score(score.self_score + event.points, min_p, max_p)
            score.advisor_score = _clamp_score(score.advisor_score + event.points, min_p, max_p)
            # Add to evidence notes
            note_line = f"[+] Cong diem tu Su Kien: {event.name} ({event.points} d)"
            score.evidence = f"{score.evidence}\n{note_line}".strip()
            score.advisor_feedback = f"{score.advisor_feedback}\n{note_line}".strip()
            break
            
    submission.self_total = round(sum(item.self_score for item in submission.scores), 2)
    submission.advisor_total = round(sum(item.advisor_score for item in submission.scores), 2)
    session.flush()
    return participation
