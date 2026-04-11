import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin


config = rx.Config(
    app_name="ptit_reflex",
    disable_plugins=[SitemapPlugin],
)
