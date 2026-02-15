class Circle:
    """Задача: circle"""

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        """Возвращает площадь (3.14 * r^2)"""
        return 3.14 * self.radius ** 2
