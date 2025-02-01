tasks_dict = {}  # Stores in-progress tasks
completed_task_dict = {}  # Stores completed tasks

def add_task():
    task_name = input("Enter your task name: ").lower().strip()
    if task_name in tasks_dict:
        print(f"Task '{task_name}' already exists.")
        return
    
    task_description = input("Enter task description: ").lower().strip()
    tasks_dict[task_name] = task_description
    print(f"✅ Task '{task_name}' added successfully.")

def update_task():
    task = input("Enter the task you want to update: ").lower().strip()
    if task not in tasks_dict:
        print(f"❌ Task '{task}' not found.")
        return

    print("1- Update Task Description\n2- Mark as Done")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_description = input("Enter new description: ").lower().strip()
        tasks_dict[task] = task_description
        print(f"✅ Task '{task}' updated.")
    
    elif choice == "2":
        mark_as_done(task)
    else:
        print("❌ Invalid choice.")

def view_tasks():
    print("\n📌 What do you want to view?")
    print("1- In-Progress Tasks")
    print("2- Completed Tasks")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        if not tasks_dict:
            print("📭 No In-Progress tasks to show.")
            return
        print("\n📝 **In-Progress Tasks**:")
        for i, (task, desc) in enumerate(tasks_dict.items(), 1):
            print(f"{i}. {task} - {desc}")
    
    elif choice == "2":
        if not completed_task_dict:
            print("📭 No Completed tasks to show.")
            return
        print("\n✅ **Completed Tasks**:")
        for i, (task, desc) in enumerate(completed_task_dict.items(), 1):
            print(f"{i}. {task} - {desc}")

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")


def mark_as_done(task=None):
    if not task:
        task = input("Enter the task name to mark as done: ").lower().strip()

    if task in tasks_dict:
        completed_task_dict[task] = tasks_dict.pop(task)
        print(f"✅ Task '{task}' marked as done.")
    else:
        print(f"❌ Task '{task}' not found.")

def delete_task():
    task = input("Enter task name to delete: ").lower().strip()
    if task in tasks_dict:
        del tasks_dict[task]
        print(f"🗑 Task '{task}' deleted.")
    else:
        print(f"❌ Task '{task}' not found.")

def count_tasks():
    print(f"📌 To-Do: {len(tasks_dict)} | ✅ Completed: {len(completed_task_dict)}")

# Main loop
while True:
    print("\n--- 📝 To-Do List App ---")
    print("1- Add Task\n2- Update Task\n3- View Tasks\n4- Mark as Done\n5- Delete Task\n6- Count Tasks\n7- Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        mark_as_done()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        count_tasks()
    elif choice == "7":
        print("👋 Thanks for using! Exiting...")
        break
    else:
        print("❌ Invalid choice. Please enter a valid option.")