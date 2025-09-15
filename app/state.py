import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    price: str
    image: str
    category: str


class State(rx.State):
    """The application state."""

    products: list[Product] = [
        {
            "id": 1,
            "name": "Classic Denim Jacket",
            "price": "$79.99",
            "image": "/placeholder.svg",
            "category": "Jackets",
        },
        {
            "id": 2,
            "name": "Striped Cotton Tee",
            "price": "$29.99",
            "image": "/placeholder.svg",
            "category": "T-Shirts",
        },
        {
            "id": 3,
            "name": "Slim-Fit Chinos",
            "price": "$59.99",
            "image": "/placeholder.svg",
            "category": "Pants",
        },
        {
            "id": 4,
            "name": "Leather Ankle Boots",
            "price": "$129.99",
            "image": "/placeholder.svg",
            "category": "Shoes",
        },
        {
            "id": 5,
            "name": "Minimalist Watch",
            "price": "$199.99",
            "image": "/placeholder.svg",
            "category": "Accessories",
        },
        {
            "id": 6,
            "name": "Wool Scarf",
            "price": "$49.99",
            "image": "/placeholder.svg",
            "category": "Accessories",
        },
        {
            "id": 7,
            "name": "Graphic Print Hoodie",
            "price": "$69.99",
            "image": "/placeholder.svg",
            "category": "Hoodies",
        },
        {
            "id": 8,
            "name": "Linen Blend Shirt",
            "price": "$45.99",
            "image": "/placeholder.svg",
            "category": "Shirts",
        },
    ]
    selected_category: str = "All"

    @rx.var
    def filtered_products(self) -> list[Product]:
        """Returns products filtered by the selected category."""
        if self.selected_category == "All":
            return self.products
        return [p for p in self.products if p["category"] == self.selected_category]

    def select_category(self, category: str):
        """Sets the selected category."""
        self.selected_category = category