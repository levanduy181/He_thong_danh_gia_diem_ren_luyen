from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.navigation import logo_block
from ptit_reflex.ui.primitives import action_button, flash_banner, form_input, form_label, form_text_area
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, SURFACE, TEXT


def login_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                logo_block(),
                rx.vstack(
                    rx.text(
                        rx.cond(ConductState.auth_mode == "login", "Đăng nhập hệ thống", "Đăng ký tài khoản"),
                        font_size="28px",
                        font_weight="800",
                        color=TEXT,
                    ),
                    rx.text(
                        rx.cond(
                            ConductState.auth_mode == "login",
                            "",
                            "",
                        ),
                        font_size="14px",
                        color=MUTED,
                        text_align="center",
                    ),
                    spacing="1",
                    align="center",
                ),
                rx.hstack(
                    action_button(
                        "Đăng nhập",
                        ConductState.show_login_form,
                        background=rx.cond(ConductState.auth_mode == "login", PRIMARY, "white"),
                        color=rx.cond(ConductState.auth_mode == "login", "white", TEXT),
                        border=rx.cond(ConductState.auth_mode == "login", "none", f"1px solid {BORDER}"),
                    ),
                    action_button(
                        "Đăng ký",
                        ConductState.show_register_form,
                        background=rx.cond(ConductState.auth_mode == "register", PRIMARY, "white"),
                        color=rx.cond(ConductState.auth_mode == "register", "white", TEXT),
                        border=rx.cond(ConductState.auth_mode == "register", "none", f"1px solid {BORDER}"),
                    ),
                    width="100%",
                    spacing="3",
                ),
                flash_banner(),
                rx.cond(
                    ConductState.auth_mode == "login",
                    rx.vstack(
                        form_label("Tên đăng nhập", required=True),
                        form_input(ConductState.login_username, "Ví dụ: admin hoặc CVHT001", ConductState.set_login_username),
                        form_label("Mật khẩu", required=True),
                        form_input(ConductState.login_password, "Nhập mật khẩu", ConductState.set_login_password, input_type="password"),
                        rx.cond(
                            ConductState.login_error != "",
                            rx.text(ConductState.login_error, color="#b91c1c", font_size="13px", font_weight="600"),
                            rx.fragment(),
                        ),
                        action_button("Đăng nhập", ConductState.login, height="44px"),
                        spacing="3",
                        align="stretch",
                        width="100%",
                    ),
                    rx.vstack(
                        form_label("Tên đăng nhập", required=True),
                        form_input(
                            ConductState.register_username,
                            "Nhập tên đăng nhập",
                            ConductState.set_register_field("register_username"),
                        ),
                        form_label("Họ tên", required=True),
                        form_input(
                            ConductState.register_full_name,
                            "Nhập họ tên",
                            ConductState.set_register_field("register_full_name"),
                        ),
                        form_label("Mã sinh viên", required=True),
                        form_input(
                            ConductState.register_student_code,
                            "Ví dụ: B23DCAT999",
                            ConductState.set_register_field("register_student_code"),
                        ),
                        form_label("Email", required=True),
                        form_input(
                            ConductState.register_email,
                            "Ví dụ: tenban@stu.ptit.edu.vn",
                            ConductState.set_register_field("register_email"),
                        ),
                        form_label("Số điện thoại", required=True),
                        form_input(
                            ConductState.register_phone,
                            "Nhập số điện thoại",
                            ConductState.set_register_field("register_phone"),
                        ),
                        form_label("Ngày sinh", required=True),
                        form_input(
                            ConductState.register_birth_date,
                            "Chọn ngày sinh",
                            ConductState.set_register_field("register_birth_date"),
                            input_type="date",
                        ),
                        form_label("Giới tính", required=True),
                        rx.select(
                            ConductState.register_gender_options,
                            value=ConductState.register_gender,
                            on_change=ConductState.set_register_field("register_gender"),
                            width="100%",
                            height="48px",
                            border=f"1px solid {BORDER}",
                            border_radius="8px",
                            background="white",
                            color=TEXT,
                        ),
                        form_label("Lớp", required=True),
                        form_input(
                            ConductState.register_class_name,
                            "Ví dụ: D23CQAT001",
                            ConductState.set_register_field("register_class_name"),
                        ),
                        form_label("Khoa", required=True),
                        rx.select(
                            ConductState.register_faculty_options,
                            value=ConductState.register_faculty,
                            on_change=ConductState.set_register_faculty,
                            width="100%",
                            height="48px",
                            border=f"1px solid {BORDER}",
                            border_radius="8px",
                            background="white",
                            color=TEXT,
                        ),
                        form_label("Ngành", required=True),
                        rx.select(
                            ConductState.register_major_options,
                            value=ConductState.register_major,
                            on_change=ConductState.set_register_field("register_major"),
                            width="100%",
                            height="48px",
                            border=f"1px solid {BORDER}",
                            border_radius="8px",
                            background="white",
                            color=TEXT,
                        ),
                        form_label("Địa chỉ", required=True),
                        form_text_area(
                            ConductState.register_address,
                            "Nhập địa chỉ hiện tại",
                            ConductState.set_register_field("register_address"),
                        ),
                        form_label("Mật khẩu", required=True),
                        form_input(
                            ConductState.register_password,
                            "Tối thiểu 6 ký tự",
                            ConductState.set_register_field("register_password"),
                            input_type="password",
                        ),
                        form_label("Xác nhận mật khẩu", required=True),
                        form_input(
                            ConductState.register_password_confirm,
                            "Nhập lại mật khẩu",
                            ConductState.set_register_field("register_password_confirm"),
                            input_type="password",
                        ),
                        action_button("Tạo tài khoản", ConductState.register_account, height="44px"),
                        spacing="3",
                        align="stretch",
                        width="100%",
                    ),
                ),
                spacing="6",
                align="center",
                width="100%",
            ),
            width="100%",
            max_width="520px",
            padding="32px",
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="18px",
            box_shadow="0 25px 60px rgba(15, 23, 42, 0.14)",
        ),
        min_height="100vh",
        width="100%",
        background="linear-gradient(180deg, #fff5f5 0%, #f8fafc 45%, #f1f5f9 100%)",
        padding="24px",
    )
