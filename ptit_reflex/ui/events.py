from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui.common import action_button, badge, modal_shell
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, SURFACE, TEXT


def event_segment(label: str, key: str) -> rx.Component:
    active = ConductState.event_tab == key
    return rx.box(
        rx.text(label, color=rx.cond(active, TEXT, MUTED), font_weight=rx.cond(active, "700", "500"), font_size="14px"),
        padding="8px 14px",
        background=rx.cond(active, "white", "transparent"),
        border_radius="6px",
        box_shadow=rx.cond(active, "0 1px 3px rgba(0, 0, 0, 0.08)", "none"),
        cursor="pointer",
        on_click=ConductState.select_event_tab(key),
    )


def joined_event_item(item: dict) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(item["date"], font_size="13px", color=MUTED, font_weight="600"),
            rx.box(rx.text(item["count"], font_size="10px", color="white", font_weight="700"), min_width="16px", height="16px", border_radius="999px", background="#ef4444", display="flex", align_items="center", justify_content="center", padding="0 4px"),
            align="center",
            spacing="3",
        ),
        rx.hstack(
            rx.text(item["time"], width="56px", text_align="right", font_size="14px", font_weight="700", color=TEXT),
            rx.box(width="4px", min_height="36px", border_radius="999px", background=item["accent"]),
            rx.text(item["title"], font_size="14px", color="#374151", flex="1"),
            align="center",
            spacing="4",
            background=SURFACE,
            border="1px solid #f1f5f9",
            border_radius="8px",
            padding="12px 14px",
            width="100%",
            cursor="pointer",
            on_click=ConductState.open_event_detail(item["id"]),
        ),
        width="100%",
        spacing="2",
        align="stretch",
    )


def registered_event_item(item: dict) -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.box(width="4px", min_height="42px", border_radius="999px", background="#53b8dc"),
            rx.vstack(
                rx.text(item["title"], font_size="15px", font_weight="600", color=TEXT),
                rx.hstack(
                    rx.text("Cộng", font_size="13px", color=MUTED),
                    rx.text(item["points"], font_size="13px", color=MUTED, font_weight="700"),
                    rx.text("điểm", font_size="13px", color=MUTED),
                    spacing="2",
                    align="center",
                ),
                rx.cond(item["status_label"] != "", rx.text(item["status_label"], font_size="12px", color=PRIMARY, font_weight="700"), rx.fragment()),
                spacing="1",
                align="start",
            ),
            align="center",
            spacing="4",
            cursor="pointer",
            on_click=ConductState.open_event_detail(item["id"]),
        ),
        rx.hstack(
            action_button("Chi tiết", ConductState.open_event_detail(item["id"]), background="white", color=TEXT, border=f"1px solid {BORDER}"),
            rx.cond(item["can_approve"], action_button("Duyệt", ConductState.approve_event(item["participation_id"]), background="#15803d"), rx.fragment()),
            badge(item["action_label"], "#f3f4f6", color=TEXT),
            spacing="3",
            align="center",
        ),
        justify="between",
        align="center",
        width="100%",
        background=SURFACE,
        border="1px solid #f1f5f9",
        border_radius="8px",
        padding="14px",
    )


def open_event_item(item: dict) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(item["title"], font_size="15px", font_weight="700", color=TEXT),
            rx.text(item["start_time"], font_size="13px", color=MUTED),
            rx.text(item["location"], font_size="13px", color=MUTED),
            spacing="1",
            align="start",
            cursor="pointer",
            on_click=ConductState.open_event_detail(item["id"]),
        ),
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.text("+", font_size="12px", font_weight="700", color="#c2410c"),
                    rx.text(item["points"], font_size="12px", font_weight="700", color="#c2410c"),
                    rx.text("điểm tối đa", font_size="12px", font_weight="700", color="#c2410c"),
                    spacing="1",
                    align="center",
                ),
                background="#fff7ed",
                border_radius="999px",
                padding="6px 12px",
            ),
            rx.cond(item["can_register"], action_button("Đăng ký", ConductState.register_event(item["id"])), badge("Chỉ sinh viên mới đăng ký", "#f3f4f6", color=TEXT)),
            spacing="3",
            align="center",
        ),
        justify="between",
        align="center",
        width="100%",
        background="white",
        border=f"1px solid {BORDER}",
        border_radius="10px",
        padding="14px",
        flex_wrap="wrap",
    )


