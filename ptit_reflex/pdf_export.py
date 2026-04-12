from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF


PAGE_MARGIN = 10
HEADER_FILL = (243, 244, 246)
GROUP_FILL = (249, 250, 251)
BORDER_COLOR = (209, 213, 219)
TEXT_COLOR = (31, 41, 55)
MUTED_TEXT_COLOR = (75, 85, 99)
TITLE_COLOR = (17, 24, 39)

COL_CONTENT = 135
COL_RANGE = 32
COL_SELF = 32
COL_CLASS = 32
COL_ADVISOR = 32
TABLE_LINE_HEIGHT = 6


def _font_paths() -> tuple[str, str]:
    windir = os.environ.get("WINDIR", "C:/Windows")
    regular_candidates = ("arial.ttf", "times.ttf", "calibri.ttf", "segoeui.ttf")
    bold_candidates = ("arialbd.ttf", "timesbd.ttf", "calibrib.ttf", "segoeuib.ttf")

    for regular_name, bold_name in zip(regular_candidates, bold_candidates):
        regular_path = Path(windir) / "Fonts" / regular_name
        bold_path = Path(windir) / "Fonts" / bold_name
        if regular_path.is_file():
            return (
                str(regular_path.resolve()),
                str((bold_path if bold_path.is_file() else regular_path).resolve()),
            )

    mac_regular = Path("/Library/Fonts/Arial Unicode.ttf")
    if mac_regular.is_file():
        return str(mac_regular), str(mac_regular)

    linux_regular = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    linux_bold = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    if linux_regular.is_file():
        return str(linux_regular), str((linux_bold if linux_bold.is_file() else linux_regular))

    raise FileNotFoundError("Không tìm thấy font hệ thống để xuất PDF (Arial, Segoe UI hoặc DejaVu).")


def _text_lines(pdf: FPDF, width: float, text: str) -> list[str]:
    return pdf.multi_cell(width, TABLE_LINE_HEIGHT, text or "", dry_run=True, output="LINES")


def _ensure_table_room(pdf: FPDF, required_height: float) -> None:
    usable_bottom = pdf.h - pdf.b_margin
    if pdf.get_y() + required_height <= usable_bottom:
        return
    pdf.add_page()
    _draw_table_header(pdf)


def _draw_table_header(pdf: FPDF) -> None:
    pdf.set_draw_color(*BORDER_COLOR)
    pdf.set_fill_color(*HEADER_FILL)
    pdf.set_text_color(*TEXT_COLOR)
    pdf.set_font("Vi", "B", 11)
    pdf.cell(COL_CONTENT, 10, "NỘI DUNG", border=1, align="C", fill=True)
    pdf.cell(COL_RANGE, 10, "Điểm tối đa", border=1, align="C", fill=True)
    pdf.cell(COL_SELF, 10, "Sinh viên", border=1, align="C", fill=True)
    pdf.cell(COL_CLASS, 10, "Duyệt", border=1, align="C", fill=True)
    pdf.cell(COL_ADVISOR, 10, "CVHT", border=1, align="C", fill=True)
    pdf.ln(10)


def _draw_group_row(pdf: FPDF, row: dict[str, str]) -> None:
    _ensure_table_room(pdf, 10)
    pdf.set_draw_color(*BORDER_COLOR)
    pdf.set_fill_color(*GROUP_FILL)
    pdf.set_text_color(*TITLE_COLOR)
    pdf.set_font("Vi", "B", 11)
    pdf.cell(COL_CONTENT, 10, row["title"], border=1, align="L", fill=True)
    pdf.cell(COL_RANGE, 10, row["range"], border=1, align="C", fill=True)
    pdf.cell(COL_SELF, 10, "", border=1, align="C", fill=True)
    pdf.cell(COL_CLASS, 10, "", border=1, align="C", fill=True)
    pdf.cell(COL_ADVISOR, 10, "", border=1, align="C", fill=True)
    pdf.ln(10)


