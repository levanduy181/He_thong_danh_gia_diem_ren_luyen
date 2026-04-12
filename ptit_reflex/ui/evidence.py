from __future__ import annotations

import reflex as rx

from ptit_reflex.state import ConductState, EVIDENCE_UPLOAD_ID
from ptit_reflex.ui.primitives import action_button, checkbox_row, form_input, form_label, form_text_area, modal_shell
from ptit_reflex.ui.styles import BORDER, MUTED, PRIMARY, PRIMARY_SOFT, SURFACE, TEXT


def evidence_category_item(item: dict) -> rx.Component:
    active = ConductState.selected_evidence_category == item["key"]
    return rx.box(
        rx.text(item["label"], font_size="14px", font_weight=rx.cond(active, "700", "500"), color=rx.cond(active, PRIMARY, "#374151")),
        padding="16px",
        border_bottom=f"1px solid {BORDER}",
        border_left=rx.cond(active, f"4px solid {PRIMARY}", "4px solid transparent"),
        background=rx.cond(active, PRIMARY_SOFT, "white"),
        cursor="pointer",
        on_click=ConductState.select_evidence_category_key(item["key"]),
    )


def _evidence_head_cell(content, *, border_right: bool = True) -> rx.Component:
    return rx.box(
        content,
        padding="14px 10px",
        border_right=f"1px solid {BORDER}" if border_right else "none",
        display="flex",
        align_items="center",
        justify_content="center",
        min_height="48px",
        min_width="0",
    )


def evidence_table_header() -> rx.Component:
    return rx.box(
        _evidence_head_cell(rx.text("TT", font_weight="700")),
        rx.cond(
            ConductState.show_student_code_col,
            _evidence_head_cell(rx.text("Mã SV", font_weight="700")),
            rx.fragment(),
        ),
        rx.cond(
            ConductState.show_full_name_col,
            _evidence_head_cell(rx.text("Họ tên", font_weight="700")),
            rx.fragment(),
        ),
        rx.cond(ConductState.show_class_col, _evidence_head_cell(rx.text("Lớp", font_weight="700")), rx.fragment()),
        rx.cond(ConductState.show_reporter_col, _evidence_head_cell(rx.text("Người khai báo", font_weight="700")), rx.fragment()),
        rx.cond(ConductState.show_status_col, _evidence_head_cell(rx.text("Trạng thái", font_weight="700")), rx.fragment()),
        rx.cond(
            ConductState.show_action_col,
            _evidence_head_cell(rx.text("Thao tác", font_weight="700"), border_right=False),
            rx.fragment(),
        ),
        width="100%",
        display="grid",
        grid_template_columns=ConductState.evidence_grid_columns,
        background=SURFACE,
    )


def _evidence_body_cell(content, *, border_right: bool = True) -> rx.Component:
    return rx.box(
        content,
        padding="14px 10px",
        border_right=f"1px solid {BORDER}" if border_right else "none",
        display="flex",
        align_items="center",
        justify_content="center",
        min_height="52px",
        min_width="0",
    )


def evidence_row(row: dict) -> rx.Component:
    return rx.box(
        _evidence_body_cell(rx.text(row["index"])),
        rx.cond(
            ConductState.show_student_code_col,
            _evidence_body_cell(rx.text(row["student_code"])),
            rx.fragment(),
        ),
        rx.cond(
            ConductState.show_full_name_col,
            _evidence_body_cell(rx.text(row["full_name"])),
            rx.fragment(),
        ),
        rx.cond(ConductState.show_class_col, _evidence_body_cell(rx.text(row["class_name"])), rx.fragment()),
        rx.cond(ConductState.show_reporter_col, _evidence_body_cell(rx.text(row["reporter_name"])), rx.fragment()),
        rx.cond(
            ConductState.show_status_col,
            _evidence_body_cell(rx.text(row["status_label"], color=PRIMARY, font_weight="600")),
            rx.fragment(),
        ),
        rx.cond(
            ConductState.show_action_col,
            _evidence_body_cell(
                rx.hstack(
                    action_button("Mở", ConductState.open_evidence_detail(row["id"]), background="white", color=TEXT, border=f"1px solid {BORDER}", height="32px", padding="0 12px"),
                    rx.cond(
                        ConductState.show_delete_evidence_action,
                        rx.cond(
                            row["can_delete"],
                            action_button("Xóa", ConductState.remove_evidence(row["id"]), background="#fff1f2", color=PRIMARY, border="1px solid #fecdd3", height="32px", padding="0 12px"),
                            rx.fragment(),
                        ),
                        rx.fragment(),
                    ),
                    spacing="2",
                    justify="center",
                    width="100%",
                    flex_wrap="wrap",
                ),
                border_right=False,
            ),
            rx.fragment(),
        ),
        width="100%",
        display="grid",
        grid_template_columns=ConductState.evidence_grid_columns,
        border_top=f"1px solid {BORDER}",
        background="white",
    )


