class Timer:
    """Задача: timer"""

    def __init__(self, sec: int):
        self.sec = sec

    def tick(self):
        """Уменьшает sec на 1, пока > 0"""
        while self.sec > 0:
            self.sec -= 1
