class Team:
    """Задача: team"""

    def __init__(self, name: str):
        self.name = name
        self.members = []

    def join(self, person_name: str):
        self.members.append(person_name)