def column_config_panel() -> rx.Component:
    return rx.cond(
        ConductState.column_config_open,
        rx.box(
            rx.vstack(
                rx.hstack(rx.text("Cấu hình cột", font_size="20px", font_weight="700", color=TEXT), rx.text("Khôi phục", color=PRIMARY, cursor="pointer", on_click=ConductState.reset_evidence_columns), justify="between", width="100%"),
                checkbox_row("Mã SV", ConductState.show_student_code_col, ConductState.toggle_show_student_code_col),
                checkbox_row("Họ tên", ConductState.show_full_name_col, ConductState.toggle_show_full_name_col),
                checkbox_row("Lớp", ConductState.show_class_col, ConductState.toggle_show_class_col),
                checkbox_row("Người khai báo", ConductState.show_reporter_col, ConductState.toggle_show_reporter_col),
                checkbox_row("Trạng thái", ConductState.show_status_col, ConductState.toggle_show_status_col),
                checkbox_row("Thao tác", ConductState.show_action_col, ConductState.toggle_show_action_col),
                rx.hstack(
                    action_button("Hủy", ConductState.toggle_column_config, background="white", color=TEXT, border=f"1px solid {BORDER}"),
                    action_button("Áp dụng", ConductState.toggle_column_config),
                    justify="end",
                    width="100%",
                ),
                width="100%",
                spacing="4",
                align="stretch",
            ),
            position="absolute",
            top="52px",
            right="0",
            width="320px",
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            box_shadow="0 18px 40px rgba(15, 23, 42, 0.16)",
            padding="18px",
            z_index="30",
        ),
        rx.fragment(),
    )


def evidence_file_picker() -> rx.Component:
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.text("Chọn tệp minh chứng", font_size="15px", font_weight="700", color=TEXT),
                rx.text("Bấm để chọn hoặc kéo thả 1 tệp vào đây.", font_size="13px", color=MUTED),
                rx.cond(
                    ConductState.evidence_file_name != "",
                    rx.box(
                        rx.text(ConductState.evidence_file_name, font_size="14px", font_weight="600", color=PRIMARY),
                        width="100%",
                        padding="10px 12px",
                        border=f"1px solid {BORDER}",
                        border_radius="8px",
                        background="white",
                    ),
                    rx.box(
                        rx.text("Chưa chọn tệp nào", font_size="14px", color=MUTED),
                        width="100%",
                        padding="10px 12px",
                        border=f"1px dashed {BORDER}",
                        border_radius="8px",
                        background="white",
                    ),
                ),
                spacing="2",
                align="stretch",
                width="100%",
            ),
            id=EVIDENCE_UPLOAD_ID,
            on_drop=ConductState.handle_evidence_upload,
            multiple=False,
            max_files=1,
            width="100%",
            padding="16px",
            border=f"1px dashed {PRIMARY}",
            border_radius="10px",
            background="#fff5f5",
            cursor="pointer",
        ),
        rx.cond(
            ConductState.evidence_file_name != "",
            rx.hstack(
                rx.text("Đã chọn:", font_size="13px", color=MUTED),
                rx.text(ConductState.evidence_file_name, font_size="13px", font_weight="700", color=TEXT),
                spacing="2",
                align="center",
                flex_wrap="wrap",
            ),
            rx.fragment(),
        ),
        rx.cond(
            ConductState.evidence_file_path != "",
            rx.box(
                rx.cond(
                    ConductState.evidence_file_is_image,
                    rx.image(
                        src=rx.get_upload_url(ConductState.evidence_file_path),
                        alt=ConductState.evidence_file_name,
                        width="100%",
                        max_height="280px",
                        object_fit="contain",
                        border_radius="10px",
                    ),
                    rx.link(
                        "Mở tệp đã chọn",
                        href=rx.get_upload_url(ConductState.evidence_file_path),
                        is_external=True,
                        color=PRIMARY,
                        font_weight="700",
                        text_decoration="underline",
                    ),
                ),
                width="100%",
                padding="10px",
                border=f"1px solid {BORDER}",
                border_radius="10px",
                background="white",
            ),
            rx.fragment(),
        ),
        width="100%",
        align="stretch",
        spacing="2",
    )


