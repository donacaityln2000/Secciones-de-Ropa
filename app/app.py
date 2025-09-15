import reflex as rx
from app.state import State
from app.components.header import header
from app.components.hero import hero_section
from app.components.product_grid import product_grid
from app.components.footer import footer


def index() -> rx.Component:
    """The main page of the app."""
    return rx.el.div(
        header(),
        rx.el.main(hero_section(), product_grid()),
        footer(),
        class_name="font-['Inter'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="VogueVerse - Modern Essentials")