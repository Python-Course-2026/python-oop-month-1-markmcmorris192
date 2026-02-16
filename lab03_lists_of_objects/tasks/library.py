class Library:
    """Задача: library"""

    def __init__(self):
        self.books = []

    def add_book(self, title: str):
        self.books.append(title)
