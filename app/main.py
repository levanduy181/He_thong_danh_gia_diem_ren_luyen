from __future__ import annotations

from datetime import datetime, time, timedelta

from nicegui import app, ui

from app.api import router as api_router
from app.config import DATA_DIR, STORAGE_SECRET
from app.db import Base, engine, get_session
from app.models import EventParticipation, ScoreEntry, Semester, Submission, SubmissionStatus, User, UserRole
from app.services.evaluation_service import (
    authenticate,
    get_active_events,
    get_active_semester,
    get_criteria_tree,
    get_or_create_submission,
    get_semesters,
    get_student_event_participations,
    get_user_by_id,
    list_students,
    load_submission,
    submit_event_participation,
    update_student_scores,
)
from app.services.seed import seed_default_data


DATA_DIR.mkdir(parents=True, exist_ok=True)
Base.metadata.create_all(engine)
with get_session() as session:
    seed_default_data(session)

app.include_router(api_router)


TEXT_MAP = {
    "Tran Minh Anh": "Trần Minh Anh",
    "Le Thu Ha": "Lê Thu Hà",
    "Nguyen Thi Co Van": "Nguyễn Thị Cố Vấn",
    "Quan tri he thong": "Quản trị hệ thống",
    "Cong nghe thong tin": "Công nghệ thông tin",
    "Ky thuat phan mem": "Kỹ thuật phần mềm",
    "He thong thong tin": "Hệ thống thông tin",
    "Hoc ky 1 nam hoc 2024-2025": "Học kỳ 1 năm học 2024-2025",
    "Hoc ky 2 nam hoc 2024-2025": "Học kỳ 2 năm học 2024-2025",
    "Hoc ky 1 nam hoc 2025-2026": "Học kỳ 1 năm học 2025-2026",
    "Hoc ky 2 nam hoc 2025-2026": "Học kỳ 2 năm học 2025-2026",
    "Tieu chi 1. Danh gia ve y thuc tham gia hoc tap": "Tiêu chí 1. Đánh giá về ý thức tham gia học tập",
    "Tieu chi 2. Danh gia ve y thuc chap hanh noi quy, quy che, quy dinh trong Hoc vien": "Tiêu chí 2. Đánh giá về ý thức chấp hành nội quy, quy chế, quy định trong Học viện",
    "Tieu chi 3. Danh gia ve y thuc va ket qua tham gia hoat dong chinh tri- xa hoi, van hoa, van nghe, the thao, phong chong toi pham cac te nan xa hoi": "Tiêu chí 3. Đánh giá về ý thức và kết quả tham gia hoạt động chính trị - xã hội, văn hóa, văn nghệ, thể thao, phòng chống tội phạm và các tệ nạn xã hội",
    "Tieu chi 4. Danh gia y thuc cong dan trong quan he cong dong": "Tiêu chí 4. Đánh giá ý thức công dân trong quan hệ cộng đồng",
    "Tieu chi 5. Danh gia ve y thuc va tham gia phu trach lop, cac doan the trong truong, thanh tich dac biet": "Tiêu chí 5. Đánh giá về ý thức và tham gia phụ trách lớp, các đoàn thể trong trường, thành tích đặc biệt",
    "Y thuc va thai do trong hoc tap": "Ý thức và thái độ trong học tập",
    "Ket qua hoc tap trong ky hoc": "Kết quả học tập trong kỳ học",
    "Y thuc chap hanh tot noi quy ve cac ky thi": "Ý thức chấp hành tốt nội quy về các kỳ thi",
    "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": "Ý thức và thái độ tham gia các hoạt động ngoại khóa, các sự kiện liên quan đến nghiên cứu khoa học, học thuật, chuyên môn, Câu lạc bộ",
    "Tinh than vuot kho, phan dau vuon len trong hoc tap": "Tinh thần vượt khó, phấn đấu vươn lên trong học tập",
    "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": "Thực hiện nghiêm túc các nội quy, quy chế, các quy định hiện hành trong Học viện",
    "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": "Thực hiện quy định về công tác nội trú, ngoại trú",
    "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": "Thực hiện nghiêm túc các buổi họp lớp, sinh hoạt đoàn thể do Học viện/Khoa/Viện/CVHT/Lớp/Chi đoàn tổ chức",
    "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": "Tham gia các buổi hội thảo việc làm, định hướng nghề nghiệp do Học viện tổ chức",
    "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": "Tham gia đầy đủ các hoạt động chính trị, xã hội, thể thao, tình nguyện, các buổi sinh hoạt chuyên đề",
    "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": "Tham gia công tác xã hội như: hiến máu nhân đạo, ủng hộ người nghèo, bão lụt",
    "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": "Tuyên truyền tích cực hình ảnh về Trường/Khoa trên mạng xã hội",
    "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": "Tích cực tham gia hoạt động phòng chống tội phạm, báo cáo hành vi liên quan tới ma túy, tệ nạn xã hội",
    "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": "Đưa tin sai lệch, thiếu kiểm chứng, bình luận tiêu cực về Học viện/Khoa",
    "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": "Chấp hành nghiêm chỉnh chủ trương của Đảng, pháp luật của Nhà nước và địa phương",
    "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": "Tích cực tham gia tuyên truyền pháp luật, có ý thức giữ gìn vệ sinh chung",
    "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": "Có mối quan hệ đúng mực với Thầy/Cô, cán bộ, nhân viên Học viện",
    "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": "Có mối quan hệ tốt với bạn bè trong lớp; tinh thần đoàn kết, chia sẻ, giúp đỡ",
    "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": "Được biểu dương khen thưởng trong các hoạt động ý thức công dân",
    "Vi pham an ninh, trat tu xa hoi, an toan giao thong": "Vi phạm an ninh, trật tự xã hội, an toàn giao thông",
    "Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": "Lớp trưởng, lớp phó, bí thư, BCH đoàn, chủ nhiệm câu lạc bộ...",
    "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": "Thành viên tham gia các Câu lạc bộ được ghi nhận hoàn thành nhiệm vụ...",
    "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": "Sinh viên đạt thành tích đặc biệt trong học tập, rèn luyện",
}


