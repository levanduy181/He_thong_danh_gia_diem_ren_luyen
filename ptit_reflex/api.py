from __future__ import annotations

from pathlib import Path

import reflex as rx
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from ptit_reflex.data import UPLOADS_URL_PREFIX, api_dashboard_payload, api_semesters_payload, api_submission_payload

LEGACY_UPLOADS_URL_PREFIX = "/uploads"


async def health_check(request) -> JSONResponse:
    return JSONResponse({"status": "ok", "service": "ptit-conduct-evaluation"})


async def api_semesters(request) -> JSONResponse:
    return JSONResponse(api_semesters_payload())


async def api_dashboard(request) -> JSONResponse:
    return JSONResponse(api_dashboard_payload())


async def api_submission(request) -> JSONResponse:
    submission_id = int(request.path_params["submission_id"])
    payload = api_submission_payload(submission_id)
    if payload is None:
        return JSONResponse({"detail": "Không tìm thấy phiếu đánh giá"}, status_code=404)
    return JSONResponse(payload)


async def api_logout(request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


def _has_route(starlette_app, path: str) -> bool:
    return any(getattr(route, "path", None) == path for route in starlette_app.routes)


def install_api(starlette_app) -> None:
    if not _has_route(starlette_app, "/api/health"):
        starlette_app.add_route("/api/health", health_check, methods=["GET"])
    if not _has_route(starlette_app, "/api/semesters"):
        starlette_app.add_route("/api/semesters", api_semesters, methods=["GET"])
    if not _has_route(starlette_app, "/api/dashboard"):
        starlette_app.add_route("/api/dashboard", api_dashboard, methods=["GET"])
    if not _has_route(starlette_app, "/api/submissions/{submission_id:int}"):
        starlette_app.add_route("/api/submissions/{submission_id:int}", api_submission, methods=["GET"])
    if not _has_route(starlette_app, "/api/logout"):
        starlette_app.add_route("/api/logout", api_logout, methods=["POST"])
    upload_dir = Path(rx.get_upload_dir())
    upload_dir.mkdir(parents=True, exist_ok=True)
    if not _has_route(starlette_app, UPLOADS_URL_PREFIX):
        starlette_app.mount(UPLOADS_URL_PREFIX, StaticFiles(directory=upload_dir), name="uploads")
    if not _has_route(starlette_app, LEGACY_UPLOADS_URL_PREFIX):
        starlette_app.mount(LEGACY_UPLOADS_URL_PREFIX, StaticFiles(directory=upload_dir), name="legacy_uploads")
