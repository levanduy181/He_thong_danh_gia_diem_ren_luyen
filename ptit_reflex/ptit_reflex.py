import reflex as rx

from ptit_reflex.api import install_api
from ptit_reflex.state import ConductState
from ptit_reflex.views import app_view


def index() -> rx.Component:
    return app_view()


app = rx.App(
    style={
        "font_family": "Inter, system-ui, sans-serif",
        "background": "#f8fafc",
        "color": "#1f2937",
    }
)
install_api(app._api)
app.add_page(index, route="/", title="Hệ thống đánh giá điểm rèn luyện", on_load=ConductState.load)
