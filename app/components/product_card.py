import reflex as rx
from app.state import Product


def product_card(product: Product) -> rx.Component:
    """A card to display a product."""
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.el.img(
                    src=product["image"],
                    class_name="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500",
                ),
                href="#",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("shopping-cart", class_name="h-5 w-5"),
                    "Add to Cart",
                    class_name="absolute bottom-4 left-1/2 -translate-x-1/2 translate-y-4 opacity-0 group-hover:opacity-100 group-hover:translate-y-0 flex items-center gap-2 px-4 py-2 bg-white text-gray-900 font-semibold rounded-lg shadow-md hover:bg-gray-100 transition-all duration-300",
                ),
                class_name="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
            ),
            class_name="relative w-full aspect-square bg-gray-100 rounded-xl overflow-hidden group",
        ),
        rx.el.div(
            rx.el.h3(
                rx.el.a(
                    product["name"],
                    href="#",
                    class_name="text-base font-semibold text-gray-800 hover:text-gray-900",
                )
            ),
            rx.el.p(product["category"], class_name="text-sm text-gray-500"),
            rx.el.p(
                product["price"], class_name="mt-2 text-lg font-bold text-gray-900"
            ),
            class_name="mt-4 flex flex-col items-start",
        ),
        class_name="flex flex-col",
    )