def evidence_form_fields() -> rx.Component:
    return rx.cond(
        ConductState.selected_evidence_category == "special_achievement",
        rx.vstack(
            form_label("Cấp đạt giải", required=True),
            rx.select(["Giải Nhất cấp Học viện", "Giải Nhì cấp Học viện", "Giải Ba cấp Học viện", "Giải khuyến khích"], value=ConductState.evidence_award_level, on_change=ConductState.set_form_value("evidence_award_level"), width="100%"),
            form_label("Nội dung hoạt động", required=True),
            form_text_area(ConductState.evidence_activity_content, "Nhập Nội dung hoạt động", ConductState.set_form_value("evidence_activity_content")),
            form_label("Ngày tham gia", required=True),
            form_input(ConductState.evidence_participation_time, "YYYY-MM-DD", ConductState.set_form_value("evidence_participation_time"), input_type="date"),
            form_label("Đường dẫn"),
            form_input(ConductState.evidence_url, "Nhập Đường dẫn", ConductState.set_form_value("evidence_url")),
            form_label("Tập tin minh chứng", required=True),
            evidence_file_picker(),
            spacing="3",
            align="stretch",
            width="100%",
        ),
        rx.cond(
            ConductState.selected_evidence_category == "positive_promotion",
            rx.vstack(
                form_label("Nội dung hoạt động", required=True),
                form_input(ConductState.evidence_activity_content, "Nhập Nội dung hoạt động", ConductState.set_form_value("evidence_activity_content")),
                form_label("Sự kiện"),
                form_input(ConductState.evidence_event_name, "Nhập Sự kiện", ConductState.set_form_value("evidence_event_name")),
                form_label("Ngày chia sẻ", required=True),
                form_input(ConductState.evidence_share_time, "YYYY-MM-DD", ConductState.set_form_value("evidence_share_time"), input_type="date"),
                form_label("Đường dẫn"),
                form_input(ConductState.evidence_url, "Nhập Đường dẫn", ConductState.set_form_value("evidence_url")),
                form_label("Tập tin minh chứng", required=True),
                evidence_file_picker(),
                spacing="3",
                align="stretch",
                width="100%",
            ),
            rx.cond(
                ConductState.selected_evidence_category == "social_work",
                rx.vstack(
                    form_label("Tham gia công tác xã hội", required=True),
                    rx.select(["Hiến máu nhân đạo", "Ủng hộ thiên tai lũ lụt", "Tình nguyện hỗ trợ cộng đồng"], value=ConductState.evidence_social_type, on_change=ConductState.set_form_value("evidence_social_type"), width="100%"),
                    form_label("Ngày tham gia", required=True),
                    form_input(ConductState.evidence_participation_time, "YYYY-MM-DD", ConductState.set_form_value("evidence_participation_time"), input_type="date"),
                    form_label("Đường dẫn"),
                    form_input(ConductState.evidence_url, "Nhập Đường dẫn", ConductState.set_form_value("evidence_url")),
                    form_label("Tập tin minh chứng", required=True),
                    evidence_file_picker(),
                    spacing="3",
                    align="stretch",
                    width="100%",
                ),
                rx.vstack(
                    form_label("Phân loại cư trú", required=True),
                    rx.select(["Nội trú", "Ngoại trú"], value=ConductState.evidence_residence_type, on_change=ConductState.set_form_value("evidence_residence_type"), width="100%"),
                    rx.cond(
                        ConductState.evidence_residence_type == "Nội trú",
                        rx.hstack(
                            rx.vstack(form_label("Ký túc xá", required=True), form_input(ConductState.evidence_dormitory, "Nhập Ký túc xá", ConductState.set_form_value("evidence_dormitory")), flex="1", spacing="2"),
                            rx.vstack(form_label("Số phòng", required=True), form_input(ConductState.evidence_room_number, "Nhập Số phòng", ConductState.set_form_value("evidence_room_number")), flex="1", spacing="2"),
                            width="100%",
                            spacing="4",
                            flex_wrap="wrap",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(form_label("Tỉnh/Thành phố", required=True), form_input(ConductState.evidence_city, "Nhập Tỉnh/Thành phố", ConductState.set_form_value("evidence_city")), flex="1", spacing="2"),
                                rx.vstack(form_label("Quận/Huyện", required=True), form_input(ConductState.evidence_district, "Nhập Quận/Huyện", ConductState.set_form_value("evidence_district")), flex="1", spacing="2"),
                                width="100%",
                                spacing="4",
                                flex_wrap="wrap",
                            ),
                            rx.hstack(
                                rx.vstack(form_label("Xã/Phường", required=True), form_input(ConductState.evidence_ward, "Nhập Xã/Phường", ConductState.set_form_value("evidence_ward")), flex="1", spacing="2"),
                                rx.vstack(form_label("Số nhà, đường phố", required=True), form_input(ConductState.evidence_street_address, "Nhập Số nhà, đường phố", ConductState.set_form_value("evidence_street_address")), flex="1", spacing="2"),
                                width="100%",
                                spacing="4",
                                flex_wrap="wrap",
                            ),
                            rx.hstack(
                                rx.vstack(form_label("Họ tên chủ nhà/trọ/người thân", required=True), form_input(ConductState.evidence_host_name, "Nhập Họ tên chủ nhà/trọ/người thân", ConductState.set_form_value("evidence_host_name")), flex="1", spacing="2"),
                                rx.vstack(form_label("SĐT của chủ nhà/trọ/người thân", required=True), form_input(ConductState.evidence_host_phone, "Nhập SĐT của chủ nhà/trọ/người thân", ConductState.set_form_value("evidence_host_phone")), flex="1", spacing="2"),
                                width="100%",
                                spacing="4",
                                flex_wrap="wrap",
                            ),
                            width="100%",
                            spacing="4",
                            align="stretch",
                        ),
                    ),
                    form_label("Tập tin minh chứng", required=True),
                    evidence_file_picker(),
                    spacing="3",
                    align="stretch",
                    width="100%",
                ),
            ),
        ),
    )