def vi(text: str | None) -> str:
    if not text:
        return ""
    return TEXT_MAP.get(text, text)


ui.add_head_html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #f5f6f8;
            --card: #ffffff;
            --line: #e9ebef;
            --text: #32363b;
            --muted: #8a8f98;
            --red: #d92314;
            --red-soft: #fde9e6;
        }
        body, .nicegui-content {
            font-family: "Inter", sans-serif;
            background: var(--bg);
            color: var(--text);
        }
        .mono { font-family: "IBM Plex Mono", monospace; }
        .s-card {
            background: var(--card);
            border: 1px solid var(--line);
            box-shadow: 0 12px 30px rgba(0,0,0,0.03);
        }
        .s-sidebar {
            background: #fff;
            border-right: 1px solid var(--line);
        }
        .menu-section {
            color: #c4c7cb;
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
        }
        .submenu-link {
            display: block;
            margin-left: 18px;
            margin-right: 12px;
            padding: 12px 16px;
            border-radius: 10px;
            color: #4e545a;
        }
        .submenu-link.active {
            background: #f2f3f5;
            color: var(--red);
            font-weight: 700;
        }
        .page-title {
            font-size: 21px;
            font-weight: 800;
        }
        .timeline-track, .timeline-fill {
            height: 4px;
            border-radius: 999px;
        }
        .timeline-track { background: #eceef2; }
        .timeline-fill { background: var(--red); }
        .timeline-node {
            width: 12px;
            height: 12px;
            border-radius: 999px;
            background: #cfd3d8;
        }
        .timeline-node.active { background: var(--red); }
        .left-list-item {
            border-top: 1px solid var(--line);
            padding: 16px 14px;
            background: #fff;
        }
        .left-list-item.active {
            background: var(--red-soft);
            color: var(--red);
            font-weight: 700;
        }
        .table-head {
            background: #fff;
            border-bottom: 1px solid var(--line);
            font-weight: 700;
        }
        .table-row {
            border-top: 1px solid var(--line);
            background: #fff;
        }
        .table-group {
            background: #fff;
            font-weight: 700;
        }
        .event-tile {
            display: flex;
            align-items: center;
            gap: 16px;
            background: #f7f7f8;
            border-radius: 10px;
            padding: 12px 16px;
        }
        .event-time {
            width: 64px;
            font-weight: 800;
            text-align: right;
        }
        .event-accent {
            width: 6px;
            height: 40px;
            border-radius: 999px;
        }
        .empty-box {
            min-height: 220px;
            border: 1px dashed var(--line);
            border-radius: 14px;
            background: #fafbfc;
        }
        .q-field--outlined .q-field__control {
            border-radius: 8px !important;
        }
        .logo-mark {
            font-size: 42px;
            font-weight: 900;
            color: var(--red);
            line-height: 1;
        }
    </style>
    """
)


def current_user() -> User | None:
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


def sync_selected_semester_from_request(semesters: list[Semester]) -> int | None:
    try:
        request = ui.context.client.request
    except Exception:
        request = None
    if not request:
        return None

    requested = request.query_params.get("semester")
    if not requested or not requested.isdigit():
        return None

    semester_id = int(requested)
    if semester_id in {semester.id for semester in semesters}:
        app.storage.user["selected_semester_id"] = semester_id
        return semester_id
    return None


def get_default_semester_id(session, semesters: list[Semester]) -> int:
    active = get_active_semester(session)
    return active.id if active else semesters[0].id


def ensure_selected_semester(session, semesters: list[Semester]) -> int:
    requested_id = sync_selected_semester_from_request(semesters)
    if requested_id is not None:
        return requested_id

    selected = get_default_semester_id(session, semesters)
    app.storage.user["selected_semester_id"] = selected
    return selected


def load_student_context() -> dict:
    with get_session() as session:
        student = get_user_by_id(session, app.storage.user.get("user_id"))
        if not student or student.role != UserRole.STUDENT:
            raise ValueError("Chỉ tài khoản sinh viên mới sử dụng được giao diện này.")
        semesters = get_semesters(session)
        selected_semester_id = ensure_selected_semester(session, semesters)
        selected_semester = next((semester for semester in semesters if semester.id == selected_semester_id), semesters[0])
        submission = get_or_create_submission(session, student.id, selected_semester.id)
        groups = get_criteria_tree(session)
        participations = get_student_event_participations(session, student.id)
        active_events = get_active_events(session, selected_semester.id)
        return {
            "student": student,
            "semesters": semesters,
            "selected_semester": selected_semester,
            "submission": submission,
            "groups": groups,
            "participations": participations,
            "active_events": active_events,
        }


def navigate_with_semester(path: str, semester_id: int) -> None:
    app.storage.user["selected_semester_id"] = semester_id
    timestamp = int(datetime.utcnow().timestamp() * 1000)
    ui.run_javascript(f"window.location.href = '{path}?semester={semester_id}&refresh={timestamp}'")


def refresh_page(path: str) -> None:
    semester_id = app.storage.user.get("selected_semester_id")
    timestamp = int(datetime.utcnow().timestamp() * 1000)
    if semester_id:
        ui.run_javascript(f"window.location.href = '{path}?semester={semester_id}&refresh={timestamp}'")
    else:
        ui.run_javascript(f"window.location.href = '{path}?refresh={timestamp}'")


def format_dt(value: datetime) -> str:
    return value.strftime("%d/%m/%Y %H:%M")


def semester_stages(semester: Semester) -> list[tuple[str, str, str]]:
    start_dt = datetime.combine(semester.start_date, time(0, 0))
    end_dt = datetime.combine(semester.end_date, time(23, 45))
    total_days = max(6, (end_dt.date() - start_dt.date()).days)
    step = max(1, total_days // 8)
    points = [start_dt + timedelta(days=step * idx) for idx in [0, 2, 4, 6]]
    labels = [
        "Cập nhật, duyệt minh chứng",
        "Sinh viên đánh giá",
        "Ban cán sự đánh giá",
        "Chủ nhiệm lớp xác nhận",
    ]
    items = []
    for idx, point in enumerate(points):
        end_point = points[idx + 1] - timedelta(minutes=15) if idx < len(points) - 1 else end_dt
        items.append((format_dt(point), format_dt(end_point), labels[idx]))
    return items


def stage_index(submission: Submission) -> int:
    if submission.status == SubmissionStatus.REVIEWED:
        return 3
    if submission.status == SubmissionStatus.SUBMITTED:
        return 2
    return 1


def render_timeline(semester: Semester, active_index: int) -> None:
    steps = semester_stages(semester)
    with ui.column().classes("w-full gap-6"):
        with ui.row().classes("w-full items-center justify-between gap-4"):
            for idx, _ in enumerate(steps):
                if idx > 0:
                    fill = "timeline-fill" if idx <= active_index else "timeline-track"
                    ui.element("div").classes(f"{fill} flex-1")
                node_css = "timeline-node active" if idx <= active_index else "timeline-node"
                ui.element("div").classes(node_css)
        with ui.row().classes("w-full items-start justify-between gap-4"):
            for idx, (start, end, label) in enumerate(steps):
                color = "text-slate-800" if idx <= active_index else "text-slate-400"
                with ui.column().classes("max-w-[220px] items-center text-center gap-1"):
                    ui.label(f"{start} -").classes(f"text-[13px] font-bold {color}")
                    ui.label(end).classes(f"text-[13px] font-bold {color}")
                    ui.label(label).classes(f"text-[13px] leading-7 {color}")


def render_topbar(student: User) -> None:
    with ui.element("div").classes("s-card sticky top-0 z-20 flex items-center justify-between px-6 py-3"):
        ui.label("Cổng thông tin rèn luyện sinh viên").classes("text-lg font-semibold text-slate-700")
        with ui.row().classes("items-center gap-5"):
            with ui.row().classes("items-center gap-3"):
                ui.avatar(vi(student.full_name)[:1].upper(), color="grey-4", text_color="white").classes("font-bold")
                ui.label(vi(student.full_name)).classes("text-lg text-slate-700")
            ui.button("Đăng xuất", icon="logout", on_click=logout).classes("bg-red-600 text-white rounded-lg")


def render_sidebar(active_leaf: str) -> None:
    with ui.column().classes("w-full gap-3"):
        with ui.row().classes("items-center gap-3 px-5 py-4"):
            ui.label("PT").classes("logo-mark")
            ui.label("S-Link").classes("text-[22px] font-medium text-slate-800")
        ui.separator()
        ui.label("RÈN LUYỆN").classes("menu-section px-6 pt-6")
        for label, path in [
            ("Khai báo minh chứng", "/evidence"),
            ("Sự kiện đã tham gia", "/events"),
            ("Phiếu điểm rèn luyện", "/score"),
        ]:
            css = "submenu-link active" if label == active_leaf else "submenu-link"
            ui.link(label, path).classes(css)


def render_page_header(title: str, semester_name: str | None = None) -> None:
    with ui.row().classes("w-full items-start justify-between gap-4 flex-wrap"):
        ui.label(title).classes("page-title")
        if semester_name:
            ui.label(semester_name).classes("rounded-lg border border-slate-200 bg-white px-4 py-3 text-[16px]")


def render_empty_box(title: str, note: str) -> None:
    with ui.column().classes("empty-box items-center justify-center gap-4 w-full"):
        ui.icon("inventory_2", size="64px").classes("text-slate-300")
        ui.label(title).classes("text-xl font-semibold text-slate-500")
        ui.label(note).classes("text-sm text-slate-400")


def render_shell(active_leaf: str, content_renderer) -> None:
    try:
        context = load_student_context()
    except ValueError as error:
        ui.notify(str(error), color="negative")
        ui.navigate.to("/login")
        return
    ui.page_title("S-Link PTIT Conduct Evaluation")
    with ui.element("div").classes("min-h-screen w-full"):
        with ui.row().classes("w-full items-start flex-nowrap"):
            with ui.column().classes("s-sidebar min-h-screen w-[280px] shrink-0"):
                render_sidebar(active_leaf)
            with ui.column().classes("flex-1 min-w-0"):
                render_topbar(context["student"])
                with ui.column().classes("w-full gap-4 p-4 md:p-6"):
                    content_renderer(context)


def get_criterion_bucket_map(submission: Submission) -> dict[int, int]:
    criterion_ids = [score.criterion_id for score in submission.scores[:3]]
    return {index + 1: criterion_id for index, criterion_id in enumerate(criterion_ids)}


def reverse_bucket_map(submission: Submission) -> dict[int, int]:
    return {criterion_id: bucket for bucket, criterion_id in get_criterion_bucket_map(submission).items()}


def build_submission_payload(submission: Submission, overrides: dict[int, dict[str, str | float]]) -> dict[int, dict[str, str | float]]:
    payload = {}
    for score in submission.scores:
        payload[score.criterion_id] = {
            "self_score": score.self_score,
            "evidence": score.evidence,
            "evidence_type": score.evidence_type or "",
            "evidence_file": score.evidence_file or "",
        }
    for criterion_id, data in overrides.items():
        payload[criterion_id].update(data)
    return payload


def delete_evidence_entry(submission_id: int, criterion_id: int) -> None:
    try:
        with get_session() as session:
            refreshed = load_submission(session, submission_id)
            payload = build_submission_payload(
                refreshed,
                {
                    criterion_id: {
                        "self_score": 0,
                        "evidence": "",
                        "evidence_type": "",
                        "evidence_file": "",
                    }
                },
            )
            update_student_scores(session, refreshed.id, payload, refreshed.student_note or "", False)
        ui.notify("Đã xóa minh chứng", color="positive")
        refresh_page("/evidence")
    except ValueError as error:
        ui.notify(str(error), color="warning")


def open_evidence_dialog(submission: Submission, criterion_id: int | None = None) -> None:
    if submission.status == SubmissionStatus.REVIEWED:
        ui.notify("Học kỳ này đã được duyệt, bạn chỉ có thể xem minh chứng.", color="warning")
        return

    bucket_map = get_criterion_bucket_map(submission)
    reverse_map = reverse_bucket_map(submission)
    selected_score = next((score for score in submission.scores if score.criterion_id == criterion_id), None)
    selected_bucket = reverse_map.get(criterion_id or 0, 1)
    uploaded_file_name = {"name": selected_score.evidence_file if selected_score and selected_score.evidence_file else ""}

    with ui.dialog() as dialog, ui.card().classes("s-card min-w-[700px] rounded-[12px] p-6 gap-4 shadow-none"):
        ui.label("Cập nhật minh chứng").classes("page-title")
        criterion_select = ui.select({1: "1", 2: "2", 3: "3"}, value=selected_bucket, label="Tiêu chí điểm").props("outlined dense").classes("w-full")
        type_select = ui.select(
            ["Thành tích đặc biệt", "Tuyên truyền tích cực về Trường/Khoa", "Tham gia công tác xã hội", "Công tác nội trú, ngoại trú", "Khác"],
            value=selected_score.evidence_type if selected_score and selected_score.evidence_type else "Khác",
            label="Loại minh chứng",
        ).props("outlined dense").classes("w-full")
        score_select = ui.select(
            {1: "1", 2: "2", 3: "3"},
            value=int(selected_score.self_score) if selected_score and int(selected_score.self_score) in [1, 2, 3] else 1,
            label="Mức độ tự đánh giá",
        ).props("outlined dense").classes("w-full")
        evidence_input = ui.textarea("Nội dung minh chứng", value=selected_score.evidence if selected_score else "").props("outlined autogrow").classes("w-full")
        ui.label("Tải lên ảnh hoặc tệp chứng minh (nếu có):").classes("text-slate-600 text-sm mt-2")
        file_hint = ui.label(f"Tệp hiện tại: {uploaded_file_name['name']}").classes(
            "text-sm font-medium text-blue-600"
        )
        if not uploaded_file_name["name"]:
            file_hint.set_visibility(False)

        def handle_upload(event):
            uploaded_file_name["name"] = event.name
            file_hint.set_text(f"Tệp hiện tại: {event.name}")
            file_hint.set_visibility(True)
            ui.notify(f"Đã tải lên: {event.name}", color="positive")

        ui.upload(auto_upload=True, on_upload=handle_upload).classes("w-full")

        def reset_form() -> None:
            criterion_select.value = 1
            type_select.value = "Khác"
            score_select.value = 1
            evidence_input.value = ""
            uploaded_file_name["name"] = ""
            file_hint.set_text("")
            file_hint.set_visibility(False)

        def delete_evidence() -> None:
            chosen_criterion_id = bucket_map[int(criterion_select.value)]
            dialog.close()
            delete_evidence_entry(submission.id, chosen_criterion_id)

        def save_evidence() -> None:
            chosen_criterion_id = bucket_map[int(criterion_select.value)]
            try:
                with get_session() as session:
                    refreshed = load_submission(session, submission.id)
                    overrides = {
                        chosen_criterion_id: {
                            "self_score": score_select.value or 0,
                            "evidence": evidence_input.value or "",
                            "evidence_type": type_select.value or "",
                            "evidence_file": uploaded_file_name["name"] or "",
                        }
                    }
                    if selected_score and selected_score.criterion_id != chosen_criterion_id:
                        overrides[selected_score.criterion_id] = {
                            "self_score": 0,
                            "evidence": "",
                            "evidence_type": "",
                            "evidence_file": "",
                        }
                    payload = build_submission_payload(refreshed, overrides)
                    update_student_scores(session, refreshed.id, payload, refreshed.student_note or "", False)
                dialog.close()
                ui.notify("Đã cập nhật minh chứng", color="positive")
                refresh_page("/evidence")
            except ValueError as error:
                ui.notify(str(error), color="warning")

        with ui.row().classes("justify-end gap-3 w-full mt-4"):
            if selected_score:
                ui.button("Xóa", icon="delete", on_click=delete_evidence).props("flat").classes("text-red-600")
            ui.button("Đặt lại", on_click=reset_form).props("flat").classes("text-slate-500")
            ui.button("Đóng", on_click=dialog.close).props("flat")
            ui.button("Lưu", on_click=save_evidence).classes("bg-blue-500 text-white rounded-lg px-6")
    dialog.open()


def evidence_page_content(context: dict) -> None:
    semesters: list[Semester] = context["semesters"]
    selected_semester: Semester = context["selected_semester"]
    submission: Submission = context["submission"]
    evidence_rows = [score for score in submission.scores if score.evidence]
    bucket_map = reverse_bucket_map(submission)
    readonly = submission.status == SubmissionStatus.REVIEWED
    active_semester = next((semester for semester in semesters if semester.is_active), selected_semester)
    categories = [
        "Thành tích đặc biệt",
        "Tuyên truyền tích cực về Trường/Khoa",
        "Tham gia công tác xã hội",
        "Công tác nội trú, ngoại trú",
    ]

    render_page_header("Khai báo minh chứng")
    with ui.card().classes("s-card rounded-[10px] p-6 gap-6 shadow-none"):
        with ui.row().classes("w-full items-center justify-end"):
            semester_options = {semester.id: vi(semester.name) for semester in semesters}
            ui.select(
                semester_options,
                value=selected_semester.id,
                on_change=lambda event: navigate_with_semester("/evidence", int(event.value)),
                label="Học kỳ",
            ).props("outlined dense").classes("min-w-[320px] bg-white")
        render_timeline(submission.semester, stage_index(submission))
        if readonly:
            with ui.row().classes("w-full items-center justify-between gap-3 rounded-lg bg-amber-50 px-4 py-3"):
                ui.label("Học kỳ này đã được duyệt nên chỉ xem được minh chứng, không thể chỉnh sửa.").classes(
                    "text-sm font-medium text-amber-700"
                )
                if active_semester.id != selected_semester.id:
                    ui.button(
                        "Chuyển sang học kỳ đang mở",
                        icon="arrow_forward",
                        on_click=lambda sid=active_semester.id: navigate_with_semester("/evidence", sid),
                    ).classes("bg-amber-600 text-white rounded-lg")
        with ui.row().classes("w-full gap-4 flex-wrap items-start"):
            with ui.column().classes("w-full lg:w-[360px] gap-3"):
                with ui.row().classes("items-center justify-between"):
                    ui.label("Loại minh chứng").classes("text-2xl font-semibold")
                    ui.button(icon="settings").props("flat round dense").classes("text-slate-500")
                with ui.card().classes("s-card rounded-[8px] overflow-hidden shadow-none"):
                    with ui.row().classes("w-full items-center justify-center px-4 py-5 border-b border-slate-200"):
                        ui.label("Loại minh chứng").classes("text-xl font-semibold")
                    for index, category in enumerate(categories):
                        css = "left-list-item active" if index == 0 else "left-list-item"
                        with ui.element("div").classes(css):
                            ui.label(category).classes("text-[15px]")

            with ui.column().classes("flex-1 min-w-[460px] gap-3"):
                with ui.row().classes("items-center justify-between gap-3 flex-wrap"):
                    ui.label("Danh sách minh chứng").classes("text-2xl font-semibold")
                    with ui.row().classes("gap-2 flex-wrap"):
                        add_btn = ui.button("Thêm mới", icon="add_circle_outline", on_click=lambda: open_evidence_dialog(submission)).classes("bg-red-600 text-white rounded-lg px-4")
                        if readonly:
                            add_btn.disable()
                        ui.input(placeholder="Tìm theo: tiêu chí, loại minh chứng...").props("outlined dense").classes("min-w-[260px] bg-white")
                        ui.button("Bộ lọc", icon="filter_alt").props("outline").classes("rounded-lg")
                        ui.button("Tải lại", icon="refresh", on_click=lambda: refresh_page("/evidence")).props("outline").classes("rounded-lg")
                with ui.card().classes("s-card rounded-[8px] p-0 shadow-none overflow-hidden"):
                    with ui.row().classes("table-head w-full"):
                        for text, width in [("TT", "w-[60px]"), ("Tiêu chí", "w-[110px]"), ("Loại minh chứng", "w-[220px]"), ("Nội dung", "flex-1"), ("Tệp", "w-[90px]"), ("Thao tác", "w-[120px]")]:
                            ui.label(text).classes(f"{width} px-4 py-4 text-[16px]")
                    if evidence_rows:
                        for index, score in enumerate(evidence_rows, start=1):
                            with ui.row().classes("table-row w-full items-center"):
                                ui.label(str(index)).classes("w-[60px] px-4 py-4 text-center")
                                ui.label(str(bucket_map.get(score.criterion_id, 1))).classes("w-[110px] px-4 py-4 text-center font-bold")
                                ui.label(score.evidence_type or "Khác").classes("w-[220px] px-4 py-4")
                                ui.label(score.evidence).classes("flex-1 px-4 py-4")
                                ui.label("Có" if score.evidence_file else "Không").classes("w-[90px] px-4 py-4 text-center")
                                with ui.row().classes("w-[120px] items-center justify-center gap-1"):
                                    edit_btn = ui.button(icon="edit", on_click=lambda cid=score.criterion_id: open_evidence_dialog(submission, cid)).props("flat round").classes("text-blue-600")
                                    delete_btn = ui.button(icon="delete", on_click=lambda cid=score.criterion_id: delete_evidence_entry(submission.id, cid)).props("flat round").classes("text-red-600")
                                    if readonly:
                                        edit_btn.disable()
                                        delete_btn.disable()
                    else:
                        render_empty_box("Không có dữ liệu", "Sinh viên chưa cập nhật minh chứng cho học kỳ này.")


def render_event_list(events: list[dict[str, str]]) -> None:
    current_date = ""
    for item in events:
        if item["date"] != current_date:
            current_date = item["date"]
            with ui.row().classes("items-center gap-3 pt-4"):
                ui.label(current_date).classes("text-[18px] font-bold text-slate-500")
                ui.badge("1", color="red")
        with ui.row().classes("event-tile w-full"):
            ui.label(item["time"]).classes("event-time text-[16px]")
            ui.element("div").style(f"background:{item['accent']}").classes("event-accent")
            ui.label(item["title"]).classes("text-[16px] text-slate-700")


def events_page_content(context: dict) -> None:
    selected_semester: Semester = context["selected_semester"]
    participations: list[EventParticipation] = context["participations"]
    active_events = context["active_events"]
    joined_events = [
        {
            "date": part.submitted_at.strftime("Ngày %d/%m/%Y"),
            "time": part.submitted_at.strftime("%H:%M"),
            "title": part.event.name if part.event else "Sự kiện",
            "accent": "#53b8dc" if part.status.value == "approved" else "#be7cff",
        }
        for part in participations
    ]

    render_page_header("Sự kiện đã tham gia", vi(selected_semester.name))
    with ui.card().classes("s-card rounded-[10px] p-6 gap-5 shadow-none"):
        with ui.tabs().props("inline-label").classes("bg-transparent") as tabs:
            joined_tab = ui.tab("Đã tham gia")
            registered_tab = ui.tab("Đã đăng ký")
        with ui.tab_panels(tabs, value=joined_tab).classes("w-full bg-transparent"):
            with ui.tab_panel(joined_tab).classes("px-0"):
                if joined_events:
                    render_event_list(joined_events)
                else:
                    render_empty_box("Chưa có sự kiện nào", "Bạn chưa có lịch sử tham gia sự kiện trong hệ thống.")
            with ui.tab_panel(registered_tab).classes("px-0"):
                if active_events:
                    for event in active_events:
                        with ui.row().classes("event-tile w-full items-center justify-between"):
                            with ui.row().classes("items-center gap-4"):
                                ui.element("div").style("background:#53b8dc").classes("event-accent")
                                with ui.column().classes("gap-1"):
                                    ui.label(event.name).classes("text-[16px] font-semibold")
                                    ui.label(f"Cộng {event.points} điểm").classes("text-sm text-slate-500")

                            def register(eid=event.id):
                                with get_session() as session:
                                    user = get_user_by_id(session, app.storage.user.get("user_id"))
                                    submit_event_participation(session, user.id, eid)
                                ui.notify("Đã đăng ký sự kiện", color="positive")
                                ui.navigate.to("/events")

                            ui.button("Đăng ký", on_click=register).classes("bg-red-600 text-white rounded-lg")
                else:
                    render_empty_box("Không có sự kiện mở", "Hiện tại chưa có sự kiện nào cho học kỳ này.")


def score_page_content(context: dict) -> None:
    semesters: list[Semester] = context["semesters"]
    selected_semester: Semester = context["selected_semester"]
    submission: Submission = context["submission"]
    groups = context["groups"]
    is_past_semester = not selected_semester.is_active
    active_semester = next((semester for semester in semesters if semester.is_active), selected_semester)

    render_page_header("Phiếu điểm rèn luyện", vi(selected_semester.name))
    with ui.card().classes("s-card rounded-[10px] p-6 gap-6 shadow-none"):
        with ui.row().classes("w-full items-center justify-end"):
            semester_options = {semester.id: vi(semester.name) for semester in semesters}
            ui.select(
                semester_options,
                value=selected_semester.id,
                on_change=lambda event: navigate_with_semester("/score", int(event.value)),
                label="Học kỳ",
            ).props("outlined dense").classes("min-w-[320px] bg-white")
        render_timeline(selected_semester, stage_index(submission))
        with ui.row().classes("w-full gap-4 flex-wrap items-start"):
            with ui.column().classes("w-full lg:w-[360px] gap-3"):
                with ui.row().classes("items-center justify-between"):
                    ui.label("Học kỳ").classes("text-2xl font-semibold")
                    ui.button(icon="settings").props("flat round dense").classes("text-slate-500")
                with ui.card().classes("s-card rounded-[8px] overflow-hidden shadow-none"):
                    with ui.row().classes("w-full items-center justify-center px-4 py-5 border-b border-slate-200"):
                        ui.label("Học kỳ").classes("text-xl font-semibold")
                    for semester in semesters:
                        active = semester.id == selected_semester.id
                        css = "left-list-item active" if active else "left-list-item"
                        with ui.element("div").classes(css):
                            ui.link(
                                vi(semester.name),
                                f"/score?semester={semester.id}",
                            ).classes("block w-full text-[15px] no-underline")

            with ui.column().classes("flex-1 min-w-[560px] gap-3"):
                with ui.row().classes("items-center justify-between gap-4 flex-wrap"):
                    with ui.row().classes("items-center gap-3"):
                        ui.label("PHIẾU ĐIỂM RÈN LUYỆN").classes("text-[22px] font-extrabold")
                        ui.label(f"{submission.self_total} điểm").classes("rounded-lg bg-red-600 px-4 py-2 text-lg font-bold text-white")
                    if is_past_semester:
                        with ui.row().classes("items-center gap-2 rounded-lg bg-slate-100 px-3 py-2"):
                            ui.label("Đang xem kết quả học kỳ trước").classes("text-sm font-semibold text-slate-600")
                            if active_semester.id != selected_semester.id:
                                ui.button(
                                    "Về học kỳ đang mở",
                                    icon="arrow_forward",
                                    on_click=lambda sid=active_semester.id: navigate_with_semester("/score", sid),
                                ).props("flat dense").classes("text-red-600")

                score_lookup: dict[int, ScoreEntry] = {score.criterion_id: score for score in submission.scores}
                student_inputs: dict[int, dict[str, object]] = {}

                with ui.column().classes("w-full gap-0"):
                    with ui.row().classes("table-head w-full"):
                        for label, width in [("NỘI DUNG", "flex-[2.9]"), ("Điểm tối đa", "w-[130px]"), ("Sinh viên tự đánh giá", "w-[160px]"), ("Ban cán sự chấm điểm", "w-[160px]"), ("CVHT chấm điểm", "w-[160px]")]:
                            ui.label(label).classes(f"{width} px-4 py-4 text-center text-[17px]")
                    for group in groups:
                        with ui.row().classes("table-row table-group w-full items-center"):
                            ui.label(vi(group.title)).classes("flex-[2.9] px-4 py-4 text-[15px] leading-7")
                            ui.label(str(int(group.max_points))).classes("w-[130px] px-4 py-4 text-center")
                            ui.label("").classes("w-[160px]")
                            ui.label("").classes("w-[160px]")
                            ui.label("").classes("w-[160px]")
                        for criterion in group.criteria:
                            score = score_lookup.get(criterion.id)
                            if score is None:
                                continue
                            readonly = is_past_semester or submission.status == SubmissionStatus.REVIEWED
                            with ui.row().classes("table-row w-full items-start"):
                                ui.label(vi(criterion.title)).classes("flex-[2.9] px-4 py-4 text-[15px] leading-7")
                                ui.label(f"[{criterion.min_points:g} - {criterion.max_points:g}]").classes("w-[130px] px-4 py-4 text-center")
                                if readonly:
                                    ui.number(value=score.self_score, format="%.1f").props("outlined dense readonly").classes("w-[160px] px-2 pt-3")
                                else:
                                    self_input = ui.number(value=score.self_score, min=criterion.min_points, max=criterion.max_points, step=0.5, format="%.1f").props("outlined dense").classes("w-[160px] px-2 pt-3")
                                    student_inputs[criterion.id] = {"self_score": self_input}
                                ui.number(value=score.advisor_score, format="%.1f").props("outlined dense readonly").classes("w-[160px] px-2 pt-3")
                                ui.number(value=score.advisor_score, format="%.1f").props("outlined dense readonly").classes("w-[160px] px-2 pt-3")
                            with ui.row().classes("w-full px-4 pb-4"):
                                if readonly:
                                    ui.textarea("Minh chứng / ghi chú", value=score.evidence).props("outlined autogrow readonly").classes("w-full")
                                else:
                                    evidence = ui.textarea("Minh chứng / ghi chú", value=score.evidence).props("outlined autogrow").classes("w-full")
                                    student_inputs[criterion.id]["evidence"] = evidence

                if not is_past_semester and submission.status != SubmissionStatus.REVIEWED:
                    note_input = ui.textarea("Nhận xét của sinh viên", value=submission.student_note).props("outlined autogrow").classes("w-full mt-4")

                    def save_score_sheet(submit: bool) -> None:
                        payload = {
                            criterion_id: {
                                "self_score": fields["self_score"].value or 0,
                                "evidence": fields["evidence"].value or "",
                            }
                            for criterion_id, fields in student_inputs.items()
                        }
                        with get_session() as session:
                            refreshed = load_submission(session, submission.id)
                            update_student_scores(session, refreshed.id, payload, note_input.value or "", submit)
                        ui.notify("Đã gửi phiếu đánh giá" if submit else "Đã lưu bản nháp", color="positive")
                        refresh_page("/score")

                    with ui.row().classes("items-center justify-between gap-4 flex-wrap mt-5"):
                        with ui.row().classes("gap-3"):
                            ui.button("Lưu bản nháp", icon="save", on_click=lambda: save_score_sheet(False)).classes("bg-white text-slate-700 border border-slate-300 rounded-lg")
                            ui.button("Gửi phiếu đánh giá", icon="send", on_click=lambda: save_score_sheet(True)).classes("bg-red-600 text-white rounded-lg")


@ui.page("/")
def home_page() -> None:
    if app.storage.user.get("user_id"):
        with get_session() as session:
            semesters = get_semesters(session)
            selected_semester_id = get_default_semester_id(session, semesters)
        app.storage.user["selected_semester_id"] = selected_semester_id
        ui.navigate.to(f"/score?semester={selected_semester_id}")
    else:
        ui.navigate.to("/login")


@ui.page("/login")
def login_page() -> None:
    if app.storage.user.get("user_id"):
        with get_session() as session:
            semesters = get_semesters(session)
            selected_semester_id = get_default_semester_id(session, semesters)
        app.storage.user["selected_semester_id"] = selected_semester_id
        ui.navigate.to(f"/score?semester={selected_semester_id}")
        return

    ui.page_title("Đăng nhập hệ thống")
    with ui.element("div").classes("min-h-screen w-full bg-[#f5f6f8]"):
        with ui.row().classes("min-h-screen w-full items-center justify-center px-4"):
            with ui.row().classes("w-full max-w-5xl items-stretch overflow-hidden rounded-[16px] border border-slate-200 bg-white shadow-[0_30px_80px_rgba(0,0,0,0.08)]"):
                with ui.column().classes("flex-1 min-w-[320px] gap-5 px-10 py-12 justify-center"):
                    with ui.row().classes("items-center gap-3"):
                        ui.label("PT").classes("logo-mark")
                        ui.label("S-Link").classes("text-[28px] font-medium text-slate-800")
                    ui.label("Hệ thống đánh giá điểm rèn luyện sinh viên. Sau khi đăng nhập, bạn chỉ làm việc với 3 chức năng: Khai báo minh chứng, Sự kiện đã tham gia, Phiếu điểm rèn luyện.").classes("max-w-xl text-lg leading-8 text-slate-500")
                    with ui.card().classes("s-card rounded-[10px] p-5 gap-3 shadow-none"):
                        ui.label("Tài khoản sinh viên demo").classes("text-xl font-semibold")
                        for account in ["b23dccn001 / student123", "b23dccn002 / student123"]:
                            ui.label(account).classes("mono text-slate-600")

                with ui.column().classes("w-full max-w-[420px] gap-5 border-l border-slate-200 bg-[#fafafa] px-10 py-12 justify-center"):
                    ui.label("Đăng nhập").classes("text-4xl font-bold text-slate-800")
                    username = ui.input("Tên đăng nhập").props("outlined dense").classes("w-full")
                    password = ui.input("Mật khẩu", password=True, password_toggle_button=True).props("outlined dense").classes("w-full")

                    def handle_login() -> None:
                        with get_session() as session:
                            user = authenticate(session, username.value or "", password.value or "")
                            semesters = get_semesters(session)
                            selected_semester_id = get_default_semester_id(session, semesters) if semesters else None
                        if not user:
                            ui.notify("Sai tên đăng nhập hoặc mật khẩu", color="negative")
                            return
                        if user.role != UserRole.STUDENT:
                            ui.notify("Bản này chỉ mở giao diện sinh viên.", color="warning")
                            return
                        app.storage.user["user_id"] = user.id
                        if selected_semester_id is not None:
                            app.storage.user["selected_semester_id"] = selected_semester_id
                        ui.notify("Đăng nhập thành công", color="positive")
                        ui.navigate.to(f"/score?semester={selected_semester_id}" if selected_semester_id is not None else "/score")

                    ui.button("Đăng nhập", icon="login", on_click=handle_login).classes("bg-red-600 text-white rounded-lg")


@ui.page("/evidence")
def evidence_page() -> None:
    if not require_login():
        return
    render_shell("Khai báo minh chứng", evidence_page_content)


@ui.page("/events")
def events_page() -> None:
    if not require_login():
        return
    render_shell("Sự kiện đã tham gia", events_page_content)


@ui.page("/score")
def score_page() -> None:
    if not require_login():
        return
    render_shell("Phiếu điểm rèn luyện", score_page_content)


ui.run(title="PTIT Conduct Evaluation", storage_secret=STORAGE_SECRET, reload=False, favicon="school")
