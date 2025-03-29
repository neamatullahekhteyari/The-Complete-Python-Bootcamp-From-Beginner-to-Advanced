from tasks import Task
from users import User
from utils.file_handler import save_data, load_data
from utils.error_handler import handle_error

class TaskManager:
    def __init__(self):
        self.tasks = load_data("tasks.json")
        self.users = load_data("users.json")

    def add_task(self, task):
        try:
            self.tasks.append(task)
            save_data("tasks.json", self.tasks)
        except Exception as e:
            handle_error(e)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_complete(self, task_id):
        try:
            task = next(t for t in self.tasks if t.task_id == task_id)
            task.mark_complete()
            save_data("tasks.json", self.tasks)
        except StopIteration:
            print("Task not found!")
        except Exception as e:
            handle_error(e)