def evidence_modal() -> rx.Component:
    return rx.cond(
        ConductState.evidence_modal_open,
        modal_shell(
            ConductState.selected_evidence_category_label,
            evidence_form_fields(),
            rx.hstack(
                action_button("Hủy", ConductState.close_evidence_modal, background="white", color=TEXT, border=f"1px solid {BORDER}"),
                action_button("Thêm mới", ConductState.submit_evidence),
                justify="center",
                spacing="4",
                width="100%",
            ),
            ConductState.close_evidence_modal,
            max_width="960px",
        ),
        rx.fragment(),
    )


def evidence_detail_modal() -> rx.Component:
    def evidence_detail_field(item: dict) -> rx.Component:
        return rx.vstack(
            rx.text(item["label"], font_size="13px", font_weight="700", color=MUTED),
            rx.cond(
                item["is_file"],
                rx.box(
                    rx.vstack(
                        rx.cond(
                            item["is_image"],
                            rx.image(
                                src=rx.get_upload_url(item["file_path"]),
                                alt=item["value"],
                                width="100%",
                                max_height="360px",
                                object_fit="contain",
                                border_radius="10px",
                            ),
                            rx.fragment(),
                        ),
                        rx.link(
                            item["value"],
                            href=rx.get_upload_url(item["file_path"]),
                            is_external=True,
                            color=PRIMARY,
                            font_weight="600",
                            font_size="15px",
                            text_decoration="underline",
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    width="100%",
                    padding="12px 14px",
                    border=f"1px solid {BORDER}",
                    border_radius="8px",
                    background=SURFACE,
                ),
                rx.cond(
                    item["is_missing_file"],
                    rx.box(
                        rx.text(
                            "Không tìm thấy tệp minh chứng cũ. Hãy tải lại minh chứng nếu cần xem ảnh.",
                            font_size="15px",
                            color="#b91c1c",
                        ),
                        width="100%",
                        padding="12px 14px",
                        border="1px solid #fecaca",
                        border_radius="8px",
                        background="#fff1f2",
                    ),
                    rx.cond(
                        item["is_link"],
                        rx.box(
                            rx.link(
                                item["value"],
                                href=item["value"],
                            is_external=True,
                            color=PRIMARY,
                            font_weight="600",
                            font_size="15px",
                            text_decoration="underline",
                        ),
                        width="100%",
                        padding="12px 14px",
                        border=f"1px solid {BORDER}",
                        border_radius="8px",
                        background=SURFACE,
                    ),
                    rx.box(
                        rx.text(item["value"], font_size="15px", color=TEXT),
                        width="100%",
                        padding="12px 14px",
                        border=f"1px solid {BORDER}",
                        border_radius="8px",
                            background=SURFACE,
                        ),
                    ),
                ),
            ),
            spacing="2",
            width="100%",
            align="stretch",
        )

    return rx.cond(
        ConductState.evidence_detail_open,
        modal_shell(
            ConductState.selected_evidence_title,
            rx.vstack(
                rx.text(ConductState.selected_evidence_status_label, color=PRIMARY, font_size="13px", font_weight="700"),
                rx.foreach(
                    ConductState.selected_evidence_fields,
                    evidence_detail_field,
                ),
                spacing="4",
                width="100%",
                align="stretch",
            ),
            rx.hstack(
                rx.cond(ConductState.selected_evidence_can_class_review, action_button("Duyệt", ConductState.approve_selected_evidence_class), rx.fragment()),
                rx.cond(ConductState.selected_evidence_can_advisor_review, action_button("Duyệt", ConductState.approve_selected_evidence_advisor, background="#15803d"), rx.fragment()),
                rx.cond(
                    ConductState.selected_evidence_can_class_review,
                    action_button("Từ chối", ConductState.reject_selected_evidence, background="#fff1f2", color=PRIMARY, border="1px solid #fecdd3"),
                    rx.cond(
                        ConductState.selected_evidence_can_advisor_review,
                        action_button("Từ chối", ConductState.reject_selected_evidence, background="#fff1f2", color=PRIMARY, border="1px solid #fecdd3"),
                        rx.fragment(),
                    ),
                ),
                action_button("Đóng", ConductState.close_evidence_detail, background="white", color=TEXT, border=f"1px solid {BORDER}"),
                justify="end",
                width="100%",
                spacing="3",
            ),
            ConductState.close_evidence_detail,
            max_width="820px",
        ),
        rx.fragment(),
    )


def evidence_page() -> rx.Component:
    show_embedded_semester_select = ConductState.active_tab != "students_evidence"
    return rx.vstack(
        rx.cond(
            ConductState.active_tab == "students_evidence",
            rx.text("Duyệt minh chứng", font_size="22px", font_weight="700", color=TEXT),
            rx.text("Khai báo minh chứng", font_size="22px", font_weight="700", color=TEXT),
        ),
        rx.cond(
            ConductState.grading_target_banner_text != "",
            rx.box(
                rx.text(ConductState.grading_target_banner_text, font_size="14px", font_weight="600", color="#1e3a8a"),
                width="100%",
                padding="10px 14px",
                background="#eff6ff",
                border=f"1px solid {BORDER}",
                border_radius="8px",
            ),
            rx.fragment(),
        ),
        rx.box(
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.cond(
                            ConductState.active_tab == "students_evidence",
                            rx.text("Duyệt minh chứng", font_size="18px", font_weight="700", color=TEXT),
                            rx.text("Khai báo minh chứng", font_size="18px", font_weight="700", color=TEXT),
                        ),
                        rx.hstack(
                            rx.text(ConductState.selected_student_name, font_size="13px", color=MUTED),
                            rx.text("•", font_size="13px", color=MUTED),
                            rx.text(ConductState.selected_student_class, font_size="13px", color=MUTED),
                            rx.text("•", font_size="13px", color=MUTED),
                            rx.text(ConductState.selected_semester_name, font_size="13px", color="#1d4ed8", font_weight="600"),
                            spacing="2",
                            align="center",
                            flex_wrap="wrap",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    rx.cond(
                        show_embedded_semester_select,
                        rx.select(
                            ConductState.semester_names,
                            value=ConductState.selected_semester_name,
                            on_change=ConductState.select_semester_by_name,
                            width="320px",
                        ),
                        rx.fragment(),
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    flex_wrap="wrap",
                ),
                padding="16px 18px",
                border_bottom=f"1px solid {BORDER}",
            ),
            rx.hstack(
                rx.box(
                    rx.box(rx.text("Loại minh chứng", font_size="15px", font_weight="700", color=TEXT), padding="14px 16px", background="#f3f4f6", border_bottom=f"1px solid {BORDER}", text_align="center"),
                    rx.foreach(ConductState.evidence_categories, evidence_category_item),
                    width="320px",
                    border_right=f"1px solid {BORDER}",
                    background="white",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Danh sách minh chứng", font_size="18px", font_weight="700", color=TEXT),
                        rx.hstack(
                            rx.cond(ConductState.show_create_evidence_action, action_button("Thêm mới", ConductState.open_evidence_modal), rx.fragment()),
                            action_button("Tải lại", ConductState.load, background="white", color=TEXT, border=f"1px solid {BORDER}"),
                            rx.box(rx.text("Tổng số: ", color=MUTED), rx.text(ConductState.evidence_count, color=PRIMARY, font_weight="700"), display="flex", align_items="center", gap="4px", padding="0 14px", height="38px", border=f"1px solid {BORDER}", border_radius="8px", background="white"),
                            rx.box(action_button("⚙", ConductState.toggle_column_config, background="white", color=TEXT, border=f"1px solid {BORDER}", padding="0 12px"), position="relative"),
                            align="center",
                            spacing="3",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                    ),
                    rx.box(
                        rx.box(
                            evidence_table_header(),
                            rx.cond(
                                ConductState.has_evidence_rows,
                                rx.vstack(rx.foreach(ConductState.evidence_rows, evidence_row), width="100%", spacing="0", align="stretch"),
                                rx.center(rx.vstack(rx.text("Không có dữ liệu", color="#9ca3af", font_size="16px", font_weight="500"), rx.text("Chưa có minh chứng trong danh mục đang chọn.", color="#c0c4cc", font_size="13px"), spacing="2", align="center"), min_height="260px", min_width="900px"),
                            ),
                            min_width="1164px",
                            width="100%",
                        ),
                        width="100%",
                        border=f"1px solid {BORDER}",
                        border_radius="8px",
                        overflow_x="auto",
                        overflow_y="hidden",
                        position="relative",
                    ),
                    width="100%",
                    align="stretch",
                    spacing="4",
                    padding="16px",
                    position="relative",
                    min_width="0",
                ),
                width="100%",
                spacing="0",
                align="stretch",
                min_width="0",
            ),
            background="white",
            border=f"1px solid {BORDER}",
            border_radius="12px",
            width="100%",
            overflow="hidden",
            position="relative",
        ),
        column_config_panel(),
        width="100%",
        align="stretch",
        spacing="4",
    )
