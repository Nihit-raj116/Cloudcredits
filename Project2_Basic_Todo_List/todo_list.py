#Basic TODO_list
tasks = []
def add_task(task):
    tasks.append({'task': task, 'completed': False})
    print(f"Task added: {task}")
def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['task']}")
    else:
        print("Invalid task number.")
def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✓ Done" if task['completed'] else "✗ Not Done"
        print(f"{i + 1}. {task['task']} [{status}]")
    print()
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: ")) - 1
                mark_completed(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()