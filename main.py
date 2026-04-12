from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path


def _require_module(module_name: str, package_name: str) -> bool:
    if importlib.util.find_spec(module_name) is not None:
        return True
    print(
        (
            f"Khong tim thay thu vien '{package_name}'. "
            f"Hay chay '{sys.executable} -m pip install -r requirements.txt' truoc khi mo ung dung."
        ),
        file=sys.stderr,
    )
    return False


def main() -> int:
    project_root = Path(__file__).resolve().parent
    data_dir = project_root / "data"
    env = os.environ.copy()

    if not data_dir.is_dir():
        print(
            "Khong tim thay thu muc data. Hay tu tao thu muc 'data' truoc khi chay ung dung.",
            file=sys.stderr,
        )
        return 1

    # Reflex is more stable on Windows when npm is preferred explicitly.
    env.setdefault("REFLEX_USE_NPM", "1")

    # Giảm hot-reload backend khi có ghi file trong thư mục data (SQLite, v.v.).
    # Dòng "Compiling" trong log = Reflex biên dịch lại sau khi tiến trình backend khởi động lại.
    if not env.get("REFLEX_HOT_RELOAD_EXCLUDE_PATHS"):
        env["REFLEX_HOT_RELOAD_EXCLUDE_PATHS"] = "data"

    nodejs_dir = Path(r"C:\Program Files\nodejs")
    if nodejs_dir.exists():
        env["PATH"] = f"{nodejs_dir};{env.get('PATH', '')}"

    npm_path = shutil.which("npm", path=env.get("PATH"))
    if not npm_path:
        print("Khong tim thay npm. Hay cai Node.js LTS tu https://nodejs.org", file=sys.stderr)
        return 1
    if not _require_module("fpdf", "fpdf2"):
        return 1

    command = [sys.executable, "-m", "reflex", "run"]
    return subprocess.call(command, cwd=project_root, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