def event_detail_modal() -> rx.Component:
    return rx.cond(
        ConductState.event_modal_open,
        modal_shell(
            "Chi tiết lịch",
            rx.vstack(
                rx.hstack(rx.text("Loại sự kiện:", color=MUTED, font_weight="700"), badge(ConductState.selected_event_type_label, "#e9d5ff", color="#6d28d9"), align="center", spacing="3"),
                rx.hstack(rx.text("Tên sự kiện:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_name, color=TEXT)),
                rx.hstack(rx.text("Thời gian bắt đầu:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_start_time, color=TEXT)),
                rx.hstack(rx.text("Thời gian kết thúc:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_end_time, color=TEXT)),
                rx.hstack(rx.text("Địa điểm:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_location, color=TEXT)),
                rx.hstack(rx.text("Tham gia sự kiện được tính điểm rèn luyện?:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_counts_to_score, color=TEXT)),
                rx.hstack(rx.text("Ghi chú:", color=MUTED, font_weight="700"), rx.text(ConductState.selected_event_note, color=TEXT)),
                spacing="4",
                width="100%",
                align="start",
            ),
            rx.hstack(action_button("Đóng", ConductState.close_event_detail, background="white", color=TEXT, border=f"1px solid {BORDER}"), justify="center", width="100%"),
            ConductState.close_event_detail,
            max_width="760px",
        ),
        rx.fragment(),
    )


def events_page() -> rx.Component:
    return rx.vstack(
        rx.text("Sự kiện tham gia", font_size="22px", font_weight="700", color=TEXT),
        rx.box(
            rx.vstack(
                rx.cond(
                    ConductState.has_open_events,
                    rx.vstack(
                        rx.text("Đăng ký sự kiện", font_size="18px", font_weight="800", color=TEXT),
                        rx.foreach(ConductState.open_events, open_event_item),
                        width="100%",
                        align="stretch",
                        spacing="4",
                    ),
                    rx.fragment(),
                ),
                rx.box(event_segment("Đã tham gia", "joined"), event_segment("Đã đăng ký", "registered"), display="inline-flex", background="#f3f4f6", border=f"1px solid {BORDER}", border_radius="8px", padding="4px", gap="4px"),
                rx.cond(
                    ConductState.event_tab == "joined",
                    rx.cond(
                        ConductState.joined_events != [],
                        rx.vstack(rx.foreach(ConductState.joined_events, joined_event_item), width="100%", align="stretch", spacing="5"),
                        rx.center(rx.text("Chưa có sự kiện nào được duyệt là đã tham gia.", color="#9ca3af", font_size="15px", font_weight="500"), min_height="180px"),
                    ),
                    rx.cond(
                        ConductState.has_registered_events,
                        rx.vstack(rx.foreach(ConductState.registered_events, registered_event_item), width="100%", align="stretch", spacing="4"),
                        rx.center(rx.text("Chưa có đăng ký sự kiện nào.", color="#9ca3af", font_size="15px", font_weight="500"), min_height="180px"),
                    ),
                ),
                width="100%",
                align="stretch",
                spacing="6",
            ),
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            width="100%",
            padding="24px",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )


def event_approval_page() -> rx.Component:
    return rx.vstack(
        rx.text("Duyệt sự kiện đã đăng ký", font_size="22px", font_weight="700", color=TEXT),
        rx.text(
            "Màn này chỉ hiển thị các sự kiện sinh viên đã đăng ký để ban cán sự duyệt, không hiển thị phần đăng ký sự kiện mới.",
            font_size="14px",
            color=MUTED,
            line_height="1.7",
        ),
        rx.box(
            rx.cond(
                ConductState.has_registered_events,
                rx.vstack(
                    rx.foreach(ConductState.registered_events, registered_event_item),
                    width="100%",
                    align="stretch",
                    spacing="4",
                ),
                rx.center(
                    rx.text("Sinh viên này chưa có đăng ký sự kiện nào.", color="#9ca3af", font_size="15px", font_weight="500"),
                    min_height="180px",
                ),
            ),
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            width="100%",
            padding="24px",
        ),
        width="100%",
        align="stretch",
        spacing="4",
    )
