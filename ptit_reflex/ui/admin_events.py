from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, form_input, form_label
from ptit_reflex.ui.styles import BORDER, MUTED, TEXT


def admin_events_page() -> rx.Component:
    return rx.vstack(
        rx.text("Tạo sự kiện", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Chỉ tạo các sự kiện tự động tính điểm rèn luyện trong học kỳ đã chọn. Sinh viên chỉ đăng ký được trong học kỳ đang hoạt động và điểm chỉ cộng cho đúng học kỳ của sự kiện đó.",
            font_size="14px",
            color=MUTED,
        ),
        rx.box(
            rx.vstack(
                form_label("Học kỳ", required=True),
                rx.select(
                    ConductState.semester_names,
                    value=ConductState.admin_new_event_semester_name,
                    on_change=ConductState.select_admin_new_event_semester,
                    width="100%",
                ),
                form_label("Tiêu chí cộng điểm", required=True),
                rx.select(
                    ConductState.criterion_choice_labels,
                    value=ConductState.admin_event_criterion_choice,
                    on_change=ConductState.set_form_value("admin_event_criterion_choice"),
                    width="100%",
                ),
                form_label("Tên sự kiện", required=True),
                form_input(
                    ConductState.admin_new_event_name,
                    "Ví dụ: Ngày hội việc làm ATTT 2026",
                    ConductState.set_form_value("admin_new_event_name"),
                ),
                rx.hstack(
                    rx.box(
                        form_label("Thời gian bắt đầu", required=True),
                        form_input(
                            ConductState.admin_new_event_start_time,
                            "Chọn thời gian bắt đầu",
                            ConductState.set_form_value("admin_new_event_start_time"),
                            input_type="datetime-local",
                        ),
                        width="100%",
                    ),
                    rx.box(
                        form_label("Thời gian kết thúc", required=True),
                        form_input(
                            ConductState.admin_new_event_end_time,
                            "Chọn thời gian kết thúc",
                            ConductState.set_form_value("admin_new_event_end_time"),
                            input_type="datetime-local",
                        ),
                        width="100%",
                    ),
                    width="100%",
                    spacing="4",
                    align="start",
                    flex_wrap="wrap",
                ),
                form_label("Địa điểm", required=True),
                form_input(
                    ConductState.admin_new_event_location,
                    "Ví dụ: Hội trường A2, cơ sở Hà Đông",
                    ConductState.set_form_value("admin_new_event_location"),
                ),
                form_label("Điểm tối đa", required=True),
                form_input(
                    ConductState.admin_new_event_points,
                    "1",
                    ConductState.set_form_value("admin_new_event_points"),
                ),
                rx.box(action_button("Tạo sự kiện", ConductState.submit_admin_event), width="200px"),
                width="100%",
                align="stretch",
                spacing="4",
                max_width="560px",
            ),
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            padding="24px",
            width="100%",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )
