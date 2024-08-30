from datetime import datetime

tasks = []

def addTask():
    task = input("Please enter a task: ")
    priority = input("Set a priority level (High, Medium, Low): ")
    deadline = input("Enter a deadline (YYYY-MM-DD) or leave empty: ")

    if deadline:
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Deadline not set.")
            deadline = ""

    tasks.append({
        "task": task,
        "priority": priority,
        "deadline": deadline,
        "status": "Incomplete"
    })
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}: {task['task']} - {task['priority']} - {task['deadline']} - {task['status']}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: ")) - 1
        if 0 <= taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task['task']}' has been removed.")
        else:
            print(f"Task #{taskToDelete+1} was not found.")
    except ValueError:
        print("Invalid input.")

def markTaskComplete():
    listTasks()
    try:
        taskToComplete = int(input("Enter the # to mark as complete: ")) - 1
        if 0 <= taskToComplete < len(tasks):
            tasks[taskToComplete]['status'] = "Complete"
            print(f"Task #{taskToComplete+1} marked as complete.")
        else:
            print(f"Task #{taskToComplete+1} was not found.")
    except ValueError:
        print("Invalid input.")

def searchTasks():
    keyword = input("Enter a keyword to search: ")
    results = [task for task in tasks if keyword.lower() in task['task'].lower()]
    if results:
        print("Search Results:")
        for task in results:
            print(f"- {task['task']} - {task['priority']} - {task['deadline']} - {task['status']}")
    else:
        print("No tasks found matching the keyword.")

if __name__ == "__main__":
    print("Welcome to the advanced to-do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Mark a task as complete")
        print("5. Search for a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            markTaskComplete()
        elif choice == "5":
            searchTasks()
        elif choice == "6":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
