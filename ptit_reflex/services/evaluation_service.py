from __future__ import annotations

from datetime import datetime

from sqlalchemy import desc, select
from sqlalchemy.orm import Session, joinedload

from ptit_reflex.models import Criterion, CriterionGroup, ScoreEntry, Semester, Submission, Event, EventParticipation, ParticipationStatus


def get_semesters(session: Session) -> list[Semester]:
    return list(session.scalars(select(Semester).order_by(desc(Semester.is_active), desc(Semester.start_date))))


def get_criteria_tree(session: Session) -> list[CriterionGroup]:
    return list(session.scalars(select(CriterionGroup).options(joinedload(CriterionGroup.criteria)).order_by(CriterionGroup.display_order)).unique())


def get_or_create_submission(session: Session, student_id: int, semester_id: int) -> Submission:
    submission = session.scalar(select(Submission).where(Submission.student_id == student_id, Submission.semester_id == semester_id).options(joinedload(Submission.scores)))
    if submission:
        return session.scalar(
            select(Submission)
            .where(Submission.id == submission.id)
            .options(joinedload(Submission.scores).joinedload(ScoreEntry.criterion))
        )

    submission = Submission(student_id=student_id, semester_id=semester_id)
    session.add(submission)
    session.flush()
    for criterion in session.scalars(select(Criterion)):
        session.add(ScoreEntry(submission_id=submission.id, criterion_id=criterion.id))
    session.flush()
    return session.scalar(
        select(Submission)
        .where(Submission.id == submission.id)
        .options(joinedload(Submission.scores).joinedload(ScoreEntry.criterion))
    )


def _clamp_score(value: float, min_points: float, max_points: float) -> float:
    return round(max(min_points, min(value, max_points)), 2)


def get_active_events(session: Session, semester_id: int) -> list[Event]:
    return list(session.scalars(select(Event).where(Event.semester_id == semester_id, Event.is_active.is_(True)).order_by(Event.name)))


def submit_event_participation(session: Session, student_id: int, event_id: int, evidence_path: str | None = None) -> EventParticipation:
    existing = session.scalar(select(EventParticipation).where(EventParticipation.student_id == student_id, EventParticipation.event_id == event_id))
    if existing:
        raise ValueError("Ban da dang ky hoac tham gia su kien nay roi.")
    participation = EventParticipation(student_id=student_id, event_id=event_id, evidence_path=evidence_path)
    session.add(participation)
    session.flush()
    return participation


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

