from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.navigation import logo_block
from ptit_reflex.ui.primitives import action_button, flash_banner, form_input, form_label
from ptit_reflex.ui.styles import BORDER, TEXT


def login_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                logo_block(),
                rx.vstack(
                    rx.text(
                        "Đăng nhập hệ thống",
                        font_size="28px",
                        font_weight="800",
                        color=TEXT,
                    ),
                    spacing="1",
                    align="center",
                ),
                flash_banner(),
                rx.vstack(
                    form_label("Tên đăng nhập", required=True),
                    form_input(ConductState.login_username, "Tên đăng nhập", ConductState.set_login_username),
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
