from __future__ import annotations

from datetime import date

from nicegui import app, ui
from sqlalchemy.exc import IntegrityError

from app.api import router as api_router
from app.config import DATA_DIR, STORAGE_SECRET
from app.db import Base, engine, get_session
from app.models import SubmissionStatus, UserRole
from app.services.evaluation_service import (
    authenticate,
    create_semester,
    create_student,
    get_active_semester,
    get_criteria_tree,
    get_dashboard_stats,
    get_or_create_submission,
    get_pending_submissions,
    get_semesters,
    get_student_submissions,
    get_user_by_id,
    group_totals,
    list_students,
    load_submission,
    set_active_semester,
    update_advisor_scores,
    update_student_scores,
)
from app.services.seed import seed_default_data


DATA_DIR.mkdir(parents=True, exist_ok=True)
Base.metadata.create_all(engine)
with get_session() as session:
    seed_default_data(session)

app.include_router(api_router)

ui.add_head_html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body, .nicegui-content {
            font-family: "Manrope", sans-serif;
            background: linear-gradient(180deg, #f7fbff 0%, #edf3f9 100%);
            color: #17324a;
        }
        .mono { font-family: "IBM Plex Mono", monospace; }
        .surface {
            background: rgba(255,255,255,0.96);
            border: 1px solid #e5edf5;
            box-shadow: 0 20px 40px rgba(15,23,42,0.08);
        }
        .sidebar-panel {
            background: linear-gradient(180deg, #0f172a 0%, #0f3d64 100%);
            box-shadow: 0 28px 60px rgba(15,23,42,0.22);
        }
        .glass {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
        }
        .soft-tag {
            border-radius: 999px;
            padding: 6px 10px;
            font-size: .82rem;
            font-weight: 700;
            background: #f5f8fb;
            color: #4b637d;
        }
        .criterion {
            border: 1px solid #e5edf5;
            border-radius: 20px;
            background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
        }
        .section-label {
            text-transform: uppercase;
            letter-spacing: .16em;
            font-size: .72rem;
            font-weight: 800;
            color: #6b8196;
        }
        .q-field--outlined .q-field__control { border-radius: 16px !important; }
    </style>
    """
)


def current_user():
    with get_session() as session:
        return get_user_by_id(session, app.storage.user.get("user_id"))


def require_login() -> bool:
    if not app.storage.user.get("user_id"):
        ui.navigate.to("/login")
        return False
    return True


def logout() -> None:
    app.storage.user.clear()
    ui.navigate.to("/login")


def role_text(role: UserRole) -> str:
    return {
        UserRole.ADMIN: "Quan tri",
        UserRole.ADVISOR: "Co van hoc tap",
        UserRole.STUDENT: "Sinh vien",
    }[role]


def status_meta(status: SubmissionStatus) -> tuple[str, str]:
    return {
        SubmissionStatus.DRAFT: ("Ban nhap", "grey"),
        SubmissionStatus.SUBMITTED: ("Cho duyet", "warning"),
        SubmissionStatus.REVIEWED: ("Da duyet", "positive"),
    }[status]


def metric_card(label: str, value: str, note: str, dark: bool = False) -> None:
    css = "glass text-white" if dark else "surface"
    with ui.card().classes(f"{css} rounded-[28px] p-5 gap-2 min-w-[210px] flex-1"):
        ui.label(label).classes("section-label")
        ui.label(value).classes("text-3xl font-extrabold")
        ui.label(note).classes("text-sm opacity-75")


def topbar(user, subtitle: str) -> None:
    with ui.card().classes("surface rounded-[30px] p-6 gap-4"):
        with ui.row().classes("w-full items-start justify-between gap-4 flex-wrap"):
            with ui.column().classes("gap-2"):
                ui.label("PTIT Conduct Evaluation").classes("text-4xl font-black text-slate-900")
                ui.label(subtitle).classes("text-[15px] leading-7 text-slate-500 max-w-3xl")
            with ui.row().classes("items-center gap-3 flex-wrap"):
                ui.badge(role_text(user.role), color="primary").props("outline")
                if user.faculty:
                    ui.badge(user.faculty, color="orange").props("outline")
                ui.button("Dang xuat", on_click=logout, icon="logout").classes("bg-slate-900 text-white rounded-2xl")


def sidebar(user) -> None:
    nav = {
        UserRole.ADMIN: ["Tong quan", "Hoc ky", "Sinh vien", "Tieu chi"],
        UserRole.ADVISOR: ["Hang cho duyet", "Duyet phieu", "Nhan xet"],
        UserRole.STUDENT: ["Tu danh gia", "Tien do", "Lich su"],
    }[user.role]
    with ui.column().classes("w-full gap-5"):
        ui.label("PTIT").classes("text-2xl font-black tracking-[0.35em] text-white")
        with ui.card().classes("glass rounded-[28px] p-5 gap-3 shadow-none"):
            ui.label("Nguoi dung").classes("section-label text-white/60")
            ui.label(user.full_name).classes("text-xl font-bold text-white")
            ui.label(role_text(user.role)).classes("text-sm text-white/75")
            if user.class_name:
                ui.label(f"Lop {user.class_name}").classes("soft-tag w-fit")
        with ui.column().classes("gap-2"):
            for idx, item in enumerate(nav):
                active = "bg-white/15 border-white/20" if idx == 0 else "bg-white/5 border-white/10"
                with ui.row().classes(f"{active} items-center gap-3 rounded-2xl border px-4 py-3 text-white"):
                    ui.icon("dashboard_customize" if idx == 0 else "chevron_right")
                    ui.label(item).classes("text-sm font-semibold")


def global_stats() -> None:
    with get_session() as session:
        stats = get_dashboard_stats(session)
    with ui.row().classes("w-full gap-4 flex-wrap"):
        metric_card("Sinh vien", str(stats["students"]), "Tong tai khoan sinh vien")
        metric_card("Hoc ky mo", str(stats["active_semesters"]), "Hoc ky dang kich hoat")
        metric_card("Cho duyet", str(stats["submitted_forms"]), "Phieu da gui co van")
        metric_card("Da duyet", str(stats["reviewed_forms"]), "Phieu da xac nhan")


def activate_semester(semester_id: int) -> None:
    with get_session() as session:
        set_active_semester(session, semester_id)
    ui.notify("Da cap nhat hoc ky hoat dong", color="positive")
    render_admin_dashboard.refresh()


@ui.refreshable
def render_admin_dashboard() -> None:
    with get_session() as session:
        semesters = get_semesters(session)
        students = list_students(session)
        criteria = get_criteria_tree(session)
        active = get_active_semester(session)

    with ui.row().classes("w-full gap-4 flex-wrap"):
        metric_card("Hoc ky hien tai", active.name if active else "Chua mo", "Hoc ky ap dung cho sinh vien")
        metric_card("Sinh vien", str(len(students)), "So tai khoan hien co")
        metric_card("Nhom tieu chi", str(len(criteria)), "Bo tieu chi danh gia")

    with ui.tabs().classes("w-full") as tabs:
        tab_overview = ui.tab("Tong quan")
        tab_semester = ui.tab("Hoc ky")
        tab_student = ui.tab("Sinh vien")
        tab_criteria = ui.tab("Tieu chi")

    with ui.tab_panels(tabs, value=tab_overview).classes("w-full bg-transparent"):
        with ui.tab_panel(tab_overview).classes("px-0"):
            with ui.row().classes("w-full gap-5 flex-wrap"):
                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-[1.2] min-w-[320px]"):
                    ui.label("Dashboard quan tri").classes("text-2xl font-bold")
                    ui.label("Khong gian nay tap trung vao mo hoc ky, quan ly tai khoan va theo doi bo tieu chi.").classes("text-slate-500 leading-7")
                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-1 min-w-[300px]"):
                    ui.label("Tac vu nhanh").classes("text-2xl font-bold")
                    for line in [
                        "1. Tao hoc ky moi.",
                        "2. Them tai khoan sinh vien.",
                        "3. Kich hoat hoc ky de mo dot danh gia.",
                    ]:
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("check_circle", color="positive")
                            ui.label(line)

        with ui.tab_panel(tab_semester).classes("px-0"):
            with ui.row().classes("w-full gap-5 flex-wrap items-start"):
                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-1 min-w-[320px]"):
                    ui.label("Tao hoc ky").classes("text-2xl font-bold")
                    semester_name = ui.input("Ten hoc ky", value="Hoc ky he 2026").props("outlined dense").classes("w-full")
                    academic_year = ui.input("Nam hoc", value="2025-2026").props("outlined dense").classes("w-full")
                    start_date = ui.input("Ngay bat dau", value=str(date.today())).props("outlined dense").classes("w-full")
                    end_date = ui.input("Ngay ket thuc", value=str(date.today())).props("outlined dense").classes("w-full")

                    def create_semester_action() -> None:
                        try:
                            with get_session() as session:
                                create_semester(session, semester_name.value or "", academic_year.value or "", date.fromisoformat(start_date.value), date.fromisoformat(end_date.value))
                            ui.notify("Da tao hoc ky moi", color="positive")
                            render_admin_dashboard.refresh()
                        except ValueError:
                            ui.notify("Ngay thang phai theo YYYY-MM-DD", color="negative")
                        except IntegrityError:
                            ui.notify("Hoc ky da ton tai", color="negative")

                    ui.button("Luu hoc ky", on_click=create_semester_action, icon="calendar_month").classes("bg-slate-900 text-white rounded-2xl")

                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-[1.35] min-w-[360px]"):
                    ui.label("Danh sach hoc ky").classes("text-2xl font-bold")
                    for semester in semesters:
                        with ui.row().classes("criterion items-center justify-between gap-4 p-4 w-full flex-wrap"):
                            with ui.column().classes("gap-1"):
                                ui.label(semester.name).classes("text-lg font-bold")
                                ui.label(f"Nam hoc {semester.academic_year}").classes("text-sm text-slate-500")
                                ui.label(f"{semester.start_date.isoformat()} den {semester.end_date.isoformat()}").classes("text-sm text-slate-500")
                            btn = ui.button("Kich hoat", on_click=lambda sid=semester.id: activate_semester(sid)).classes("bg-orange-500 text-white rounded-2xl")
                            if semester.is_active:
                                btn.disable()

        with ui.tab_panel(tab_student).classes("px-0"):
            with ui.row().classes("w-full gap-5 flex-wrap items-start"):
                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-1 min-w-[320px]"):
                    ui.label("Them sinh vien").classes("text-2xl font-bold")
                    username = ui.input("Username", value="b23dccn999").props("outlined dense").classes("w-full")
                    password = ui.input("Mat khau", value="student123").props("outlined dense").classes("w-full")
                    full_name = ui.input("Ho ten", value="Sinh Vien Moi").props("outlined dense").classes("w-full")
                    student_code = ui.input("Ma sinh vien", value="B23DCCN999").props("outlined dense").classes("w-full")
                    class_name = ui.input("Lop", value="D23CQCN01-N").props("outlined dense").classes("w-full")
                    faculty = ui.input("Khoa", value="Cong nghe thong tin").props("outlined dense").classes("w-full")
                    major = ui.input("Nganh", value="Cong nghe thong tin").props("outlined dense").classes("w-full")
                    email = ui.input("Email", value="svmoi@ptit.edu.vn").props("outlined dense").classes("w-full")

                    def create_student_action() -> None:
                        try:
                            with get_session() as session:
                                create_student(session, username.value or "", password.value or "", full_name.value or "", student_code.value or "", class_name.value or "", faculty.value or "", major.value or "", email.value or "")
                            ui.notify("Da them sinh vien", color="positive")
                            render_admin_dashboard.refresh()
                        except IntegrityError:
                            ui.notify("Du lieu trung lap", color="negative")

                    ui.button("Tao tai khoan", on_click=create_student_action, icon="person_add").classes("bg-slate-900 text-white rounded-2xl")

                with ui.card().classes("surface rounded-[28px] p-6 gap-4 flex-[1.4] min-w-[360px]"):
                    ui.label("Danh sach sinh vien").classes("text-2xl font-bold")
                    for student in students:
                        with ui.row().classes("criterion items-center justify-between gap-4 p-4 w-full flex-wrap"):
                            with ui.column().classes("gap-1"):
                                ui.label(student.full_name).classes("text-lg font-bold")
                                ui.label(f"{student.student_code} • {student.class_name}").classes("text-sm text-slate-500 mono")
                                ui.label(f"{student.major} • {student.email}").classes("text-sm text-slate-500")
                            ui.badge(student.faculty or "PTIT", color="primary").props("outline")

        with ui.tab_panel(tab_criteria).classes("px-0"):
            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                ui.label("Bo tieu chi").classes("text-2xl font-bold")
                for group in criteria:
                    with ui.expansion(f"{group.title} • toi da {group.max_points} diem", value=False).classes("w-full bg-slate-50"):
                        for criterion in group.criteria:
                            with ui.row().classes("criterion items-start justify-between gap-4 p-4 w-full flex-wrap"):
                                with ui.column().classes("gap-1 flex-1"):
                                    ui.label(criterion.title).classes("font-bold")
                                    ui.label(criterion.description).classes("text-sm text-slate-500")
                                ui.label(f"{criterion.max_points} diem").classes("soft-tag")


@ui.refreshable
def render_student_dashboard(student_id: int) -> None:
    with get_session() as session:
        active = get_active_semester(session)
        submissions = get_student_submissions(session, student_id)
        groups = get_criteria_tree(session)
        submission = get_or_create_submission(session, student_id, active.id) if active else None

    if not active or not submission:
        with ui.card().classes("surface rounded-[28px] p-6"):
            ui.label("Chua co hoc ky dang hoat dong").classes("text-2xl font-bold")
            ui.label("Quan tri can kich hoat hoc ky truoc khi sinh vien tu danh gia.").classes("text-slate-500")
        return

    status_label, status_color = status_meta(submission.status)
    submitted_count = sum(1 for item in submissions if item.status != SubmissionStatus.DRAFT)

    with ui.row().classes("w-full gap-4 flex-wrap"):
        metric_card("Hoc ky", active.name, "Dot danh gia hien tai")
        metric_card("Trang thai", status_label, "Tien trinh xu ly cua phieu")
        metric_card("So lan nop", str(submitted_count), "Phieu da gui trong lich su")

    with ui.row().classes("w-full gap-5 flex-wrap items-start"):
        with ui.column().classes("flex-[1.7] min-w-[380px] gap-5"):
            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                with ui.row().classes("w-full items-start justify-between gap-4 flex-wrap"):
                    with ui.column().classes("gap-2"):
                        ui.label("Phieu tu danh gia ren luyen").classes("text-2xl font-bold")
                        ui.label("Bo cuc theo huong cong sinh vien: tach nhom tieu chi, nhap diem, bo sung minh chung va nop cho co van.").classes("text-slate-500 leading-7")
                    ui.badge(status_label, color=status_color)

                student_inputs = {}
                score_lookup = {score.criterion_id: score for score in submission.scores}

                for group in groups:
                    current_total = sum(score_lookup[item.id].self_score for item in group.criteria)
                    with ui.expansion(f"{group.title} • {current_total}/{group.max_points} diem", value=True).classes("w-full bg-slate-50"):
                        for criterion in group.criteria:
                            score = score_lookup[criterion.id]
                            with ui.row().classes("criterion items-start gap-4 p-4 w-full flex-wrap"):
                                with ui.column().classes("flex-1 min-w-[260px] gap-2"):
                                    ui.label(criterion.title).classes("text-lg font-bold")
                                    ui.label(criterion.description).classes("text-sm text-slate-500 leading-7")
                                    ui.label(f"Diem toi da: {criterion.max_points}").classes("soft-tag w-fit")
                                with ui.column().classes("flex-1 min-w-[260px] gap-3"):
                                    score_input = ui.number("Diem tu cham", value=score.self_score, min=0, max=criterion.max_points, step=0.5, format="%.1f").props("outlined dense").classes("w-full")
                                    evidence_input = ui.textarea("Minh chung / ghi chu", value=score.evidence).props("outlined autogrow").classes("w-full")
                                student_inputs[criterion.id] = {"self_score": score_input, "evidence": evidence_input}

                student_note = ui.textarea("Nhan xet cua sinh vien", value=submission.student_note).props("outlined autogrow").classes("w-full")

                def save_student_form(submit: bool) -> None:
                    payload = {
                        criterion_id: {"self_score": fields["self_score"].value or 0, "evidence": fields["evidence"].value or ""}
                        for criterion_id, fields in student_inputs.items()
                    }
                    with get_session() as session:
                        update_student_scores(session, submission.id, payload, student_note.value or "", submit)
                    ui.notify("Da gui phieu danh gia" if submit else "Da luu ban nhap", color="positive")
                    render_student_dashboard.refresh(student_id)

                with ui.row().classes("items-center justify-between gap-4 flex-wrap"):
                    with ui.row().classes("gap-3 flex-wrap"):
                        ui.button("Luu ban nhap", on_click=lambda: save_student_form(False), icon="save").classes("bg-slate-900 text-white rounded-2xl")
                        submit_btn = ui.button("Gui co van duyet", on_click=lambda: save_student_form(True), icon="send").classes("bg-orange-500 text-white rounded-2xl")
                        if submission.status == SubmissionStatus.REVIEWED:
                            submit_btn.disable()
                    ui.label(f"Tong diem tu cham: {submission.self_total}").classes("soft-tag")

        with ui.column().classes("flex-1 min-w-[320px] gap-5"):
            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                ui.label("Tong hop theo nhom").classes("text-2xl font-bold")
                for total in group_totals(submission):
                    percent = 0 if not total["max_points"] else total["self_total"] / total["max_points"]
                    ui.label(total["title"]).classes("font-bold")
                    ui.linear_progress(value=percent, color="primary").classes("w-full h-3 rounded-full")
                    ui.label(f"Sinh vien {total['self_total']} • Co van {total['advisor_total']} / {total['max_points']}").classes("text-sm text-slate-500")

            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                ui.label("Lich su ket qua").classes("text-2xl font-bold")
                for item in submissions or [submission]:
                    label, color = status_meta(item.status)
                    with ui.row().classes("criterion items-center justify-between gap-4 p-4 w-full flex-wrap"):
                        with ui.column().classes("gap-1"):
                            ui.label(item.semester.name if item.semester else "Hoc ky").classes("font-bold")
                            ui.label(f"Tu cham {item.self_total} • Co van {item.advisor_total}").classes("text-sm text-slate-500")
                        ui.badge(label, color=color)


@ui.refreshable
def render_advisor_dashboard() -> None:
    with get_session() as session:
        submissions = get_pending_submissions(session)

    with ui.row().classes("w-full gap-4 flex-wrap"):
        metric_card("Cho duyet", str(sum(1 for item in submissions if item.status == SubmissionStatus.SUBMITTED)), "Sinh vien da nop phieu")
        metric_card("Da duyet", str(sum(1 for item in submissions if item.status == SubmissionStatus.REVIEWED)), "Phieu da xac nhan")
        metric_card("Tong ho so", str(len(submissions)), "Danh sach hien thi cho co van")

    if not submissions:
        with ui.card().classes("surface rounded-[28px] p-6"):
            ui.label("Chua co phieu nao can xu ly").classes("text-2xl font-bold")
            return

    with ui.row().classes("w-full gap-5 flex-wrap items-start"):
        with ui.column().classes("flex-1 min-w-[320px] gap-5"):
            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                ui.label("Hang cho duyet").classes("text-2xl font-bold")
                options = {f"{item.student.student_code} • {item.student.full_name} • {item.semester.name}": item.id for item in submissions}
                selected = ui.select(options=options, label="Chon phieu can xem", value=next(iter(options.values()))).props("outlined dense").classes("w-full")
                for item in submissions:
                    label, color = status_meta(item.status)
                    with ui.card().classes("criterion p-4 gap-2 shadow-none"):
                        ui.label(item.student.full_name).classes("font-bold")
                        ui.label(f"{item.student.student_code} • {item.semester.name}").classes("text-sm text-slate-500 mono")
                        ui.badge(label, color=color)

        with ui.column().classes("flex-[1.55] min-w-[380px] gap-5"):
            detail_container = ui.column().classes("w-full gap-4")

    def render_submission_detail(submission_id: int) -> None:
        detail_container.clear()
        with detail_container:
            with get_session() as session:
                submission = load_submission(session, submission_id)
            if not submission:
                ui.label("Khong tim thay phieu.")
                return

            label, color = status_meta(submission.status)
            with ui.card().classes("surface rounded-[28px] p-6 gap-4"):
                with ui.row().classes("w-full items-start justify-between gap-4 flex-wrap"):
                    with ui.column().classes("gap-1"):
                        ui.label(submission.student.full_name).classes("text-2xl font-bold")
                        ui.label(f"{submission.student.student_code} • {submission.semester.name}").classes("text-slate-500 mono")
                    ui.badge(label, color=color)

                advisor_inputs = {}
                for score in submission.scores:
                    with ui.row().classes("criterion items-start gap-4 p-4 w-full flex-wrap"):
                        with ui.column().classes("flex-1 min-w-[260px] gap-2"):
                            ui.label(score.criterion.group.title if score.criterion and score.criterion.group else "").classes("section-label")
                            ui.label(score.criterion.title if score.criterion else "").classes("text-lg font-bold")
                            ui.label(score.criterion.description if score.criterion else "").classes("text-sm text-slate-500 leading-7")
                            ui.label(f"Minh chung: {score.evidence or 'Chua bo sung'}").classes("text-sm text-slate-500")
                            ui.label(f"Tu cham: {score.self_score}/{score.criterion.max_points}").classes("soft-tag w-fit")
                        with ui.column().classes("flex-1 min-w-[260px] gap-3"):
                            advisor_score = ui.number("Diem co van", value=score.advisor_score or score.self_score, min=0, max=score.criterion.max_points if score.criterion else 0, step=0.5, format="%.1f").props("outlined dense").classes("w-full")
                            advisor_feedback = ui.textarea("Nhan xet tieu chi", value=score.advisor_feedback).props("outlined autogrow").classes("w-full")
                        advisor_inputs[score.criterion_id] = {"advisor_score": advisor_score, "advisor_feedback": advisor_feedback}

                advisor_note = ui.textarea("Nhan xet tong quan", value=submission.advisor_note).props("outlined autogrow").classes("w-full")

                def approve_submission() -> None:
                    payload = {
                        criterion_id: {"advisor_score": fields["advisor_score"].value or 0, "advisor_feedback": fields["advisor_feedback"].value or ""}
                        for criterion_id, fields in advisor_inputs.items()
                    }
                    with get_session() as session:
                        update_advisor_scores(session, submission.id, payload, advisor_note.value or "")
                    ui.notify("Da duyet phieu danh gia", color="positive")
                    render_advisor_dashboard.refresh()

                ui.button("Hoan tat duyet", on_click=approve_submission, icon="task_alt").classes("bg-slate-900 text-white rounded-2xl")

    selected.on_value_change(lambda event: render_submission_detail(int(event.value)))
    render_submission_detail(int(selected.value))


@ui.page("/login")
def login_page() -> None:
    if app.storage.user.get("user_id"):
        ui.navigate.to("/")
        return

    ui.page_title("Dang nhap he thong")
    with ui.element("div").classes("min-h-screen w-full bg-[linear-gradient(135deg,#0f172a_0%,#0f3d64_45%,#f97316_120%)]"):
        with ui.row().classes("mx-auto min-h-screen max-w-7xl items-center gap-8 px-4 py-8 lg:flex-nowrap flex-wrap"):
            with ui.column().classes("flex-1 min-w-[320px] gap-6 text-white"):
                ui.label("Nghien cuu xay dung phan mem danh gia diem ren luyen").classes("text-4xl md:text-5xl font-black leading-tight max-w-3xl")
                ui.label("Frontend theo huong portal dai hoc: dang nhap ro vai tro, dashboard co sidebar, va luong xu ly sinh vien - co van - quan tri.").classes("max-w-2xl text-[15px] leading-8 text-white/80")
                with ui.row().classes("w-full gap-4 flex-wrap"):
                    metric_card("Python UI", "NiceGUI", "Mot codebase cho giao dien va backend", dark=True)
                    metric_card("Database", "SQLite", "Du lieu mau tu khoi tao lan dau", dark=True)
                    metric_card("Workflow", "3 vai tro", "Sinh vien, co van, quan tri", dark=True)
                with ui.card().classes("glass rounded-[30px] p-6 gap-4 shadow-none"):
                    ui.label("Tai khoan demo").classes("text-xl font-bold text-white")
                    for account in ["admin / admin123", "covan / covan123", "b23dccn001 / student123"]:
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("verified_user").classes("text-orange-200")
                            ui.label(account).classes("mono text-white")

            with ui.card().classes("surface rounded-[36px] p-8 md:p-10 gap-5 w-full max-w-[520px]"):
                ui.label("Dang nhap he thong").classes("text-3xl font-black text-slate-900")
                ui.label("Nhap tai khoan de truy cap workspace dung vai tro.").classes("text-slate-500")
                username = ui.input("Ten dang nhap", placeholder="admin hoac ma sinh vien").props("outlined dense").classes("w-full")
                password = ui.input("Mat khau", password=True, password_toggle_button=True).props("outlined dense").classes("w-full")

                def handle_login() -> None:
                    with get_session() as session:
                        user = authenticate(session, username.value or "", password.value or "")
                    if not user:
                        ui.notify("Sai ten dang nhap hoac mat khau", color="negative")
                        return
                    app.storage.user["user_id"] = user.id
                    ui.notify("Dang nhap thanh cong", color="positive")
                    ui.navigate.to("/")

                ui.button("Vao dashboard", on_click=handle_login, icon="arrow_forward").classes("bg-slate-900 text-white rounded-2xl")


@ui.page("/")
def home_page() -> None:
    if not require_login():
        return
    user = current_user()
    if not user:
        ui.navigate.to("/login")
        return

    subtitle = {
        UserRole.ADMIN: "Dieu phoi hoc ky, tai khoan va bo tieu chi tren mot dashboard co cau truc ro rang.",
        UserRole.ADVISOR: "Duyet phieu cua sinh vien theo hang cho, doi chieu minh chung va nhap diem xac nhan.",
        UserRole.STUDENT: "Tu danh gia theo hoc ky, bo sung minh chung va theo doi diem cuoi cung.",
    }[user.role]

    ui.page_title("PTIT Conduct Evaluation")
    with ui.element("div").classes("min-h-screen w-full p-3 md:p-5"):
        with ui.row().classes("w-full max-w-[1680px] mx-auto gap-5 items-start flex-wrap lg:flex-nowrap"):
            with ui.column().classes("sidebar-panel w-full lg:w-[300px] shrink-0 rounded-[34px] p-5 md:p-6 gap-6"):
                sidebar(user)
            with ui.column().classes("flex-1 min-w-0 gap-5"):
                topbar(user, subtitle)
                global_stats()
                if user.role == UserRole.ADMIN:
                    render_admin_dashboard()
                elif user.role == UserRole.ADVISOR:
                    render_advisor_dashboard()
                else:
                    render_student_dashboard(user.id)


ui.run(title="PTIT Conduct Evaluation", storage_secret=STORAGE_SECRET, reload=False, favicon="school")
