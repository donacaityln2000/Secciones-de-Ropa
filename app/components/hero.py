import reflex as rx


def hero_section() -> rx.Component:
    """The hero section with a call to action."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Discover Your Signature Style",
                    class_name="text-4xl md:text-6xl font-bold text-gray-900 leading-tight",
                ),
                rx.el.p(
                    "Explore our curated collection of modern essentials. Timeless pieces for the contemporary wardrobe.",
                    class_name="mt-4 max-w-xl text-lg text-gray-600",
                ),
                rx.el.div(
                    rx.el.button(
                        "Shop New Arrivals",
                        rx.icon("arrow-right", class_name="ml-2 h-5 w-5"),
                        class_name="inline-flex items-center justify-center px-8 py-4 bg-gray-900 text-white font-semibold rounded-xl hover:bg-gray-800 transition-all shadow-md hover:shadow-lg transform hover:-translate-y-1",
                    ),
                    rx.el.button(
                        "Explore Collections",
                        variant="outline",
                        class_name="inline-flex items-center justify-center px-8 py-4 bg-transparent border border-gray-300 text-gray-800 font-semibold rounded-xl hover:bg-gray-50 transition-all",
                    ),
                    class_name="mt-8 flex flex-wrap gap-4",
                ),
                class_name="flex flex-col items-start",
            ),
            class_name="container mx-auto px-4 md:px-6 py-24 md:py-32",
        ),
        class_name="w-full bg-gray-50 border-b border-gray-200",
    )