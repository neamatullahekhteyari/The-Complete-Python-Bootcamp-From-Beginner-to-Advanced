from manager import TaskManager
from tasks import Task

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task Complete\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority (Low/Normal/High): ")

            new_task = Task(len(task_manager.tasks) + 1, title, description, due_date, priority)
            task_manager.add_task(new_task)

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter Task ID: "))
            task_manager.mark_task_complete(task_id)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
