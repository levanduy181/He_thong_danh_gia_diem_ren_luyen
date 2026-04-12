from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.styles import BORDER, PRIMARY, TEXT


def action_button(
    label: str,
    on_click=None,
    background: str = PRIMARY,
    color: str = "white",
    border: str = "none",
    height: str = "38px",
    padding: str = "0 16px",
    disabled=False,
) -> rx.Component:
    return rx.button(
        label,
        on_click=on_click,
        disabled=disabled,
        background=background,
        color=color,
        border=border,
        border_radius="8px",
        height=height,
        padding=padding,
        font_weight="600",
        font_size="14px",
        cursor=rx.cond(disabled, "not-allowed", "pointer"),
        opacity=rx.cond(disabled, 0.55, 1),
        box_shadow="none",
    )


def badge(text, background, color="white") -> rx.Component:
    return rx.box(
        rx.text(text, font_size="12px", font_weight="700", color=color),
        padding="6px 12px",
        border_radius="999px",
        background=background,
    )


def checkbox_row(label: str, checked, on_click) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.cond(
                checked,
                rx.text("✓", color="white", font_size="12px", font_weight="700"),
                rx.text(""),
            ),
            width="20px",
            height="20px",
            border_radius="6px",
            background=rx.cond(checked, PRIMARY, "white"),
            border=f"1px solid {PRIMARY}",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.text(label, font_size="14px", color=TEXT, font_weight="500"),
        width="100%",
        align="center",
        spacing="3",
        cursor="pointer",
        on_click=on_click,
    )


def flash_banner() -> rx.Component:
    background = rx.cond(
        ConductState.flash_kind == "error",
        "#fee2e2",
        rx.cond(ConductState.flash_kind == "success", "#dcfce7", "#e0f2fe"),
    )
    color = rx.cond(
        ConductState.flash_kind == "error",
        "#b91c1c",
        rx.cond(ConductState.flash_kind == "success", "#166534", "#075985"),
    )
    return rx.cond(
        ConductState.flash_message != "",
        rx.hstack(
            rx.text(ConductState.flash_message, font_size="14px", font_weight="600", color=color),
            rx.text("Đóng", color=color, font_size="13px", cursor="pointer", on_click=ConductState.clear_flash),
            justify="between",
            align="center",
            width="100%",
            padding="12px 16px",
            background=background,
            border=f"1px solid {BORDER}",
            border_radius="10px",
            on_mount=ConductState.schedule_flash_auto_clear,
            key=ConductState.flash_token,
        ),
        rx.fragment(),
    )


def modal_shell(title, content, footer, on_close, max_width="760px") -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.text(title, font_size="18px", font_weight="700", color=TEXT),
                rx.text("✕", font_size="22px", color="#9ca3af", cursor="pointer", on_click=on_close),
                justify="between",
                align="center",
                width="100%",
                padding="20px 24px",
                border_bottom=f"1px solid {BORDER}",
            ),
            rx.box(content, padding="24px", flex="1", min_height="0", overflow_y="auto"),
            rx.box(footer, padding="0 24px 24px"),
            width="100%",
            max_width=max_width,
            max_height="calc(100vh - 48px)",
            background="white",
            border_radius="14px",
            box_shadow="0 24px 60px rgba(15, 23, 42, 0.18)",
            display="flex",
            flex_direction="column",
        ),
        position="fixed",
        inset="0",
        background="rgba(15, 23, 42, 0.45)",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="24px",
        z_index="100",
    )


def form_label(text: str, required: bool = False) -> rx.Component:
    return rx.text(
        ("* " if required else "") + text,
        font_size="15px",
        font_weight="500",
        color=TEXT,
    )


def form_input(value, placeholder: str, on_change, input_type: str = "text") -> rx.Component:
    return rx.input(
        value=value,
        placeholder=placeholder,
        on_change=on_change,
        type=input_type,
        width="100%",
        height="48px",
        border=f"1px solid {BORDER}",
        border_radius="8px",
        background="white",
    )


def form_text_area(value, placeholder: str, on_change) -> rx.Component:
    return rx.text_area(
        value=value,
        placeholder=placeholder,
        on_change=on_change,
        width="100%",
        min_height="100px",
        border=f"1px solid {BORDER}",
        border_radius="8px",
        background="white",
    )
