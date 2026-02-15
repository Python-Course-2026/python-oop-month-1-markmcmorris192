class Thermometer:
    """Задача: thermometer"""

    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """(C * 9/5) + 32"""
        return self.celsius * 9 / 5 + 32
