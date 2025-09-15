import reflex as rx
from app.state import State


def nav_link(text: str) -> rx.Component:
    """A navigation link component."""
    return rx.el.a(
        text,
        href="#",
        class_name=rx.cond(
            State.selected_category == text,
            "text-gray-900 font-semibold border-b-2 border-gray-900",
            "text-gray-500 hover:text-gray-900 transition-colors",
        ),
        on_click=lambda: State.select_category(text),
    )


def header() -> rx.Component:
    """The header component for the app."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("shirt", class_name="h-8 w-8 text-gray-900"),
                rx.el.span(
                    "VogueVerse",
                    class_name="text-2xl font-bold text-gray-900 tracking-tight",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.nav(
                nav_link("All"),
                nav_link("Jackets"),
                nav_link("T-Shirts"),
                nav_link("Pants"),
                nav_link("Shoes"),
                nav_link("Accessories"),
                class_name="hidden md:flex items-center gap-8 font-medium",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "search",
                        class_name="h-6 w-6 text-gray-500 hover:text-gray-900 transition-colors",
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.icon(
                        "user",
                        class_name="h-6 w-6 text-gray-500 hover:text-gray-900 transition-colors",
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.icon(
                        "shopping-bag",
                        class_name="h-6 w-6 text-gray-500 hover:text-gray-900 transition-colors",
                    ),
                    rx.el.span(
                        "2",
                        class_name="absolute -top-2 -right-2 flex items-center justify-center h-5 w-5 rounded-full bg-gray-900 text-white text-xs font-bold",
                    ),
                    href="#",
                    class_name="relative",
                ),
                class_name="flex items-center gap-6",
            ),
            class_name="container mx-auto flex items-center justify-between h-20 px-4 md:px-6",
        ),
        class_name="w-full bg-white/80 backdrop-blur-md border-b border-gray-200 sticky top-0 z-50",
    )