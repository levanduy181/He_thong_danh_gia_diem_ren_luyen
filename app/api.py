from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.db import get_session
from app.services.evaluation_service import get_active_semester, get_pending_submissions, get_semesters, load_submission, serialize_submission


router = APIRouter(prefix="/api", tags=["api"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "ptit-conduct-evaluation"}


@router.get("/semesters")
def api_semesters() -> list[dict]:
    with get_session() as session:
        return [{"id": semester.id, "name": semester.name, "academic_year": semester.academic_year, "is_active": semester.is_active} for semester in get_semesters(session)]


@router.get("/dashboard")
def api_dashboard() -> dict:
    with get_session() as session:
        active = get_active_semester(session)
        submissions = get_pending_submissions(session)
        return {"active_semester": active.name if active else None, "review_queue": len(submissions)}


@router.get("/submissions/{submission_id}")
def api_submission(submission_id: int) -> dict:
    with get_session() as session:
        submission = load_submission(session, submission_id)
        if not submission:
            raise HTTPException(status_code=404, detail="Khong tim thay phieu danh gia")
        return serialize_submission(submission)
