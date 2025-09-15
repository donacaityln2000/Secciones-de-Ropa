import reflex as rx


def footer_link_group(title: str, links: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
        ),
        rx.el.ul(
            rx.foreach(
                links,
                lambda link: rx.el.li(
                    rx.el.a(
                        link,
                        href="#",
                        class_name="text-base text-gray-500 hover:text-gray-900",
                    ),
                    class_name="mt-4",
                ),
            ),
            role="list",
        ),
    )


def footer() -> rx.Component:
    """The footer component."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    footer_link_group("Shop", ["Men", "Women", "Kids", "Accessories"]),
                    footer_link_group("About", ["Our Story", "Careers", "Press"]),
                    footer_link_group(
                        "Help", ["Contact Us", "FAQs", "Shipping & Returns"]
                    ),
                    class_name="grid grid-cols-2 md:grid-cols-3 gap-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Subscribe to our newsletter",
                        class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
                    ),
                    rx.el.p(
                        "The latest deals and savings, sent to your inbox weekly.",
                        class_name="mt-4 text-base text-gray-500",
                    ),
                    rx.el.form(
                        rx.el.label(
                            "Email address",
                            html_for="email-address",
                            class_name="sr-only",
                        ),
                        rx.el.input(
                            type="email",
                            id="email-address",
                            name="email-address",
                            placeholder="Enter your email",
                            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-gray-900 focus:border-gray-900",
                        ),
                        rx.el.button(
                            "Sign up",
                            type="submit",
                            class_name="mt-2 w-full flex justify-center py-2 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-gray-900 hover:bg-gray-800",
                        ),
                        class_name="mt-4",
                    ),
                    class_name="mt-12 md:mt-0",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("shirt", class_name="h-6 w-6 text-gray-500"),
                    rx.el.p(
                        "© 2024 VogueVerse, Inc. All rights reserved.",
                        class_name="text-sm text-gray-500",
                    ),
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "github",
                            class_name="h-6 w-6 text-gray-500 hover:text-gray-900",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "twitter",
                            class_name="h-6 w-6 text-gray-500 hover:text-gray-900",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "instagram",
                            class_name="h-6 w-6 text-gray-500 hover:text-gray-900",
                        ),
                        href="#",
                    ),
                    class_name="flex items-center space-x-6",
                ),
                class_name="mt-12 pt-8 border-t border-gray-200 flex items-center justify-between",
            ),
            class_name="container mx-auto px-4 md:px-6 py-12",
        ),
        class_name="bg-gray-50",
    )