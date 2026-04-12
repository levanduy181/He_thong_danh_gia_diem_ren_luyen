from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState
from ptit_reflex.ui import (
    advisor_gpa_page,
    event_approval_page,
    evidence_review_list_page,
    events_review_list_page,
    event_detail_modal,
    events_page,
    evidence_detail_modal,
    evidence_modal,
    evidence_page,
    flash_banner,
    full_header_bar,
    login_page,
    role_management_page,
    score_review_list_page,
    score_page,
    sidebar,
    student_info_card,
    students_list_page,
)
from ptit_reflex.ui.admin_conduct_timeline import admin_conduct_timeline_page
from ptit_reflex.ui.admin_events import admin_events_page
from ptit_reflex.ui.styles import MUTED, SURFACE


def main_tab_body() -> rx.Component:
    return rx.cond(
        ConductState.active_tab == "student_info",
        student_info_card(),
        rx.cond(
            ConductState.active_tab == "student_detail",
            student_info_card(),
            rx.cond(
                ConductState.active_tab == "evidence",
                evidence_page(),
                rx.cond(
                    ConductState.active_tab == "role_management",
                    role_management_page(),
                    rx.cond(
                        ConductState.active_tab == "admin_conduct_timeline",
                        admin_conduct_timeline_page(),
                        rx.cond(
                            ConductState.active_tab == "events",
                            events_page(),
                            rx.cond(
                                ConductState.active_tab == "admin_events",
                                admin_events_page(),
                                rx.cond(
                                    ConductState.active_tab == "students",
                                    students_list_page(),
                                    rx.cond(
                                        ConductState.active_tab == "students_score_list",
                                        score_review_list_page(),
                                        rx.cond(
                                            ConductState.active_tab == "students_evidence_list",
                                            evidence_review_list_page(),
                                            rx.cond(
                                                ConductState.active_tab == "students_events_list",
                                                events_review_list_page(),
                                                rx.cond(
                                                    ConductState.active_tab == "students_events",
                                                    event_approval_page(),
                                                    rx.cond(
                                                            ConductState.active_tab == "students_evidence",
                                                            evidence_page(),
                                                            rx.cond(
                                                                ConductState.active_tab == "students_gpa",
                                                                advisor_gpa_page(),
                                                                rx.cond(ConductState.active_tab == "students_score", score_page(), score_page()),
                                                            ),
                                                        ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


def scrollable_workspace() -> rx.Component:
    return rx.vstack(
        flash_banner(),
        main_tab_body(),
        width="100%",
        align="stretch",
        spacing="4",
        min_width="0",
    )


def loading_screen() -> rx.Component:
    return rx.center(
        rx.text("Đang tải dữ liệu...", font_size="16px", color=MUTED, font_weight="500"),
        min_height="50vh",
        width="100%",
    )


def app_view() -> rx.Component:
    return rx.cond(
        ConductState.is_authenticated,
        rx.box(
            rx.vstack(
                full_header_bar(),
                rx.hstack(
                    sidebar(),
                    rx.box(
                        rx.cond(ConductState.loading, loading_screen(), scrollable_workspace()),
                        width="100%",
                        flex="1",
                        min_height="0",
                        overflow_y="auto",
                        padding="24px",
                        background=SURFACE,
                        overflow_x="hidden",
                        min_width="0",
                    ),
                    width="100%",
                    flex="1",
                    min_height="0",
                    align="stretch",
                    spacing="0",
                    min_width="0",
                ),
                width="100%",
                height="100vh",
                max_height="100vh",
                align="stretch",
                spacing="0",
                background=SURFACE,
                min_width="0",
                overflow="hidden",
            ),
            evidence_modal(),
            evidence_detail_modal(),
            event_detail_modal(),
            width="100%",
            height="100vh",
            max_height="100vh",
            overflow="hidden",
            overflow_x="hidden",
        ),
        login_page(),
    )
