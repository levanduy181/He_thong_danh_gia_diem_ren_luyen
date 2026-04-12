from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, form_input, form_label
from ptit_reflex.ui.styles import BORDER, MUTED, TEXT


def _admin_stage_block(title: str, lab, start, end, set_lab, set_start, set_end) -> rx.Component:
    return rx.box(
        rx.text(title, font_size="14px", font_weight="700", color=TEXT, margin_bottom="8px"),
        form_label("Tên bước"),
        form_input(lab, "Ví dụ: Sinh viên đánh giá", set_lab),
        form_label("Bắt đầu (dd/mm/yyyy hh:mm)"),
        form_input(start, "01/02/2026 00:00", set_start),
        form_label("Kết thúc (dd/mm/yyyy hh:mm)"),
        form_input(end, "31/07/2026 23:45", set_end),
        width="100%",
        padding="14px 0",
        border_bottom=f"1px solid {BORDER}",
    )


def admin_conduct_timeline_page() -> rx.Component:
    return rx.vstack(
        rx.text("Mốc thời gian phiếu điểm rèn luyện", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Cấu hình 4 bước trên timeline (minh chứng → tự đánh giá → ban cán sự → CVHT). Áp dụng cho học kỳ đã chọn. Định dạng: dd/mm/yyyy hh:mm.",
            font_size="14px",
            color=MUTED,
        ),
        rx.box(
            rx.vstack(
                form_label("Học kỳ", required=True),
                rx.select(
                    ConductState.semester_names,
                    value=ConductState.selected_semester_name,
                    on_change=ConductState.select_semester_by_name,
                    width="100%",
                ),
                _admin_stage_block(
                    "Bước 1",
                    ConductState.admin_stage_0_label,
                    ConductState.admin_stage_0_start,
                    ConductState.admin_stage_0_end,
                    ConductState.set_form_value("admin_stage_0_label"),
                    ConductState.set_form_value("admin_stage_0_start"),
                    ConductState.set_form_value("admin_stage_0_end"),
                ),
                _admin_stage_block(
                    "Bước 2",
                    ConductState.admin_stage_1_label,
                    ConductState.admin_stage_1_start,
                    ConductState.admin_stage_1_end,
                    ConductState.set_form_value("admin_stage_1_label"),
                    ConductState.set_form_value("admin_stage_1_start"),
                    ConductState.set_form_value("admin_stage_1_end"),
                ),
                _admin_stage_block(
                    "Bước 3",
                    ConductState.admin_stage_2_label,
                    ConductState.admin_stage_2_start,
                    ConductState.admin_stage_2_end,
                    ConductState.set_form_value("admin_stage_2_label"),
                    ConductState.set_form_value("admin_stage_2_start"),
                    ConductState.set_form_value("admin_stage_2_end"),
                ),
                _admin_stage_block(
                    "Bước 4",
                    ConductState.admin_stage_3_label,
                    ConductState.admin_stage_3_start,
                    ConductState.admin_stage_3_end,
                    ConductState.set_form_value("admin_stage_3_label"),
                    ConductState.set_form_value("admin_stage_3_start"),
                    ConductState.set_form_value("admin_stage_3_end"),
                ),
                rx.box(action_button("Lưu mốc thời gian", ConductState.save_admin_stage_windows), width="200px"),
                width="100%",
                align="stretch",
                spacing="4",
                max_width="640px",
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
