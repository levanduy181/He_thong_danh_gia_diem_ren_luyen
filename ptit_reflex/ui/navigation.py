from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.primitives import action_button, badge
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, TEXT


PTIT_LOGO_URL = "https://slink.ptit.edu.vn/logo.png"


def logo_block() -> rx.Component:
    return rx.hstack(
        rx.image(src=PTIT_LOGO_URL, width="58px", height="58px", object_fit="contain", alt="PTIT"),
        rx.vstack(
            rx.text("HỆ THỐNG ĐÁNH GIÁ", font_size="14px", font_weight="700", color=TEXT),
            rx.text("ĐIỂM RÈN LUYỆN", font_size="14px", font_weight="700", color=TEXT, line_height="1.2"),
            spacing="0",
            align="start",
        ),
        align="center",
        spacing="4",
    )


def sidebar_nav_item(label, tab_key: str) -> rx.Component:
    active = ConductState.active_tab == tab_key
    return rx.box(
        rx.text(
            label,
            color=rx.cond(active, "white", "#374151"),
            font_size="14px",
            font_weight=rx.cond(active, "700", "500"),
            line_height="1.45",
        ),
        padding="12px 14px",
        border_radius="8px",
        background=rx.cond(active, PRIMARY, "transparent"),
        cursor="pointer",
        width="100%",
        on_click=ConductState.select_tab(tab_key),
    )


def sidebar_nav_sub_item(label: str, tab_key: str) -> rx.Component:
    active = (
        (ConductState.active_tab == tab_key)
        | ((tab_key == "students_score_list") & (ConductState.active_tab == "students_score"))
        | ((tab_key == "students_evidence_list") & (ConductState.active_tab == "students_evidence"))
        | ((tab_key == "students_events_list") & (ConductState.active_tab == "students_events"))
    )
    return rx.box(
        rx.text(
            label,
            color=rx.cond(active, "white", "#4b5563"),
            font_size="13px",
            font_weight=rx.cond(active, "700", "500"),
            line_height="1.45",
        ),
        padding="8px 12px 8px 28px",
        border_radius="8px",
        background=rx.cond(active, PRIMARY, "transparent"),
        cursor="pointer",
        width="100%",
        on_click=ConductState.select_tab(tab_key),
    )


def sidebar_nav_sub_indicator(label: str, tab_key: str) -> rx.Component:
    active = ConductState.active_tab == tab_key
    return rx.box(
        rx.text(
            label,
            color=rx.cond(active, "white", "#6b7280"),
            font_weight=rx.cond(active, "700", "500"),
            font_size="13px",
            line_height="1.45",
        ),
        padding="8px 12px 8px 28px",
        border_radius="8px",
        background=rx.cond(active, PRIMARY, "transparent"),
        cursor="default",
        width="100%",
    )


def sidebar_students_group() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.text(
                    ConductState.student_directory_sidebar_label,
                    font_size="14px",
                    font_weight=rx.cond(ConductState.nav_students_parent_active, "700", "600"),
                    color=rx.cond(ConductState.nav_students_parent_active, "white", "#374151"),
                ),
                flex="1",
                padding="12px 8px 12px 14px",
                cursor="pointer",
                on_click=ConductState.open_students_list,
            ),
            rx.box(
                rx.text(rx.cond(ConductState.nav_students_open, "▾", "▸"), font_size="12px", color=MUTED, font_weight="700"),
                padding="12px 10px",
                cursor="pointer",
                on_click=ConductState.toggle_students_nav,
            ),
            width="100%",
            align="center",
            spacing="0",
            border_radius="8px",
            background=rx.cond(ConductState.nav_students_parent_active, PRIMARY, "transparent"),
        ),
        rx.cond(
            ConductState.nav_students_open,
            rx.cond(
                ConductState.current_user_role == "class_monitor",
                rx.vstack(
                    sidebar_nav_sub_item("Duyệt phiếu điểm rèn luyện", "students_score_list"),
                    sidebar_nav_sub_item("Duyệt minh chứng", "students_evidence_list"),
                    sidebar_nav_sub_item("Duyệt sự kiện", "students_events_list"),
                    spacing="2",
                    width="100%",
                    align="stretch",
                    padding_bottom="4px",
                ),
                rx.vstack(
                    rx.cond(ConductState.show_students_score_tab, sidebar_nav_sub_indicator("Phiếu điểm rèn luyện", "students_score"), rx.fragment()),
                    rx.cond(ConductState.show_students_evidence_tab, sidebar_nav_sub_item("Duyệt minh chứng", "students_evidence"), rx.fragment()),
                    rx.cond(ConductState.show_students_events_tab, sidebar_nav_sub_item("Duyệt sự kiện", "students_events"), rx.fragment()),
                    spacing="2",
                    width="100%",
                    align="stretch",
                    padding_bottom="4px",
                ),
            ),
            rx.fragment(),
        ),
        width="100%",
        align="stretch",
        spacing="2",
    )


