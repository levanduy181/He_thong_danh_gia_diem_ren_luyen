import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin


config = rx.Config(
    app_name="ptit_reflex",
    disable_plugins=[SitemapPlugin],
    backend_host="0.0.0.0",
    vite_allowed_hosts=True,
)
