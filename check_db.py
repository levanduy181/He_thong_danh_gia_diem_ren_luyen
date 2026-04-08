from app.db import get_session
from app.models import Submission, Semester
from sqlalchemy import select

with get_session() as s:
    subs = list(s.scalars(select(Submission)))
    for sub in subs:
        sem = s.get(Semester, sub.semester_id)
        sem_name = sem.name if sem else "?"
        print(f"Submission id={sub.id} semester={sem_name} self_total={sub.self_total} status={sub.status}")
