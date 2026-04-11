from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos


def _unicode_ttf_path() -> str:
    windir = os.environ.get("WINDIR", "C:/Windows")
    for name in ("arial.ttf", "times.ttf", "calibri.ttf", "segoeui.ttf"):
        p = Path(windir) / "Fonts" / name
        if p.is_file():
            return str(p.resolve())
    mac = Path("/Library/Fonts/Arial Unicode.ttf")
    if mac.is_file():
        return str(mac)
    linux = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    if linux.is_file():
        return str(linux)
    raise FileNotFoundError("Không tìm thấy font hệ thống để xuất PDF (Arial hoặc DejaVu).")


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
    table_rows: list[tuple[str, str, str, str, str]],
) -> bytes:
    """table_rows: (tieu_de, toi_da, sv, duyet, cvht)."""
    font_path = _unicode_ttf_path()
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    pdf.add_font("Vi", "", font_path)
    pdf.set_font("Vi", size=13)
    pdf.cell(0, 9, "Phiếu điểm rèn luyện", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("Vi", size=10)
    pdf.cell(0, 6, f"Học kỳ: {semester_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 6, f"Sinh viên: {student_name}  —  Mã: {student_code}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 6, f"Lớp: {class_name}  —  Trạng thái: {status_label}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)
    pdf.set_font("Vi", size=10)
    pdf.cell(0, 7, f"Tổng điểm: SV {self_total}  |  Duyệt {class_total}  |  CVHT {advisor_total}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 7, f"Xếp loại (tham khảo thang 100): {grade_label}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Vi", size=9)
    for title, mx, sv, duyet, cvht in table_rows:
        pdf.multi_cell(0, 5, title, border="B")
        pdf.set_font("Vi", size=8)
        pdf.cell(0, 5, f"Tối đa {mx}  —  SV: {sv}  —  Duyệt: {duyet}  —  CVHT: {cvht}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Vi", size=9)
        pdf.ln(1)
    out = pdf.output()
    if isinstance(out, (bytes, bytearray)):
        return bytes(out)
    return str(out).encode("latin-1")
