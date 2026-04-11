from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, badge, timeline
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, PRIMARY_SOFT, SURFACE, TEXT


def score_value_input(row: dict, field_name: str, editable_key: str) -> rx.Component:
    return rx.cond(
        row[editable_key],
        rx.input(
            value=row[field_name],
            on_change=ConductState.update_score(row["criterion_id"], field_name),
            width="100px",
            height="38px",
            text_align="center",
            border=f"1px solid {BORDER}",
            border_radius="6px",
            background="white",
        ),
        rx.box(
            rx.text(row[field_name], font_size="14px", color=rx.cond(row[field_name] == "", "#c7c7c7", MUTED)),
            width="100px",
            height="38px",
            border=f"1px solid {BORDER}",
            border_radius="6px",
            background=SURFACE,
            display="flex",
            align_items="center",
            justify_content="center",
        ),
    )


def score_header_cell(label: str, width: str, align: str = "center") -> rx.Component:
    return rx.box(
        rx.text(label, font_size="13px", font_weight="700", color="#374151", text_align=align),
        width=width,
        flex=rx.cond(width == "auto", "1", "none"),
        padding="14px 10px",
        border_right=f"1px solid {BORDER}",
        display="flex",
        align_items="center",
        justify_content="center" if align == "center" else "flex-start",
    )


def score_group_row(group: dict) -> rx.Component:
    return rx.hstack(
        rx.box(rx.text(group["title"], font_size="14px", font_weight="600", color=TEXT, line_height="1.6"), flex="1", padding="14px 16px"),
        rx.box(rx.text(group["max_points"], font_size="14px", font_weight="600", color=TEXT), width="120px", padding="14px 10px", text_align="center"),
        rx.box(width="160px"),
        rx.box(width="160px"),
        rx.box(width="160px"),
        width="100%",
        spacing="0",
        border_top=f"1px solid {BORDER}",
        background="white",
    )


def score_item_row(row: dict) -> rx.Component:
    return rx.hstack(
        rx.box(rx.text(row["title"], font_size="14px", color="#374151", line_height="1.6", overflow_wrap="anywhere"), flex="1", min_width="200px", padding="14px 12px"),
        rx.box(rx.text(row["range"], font_size="14px", color=MUTED), width="120px", padding="14px 10px", text_align="center"),
        rx.box(score_value_input(row, "self_score", "self_editable"), width="160px", padding="10px 12px", display="flex", justify_content="center"),
        rx.box(score_value_input(row, "class_score", "class_editable"), width="160px", padding="10px 12px", display="flex", justify_content="center"),
        rx.box(score_value_input(row, "advisor_score", "advisor_editable"), width="160px", padding="10px 12px", display="flex", justify_content="center"),
        width="100%",
        spacing="0",
        border_top=f"1px solid {BORDER}",
        background="white",
        align="center",
    )


def score_table_row(row: dict) -> rx.Component:
    return rx.cond(row["kind"] == "group", score_group_row(row), score_item_row(row))


def total_row() -> rx.Component:
    return rx.hstack(
        rx.box(rx.text("TỔNG ĐIỂM", font_size="16px", font_weight="700", color=TEXT), flex="1", padding="16px"),
        rx.box(rx.text("100", font_size="14px", font_weight="700", color=TEXT), width="120px", padding="16px 10px", text_align="center"),
        rx.box(rx.text(ConductState.score_total, font_size="14px", font_weight="700", color=TEXT), width="160px", padding="16px 10px", text_align="center"),
        rx.box(rx.text(ConductState.score_total_class, font_size="14px", font_weight="700", color=TEXT), width="160px", padding="16px 10px", text_align="center"),
        rx.box(rx.text(ConductState.score_total_advisor, font_size="14px", font_weight="700", color=TEXT), width="160px", padding="16px 10px", text_align="center"),
        width="100%",
        spacing="0",
        border_top=f"1px solid {BORDER}",
        background="#f9fafb",
    )


SEMESTER_COL_WIDTH = "200px"