def _draw_item_row(pdf: FPDF, row: dict[str, str]) -> None:
    pdf.set_font("Vi", "", 10)
    content_lines = max(1, len(_text_lines(pdf, COL_CONTENT - 4, row["title"])))
    range_lines = max(1, len(_text_lines(pdf, COL_RANGE - 4, row["range"])))
    row_height = max(content_lines, range_lines, 1) * TABLE_LINE_HEIGHT
    _ensure_table_room(pdf, row_height)

    start_x = pdf.get_x()
    start_y = pdf.get_y()

    pdf.set_draw_color(*BORDER_COLOR)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(*TEXT_COLOR)

    pdf.rect(start_x, start_y, COL_CONTENT, row_height)
    pdf.multi_cell(
        COL_CONTENT,
        TABLE_LINE_HEIGHT,
        row["title"],
        border=0,
        align="L",
        new_x="RIGHT",
        new_y="TOP",
    )
    pdf.set_xy(start_x + COL_CONTENT, start_y)

    pdf.set_text_color(*MUTED_TEXT_COLOR)
    pdf.rect(pdf.get_x(), start_y, COL_RANGE, row_height)
    pdf.multi_cell(
        COL_RANGE,
        TABLE_LINE_HEIGHT,
        row["range"],
        border=0,
        align="C",
        new_x="RIGHT",
        new_y="TOP",
    )
    pdf.set_xy(start_x + COL_CONTENT + COL_RANGE, start_y)

    score_columns = (
        (COL_SELF, row["self_score"]),
        (COL_CLASS, row["class_score"]),
        (COL_ADVISOR, row["advisor_score"]),
    )
    pdf.set_text_color(*TEXT_COLOR)
    for width, value in score_columns:
        pdf.rect(pdf.get_x(), start_y, width, row_height)
        pdf.multi_cell(
            width,
            row_height,
            value,
            border=0,
            align="C",
            new_x="RIGHT",
            new_y="TOP",
        )

    pdf.set_xy(start_x, start_y + row_height)


def _draw_total_row(pdf: FPDF, self_total: str, class_total: str, advisor_total: str) -> None:
    _ensure_table_room(pdf, 10)
    pdf.set_draw_color(*BORDER_COLOR)
    pdf.set_fill_color(*GROUP_FILL)
    pdf.set_text_color(*TITLE_COLOR)
    pdf.set_font("Vi", "B", 11)
    pdf.cell(COL_CONTENT, 10, "TỔNG ĐIỂM", border=1, align="L", fill=True)
    pdf.cell(COL_RANGE, 10, "100", border=1, align="C", fill=True)
    pdf.cell(COL_SELF, 10, self_total, border=1, align="C", fill=True)
    pdf.cell(COL_CLASS, 10, class_total, border=1, align="C", fill=True)
    pdf.cell(COL_ADVISOR, 10, advisor_total, border=1, align="C", fill=True)
    pdf.ln(10)


def build_conduct_pdf_bytes(
    semester_name: str,
    student_name: str,
    student_code: str,
    class_name: str,
    status_label: str,
    self_total: str,
    class_total: str,
    advisor_total: str,
    grade_label: str,
    table_rows: list[dict[str, str]],
) -> bytes:
    regular_font_path, bold_font_path = _font_paths()
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=PAGE_MARGIN)
    pdf.set_margins(PAGE_MARGIN, PAGE_MARGIN, PAGE_MARGIN)
    pdf.add_page()
    pdf.add_font("Vi", "", regular_font_path)
    pdf.add_font("Vi", "B", bold_font_path)

    pdf.set_text_color(*TITLE_COLOR)
    pdf.set_font("Vi", "B", 15)
    pdf.cell(0, 10, "PHIẾU ĐIỂM RÈN LUYỆN", align="C")
    pdf.ln(12)

    pdf.set_font("Vi", "", 10)
    pdf.set_text_color(*TEXT_COLOR)
    pdf.cell(0, 6, f"Học kỳ: {semester_name}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Sinh viên: {student_name}    Mã sinh viên: {student_code}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Lớp: {class_name}    Trạng thái: {status_label}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(
        0,
        6,
        f"Tổng điểm: SV {self_total}    Duyệt {class_total}    CVHT {advisor_total}    Xếp loại: {grade_label}",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(3)

    _draw_table_header(pdf)
    for row in table_rows:
        if row["kind"] == "group":
            _draw_group_row(pdf, row)
        else:
            _draw_item_row(pdf, row)

    _draw_total_row(pdf, self_total, class_total, advisor_total)

    out = pdf.output()
    if isinstance(out, (bytes, bytearray)):
        return bytes(out)
    return str(out).encode("latin-1")
