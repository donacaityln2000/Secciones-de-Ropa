import reflex as rx
from app.state import State
from app.components.product_card import product_card


def product_grid() -> rx.Component:
    """A grid to display products."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "New Arrivals",
                    class_name="text-3xl font-bold tracking-tight text-gray-900",
                ),
                rx.el.p(
                    f"Showing products for: {State.selected_category}",
                    class_name="text-gray-600",
                ),
                class_name="mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(State.filtered_products, product_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-12",
            ),
            class_name="container mx-auto px-4 md:px-6 py-16",
        ),
        class_name="bg-white",
    )