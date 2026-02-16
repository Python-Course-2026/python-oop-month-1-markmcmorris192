class Student:
    """Задача: student_grades"""

    def __init__(self, name: str):
        self.grades = []

    def add_grade(self, g: int):
        self.grades.append(g)

    def average(self) -> float:
        self.grades.sort(reverse=True)
        return sum(self.grades) / len(self.grades)
