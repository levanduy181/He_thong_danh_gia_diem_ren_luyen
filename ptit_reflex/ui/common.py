from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, SURFACE, TEXT


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


PTIT_LOGO_URL = "https://slink.ptit.edu.vn/logo.png"


def logo_block() -> rx.Component:
    return rx.hstack(
        rx.image(src=PTIT_LOGO_URL, width="58px", height="58px", object_fit="contain", alt="PTIT"),
        rx.vstack(
            rx.text("Hệ thống đánh giá", font_size="14px", font_weight="700", color=TEXT),
            rx.text("điểm rèn luyện", font_size="22px", font_weight="800", color=TEXT, line_height="1.2"),
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
    return         rx.hstack(
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


def profile_item(label: str, value) -> rx.Component:
    return rx.vstack(
        rx.text(label, font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
        rx.text(value, font_size="15px", color=TEXT, font_weight="600", line_height="1.5"),
        spacing="1",
        align="start",
        min_width="180px",
        width="100%",
    )


def profile_edit_field(label: str, field) -> rx.Component:
    return rx.vstack(
        rx.text(label, font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
        field,
        spacing="2",
        align="stretch",
        width="100%",
    )


def _admin_info_card() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin quản trị viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.current_user_name, font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                badge(ConductState.current_user_role_label, "#111827"),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.grid(
                profile_item("Họ tên", ConductState.current_user_name),
                profile_item("Email", ConductState.current_user_email),
                profile_item("Đơn vị", ConductState.current_user_faculty),
                profile_item("Vai trò", ConductState.current_user_role_label),
                columns="2",
                spacing="5",
                width="100%",
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def _advisor_info_card() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin giảng viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.current_user_name, font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                badge(ConductState.current_user_role_label, "#111827"),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.grid(
                profile_item("Họ tên", ConductState.current_user_name),
                profile_item("Email", ConductState.current_user_email),
                profile_item("Đơn vị", ConductState.current_user_faculty),
                profile_item("Lớp phụ trách", ConductState.current_user_class_name),
                columns="2",
                spacing="5",
                width="100%",
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def _student_profile_card() -> rx.Component:
    action_area = rx.cond(
        ConductState.can_edit_own_profile,
        rx.cond(
            ConductState.profile_editing,
            rx.hstack(
                action_button(
                    "Hủy",
                    ConductState.cancel_profile_edit,
                    background="white",
                    color=TEXT,
                    border=f"1px solid {BORDER}",
                ),
                action_button("Lưu thông tin", ConductState.save_profile),
                spacing="2",
                align="center",
                flex_wrap="wrap",
            ),
            action_button(
                "Sửa thông tin",
                ConductState.start_profile_edit,
                background="white",
                color=TEXT,
                border=f"1px solid {BORDER}",
            ),
        ),
        rx.fragment(),
    )
    advisor_gpa_area = rx.cond(
        ConductState.can_edit_student_gpa,
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text("GPA học kỳ", font_size="14px", font_weight="800", color=TEXT),
                        rx.text(
                            "Cố vấn nhập GPA tại đây để hệ thống tự tính tiêu chí kết quả học tập trong phiếu rèn luyện.",
                            font_size="12px",
                            color=MUTED,
                            line_height="1.6",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    _review_semester_select(),
                    width="100%",
                    justify="between",
                    align="start",
                    flex_wrap="wrap",
                    spacing="3",
                ),
                rx.hstack(
                    rx.box(
                        form_input(
                            ConductState.advisor_gpa_input,
                            "Ví dụ: 3.25",
                            ConductState.set_advisor_gpa_input,
                            input_type="number",
                        ),
                        width="240px",
                        max_width="100%",
                    ),
                    action_button("Lưu GPA", ConductState.save_advisor_gpa),
                    rx.text("Thang 4.0", font_size="12px", color=MUTED),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap",
                ),
                width="100%",
                spacing="3",
                align="stretch",
            ),
            width="100%",
            padding="16px",
            background="#fffbeb",
            border="1px solid #fde68a",
            border_radius="12px",
        ),
        rx.fragment(),
    )
    display_content = rx.vstack(
        rx.grid(
            profile_item("Mã sinh viên", ConductState.student_profile["student_code"]),
            profile_item("Họ tên", ConductState.student_profile["full_name"]),
            profile_item("Lớp", ConductState.student_profile["class_name"]),
            profile_item("Khoa", ConductState.student_profile["faculty"]),
            profile_item("Ngành", ConductState.student_profile["major"]),
            profile_item("Thông tin giảng viên", ConductState.student_profile["advisor_name"]),
            profile_item("Ban cán sự", ConductState.student_profile["class_monitor_name"]),
            profile_item("Email", ConductState.student_profile["email"]),
            profile_item("Số điện thoại", ConductState.student_profile["phone"]),
            profile_item("Ngày sinh", ConductState.student_profile["birth_date"]),
            profile_item("Giới tính", ConductState.student_profile["gender"]),
            profile_item("Trạng thái", ConductState.student_profile["status"]),
            columns="3",
            spacing="5",
            width="100%",
        ),
        rx.vstack(
            rx.text("Địa chỉ", font_size="12px", color=MUTED, font_weight="700", text_transform="uppercase"),
            rx.box(
                rx.text(ConductState.student_profile["address"], font_size="14px", color="#374151", line_height="1.7"),
                width="100%",
                padding="14px 16px",
                background=SURFACE,
                border=f"1px solid {BORDER}",
                border_radius="10px",
            ),
            spacing="2",
            align="stretch",
            width="100%",
        ),
        advisor_gpa_area,
        spacing="4",
        align="stretch",
        width="100%",
    )
    edit_content = rx.vstack(
        rx.grid(
            profile_edit_field(
                "Họ tên",
                form_input(
                    ConductState.profile_edit_full_name,
                    "Nhập họ tên",
                    ConductState.set_profile_field("profile_edit_full_name"),
                ),
            ),
            profile_edit_field(
                "Email",
                form_input(
                    ConductState.profile_edit_email,
                    "Nhập email",
                    ConductState.set_profile_field("profile_edit_email"),
                    input_type="email",
                ),
            ),
            profile_edit_field(
                "Số điện thoại",
                form_input(
                    ConductState.profile_edit_phone,
                    "Nhập số điện thoại",
                    ConductState.set_profile_field("profile_edit_phone"),
                ),
            ),
            profile_edit_field(
                "Ngày sinh",
                form_input(
                    ConductState.profile_edit_birth_date,
                    "Chọn ngày sinh",
                    ConductState.set_profile_field("profile_edit_birth_date"),
                    input_type="date",
                ),
            ),
            profile_edit_field(
                "Giới tính",
                rx.select(
                    ConductState.register_gender_options,
                    value=ConductState.profile_edit_gender,
                    on_change=ConductState.set_profile_field("profile_edit_gender"),
                    width="100%",
                    height="48px",
                    border=f"1px solid {BORDER}",
                    border_radius="8px",
                    background="white",
                    color=TEXT,
                ),
            ),
            profile_item("Mã sinh viên", ConductState.student_profile["student_code"]),
            profile_item("Lớp", ConductState.student_profile["class_name"]),
            profile_item("Khoa", ConductState.student_profile["faculty"]),
            profile_item("Ngành", ConductState.student_profile["major"]),
            profile_item("Thông tin giảng viên", ConductState.student_profile["advisor_name"]),
            profile_item("Ban cán sự", ConductState.student_profile["class_monitor_name"]),
            profile_item("Trạng thái", ConductState.student_profile["status"]),
            columns="3",
            spacing="5",
            width="100%",
        ),
        profile_edit_field(
            "Địa chỉ",
            form_text_area(
                ConductState.profile_edit_address,
                "Nhập địa chỉ hiện tại",
                ConductState.set_profile_field("profile_edit_address"),
            ),
        ),
        spacing="4",
        align="stretch",
        width="100%",
    )
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Thông tin sinh viên", font_size="18px", font_weight="800", color=TEXT),
                    rx.text(ConductState.student_profile["full_name"], font_size="14px", color=MUTED),
                    spacing="0",
                    align="start",
                ),
                rx.hstack(
                    badge(ConductState.student_profile["class_name"], "#111827"),
                    rx.box(
                        rx.hstack(rx.text("GPA", font_size="12px", font_weight="700", color="#1d4ed8"), rx.text(ConductState.student_profile["gpa"], font_size="12px", font_weight="700", color="#1d4ed8"), spacing="1", align="center"),
                        background="#eff6ff",
                        border_radius="999px",
                        padding="6px 12px",
                    ),
                    action_area,
                    spacing="2",
                    align="center",
                    flex_wrap="wrap",
                ),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
            ),
            rx.cond(
                ConductState.profile_editing,
                rx.cond(ConductState.can_edit_own_profile, edit_content, display_content),
                display_content,
            ),
            spacing="4",
            align="stretch",
            width="100%",
        ),
        width="100%",
        padding="20px",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="12px",
    )


def student_info_card() -> rx.Component:
    return rx.cond(
        ConductState.active_tab == "student_detail",
        _student_profile_card(),
        rx.cond(
            ConductState.current_user_role == "admin",
            _admin_info_card(),
            rx.cond(ConductState.current_user_role == "advisor", _advisor_info_card(), _student_profile_card()),
        ),
    )


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
                            "Nhập tài khoản của bạn; hệ thống nhận diện vai trò theo dữ liệu tài khoản.",
                            "Tài khoản mới mặc định có quyền Sinh viên. Admin có thể cấp mọi quyền; cố vấn chỉ cấp Ban cán sự cho sinh viên.",
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
                            "Ví dụ: D23CQAT01",
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
                rx.vstack(
                    rx.cond(
                        ConductState.auth_mode == "login",
                        rx.box(
                            rx.vstack(
                                rx.text("Tài khoản mặc định", font_size="13px", color=TEXT, font_weight="700"),
                                rx.text("Admin: admin / admin123", font_size="12px", color=MUTED),
                                rx.text("Cố vấn D23CQAT01: CVHT001 / CVHT001", font_size="12px", color=MUTED),
                                rx.text("Cố vấn D23CQAT02: CVHT002 / CVHT002", font_size="12px", color=MUTED),
                                rx.text("Cố vấn D23CQCN01: CVHT003 / CVHT003", font_size="12px", color=MUTED),
                                rx.text("Cố vấn D23CQCN02: CVHT004 / CVHT004", font_size="12px", color=MUTED),
                                rx.text("Sinh viên mẫu: B23DCAT001 / B23DCAT001", font_size="12px", color=MUTED),
                                spacing="1",
                                align="start",
                            ),
                            width="100%",
                            padding="14px 16px",
                            border=f"1px solid {BORDER}",
                            border_radius="10px",
                            background=SURFACE,
                        ),
                        rx.fragment(),
                    ),
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