def score_page() -> rx.Component:
    semester_header = rx.box(
        rx.text("Học kỳ", font_size="14px", font_weight="700", color=TEXT),
        width="100%",
        min_height="52px",
        padding="12px 10px",
        display="flex",
        align_items="center",
        justify_content="center",
        text_align="center",
        border_bottom=f"1px solid {BORDER}",
        background="#fafafa",
    )
    score_title_row = rx.hstack(
        rx.hstack(
            rx.text("PHIẾU ĐIỂM RÈN LUYỆN", font_size="16px", font_weight="800", color=TEXT),
            rx.box(
                rx.hstack(
                    rx.text(ConductState.score_effective_total, color="white", font_size="13px", font_weight="700"),
                    rx.text("điểm", color="white", font_size="13px", font_weight="700"),
                    spacing="1",
                    align="center",
                ),
                background=PRIMARY,
                border_radius="8px",
                padding="6px 12px",
            ),
            badge(ConductState.conduct_grade_label, "#e0f2fe", color="#0369a1"),
            align="center",
            spacing="3",
            flex_wrap="wrap",
        ),
        rx.hstack(
            badge(ConductState.submission_status_label, "#e5e7eb", color=TEXT),
            rx.cond(ConductState.outside_window, badge("Ngoài thời gian chấm điểm", PRIMARY), rx.fragment()),
            spacing="3",
            align="center",
            flex_wrap="wrap",
        ),
        justify="between",
        align="center",
        width="100%",
        min_height="52px",
        padding="8px 12px",
        spacing="3",
        flex_wrap="wrap",
        border_bottom=f"1px solid {BORDER}",
        background="white",
    )
    merged_top_row = rx.hstack(
        rx.box(semester_header, width=SEMESTER_COL_WIDTH, flex_shrink="0", border_right=f"1px solid {BORDER}"),
        rx.box(score_title_row, flex="1", min_width="0"),
        width="100%",
        spacing="0",
        align="stretch",
        border_bottom=f"1px solid {BORDER}",
        background="white",
    )
    semester_list = rx.box(
        rx.foreach(
            ConductState.semesters,
            lambda semester: rx.box(
                rx.text(
                    semester["name"],
                    color=rx.cond(semester["id"] == ConductState.selected_semester_id, PRIMARY, "#374151"),
                    font_size="12px",
                    font_weight=rx.cond(semester["id"] == ConductState.selected_semester_id, "700", "500"),
                    line_height="1.45",
                ),
                padding="10px 8px",
                border_bottom=f"1px solid {BORDER}",
                border_left=rx.cond(semester["id"] == ConductState.selected_semester_id, f"3px solid {PRIMARY}", "3px solid transparent"),
                background=rx.cond(semester["id"] == ConductState.selected_semester_id, PRIMARY_SOFT, "white"),
                cursor="pointer",
                on_click=ConductState.select_semester_by_name(semester["name"]),
            ),
        ),
        width="100%",
        flex="1",
        min_height="0",
        overflow_y="auto",
        background="white",
    )
    semester_column = rx.box(
        semester_list,
        width=SEMESTER_COL_WIDTH,
        flex_shrink="0",
        border_right=f"1px solid {BORDER}",
        display="flex",
        flex_direction="column",
        min_height="0",
        background="white",
    )
    table_frame = rx.box(
        rx.box(
            rx.hstack(
                score_header_cell("NỘI DUNG", "auto"),
                score_header_cell("Điểm tối đa", "120px"),
                score_header_cell("Sinh viên", "160px"),
                score_header_cell("Duyệt", "160px"),
                score_header_cell("CVHT", "160px"),
                width="100%",
                spacing="0",
                background=SURFACE,
            ),
            rx.foreach(ConductState.score_rows, score_table_row),
            total_row(),
            rx.cond(
                ConductState.submission_status == "student_submitted",
                rx.box(
                    rx.text("Đã gửi đánh giá", font_size="14px", font_weight="600", color="#15803d"),
                    width="100%",
                    padding="12px 16px",
                    text_align="center",
                    border_top=f"1px solid {BORDER}",
                    background="#f0fdf4",
                ),
                rx.fragment(),
            ),
            min_width="900px",
            width="100%",
            background="white",
        ),
        width="100%",
        max_width="100%",
        overflow_x="auto",
        overflow_y="hidden",
        flex="1",
        min_height="0",
        border=f"1px solid {BORDER}",
        border_radius="8px",
        background="white",
    )
    main_column = rx.vstack(
        table_frame,
        rx.hstack(
            rx.cond(ConductState.can_save_student, action_button("Lưu tạm", ConductState.save_student_draft, background="white", color=TEXT, border=f"1px solid {BORDER}"), rx.fragment()),
            rx.cond(ConductState.can_submit_student, action_button("Gửi đánh giá", ConductState.submit_student_scores), rx.fragment()),
            rx.cond(ConductState.can_review_class, action_button("Duyệt", ConductState.approve_class_scores, background="#b91c1c"), rx.fragment()),
            rx.cond(ConductState.can_review_advisor, action_button("Xác nhận", ConductState.approve_advisor_scores, background="#15803d"), rx.fragment()),
            rx.cond(
                ConductState.can_download_conduct_pdf,
                action_button("Tải PDF", ConductState.download_conduct_pdf, background="white", color=TEXT, border=f"1px solid {BORDER}"),
                rx.fragment(),
            ),
            rx.cond(ConductState.can_reset_submission, action_button("Đặt lại", ConductState.reset_submission, background="#fff1f2", color=PRIMARY, border="1px solid #fecdd3"), rx.fragment()),
            justify="end",
            width="100%",
            flex_wrap="wrap",
            spacing="3",
        ),
        width="100%",
        align="stretch",
        spacing="4",
        min_width="0",
        flex="1",
    )
    body_row = rx.hstack(
        semester_column,
        rx.box(main_column, flex="1", min_width="0", padding="12px", display="flex", flex_direction="column"),
        width="100%",
        flex="1",
        min_height="0",
        align="stretch",
        spacing="0",
    )
    return rx.vstack(
        rx.text("Phiếu điểm rèn luyện", font_size="22px", font_weight="700", color=TEXT),
        rx.cond(
            ConductState.grading_target_banner_text != "",
            rx.box(
                rx.text(ConductState.grading_target_banner_text, font_size="14px", font_weight="600", color="#1e3a8a"),
                width="100%",
                padding="10px 14px",
                background="#eff6ff",
                border=f"1px solid {BORDER}",
                border_radius="8px",
            ),
            rx.fragment(),
        ),
        rx.box(
            rx.vstack(
                timeline(),
                rx.box(
                    merged_top_row,
                    body_row,
                    width="100%",
                    flex="1",
                    min_height="0",
                    display="flex",
                    flex_direction="column",
                    border=f"1px solid {BORDER}",
                    border_radius="10px",
                    overflow="hidden",
                    background="white",
                ),
                width="100%",
                align="stretch",
                spacing="4",
                min_height="0",
            ),
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            width="100%",
            max_width="100%",
            min_width="0",
            padding="20px",
        ),
        width="100%",
        align="stretch",
        spacing="4",
        min_width="0",
    )
