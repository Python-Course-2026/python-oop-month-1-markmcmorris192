class Product:
    """Задача: product"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_total(self, qty: int) -> float:
        self.price = qty * self.price
