class Task:
    def __init__(self, task_id, title, description, due_date, priority="Normal"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "❌ Pending"
        return f"[{self.task_id}] {self.title} ({self.priority}) - {status}"
