class TodoList:
    """Задача: todo_list"""

    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)
