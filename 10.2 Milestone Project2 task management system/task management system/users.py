class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"User: {self.name}, Tasks Assigned: {len(self.tasks)}"
