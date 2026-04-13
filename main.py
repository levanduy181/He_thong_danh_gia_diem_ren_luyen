from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parent
    env = os.environ.copy()
    env.setdefault("REFLEX_USE_NPM", "1")
    env.setdefault("REFLEX_HOT_RELOAD_EXCLUDE_PATHS", "data")
    command = [
        sys.executable,
        "-m",
        "reflex",
        "run",
        "--backend-host",
        "0.0.0.0",
        "--frontend-port",
        "3000",
        "--backend-port",
        "8000",
    ]
    return subprocess.call(command, cwd=project_root, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
