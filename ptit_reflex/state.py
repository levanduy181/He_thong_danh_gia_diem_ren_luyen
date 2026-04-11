from __future__ import annotations

import reflex as rx

from ptit_reflex.data import (
    CATEGORY_LABELS,
    approve_registered_event,
    authenticate_user,
    build_snapshot,
    create_admin_event,
    create_evidence,
    delete_evidence,
    export_conduct_pdf_bytes,
    load_evidence_detail,
    register_user_account,
    register_event_for_student,
    review_evidence,
    save_submission_scores,
    update_semester_stage_windows,
    update_user_role,
)


EVIDENCE_UPLOAD_ID = "evidence_upload"


class ConductState(rx.State):
    loading: bool = True
    flash_message: str = ""
    flash_kind: str = "info"
    is_authenticated: bool = False
    auth_mode: str = "login"
    login_username: str = ""
    login_password: str = ""
    login_error: str = ""
    register_username: str = ""
    register_password: str = ""
    register_password_confirm: str = ""
    register_full_name: str = ""
    register_student_code: str = ""
    register_email: str = ""
    register_class_name: str = ""
    register_faculty: str = ""
    register_major: str = ""

    active_tab: str = "student_info"
    event_tab: str = "joined"
    nav_students_open: bool = True

    selected_account_id: int = 0
    current_user_name: str = ""
    current_user_initial: str = ""
    current_user_role: str = ""
    current_user_role_label: str = ""
    current_user_email: str = ""
    current_user_faculty: str = ""
    current_user_class_name: str = ""
    current_user_student_code: str = ""
    role_management_rows: list[dict] = []

    students: list[dict] = []
    selected_student_id: int = 0
    selected_student_label: str = ""
    selected_student_name: str = ""
    selected_student_code: str = ""
    selected_student_class: str = ""

    semesters: list[dict] = []
    selected_semester_id: int = 0
    selected_semester_name: str = ""

    timeline: list[dict] = []
    outside_window: bool = True
    submission_status: str = ""
    submission_status_label: str = ""

    score_rows: list[dict] = []
    score_total: str = "0"
    score_effective_total: str = "0"
    score_total_class: str = "0"
    score_total_advisor: str = "0"
    conduct_grade_label: str = "—"
    student_note: str = ""
    class_note: str = ""
    advisor_note: str = ""
    can_edit_student_note: bool = False
    can_edit_class_note: bool = False
    can_edit_advisor_note: bool = False
    can_save_student: bool = False
    can_submit_student: bool = False
    can_review_class: bool = False
    can_review_advisor: bool = False
    can_reset_submission: bool = False
    can_download_conduct_pdf: bool = False
    student_list_filter: str = ""

    evidence_categories: list[dict] = []
    selected_evidence_category: str = "special_achievement"
    evidence_rows: list[dict] = []
    has_evidence_rows: bool = False
    evidence_count: str = "0"
    can_create_evidence: bool = False

    show_student_code_col: bool = True
    show_full_name_col: bool = True
    show_class_col: bool = True
    show_reporter_col: bool = True
    show_status_col: bool = True
    show_action_col: bool = True
    column_config_open: bool = False

    evidence_modal_open: bool = False
    evidence_detail_open: bool = False
    selected_evidence_detail: dict = {}
    selected_evidence_title: str = ""
    selected_evidence_status_label: str = ""
    selected_evidence_fields: list[dict] = []
    selected_evidence_can_class_review: bool = False
    selected_evidence_can_advisor_review: bool = False

    evidence_award_level: str = ""
    evidence_activity_content: str = ""
    evidence_participation_time: str = ""
    evidence_url: str = ""
    evidence_file_name: str = ""
    evidence_event_name: str = ""
    evidence_share_time: str = ""
    evidence_social_type: str = ""
    evidence_residence_type: str = "Ngoại trú"
    evidence_dormitory: str = ""
    evidence_room_number: str = ""
    evidence_city: str = ""
    evidence_district: str = ""
    evidence_ward: str = ""
    evidence_street_address: str = ""
    evidence_host_name: str = ""
    evidence_host_phone: str = ""

    student_profile: dict = {}
    joined_events: list[dict] = []
    registered_events: list[dict] = []
    has_registered_events: bool = False
    open_events: list[dict] = []
    has_open_events: bool = False
    selected_semester_is_active: bool = False
    criterion_choice_labels: list[str] = []
    admin_new_event_name: str = ""
    admin_new_event_points: str = "1"
    admin_new_event_semester_id: int = 0
    admin_event_criterion_choice: str = ""
    admin_stage_0_label: str = ""
    admin_stage_0_start: str = ""
    admin_stage_0_end: str = ""
    admin_stage_1_label: str = ""
    admin_stage_1_start: str = ""
    admin_stage_1_end: str = ""
    admin_stage_2_label: str = ""
    admin_stage_2_start: str = ""
    admin_stage_2_end: str = ""
    admin_stage_3_label: str = ""
    admin_stage_3_start: str = ""
    admin_stage_3_end: str = ""
    event_modal_open: bool = False
    selected_event: dict = {}
    selected_event_type_label: str = ""
    selected_event_name: str = ""
    selected_event_start_time: str = ""
    selected_event_end_time: str = ""
    selected_event_location: str = ""
    selected_event_counts_to_score: str = ""
    selected_event_note: str = ""

    def _set_flash(self, message: str, kind: str = "info") -> None:
        self.flash_message = message
        self.flash_kind = kind

    def clear_flash(self) -> None:
        self.flash_message = ""
        self.flash_kind = "info"
        self.login_error = ""

    def _apply_snapshot(self, snapshot: dict) -> None:
        self.selected_account_id = snapshot["selected_account_id"]
        self.current_user_name = snapshot["current_user_name"]
        self.current_user_initial = snapshot["current_user_initial"]
        self.current_user_role = snapshot["current_user_role"]
        self.current_user_role_label = snapshot["current_user_role_label"]
        self.current_user_email = str(snapshot.get("current_user_email", ""))
        self.current_user_faculty = str(snapshot.get("current_user_faculty", ""))
        self.current_user_class_name = str(snapshot.get("current_user_class_name", ""))
        self.current_user_student_code = str(snapshot.get("current_user_student_code", ""))
        self.role_management_rows = list(snapshot.get("role_management_rows", []))
        self.students = snapshot["students"]
        self.selected_student_id = snapshot["selected_student_id"]
        self.selected_student_label = snapshot["selected_student_label"]
        self.selected_student_name = snapshot["selected_student_name"]
        self.selected_student_code = snapshot["selected_student_code"]
        self.selected_student_class = snapshot["selected_student_class"]
        self.semesters = snapshot["semesters"]
        self.selected_semester_id = snapshot["selected_semester_id"]
        self.selected_semester_name = snapshot["selected_semester_name"]
        self.timeline = snapshot["timeline"]
        self.outside_window = snapshot["outside_window"]
        self.submission_status = snapshot["submission_status"]
        self.submission_status_label = snapshot["submission_status_label"]
        self.score_rows = snapshot["score_rows"]
        self.score_total = snapshot["score_total"]
        self.score_effective_total = str(snapshot.get("score_effective_total", snapshot.get("score_total", "0")))
        self.score_total_class = snapshot["score_total_class"]
        self.score_total_advisor = snapshot["score_total_advisor"]
        self.conduct_grade_label = str(snapshot.get("conduct_grade_label", "—"))
        self.student_note = snapshot["student_note"]
        self.class_note = snapshot["class_note"]
        self.advisor_note = snapshot["advisor_note"]
        self.can_edit_student_note = snapshot["can_edit_student_note"]
        self.can_edit_class_note = snapshot["can_edit_class_note"]
        self.can_edit_advisor_note = snapshot["can_edit_advisor_note"]
        self.can_save_student = snapshot["can_save_student"]
        self.can_submit_student = snapshot["can_submit_student"]
        self.can_review_class = snapshot["can_review_class"]
        self.can_review_advisor = snapshot["can_review_advisor"]
        self.can_reset_submission = snapshot["can_reset_submission"]
        self.can_download_conduct_pdf = bool(snapshot.get("can_download_conduct_pdf", False))
        self.evidence_categories = snapshot["evidence_categories"]
        self.selected_evidence_category = snapshot["selected_evidence_category"]
        self.evidence_rows = snapshot["evidence_rows"]
        self.has_evidence_rows = snapshot["has_evidence_rows"]
        self.evidence_count = snapshot["evidence_count"]
        self.can_create_evidence = snapshot["can_create_evidence"]
        self.student_profile = snapshot["student_profile"]
        self.joined_events = snapshot["joined_events"]
        self.registered_events = snapshot["registered_events"]
        self.has_registered_events = snapshot["has_registered_events"]
        self.open_events = snapshot["open_events"]
        self.has_open_events = snapshot["has_open_events"]
        self.selected_semester_is_active = bool(snapshot.get("selected_semester_is_active", True))
        self.criterion_choice_labels = list(snapshot.get("criterion_choice_labels", []))
        if self.admin_new_event_semester_id == 0 or not any(
            int(item["id"]) == self.admin_new_event_semester_id for item in self.semesters
        ):
            self.admin_new_event_semester_id = int(self.selected_semester_id)
        choices = self.criterion_choice_labels
        if choices and (not self.admin_event_criterion_choice or self.admin_event_criterion_choice not in choices):
            self.admin_event_criterion_choice = choices[0]
        self._sync_admin_stage_fields_from_snapshot(snapshot)
        self.loading = False

    def _sync_admin_stage_fields_from_snapshot(self, snapshot: dict) -> None:
        rows = list(snapshot.get("admin_stage_window_rows", [])) if self.current_user_role == "admin" else []
        self.admin_stage_0_label = str(rows[0]["label"]) if len(rows) > 0 else ""
        self.admin_stage_0_start = str(rows[0]["start"]) if len(rows) > 0 else ""
        self.admin_stage_0_end = str(rows[0]["end"]) if len(rows) > 0 else ""
        self.admin_stage_1_label = str(rows[1]["label"]) if len(rows) > 1 else ""
        self.admin_stage_1_start = str(rows[1]["start"]) if len(rows) > 1 else ""
        self.admin_stage_1_end = str(rows[1]["end"]) if len(rows) > 1 else ""
        self.admin_stage_2_label = str(rows[2]["label"]) if len(rows) > 2 else ""
        self.admin_stage_2_start = str(rows[2]["start"]) if len(rows) > 2 else ""
        self.admin_stage_2_end = str(rows[2]["end"]) if len(rows) > 2 else ""
        self.admin_stage_3_label = str(rows[3]["label"]) if len(rows) > 3 else ""
        self.admin_stage_3_start = str(rows[3]["start"]) if len(rows) > 3 else ""
        self.admin_stage_3_end = str(rows[3]["end"]) if len(rows) > 3 else ""

    def _refresh(self) -> None:
        if not self.is_authenticated or not self.selected_account_id:
            self.loading = False
            return
        snapshot = build_snapshot(
            current_user_id=self.selected_account_id or None,
            selected_semester_id=self.selected_semester_id or None,
            target_student_id=self.selected_student_id or None,
            selected_category_key=self.selected_evidence_category or None,
        )
        self._apply_snapshot(snapshot)

    def load(self) -> None:
        """Tải snapshot khi vào trang; không bật loading toàn màn hình để tránh giật UI."""
        if self.is_authenticated and self.selected_account_id:
            self._refresh()

    def set_login_username(self, value: str) -> None:
        self.login_username = value

    def set_login_password(self, value: str) -> None:
        self.login_password = value

    def show_login_form(self) -> None:
        self.auth_mode = "login"
        self.login_error = ""
        self.flash_message = ""

    def show_register_form(self) -> None:
        self.auth_mode = "register"
        self.login_error = ""
        self.flash_message = ""

    def set_register_field(self, field_name: str, value: str) -> None:
        setattr(self, field_name, value)

    def reset_register_form(self) -> None:
        self.register_username = ""
        self.register_password = ""
        self.register_password_confirm = ""
        self.register_full_name = ""
        self.register_student_code = ""
        self.register_email = ""
        self.register_class_name = ""
        self.register_faculty = ""
        self.register_major = ""

    def register_account(self) -> None:
        if self.register_password != self.register_password_confirm:
            self._set_flash("Mật khẩu xác nhận không khớp.", "error")
            return
        try:
            account = register_user_account(
                username=self.register_username,
                password=self.register_password,
                full_name=self.register_full_name,
                student_code=self.register_student_code,
                email=self.register_email,
                class_name=self.register_class_name,
                faculty=self.register_faculty,
                major=self.register_major,
            )
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.login_username = str(account["username"])
        self.login_password = ""
        self.auth_mode = "login"
        self.login_error = ""
        self.reset_register_form()
        self._set_flash("Đăng ký thành công. Tài khoản mới mặc định có quyền Sinh viên.", "success")

    def login(self) -> None:
        try:
            auth = authenticate_user(
                username=self.login_username.strip(),
                password=self.login_password,
            )
        except ValueError as exc:
            self.login_error = str(exc)
            self.is_authenticated = False
            return
        self.login_error = ""
        self.is_authenticated = True
        self.auth_mode = "login"
        self.loading = True
        self.selected_account_id = int(auth["id"])
        self.selected_student_id = 0
        self.selected_semester_id = 0
        role = str(auth["role"])
        if role in {"advisor", "class_monitor"}:
            self.active_tab = "students"
            self.nav_students_open = True
        else:
            self.active_tab = "student_info"
            self.nav_students_open = role == "admin"
        self.event_tab = "joined"
        self.login_password = ""
        self._refresh()
        self._set_flash(f"Đăng nhập thành công ({auth['role_label']}).", "success")

    def logout(self) -> None:
        self.is_authenticated = False
        self.loading = False
        self.auth_mode = "login"
        self.selected_account_id = 0
        self.selected_student_id = 0
        self.selected_semester_id = 0
        self.students = []
        self.semesters = []
        self.current_user_class_name = ""
        self.current_user_student_code = ""
        self.role_management_rows = []
        self.score_rows = []
        self.evidence_rows = []
        self.joined_events = []
        self.registered_events = []
        self.open_events = []
        self.student_profile = {}
        self.flash_message = ""
        self.flash_kind = "info"
        self.login_error = ""
        self.reset_register_form()
        self.login_password = ""
        self.nav_students_open = True

    def toggle_students_nav(self) -> None:
        self.nav_students_open = not self.nav_students_open

    def open_students_list(self) -> None:
        self.nav_students_open = True
        self.active_tab = "students"
        self._refresh()

    def select_tab(self, tab: str) -> None:
        if tab == "role_management" and self.current_user_role not in {"admin", "advisor"}:
            self._set_flash("Bạn không có quyền truy cập phần phân quyền tài khoản.", "error")
            self.active_tab = "student_info"
            self._refresh()
            return
        if tab == "admin_conduct_timeline" and self.current_user_role != "admin":
            self._set_flash("Chỉ quản trị viên được cấu hình mốc thời gian.", "error")
            self.active_tab = "student_info"
            self._refresh()
            return
        if tab == "admin_events" and self.current_user_role != "admin":
            self._set_flash("Chỉ quản trị viên được tạo sự kiện.", "error")
            self.active_tab = "student_info"
            self._refresh()
            return
        if tab == "students_evidence" and self.current_user_role != "class_monitor":
            self._set_flash("Cố vấn học tập và admin không duyệt minh chứng.", "error")
            self.active_tab = "students"
            self.nav_students_open = True
            self._refresh()
            return
        if tab in ("students_score", "students_evidence"):
            if not self.selected_student_id:
                self._set_flash("Hãy vào Danh sách sinh viên và chọn một sinh viên trước.", "error")
                self.active_tab = "students"
                self.nav_students_open = True
                self._refresh()
                return
        if tab in ("students", "students_score", "students_evidence"):
            self.nav_students_open = True
        if tab in {"score", "evidence", "events"} and self.current_user_role in {"student", "class_monitor"}:
            self.selected_student_id = self.selected_account_id
            self.selected_semester_id = 0
        if tab == "student_info" and self.current_user_role in {"student", "class_monitor"}:
            self.selected_student_id = self.selected_account_id
        self.active_tab = tab
        self._refresh()

    def select_event_tab(self, tab: str) -> None:
        self.event_tab = tab

    def select_student_by_label(self, label: str) -> None:
        found = next((item for item in self.students if item["label"] == label), None)
        if not found:
            return
        self.selected_student_id = int(found["id"])
        self._refresh()

    def pick_student_open_score(self, label: str) -> None:
        self.select_student_by_label(label)
        if self.current_user_role in {"class_monitor", "advisor", "admin"}:
            self.active_tab = "students_score"
            self.nav_students_open = True
        else:
            self.active_tab = "score"

    def pick_student_open_info(self, label: str) -> None:
        self.select_student_by_label(label)
        self.active_tab = "student_detail"
        self.nav_students_open = True

    def select_semester_by_name(self, name: str) -> None:
        found = next((item for item in self.semesters if item["name"] == name), None)
        if not found:
            return
        self.selected_semester_id = int(found["id"])
        self._refresh()

    def select_admin_new_event_semester(self, name: str) -> None:
        found = next((item for item in self.semesters if item["name"] == name), None)
        if found:
            self.admin_new_event_semester_id = int(found["id"])

    def submit_admin_event(self) -> None:
        if self.current_user_role != "admin":
            return
        name = self.admin_new_event_name.strip()
        if not name:
            self._set_flash("Nhập tên sự kiện.", "error")
            return
        choice = (self.admin_event_criterion_choice or "").strip()
        if "|" not in choice:
            self._set_flash("Chọn tiêu chí cộng điểm.", "error")
            return
        try:
            criterion_id = int(choice.split("|", 1)[0])
        except ValueError:
            self._set_flash("Chọn tiêu chí cộng điểm.", "error")
            return
        raw_points = (self.admin_new_event_points or "0").strip().replace(",", ".")
        try:
            points = float(raw_points)
        except ValueError:
            self._set_flash("Điểm tối đa không hợp lệ.", "error")
            return
        semester_id = int(self.admin_new_event_semester_id or self.selected_semester_id)
        try:
            create_admin_event(self.selected_account_id, semester_id, criterion_id, name, points)
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.admin_new_event_name = ""
        self.admin_new_event_points = "1"
        self._refresh()
        self._set_flash("Đã tạo sự kiện mới.", "success")

    def save_admin_stage_windows(self) -> None:
        if self.current_user_role != "admin":
            return
        sid = int(self.selected_semester_id or 0) or int(self.admin_new_event_semester_id or 0)
        if not sid:
            self._set_flash("Chọn học kỳ (ô bên dưới).", "error")
            return
        rows = [
            {"label": self.admin_stage_0_label.strip(), "start": self.admin_stage_0_start.strip(), "end": self.admin_stage_0_end.strip()},
            {"label": self.admin_stage_1_label.strip(), "start": self.admin_stage_1_start.strip(), "end": self.admin_stage_1_end.strip()},
            {"label": self.admin_stage_2_label.strip(), "start": self.admin_stage_2_start.strip(), "end": self.admin_stage_2_end.strip()},
            {"label": self.admin_stage_3_label.strip(), "start": self.admin_stage_3_start.strip(), "end": self.admin_stage_3_end.strip()},
        ]
        try:
            update_semester_stage_windows(self.selected_account_id, sid, rows)
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self._refresh()
        self._set_flash("Đã lưu mốc thời gian đánh giá rèn luyện cho học kỳ đã chọn.", "success")

    def assign_role(self, user_id: int, role_value: str) -> None:
        try:
            update_user_role(self.selected_account_id, int(user_id), role_value)
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self._refresh()
        self._set_flash("Đã cập nhật quyền tài khoản.", "success")

    def select_evidence_category_key(self, category_key: str) -> None:
        self.selected_evidence_category = category_key
        self._refresh()

    def toggle_column_config(self) -> None:
        self.column_config_open = not self.column_config_open

    def reset_evidence_columns(self) -> None:
        self.show_student_code_col = True
        self.show_full_name_col = True
        self.show_class_col = True
        self.show_reporter_col = True
        self.show_status_col = True
        self.show_action_col = True

    def set_show_student_code_col(self, value: bool) -> None:
        self.show_student_code_col = value

    def toggle_show_student_code_col(self) -> None:
        self.show_student_code_col = not self.show_student_code_col

    def set_show_full_name_col(self, value: bool) -> None:
        self.show_full_name_col = value

    def toggle_show_full_name_col(self) -> None:
        self.show_full_name_col = not self.show_full_name_col

    def set_show_class_col(self, value: bool) -> None:
        self.show_class_col = value

    def toggle_show_class_col(self) -> None:
        self.show_class_col = not self.show_class_col

    def set_show_reporter_col(self, value: bool) -> None:
        self.show_reporter_col = value

    def toggle_show_reporter_col(self) -> None:
        self.show_reporter_col = not self.show_reporter_col

    def set_show_status_col(self, value: bool) -> None:
        self.show_status_col = value

    def toggle_show_status_col(self) -> None:
        self.show_status_col = not self.show_status_col

    def set_show_action_col(self, value: bool) -> None:
        self.show_action_col = value

    def toggle_show_action_col(self) -> None:
        self.show_action_col = not self.show_action_col

    def set_form_value(self, field_name: str, value: str) -> None:
        setattr(self, field_name, value)

    def set_note_value(self, field_name: str, value: str) -> None:
        setattr(self, field_name, value)

    def reset_evidence_form(self) -> None:
        self.evidence_award_level = ""
        self.evidence_activity_content = ""
        self.evidence_participation_time = ""
        self.evidence_url = ""
        self.evidence_file_name = ""
        self.evidence_event_name = ""
        self.evidence_share_time = ""
        self.evidence_social_type = ""
        self.evidence_residence_type = "Ngoại trú"
        self.evidence_dormitory = ""
        self.evidence_room_number = ""
        self.evidence_city = ""
        self.evidence_district = ""
        self.evidence_ward = ""
        self.evidence_street_address = ""
        self.evidence_host_name = ""
        self.evidence_host_phone = ""

    def handle_evidence_upload(self, files: list[rx.UploadFile]) -> None:
        if not files:
            self.evidence_file_name = ""
            return
        self.evidence_file_name = str(files[0].filename or "")

    def open_evidence_modal(self) -> None:
        self.reset_evidence_form()
        self.evidence_modal_open = True
        return rx.clear_selected_files(EVIDENCE_UPLOAD_ID)

    def close_evidence_modal(self) -> None:
        self.evidence_modal_open = False
        return rx.clear_selected_files(EVIDENCE_UPLOAD_ID)

    def _evidence_payload(self) -> dict[str, str]:
        if self.selected_evidence_category == "special_achievement":
            return {
                "award_level": self.evidence_award_level.strip(),
                "activity_content": self.evidence_activity_content.strip(),
                "participation_time": self.evidence_participation_time.strip(),
                "url": self.evidence_url.strip(),
                "file_name": self.evidence_file_name.strip(),
            }
        if self.selected_evidence_category == "positive_promotion":
            return {
                "activity_content": self.evidence_activity_content.strip(),
                "event_name": self.evidence_event_name.strip(),
                "share_time": self.evidence_share_time.strip(),
                "url": self.evidence_url.strip(),
                "file_name": self.evidence_file_name.strip(),
            }
        if self.selected_evidence_category == "social_work":
            return {
                "social_type": self.evidence_social_type.strip(),
                "participation_time": self.evidence_participation_time.strip(),
                "url": self.evidence_url.strip(),
                "file_name": self.evidence_file_name.strip(),
            }
        if self.evidence_residence_type.strip() == "Nội trú":
            return {
                "residence_type": self.evidence_residence_type.strip(),
                "dormitory": self.evidence_dormitory.strip(),
                "room_number": self.evidence_room_number.strip(),
                "file_name": self.evidence_file_name.strip(),
            }
        return {
            "residence_type": self.evidence_residence_type.strip(),
            "city": self.evidence_city.strip(),
            "district": self.evidence_district.strip(),
            "ward": self.evidence_ward.strip(),
            "street_address": self.evidence_street_address.strip(),
            "host_name": self.evidence_host_name.strip(),
            "host_phone": self.evidence_host_phone.strip(),
            "file_name": self.evidence_file_name.strip(),
        }

    def submit_evidence(self) -> None:
        payload = self._evidence_payload()
        required = {
            "special_achievement": ["award_level", "activity_content", "participation_time", "file_name"],
            "positive_promotion": ["activity_content", "share_time", "file_name"],
            "social_work": ["social_type", "participation_time", "file_name"],
            "residence": ["residence_type"],
        }[self.selected_evidence_category]
        if self.selected_evidence_category == "residence":
            if self.evidence_residence_type.strip() == "Nội trú":
                required = ["residence_type", "dormitory", "room_number", "file_name"]
            else:
                required = ["residence_type", "city", "district", "ward", "street_address", "host_name", "host_phone", "file_name"]
        missing = [key for key in required if not payload.get(key)]
        if missing:
            self._set_flash("Vui lòng nhập đầy đủ các trường bắt buộc của minh chứng.", "error")
            return
        try:
            create_evidence(
                current_user_id=self.selected_account_id,
                target_student_id=self.selected_student_id,
                semester_id=self.selected_semester_id,
                category_key=self.selected_evidence_category,
                payload=payload,
            )
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.evidence_modal_open = False
        self.reset_evidence_form()
        self._refresh()
        self._set_flash("Đã thêm minh chứng mới.", "success")
        return rx.clear_selected_files(EVIDENCE_UPLOAD_ID)

    def open_evidence_detail(self, evidence_id: int) -> None:
        try:
            detail = load_evidence_detail(
                evidence_id=evidence_id,
                current_user_id=self.selected_account_id,
                target_student_id=self.selected_student_id,
            )
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.selected_evidence_detail = detail
        self.selected_evidence_title = str(detail.get("title", "Chi tiết minh chứng"))
        self.selected_evidence_status_label = str(detail.get("status_label", ""))
        self.selected_evidence_fields = list(detail.get("fields", []))
        self.selected_evidence_can_class_review = bool(detail.get("can_class_review", False))
        self.selected_evidence_can_advisor_review = bool(detail.get("can_advisor_review", False))
        self.evidence_detail_open = True

    def close_evidence_detail(self) -> None:
        self.evidence_detail_open = False
        self.selected_evidence_detail = {}
        self.selected_evidence_title = ""
        self.selected_evidence_status_label = ""
        self.selected_evidence_fields = []
        self.selected_evidence_can_class_review = False
        self.selected_evidence_can_advisor_review = False

    def approve_selected_evidence_class(self) -> None:
        try:
            review_evidence(self.selected_account_id, int(self.selected_evidence_detail["id"]), "class_approve")
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.close_evidence_detail()
        self._refresh()
        self._set_flash("Ban cán sự đã duyệt minh chứng.", "success")

    def approve_selected_evidence_advisor(self) -> None:
        try:
            review_evidence(self.selected_account_id, int(self.selected_evidence_detail["id"]), "advisor_approve")
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.close_evidence_detail()
        self._refresh()
        self._set_flash("Cố vấn học tập đã xác nhận minh chứng.", "success")

    def reject_selected_evidence(self) -> None:
        try:
            review_evidence(self.selected_account_id, int(self.selected_evidence_detail["id"]), "reject")
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self.close_evidence_detail()
        self._refresh()
        self._set_flash("Đã từ chối minh chứng.", "success")

    def remove_evidence(self, evidence_id: int) -> None:
        try:
            delete_evidence(self.selected_account_id, evidence_id)
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self._refresh()
        self._set_flash("Đã xóa minh chứng.", "success")

    def open_event_detail(self, event_id: str) -> None:
        event = next((item for item in self.joined_events if item["id"] == event_id), None)
        if event is None:
            event = next((item for item in self.registered_events if item["id"] == event_id), None)
        if event is None:
            event = next((item for item in self.open_events if item["id"] == event_id), None)
        if event is None:
            self._set_flash("Không tìm thấy chi tiết sự kiện.", "error")
            return
        self.selected_event = event
        self.selected_event_type_label = str(event.get("type_label", "Sự kiện"))
        self.selected_event_name = str(event.get("event_name", ""))
        self.selected_event_start_time = str(event.get("start_time", ""))
        self.selected_event_end_time = str(event.get("end_time", ""))
        self.selected_event_location = str(event.get("location", ""))
        self.selected_event_counts_to_score = str(event.get("counts_to_score", ""))
        self.selected_event_note = str(event.get("note", ""))
        self.event_modal_open = True

    def close_event_detail(self) -> None:
        self.event_modal_open = False
        self.selected_event = {}
        self.selected_event_type_label = ""
        self.selected_event_name = ""
        self.selected_event_start_time = ""
        self.selected_event_end_time = ""
        self.selected_event_location = ""
        self.selected_event_counts_to_score = ""
        self.selected_event_note = ""

    def register_event(self, event_id: str) -> None:
        try:
            register_event_for_student(self.selected_account_id, self.selected_student_id, int(event_id))
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self._refresh()
        self._set_flash("Đã đăng ký sự kiện.", "success")

    def approve_event(self, participation_id: int) -> None:
        try:
            approve_registered_event(self.selected_account_id, participation_id)
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return
        self._refresh()
        self._set_flash("Đã duyệt tham gia sự kiện.", "success")

    def update_score(self, criterion_id: int, field_name: str, value: str) -> None:
        updated_rows = []
        for row in self.score_rows:
            if row.get("criterion_id") == int(criterion_id):
                row = {**row, field_name: value}
            updated_rows.append(row)
        self.score_rows = updated_rows

    def _score_payload(self) -> dict[int, dict[str, str]]:
        payload: dict[int, dict[str, str]] = {}
        for row in self.score_rows:
            criterion_id = int(row.get("criterion_id", 0) or 0)
            if not criterion_id:
                continue
            payload[criterion_id] = {
                "self_score": str(row.get("self_score", "")),
                "class_score": str(row.get("class_score", "")),
                "advisor_score": str(row.get("advisor_score", "")),
            }
        return payload

    def _save_scores(self, action: str) -> bool:
        try:
            save_submission_scores(
                current_user_id=self.selected_account_id,
                target_student_id=self.selected_student_id,
                semester_id=self.selected_semester_id,
                payload=self._score_payload(),
                notes={
                    "student_note": self.student_note,
                    "class_note": self.class_note,
                    "advisor_note": self.advisor_note,
                },
                action=action,
            )
        except ValueError as exc:
            self._set_flash(str(exc), "error")
            return False
        self._refresh()
        return True

    def save_student_draft(self) -> None:
        if self._save_scores("save_draft"):
            self._set_flash("Đã lưu phiếu điểm.", "success")

    def submit_student_scores(self) -> None:
        if self._save_scores("submit_student"):
            self._set_flash("Sinh viên đã gửi phiếu đánh giá.", "success")

    def approve_class_scores(self) -> None:
        if self._save_scores("review_class"):
            self._set_flash("Đã duyệt phiếu điểm.", "success")

    def approve_advisor_scores(self) -> None:
        if self._save_scores("review_advisor"):
            self._set_flash("Cố vấn học tập đã xác nhận phiếu điểm.", "success")

    def reset_submission(self) -> None:
        if self._save_scores("reset"):
            self._set_flash("Admin đã đặt lại phiếu về trạng thái chưa gửi.", "success")

    def download_conduct_pdf(self):
        if not self.can_download_conduct_pdf:
            self._set_flash("Bạn không có quyền tải phiếu này.", "error")
            return
        try:
            data = export_conduct_pdf_bytes(
                self.selected_account_id,
                self.selected_student_id,
                self.selected_semester_id,
            )
        except (ValueError, FileNotFoundError) as exc:
            self._set_flash(str(exc), "error")
            return
        code = (self.selected_student_code or "sv").strip().replace("/", "-")
        return rx.download(data=data, filename=f"phieu_rl_{code}.pdf", mime_type="application/pdf")

    def set_student_list_filter(self, value: str) -> None:
        self.student_list_filter = value

    @rx.var
    def filtered_students(self) -> list[dict]:
        q = (self.student_list_filter or "").lower().strip()
        base = list(self.students)
        if not q:
            return base
        out: list[dict] = []
        for r in base:
            label = str(r.get("label", "")).lower()
            total = str(r.get("score_total", "")).lower()
            grade = str(r.get("conduct_grade", "")).lower()
            if q in label or q in total or q in grade:
                out.append(r)
        return out

    @rx.var
    def selected_evidence_category_label(self) -> str:
        return CATEGORY_LABELS.get(self.selected_evidence_category, "Minh chứng")

    @rx.var
    def student_labels(self) -> list[str]:
        return [str(item["label"]) for item in self.students]

    @rx.var
    def semester_names(self) -> list[str]:
        return [str(item["name"]) for item in self.semesters]

    @rx.var
    def evidence_grid_columns(self) -> str:
        parts = ["64px"]
        if self.show_student_code_col:
            parts.append("160px")
        if self.show_full_name_col:
            parts.append("220px")
        if self.show_class_col:
            parts.append("160px")
        if self.show_reporter_col:
            parts.append("180px")
        if self.show_status_col:
            parts.append("180px")
        if self.show_action_col:
            parts.append("minmax(200px, 1fr)")
        return " ".join(parts)

    @rx.var
    def admin_new_event_semester_name(self) -> str:
        for item in self.semesters:
            if int(item["id"]) == int(self.admin_new_event_semester_id or 0):
                return str(item["name"])
        if self.semesters:
            return str(self.semesters[0]["name"])
        return ""

    @rx.var
    def show_declaration_tabs(self) -> bool:
        return self.current_user_role in {"student", "class_monitor"}

    @rx.var
    def show_student_directory_tab(self) -> bool:
        return self.current_user_role in {"class_monitor", "advisor", "admin"}

    @rx.var
    def show_self_score_tab(self) -> bool:
        return self.current_user_role == "student"

    @rx.var
    def show_students_score_tab(self) -> bool:
        return self.current_user_role in {"class_monitor", "advisor", "admin"}

    @rx.var
    def show_students_evidence_tab(self) -> bool:
        return self.current_user_role == "class_monitor"

    @rx.var
    def show_role_management_tab(self) -> bool:
        return self.current_user_role in {"admin", "advisor"}

    @rx.var
    def main_info_sidebar_label(self) -> str:
        if self.current_user_role == "admin":
            return "Thông tin quản trị viên"
        if self.current_user_role == "advisor":
            return "Thông tin giảng viên"
        return "Thông tin sinh viên"

    @rx.var
    def nav_students_parent_active(self) -> bool:
        return self.active_tab in {"students", "students_score", "students_evidence"}

    @rx.var
    def grading_target_banner_text(self) -> str:
        if self.active_tab not in {"students_score", "students_evidence"}:
            return ""
        if self.current_user_role not in {"class_monitor", "advisor", "admin"}:
            return ""
        name = self.selected_student_name or ""
        code = self.selected_student_code or ""
        if not name and not code:
            return ""
        return f"Đang xét cho: {name} ({code})".strip()