def sidebar_nav() -> rx.Component:
    return rx.vstack(
        rx.text("Menu", font_size="11px", font_weight="700", color=MUTED, letter_spacing="0.06em", text_transform="uppercase", padding="4px 14px 8px"),
        sidebar_nav_item(ConductState.main_info_sidebar_label, "student_info"),
        rx.cond(ConductState.show_role_management_tab, sidebar_nav_item("Quản lý tài khoản", "role_management"), rx.fragment()),
        rx.cond(
            ConductState.current_user_role == "admin",
            sidebar_nav_item("Mốc thời gian đánh giá", "admin_conduct_timeline"),
            rx.fragment(),
        ),
        rx.cond(ConductState.show_student_directory_tab, sidebar_students_group(), rx.fragment()),
        rx.cond(
            ConductState.show_declaration_tabs,
            rx.vstack(
                sidebar_nav_item("Khai báo minh chứng", "evidence"),
                sidebar_nav_item("Sự kiện đã tham gia", "events"),
                spacing="2",
                width="100%",
                align="stretch",
            ),
            rx.fragment(),
        ),
        rx.cond(ConductState.current_user_role == "admin", sidebar_nav_item("Tạo sự kiện", "admin_events"), rx.fragment()),
        rx.cond(ConductState.show_self_score_tab, sidebar_nav_item("Phiếu điểm rèn luyện", "score"), rx.fragment()),
        width="100%",
        align="stretch",
        spacing="2",
        padding="8px 10px 16px",
    )


def sidebar() -> rx.Component:
    return rx.box(
        sidebar_nav(),
        width="272px",
        height="100%",
        min_height="0",
        background="white",
        border_right=f"1px solid {BORDER}",
        box_shadow="2px 0 5px rgba(0, 0, 0, 0.02)",
        flex_shrink="0",
        display="flex",
        flex_direction="column",
        overflow_y="auto",
    )


def _header_user_block() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(ConductState.current_user_initial, color="white", font_weight="700", font_size="18px"),
            width="44px",
            height="44px",
            background="#c4c4c4",
            border_radius="999px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.vstack(
            rx.text(ConductState.current_user_name, font_size="14px", color=TEXT, font_weight="600"),
            rx.cond(
                ConductState.current_user_student_code != "",
                rx.text(ConductState.current_user_student_code, font_size="12px", color=MUTED),
                rx.fragment(),
            ),
            spacing="0",
            align="start",
        ),
        badge(ConductState.current_user_role_label, "#111827"),
        action_button("Đăng xuất", ConductState.logout, background="white", color=TEXT, border=f"1px solid {BORDER}"),
        align="center",
        spacing="3",
        flex_wrap="wrap",
    )


def full_header_bar() -> rx.Component:
    return rx.hstack(
        logo_block(),
        rx.box(flex="1", min_width="16px"),
        _header_user_block(),
        width="100%",
        padding="10px 20px",
        background="white",
        border_bottom=f"1px solid {BORDER}",
        flex_shrink="0",
        align="center",
        spacing="3",
    )
