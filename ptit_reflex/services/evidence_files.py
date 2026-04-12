from __future__ import annotations

import shutil
from pathlib import Path
from uuid import uuid4

import reflex as rx

from ptit_reflex.config import DATA_DIR


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}


def is_image_file(file_name: str) -> bool:
    return Path((file_name or "").strip()).suffix.lower() in IMAGE_EXTENSIONS


def _normalize_file_name(file_name: str) -> str:
    clean_name = Path((file_name or "").strip()).name
    return clean_name or f"minh_chung_{uuid4().hex}"


def _normalize_relative_path(relative_path: str) -> str:
    return str(Path(relative_path.strip().lstrip("/"))).replace("\\", "/")


def _stored_file_path(relative_path: str) -> Path:
    upload_root = rx.get_upload_dir().resolve()
    candidate = (upload_root / Path(_normalize_relative_path(relative_path))).resolve()
    try:
        candidate.relative_to(upload_root)
    except ValueError as exc:
        raise ValueError("Đường dẫn tệp minh chứng không hợp lệ.") from exc
    return candidate


def _legacy_upload_paths(file_name: str) -> list[Path]:
    base_name = _normalize_file_name(file_name)
    if not base_name:
        return []

    candidates: list[Path] = []
    upload_root = rx.get_upload_dir().resolve()
    data_upload_root = (DATA_DIR / "uploads").resolve()

    for root in (upload_root, data_upload_root):
        if not root.exists():
            continue
        try:
            candidates.extend(path.resolve() for path in root.rglob(base_name) if path.is_file())
        except OSError:
            continue

    return candidates


def resolve_evidence_upload(relative_path: str, file_name: str = "") -> str:
    relative = _normalize_relative_path(relative_path or "")
    if relative:
        try:
            absolute_path = _stored_file_path(relative)
        except ValueError:
            absolute_path = None
        if absolute_path and absolute_path.is_file():
            return relative

    for legacy_path in _legacy_upload_paths(file_name):
        upload_root = rx.get_upload_dir().resolve()
        try:
            inside_upload_root = legacy_path.relative_to(upload_root)
            return str(inside_upload_root).replace("\\", "/")
        except ValueError:
            suffix = legacy_path.suffix.lower()
            if len(suffix) > 10:
                suffix = ""
            restored_relative = _normalize_relative_path(f"evidence/legacy_{uuid4().hex}{suffix}")
            restored_absolute = _stored_file_path(restored_relative)
            restored_absolute.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(legacy_path, restored_absolute)
            return restored_relative

    return ""


async def save_evidence_upload(file: rx.UploadFile) -> tuple[str, str]:
    original_name = _normalize_file_name(str(file.filename or ""))
    suffix = Path(original_name).suffix.lower()
    if len(suffix) > 10:
        suffix = ""
    relative_path = _normalize_relative_path(f"evidence/{uuid4().hex}{suffix}")
    absolute_path = _stored_file_path(relative_path)
    absolute_path.parent.mkdir(parents=True, exist_ok=True)

    with absolute_path.open("wb") as uploaded_file:
        uploaded_file.write(await file.read())

    return relative_path, original_name


def delete_evidence_upload(relative_path: str) -> None:
    relative = resolve_evidence_upload(relative_path or "")
    if not relative:
        return

    try:
        absolute_path = _stored_file_path(relative)
    except ValueError:
        return
    if absolute_path.is_file():
        absolute_path.unlink()
