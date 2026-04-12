from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.primitives import action_button, badge
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, TEXT


def _student_filter_input() -> rx.Component:
    return rx.input(
        placeholder="Lọc theo tên, mã SV, điểm hoặc xếp loại…",
        value=ConductState.student_list_filter,
        on_change=ConductState.set_student_list_filter,
        width="100%",
        max_width="520px",
        height="40px",
        border=f"1px solid {BORDER}",
        border_radius="8px",
        padding_left="12px",
        padding_right="12px",
    )


def _review_semester_select() -> rx.Component:
    return rx.select(
        ConductState.semester_names,
        value=ConductState.selected_semester_name,
        on_change=ConductState.select_semester_by_name,
        width="280px",
        min_width="240px",
        max_width="280px",
        height="40px",
        border=f"1px solid {PRIMARY}",
        border_radius="10px",
        background="white",
        color=TEXT,
        font_size="14px",
        font_weight="500",
        padding_left="12px",
        padding_right="12px",
        flex_shrink="0",
    )


def _review_filters_row() -> rx.Component:
    return rx.hstack(
        rx.box(_student_filter_input(), flex="1", min_width="280px"),
        _review_semester_select(),
        width="100%",
        align="center",
        justify="between",
        spacing="3",
        flex_wrap="wrap",
    )


