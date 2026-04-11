from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, badge
from ptit_reflex.ui.styles import BORDER, MUTED, TEXT


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


def meta_chip(label: str, value) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(label, font_size="12px", font_weight="700", color=MUTED),
            rx.text(value, font_size="12px", font_weight="600", color=TEXT),
            spacing="1",
            align="center",
        ),
        padding="6px 10px",
        border=f"1px solid {BORDER}",
        border_radius="999px",
        background="white",
    )


def admin_role_actions(row: dict) -> rx.Component:
    return rx.hstack(
        rx.cond(
            row["can_set_student"],
            rx.cond(
                row["role"] != "student",
                action_button(
                    "Sinh viên",
                    ConductState.assign_role(row["id"], "student"),
                    background="#ecfdf5",
                    color="#166534",
                    border="1px solid #86efac",
                    height="34px",
                    padding="0 12px",
                ),
                rx.fragment(),
            ),
            rx.fragment(),
        ),
        rx.cond(
            row["can_set_class_monitor"],
            rx.cond(
                row["role"] != "class_monitor",
                action_button(
                    "Ban cán sự",
                    ConductState.assign_role(row["id"], "class_monitor"),
                    background="#fff7ed",
                    color="#9a3412",
                    border="1px solid #fdba74",
                    height="34px",
                    padding="0 12px",
                ),
                rx.fragment(),
            ),
            rx.fragment(),
        ),
        rx.cond(
            row["can_set_advisor"],
            rx.cond(
                row["role"] != "advisor",
                action_button(
                    "Cố vấn học tập",
                    ConductState.assign_role(row["id"], "advisor"),
                    background="#eff6ff",
                    color="#1d4ed8",
                    border="1px solid #93c5fd",
                    height="34px",
                    padding="0 12px",
                ),
                rx.fragment(),
            ),
            rx.fragment(),
        ),
        rx.cond(
            row["can_set_admin"],
            rx.cond(
                row["role"] != "admin",
                action_button(
                    "Admin",
                    ConductState.assign_role(row["id"], "admin"),
                    background="#111827",
                    color="white",
                    height="34px",
                    padding="0 12px",
                ),
                rx.fragment(),
            ),
            rx.fragment(),
        ),
        justify="end",
        align="center",
        spacing="2",
        flex_wrap="wrap",
        width="100%",
    )


def advisor_role_actions(row: dict) -> rx.Component:
    return rx.hstack(
        rx.cond(
            row["can_set_class_monitor"],
            action_button(
                "Cấp ban cán sự",
                ConductState.assign_role(row["id"], "class_monitor"),
                background="#fff7ed",
                color="#9a3412",
                border="1px solid #fdba74",
                height="34px",
                padding="0 12px",
            ),
            rx.fragment(),
        ),
        rx.cond(
            row["can_set_student"],
            action_button(
                "Thu về sinh viên",
                ConductState.assign_role(row["id"], "student"),
                background="#ecfdf5",
                color="#166534",
                border="1px solid #86efac",
                height="34px",
                padding="0 12px",
            ),
            rx.fragment(),
        ),
        justify="end",
        align="center",
        spacing="2",
        flex_wrap="wrap",
        width="100%",
    )


def role_actions(row: dict) -> rx.Component:
    return rx.vstack(
        rx.cond(
            row["is_self"],
            rx.text("Tài khoản hiện tại không tự đổi quyền.", font_size="13px", color=MUTED, text_align="right"),
            rx.cond(
                ConductState.current_user_role == "admin",
                admin_role_actions(row),
                advisor_role_actions(row),
            ),
        ),
        width="100%",
        align="end",
        spacing="2",
    )


def role_management_row(row: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.text(row["full_name"], font_size="17px", font_weight="800", color=TEXT),
                    role_badge(row),
                    rx.cond(row["is_self"], badge("Tài khoản hiện tại", "#e5e7eb", color=TEXT), rx.fragment()),
                    spacing="2",
                    align="center",
                    flex_wrap="wrap",
                ),
                rx.hstack(
                    meta_chip("Tài khoản", row["username"]),
                    meta_chip("Mã", rx.cond(row["student_code"] != "", row["student_code"], "Chưa có")),
                    meta_chip("Lớp", rx.cond(row["class_name"] != "", row["class_name"], "Chưa gán")),
                    spacing="2",
                    align="center",
                    flex_wrap="wrap",
                    width="100%",
                ),
                rx.cond(
                    row["email"] != "",
                    rx.text(row["email"], font_size="13px", color=MUTED),
                    rx.fragment(),
                ),
                spacing="3",
                align="start",
                width="100%",
                min_width="0",
            ),
            rx.box(role_actions(row), width="100%", max_width="340px", flex_shrink="0"),
            justify="between",
            align="start",
            width="100%",
            spacing="4",
            flex_wrap="wrap",
        ),
        width="100%",
        padding="18px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def role_management_page() -> rx.Component:
    title = rx.cond(
        ConductState.current_user_role == "admin",
        "Phân quyền tài khoản",
        "Cấp quyền ban cán sự",
    )
    description = rx.cond(
        ConductState.current_user_role == "admin",
        "Admin có thể đổi bất kỳ tài khoản nào sang Sinh viên, Ban cán sự, Cố vấn học tập hoặc Admin.",
        "Cố vấn chỉ được đổi giữa Sinh viên và Ban cán sự trong lớp mình phụ trách.",
    )
    return rx.vstack(
        rx.text(title, font_size="22px", font_weight="700", color=TEXT),
        rx.text(description, font_size="14px", color=MUTED),
        rx.box(
            rx.text(
                "Tài khoản mới đăng ký mặc định có quyền Sinh viên. Dùng các nút bên phải để đổi quyền ngay trên từng tài khoản.",
                font_size="14px",
                color="#92400e",
                line_height="1.6",
            ),
            width="100%",
            padding="14px 16px",
            background="#fffbeb",
            border="1px solid #fde68a",
            border_radius="10px",
        ),
        rx.vstack(
            rx.foreach(ConductState.role_management_rows, role_management_row),
            width="100%",
            spacing="3",
            align="stretch",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )
