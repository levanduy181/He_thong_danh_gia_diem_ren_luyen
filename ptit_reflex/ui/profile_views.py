from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.primitives import action_button, badge, form_input, form_text_area
from ptit_reflex.ui.student_lists import _review_semester_select
from ptit_reflex.ui.styles import BORDER, MUTED, SURFACE, TEXT


def profile_item(label: str, value) -> rx.Component:
    return rx.vstack(
        rx.text(label, font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
        rx.text(value, font_size="15px", color=TEXT, font_weight="600", line_height="1.5"),
        spacing="1",
        align="start",
        min_width="180px",
        width="100%",
    )


def profile_edit_field(label: str, field) -> rx.Component:
    return rx.vstack(
        rx.text(label, font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
        field,
        spacing="2",
        align="stretch",
        width="100%",
    )


def _admin_info_card() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin quản trị viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.current_user_name, font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                badge(ConductState.current_user_role_label, "#111827"),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.grid(
                profile_item("Họ tên", ConductState.current_user_name),
                profile_item("Email", ConductState.current_user_email),
                profile_item("Đơn vị", ConductState.current_user_faculty),
                profile_item("Vai trò", ConductState.current_user_role_label),
                columns="2",
                spacing="5",
                width="100%",
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def _advisor_info_card() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin giảng viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.current_user_name, font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                badge(ConductState.current_user_role_label, "#111827"),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.grid(
                profile_item("Họ tên", ConductState.current_user_name),
                profile_item("Email", ConductState.current_user_email),
                profile_item("Đơn vị", ConductState.current_user_faculty),
                profile_item("Lớp phụ trách", ConductState.current_user_class_name),
                columns="2",
                spacing="5",
                width="100%",
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def _student_profile_card() -> rx.Component:
    action_area = rx.cond(
        ConductState.can_edit_own_profile,
        rx.cond(
            ConductState.profile_editing,
            rx.hstack(
                action_button(
                    "Hủy",
                    ConductState.cancel_profile_edit,
                    background="white",
                    color=TEXT,
                    border=f"1px solid {BORDER}",
                ),
                action_button("Lưu thông tin", ConductState.save_profile),
                spacing="2",
                align="center",
                flex_wrap="wrap",
            ),
            action_button(
                "Sửa thông tin",
                ConductState.start_profile_edit,
                background="white",
                color=TEXT,
                border=f"1px solid {BORDER}",
            ),
        ),
        rx.fragment(),
    )
    advisor_gpa_area = rx.cond(
        ConductState.can_edit_student_gpa,
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text("GPA học kỳ", font_size="14px", font_weight="800", color=TEXT),
                        rx.text(
                            "Cố vấn nhập GPA tại đây để hệ thống tự tính tiêu chí kết quả học tập trong phiếu rèn luyện.",
                            font_size="12px",
                            color=MUTED,
                            line_height="1.6",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    _review_semester_select(),
                    width="100%",
                    justify="between",
                    align="start",
                    flex_wrap="wrap",
                    spacing="3",
                ),
                rx.hstack(
                    rx.box(
                        form_input(
                            ConductState.advisor_gpa_input,
                            "Ví dụ: 3.25",
                            ConductState.set_advisor_gpa_input,
                            input_type="number",
                        ),
                        width="240px",
                        max_width="100%",
                    ),
                    action_button("Lưu GPA", ConductState.save_advisor_gpa),
                    rx.text("Thang 4.0", font_size="12px", color=MUTED),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap",
                ),
                width="100%",
                spacing="3",
                align="stretch",
            ),
            width="100%",
            padding="16px",
            background="#fffbeb",
            border="1px solid #fde68a",
            border_radius="12px",
        ),
        rx.fragment(),
    )
    display_content = rx.vstack(
        rx.grid(
            profile_item("Mã sinh viên", ConductState.student_profile["student_code"]),
            profile_item("Họ tên", ConductState.student_profile["full_name"]),
            profile_item("Lớp", ConductState.student_profile["class_name"]),
            profile_item("Khoa", ConductState.student_profile["faculty"]),
            profile_item("Ngành", ConductState.student_profile["major"]),
            profile_item("Thông tin giảng viên", ConductState.student_profile["advisor_name"]),
            profile_item("Ban cán sự", ConductState.student_profile["class_monitor_name"]),
            profile_item("Email", ConductState.student_profile["email"]),
            profile_item("Số điện thoại", ConductState.student_profile["phone"]),
            profile_item("Ngày sinh", ConductState.student_profile["birth_date"]),
            profile_item("Giới tính", ConductState.student_profile["gender"]),
            profile_item("Trạng thái", ConductState.student_profile["status"]),
            columns="3",
            spacing="5",
            width="100%",
        ),
        rx.vstack(
            rx.text("Địa chỉ", font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
            rx.box(
                rx.text(ConductState.student_profile["address"], font_size="14px", color="#374151", line_height="1.7"),
                width="100%",
                padding="14px 16px",
                background=SURFACE,
                border=f"1px solid {BORDER}",
                border_radius="10px",
            ),
            spacing="2",
            align="stretch",
            width="100%",
        ),
        advisor_gpa_area,
        spacing="4",
        align="stretch",
        width="100%",
    )
    edit_content = rx.vstack(
        rx.grid(
            profile_edit_field(
                "Họ tên",
                form_input(
                    ConductState.profile_edit_full_name,
                    "Nhập họ tên",
                    ConductState.set_profile_field("profile_edit_full_name"),
                ),
            ),
            profile_edit_field(
                "Email",
                form_input(
                    ConductState.profile_edit_email,
                    "Nhập email",
                    ConductState.set_profile_field("profile_edit_email"),
                    input_type="email",
                ),
            ),
            profile_edit_field(
                "Số điện thoại",
                form_input(
                    ConductState.profile_edit_phone,
                    "Nhập số điện thoại",
                    ConductState.set_profile_field("profile_edit_phone"),
                ),
            ),
            profile_edit_field(
                "Ngày sinh",
                form_input(
                    ConductState.profile_edit_birth_date,
                    "Chọn ngày sinh",
                    ConductState.set_profile_field("profile_edit_birth_date"),
                    input_type="date",
                ),
            ),
            profile_edit_field(
                "Giới tính",
                rx.select(
                    ConductState.register_gender_options,
                    value=ConductState.profile_edit_gender,
                    on_change=ConductState.set_profile_field("profile_edit_gender"),
                    width="100%",
                    height="48px",
                    border=f"1px solid {BORDER}",
                    border_radius="8px",
                    background="white",
                    color=TEXT,
                ),
            ),
            profile_item("Mã sinh viên", ConductState.student_profile["student_code"]),
            profile_item("Lớp", ConductState.student_profile["class_name"]),
            profile_item("Khoa", ConductState.student_profile["faculty"]),
            profile_item("Ngành", ConductState.student_profile["major"]),
            profile_item("Thông tin giảng viên", ConductState.student_profile["advisor_name"]),
            profile_item("Ban cán sự", ConductState.student_profile["class_monitor_name"]),
            profile_item("Trạng thái", ConductState.student_profile["status"]),
            columns="3",
            spacing="5",
            width="100%",
        ),
        profile_edit_field(
            "Địa chỉ",
            form_text_area(
                ConductState.profile_edit_address,
                "Nhập địa chỉ hiện tại",
                ConductState.set_profile_field("profile_edit_address"),
            ),
        ),
        spacing="4",
        align="stretch",
        width="100%",
    )
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin sinh viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.student_profile["full_name"], font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                rx.hstack(
                    badge(ConductState.student_profile["class_name"], "#111827"),
                    rx.box(
                        rx.hstack(
                            rx.text("GPA", font_size="12px", font_weight="700", color="#1d4ed8"),
                            rx.text(ConductState.student_profile["gpa"], font_size="12px", font_weight="700", color="#1d4ed8"),
                            spacing="1",
                            align="center",
                        ),
                        background="#eff6ff",
                        border_radius="999px",
                        padding="6px 12px",
                    ),
                    action_area,
                    spacing="2",
                    align="center",
                    flex_wrap="wrap",
                ),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.cond(
                ConductState.profile_editing,
                rx.cond(ConductState.can_edit_own_profile, edit_content, display_content),
                display_content,
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def student_info_card() -> rx.Component:
    return rx.cond(
        ConductState.active_tab == "student_detail",
        _student_profile_card(),
        rx.cond(
            ConductState.current_user_role == "admin",
            _admin_info_card(),
            rx.cond(ConductState.current_user_role == "advisor", _advisor_info_card(), _student_profile_card()),
        ),
    )