def students_list_page() -> rx.Component:
    return rx.vstack(
        rx.text("Danh sách sinh viên", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Nhấn vào tên sinh viên để xem thông tin chi tiết; dùng nút bên phải để mở phiếu điểm rèn luyện.",
            font_size="14px",
            color=MUTED,
        ),
        _review_filters_row(),
        rx.vstack(
            rx.foreach(
                ConductState.filtered_students,
                lambda row: rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                row["label"],
                                font_size="15px",
                                font_weight="700",
                                color=TEXT,
                                cursor="pointer",
                                on_click=ConductState.pick_student_open_info(row["label"]),
                            ),
                            rx.hstack(
                                rx.text("Điểm:", font_size="12px", font_weight="700", color=MUTED),
                                rx.text(row["score_total"], font_size="12px", font_weight="700", color="#92400e"),
                                rx.text("•", font_size="12px", color=MUTED),
                                rx.text(row["conduct_grade"], font_size="12px", font_weight="700", color="#0369a1"),
                                spacing="2",
                                align="center",
                                flex_wrap="wrap",
                            ),
                            spacing="1",
                            align="start",
                        ),
                        rx.hstack(
                            action_button(
                                "Xem phiếu điểm rèn luyện",
                                ConductState.pick_student_open_score(row["label"]),
                                background="white",
                                color=TEXT,
                                border=f"1px solid {BORDER}",
                            ),
                            spacing="3",
                            align="center",
                            flex_wrap="wrap",
                            justify="end",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                    ),
                    padding="16px 18px",
                    border=f"1px solid {BORDER}",
                    border_radius="10px",
                    background="white",
                    width="100%",
                    _hover={"background": "#f9fafb"},
                    key=row["id"],
                ),
            ),
            width="100%",
            spacing="3",
            align="stretch",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def score_review_list_page() -> rx.Component:
    return rx.vstack(
        rx.text("Duyệt phiếu điểm rèn luyện", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Danh sách dưới đây dành cho ban cán sự. Mở phiếu để xem, chỉnh điểm và chỉ duyệt trong màn phiếu khi đúng thời gian ban cán sự đánh giá.",
            font_size="14px",
            color=MUTED,
        ),
        _review_filters_row(),
        rx.vstack(
            rx.foreach(
                ConductState.filtered_students,
                lambda row: rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(row["full_name"], font_size="16px", font_weight="700", color=TEXT),
                            rx.hstack(
                                rx.text(row["student_code"], font_size="13px", color=MUTED),
                                rx.text("•", font_size="13px", color=MUTED),
                                rx.text(row["class_name"], font_size="13px", color=MUTED),
                                spacing="2",
                                align="center",
                                flex_wrap="wrap",
                            ),
                            badge(row["conduct_grade"], "#f0fdf4", color="#166534"),
                            spacing="2",
                            align="start",
                            min_width="0",
                        ),
                        rx.hstack(
                            rx.box(
                                rx.hstack(
                                    rx.text("Điểm:", font_size="12px", font_weight="700", color="#92400e"),
                                    rx.text(row["score_total"], font_size="12px", font_weight="700", color="#92400e"),
                                    spacing="1",
                                    align="center",
                                ),
                                background="#fffbeb",
                                border_radius="999px",
                                padding="6px 12px",
                            ),
                            action_button(
                                "Xem phiếu điểm rèn luyện",
                                ConductState.pick_student_open_score(row["label"]),
                                background="white",
                                color=TEXT,
                                border=f"1px solid {BORDER}",
                            ),
                            spacing="3",
                            align="center",
                            justify="end",
                            flex_wrap="wrap",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                        spacing="4",
                    ),
                    padding="18px",
                    border=f"1px solid {BORDER}",
                    border_radius="12px",
                    background="white",
                    width="100%",
                    _hover={"background": "#f9fafb"},
                    key=row["id"],
                ),
            ),
            width="100%",
            spacing="3",
            align="stretch",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def evidence_review_list_page() -> rx.Component:
    return rx.vstack(
        rx.text("Duyệt minh chứng", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Chọn từng sinh viên để mở lại màn hình duyệt minh chứng hiện có. Danh sách vẫn hiển thị số minh chứng đang chờ ban cán sự xử lý.",
            font_size="14px",
            color=MUTED,
        ),
        _review_filters_row(),
        rx.vstack(
            rx.foreach(
                ConductState.filtered_students,
                lambda row: rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(row["full_name"], font_size="16px", font_weight="700", color=TEXT),
                            rx.hstack(
                                rx.text(row["student_code"], font_size="13px", color=MUTED),
                                rx.text("•", font_size="13px", color=MUTED),
                                rx.text(row["class_name"], font_size="13px", color=MUTED),
                                spacing="2",
                                align="center",
                                flex_wrap="wrap",
                            ),
                            rx.hstack(
                                rx.text("Minh chứng chờ duyệt:", font_size="13px", font_weight="600", color="#9a3412"),
                                rx.text(row["pending_evidence_count"], font_size="13px", font_weight="700", color="#9a3412"),
                                spacing="2",
                                align="center",
                            ),
                            spacing="2",
                            align="start",
                            min_width="0",
                        ),
                        action_button(
                            "Mở duyệt minh chứng",
                            ConductState.pick_student_open_evidence(row["label"]),
                            background="white",
                            color=TEXT,
                            border=f"1px solid {BORDER}",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                        spacing="4",
                    ),
                    padding="18px",
                    border=f"1px solid {BORDER}",
                    border_radius="12px",
                    background="white",
                    width="100%",
                    _hover={"background": "#f9fafb"},
                    key=row["id"],
                ),
            ),
            width="100%",
            spacing="3",
            align="stretch",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def events_review_list_page() -> rx.Component:
    return rx.vstack(
        rx.text("Duyệt sự kiện", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Chọn từng sinh viên để mở danh sách sự kiện đã đăng ký và duyệt các đăng ký đang chờ xử lý.",
            font_size="14px",
            color=MUTED,
        ),
        _review_filters_row(),
        rx.vstack(
            rx.foreach(
                ConductState.filtered_students,
                lambda row: rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(row["full_name"], font_size="16px", font_weight="700", color=TEXT),
                            rx.hstack(
                                rx.text(row["student_code"], font_size="13px", color=MUTED),
                                rx.text("•", font_size="13px", color=MUTED),
                                rx.text(row["class_name"], font_size="13px", color=MUTED),
                                spacing="2",
                                align="center",
                                flex_wrap="wrap",
                            ),
                            rx.hstack(
                                rx.text("Sự kiện chờ duyệt:", font_size="13px", font_weight="600", color="#9a3412"),
                                rx.text(row["pending_event_count"], font_size="13px", font_weight="700", color="#9a3412"),
                                spacing="2",
                                align="center",
                            ),
                            spacing="2",
                            align="start",
                            min_width="0",
                        ),
                        action_button(
                            "Mở duyệt sự kiện",
                            ConductState.pick_student_open_events(row["label"]),
                            background="white",
                            color=TEXT,
                            border=f"1px solid {BORDER}",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                        spacing="4",
                    ),
                    padding="18px",
                    border=f"1px solid {BORDER}",
                    border_radius="12px",
                    background="white",
                    width="100%",
                    _hover={"background": "#f9fafb"},
                    key=row["id"],
                ),
            ),
            width="100%",
            spacing="3",
            align="stretch",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def timeline_step(item: dict) -> rx.Component:
    color = rx.cond(item["state"] == "upcoming", "#bdbdbd", PRIMARY)
    return rx.box(
        rx.cond(
            item["id"] != "3",
            rx.box(
                position="absolute",
                top="5px",
                left="calc(50% + 10px)",
                width="calc(100% - 20px)",
                height="3px",
                background=rx.cond(item["line_after"] == "done", PRIMARY, BORDER),
                border_radius="999px",
                z_index="1",
            ),
            rx.fragment(),
        ),
        rx.vstack(
            rx.box(width="12px", height="12px", border_radius="999px", background=color, box_shadow="0 0 0 4px white", z_index="2"),
            rx.text(item["start"], font_size="11px", font_weight="700", color=rx.cond(item["state"] == "upcoming", "#8a8a8a", TEXT)),
            rx.text(item["end"], font_size="11px", font_weight="700", color=rx.cond(item["state"] == "upcoming", "#8a8a8a", TEXT)),
            rx.text(item["label"], font_size="11px", color=rx.cond(item["state"] == "upcoming", "#8a8a8a", TEXT), text_align="center", line_height="1.5"),
            align="center",
            spacing="2",
            width="100%",
        ),
        position="relative",
        width="25%",
        min_height="120px",
        padding_top="0",
    )


def timeline() -> rx.Component:
    return rx.hstack(rx.foreach(ConductState.timeline, timeline_step), width="100%", spacing="0", align="start")
