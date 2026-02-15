class CoffeeMachine:
    """Задача: coffee_machine"""

    def __init__(self, water: int, beans: int):
        self.water = water
        self.beans = beans

    def make_coffee(self):
        """Нужно 200мл воды и 20г зерен. Вернуть 'OK' или 'Error'"""
        if self.water >= 200 and self.beans >= 20:
            return 'OK'
        else:
            return 'Error'
