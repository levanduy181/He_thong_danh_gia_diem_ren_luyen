from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, badge
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, SURFACE, TEXT


GRID_TEMPLATE = "minmax(280px, 1.8fr) minmax(120px, 0.7fr) minmax(170px, 1fr) minmax(220px, 1.2fr) 150px"
ADMIN_ROLE_OPTIONS = ["Sinh viên", "Ban cán sự", "Cố vấn học tập", "Admin"]
ADVISOR_ROLE_OPTIONS = ["Sinh viên", "Ban cán sự"]


def role_badge(row: dict) -> rx.Component:
    background = rx.cond(
        row["role"] == "admin",
        "#111827",
        rx.cond(
            row["role"] == "advisor",
            "#1d4ed8",
            rx.cond(row["role"] == "class_monitor", "#b45309", "#047857"),
        ),
    )
    return badge(row["role_label"], background)


def class_filter_button(class_name) -> rx.Component:
    active = ConductState.selected_role_management_class == class_name
    return rx.button(
        class_name,
        on_click=ConductState.select_role_management_class(class_name),
        background=rx.cond(active, PRIMARY, "white"),
        color=rx.cond(active, "white", TEXT),
        border=rx.cond(active, "none", f"1px solid {BORDER}"),
        border_radius="12px",
        padding="0 18px",
        height="54px",
        width="100%",
        font_size="15px",
        font_weight=rx.cond(active, "700", "600"),
        cursor="pointer",
        box_shadow="none",
        justify_content="flex-start",
    )


def role_select_cell(row: dict) -> rx.Component:
    options = rx.cond(
        ConductState.current_user_role == "admin",
        ADMIN_ROLE_OPTIONS,
        ADVISOR_ROLE_OPTIONS,
    )
    return rx.select(
        options,
        value=row["role_label"],
        on_change=ConductState.assign_role_by_label(row["id"]),
        disabled=row["role_select_disabled"],
        width="100%",
        height="40px",
        border=f"1px solid {BORDER}",
        border_radius="8px",
        background=rx.cond(row["role_select_disabled"], SURFACE, "white"),
        color=TEXT,
        font_size="14px",
        key=row["id"],
    )


def delete_cell(row: dict) -> rx.Component:
    return rx.cond(
        row["can_delete_account"],
        action_button(
            "Xóa tài khoản",
            ConductState.delete_account(row["id"]),
            background="#fef2f2",
            color="#b91c1c",
            border="1px solid #fca5a5",
            height="36px",
            padding="0 12px",
        ),
        rx.text("—", font_size="14px", color=MUTED, text_align="center", width="100%"),
    )


def management_header_cell(label: str, align: str = "left") -> rx.Component:
    return rx.box(
        rx.text(label, font_size="12px", font_weight="800", color=MUTED, text_transform="uppercase", text_align=align),
        width="100%",
        padding="12px 18px",
        display="flex",
        align_items="center",
        justify_content="center" if align == "center" else "flex-start",
    )


def management_row(row: dict) -> rx.Component:
    return rx.grid(
        rx.box(
            rx.vstack(
                rx.text(row["full_name"], font_size="15px", font_weight="800", color=TEXT, line_height="1.4"),
                rx.text(row["username"], font_size="13px", color=MUTED),
                rx.cond(
                    row["is_self"],
                    rx.text("Tài khoản hiện tại", font_size="12px", color="#92400e", font_weight="700"),
                    rx.fragment(),
                ),
                spacing="1",
                align="start",
                width="100%",
                min_width="0",
            ),
            width="100%",
            padding="12px 18px",
        ),
        rx.box(
            rx.text(
                rx.cond(row["student_code"] != "", row["student_code"], "—"),
                font_size="14px",
                color=TEXT,
                font_weight="600",
                text_align="center",
            ),
            width="100%",
            display="flex",
            align_items="center",
            justify_content="center",
            padding="12px 8px",
        ),
        rx.box(
            role_badge(row),
            width="100%",
            display="flex",
            align_items="center",
            justify_content="center",
            padding="12px 8px",
        ),
        rx.box(role_select_cell(row), width="100%", padding="10px 12px"),
        rx.box(delete_cell(row), width="100%", padding="10px 12px"),
        grid_template_columns=GRID_TEMPLATE,
        width="100%",
        align_items="center",
        border_top=f"1px solid {BORDER}",
        background="white",
    )


def role_management_table() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.grid(
                management_header_cell("Tên"),
                management_header_cell("Mã", "center"),
                management_header_cell("Role", "center"),
                management_header_cell("Phân quyền", "center"),
                management_header_cell("Xóa tài khoản", "center"),
                grid_template_columns=GRID_TEMPLATE,
                width="100%",
                background=SURFACE,
            ),
            rx.foreach(ConductState.filtered_role_management_rows, management_row),
            width="100%",
            spacing="0",
            align="stretch",
        ),
        width="100%",
        border=f"1px solid {BORDER}",
        border_radius="12px",
        overflow_x="auto",
        background="white",
    )


def role_management_picker_page() -> rx.Component:
    description = rx.cond(
        ConductState.current_user_role == "admin",
        "Chọn một lớp để mở danh sách tài khoản trong lớp đó. Tài khoản hệ thống được tách riêng ở góc phải.",
        "Cố vấn học tập chỉ được đổi quyền giữa Sinh viên và Ban cán sự trong lớp mình phụ trách.",
    )
    return rx.vstack(
        rx.hstack(
            rx.text("Quản lý tài khoản", font_size="22px", font_weight="700", color=TEXT),
            rx.cond(
                ConductState.current_user_role == "admin",
                action_button(
                    "Tài khoản hệ thống",
                    ConductState.select_role_management_class("Tài khoản hệ thống"),
                    background="white",
                    color=TEXT,
                    border=f"1px solid {BORDER}",
                    height="42px",
                ),
                rx.fragment(),
            ),
            width="100%",
            justify="between",
            align="center",
            flex_wrap="wrap",
            spacing="3",
        ),
        rx.text(description, font_size="14px", color=MUTED, line_height="1.7"),
        rx.box(
            rx.vstack(
                rx.text("Danh sách lớp", font_size="13px", font_weight="800", color=MUTED, text_transform="uppercase"),
                rx.foreach(ConductState.role_management_class_groups, class_filter_button),
                spacing="3",
                width="100%",
                align="stretch",
            ),
            width="100%",
            padding="18px",
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def role_management_detail_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text("Đang hiển thị:", font_size="14px", color=MUTED, font_weight="600"),
                badge(ConductState.selected_role_management_class, "#111827"),
                spacing="2",
                align="center",
                flex_wrap="wrap",
            ),
            action_button(
                "Quay lại danh sách lớp",
                ConductState.select_role_management_class(""),
                background="white",
                color=TEXT,
                border=f"1px solid {BORDER}",
                height="38px",
            ),
            width="100%",
            justify="between",
            align="center",
            flex_wrap="wrap",
            spacing="3",
        ),
        rx.cond(
            ConductState.has_filtered_role_management_rows,
            role_management_table(),
            rx.box(
                rx.text("Không có tài khoản nào trong nhóm đang chọn.", font_size="14px", color=MUTED),
                width="100%",
                padding="20px",
                background="white",
                border=f"1px solid {BORDER}",
                border_radius="12px",
            ),
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def role_management_page() -> rx.Component:
    return rx.cond(
        ConductState.role_management_has_selection,
        role_management_detail_page(),
        role_management_picker_page(),
    )
