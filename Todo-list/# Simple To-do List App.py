# Simple To-do List App
todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("Which task number do you want to remove?")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Task number: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            expect ValueError:
        print("Please enter a valid number.")
    elif choice == "4":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")



