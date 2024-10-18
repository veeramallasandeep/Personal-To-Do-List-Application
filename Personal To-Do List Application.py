import json  # Import JSON module for file handling
import os  # Import os module for file checking

# Task class to represent individual tasks
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False  # By default, the task is not completed

    def mark_completed(self):
        self.completed = True  # Method to mark task as completed

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        # Save tasks as a list of dictionaries
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):  # Check if the file exists
        with open('tasks.json', 'r') as f:
            # Load tasks and convert them back to Task objects
            return [Task(**data) for data in json.load(f)]
    return []  # Return an empty list if the file doesn't exist

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)  # Create a new task
    tasks.append(task)  # Add the task to the list
    print("Task added successfully!")

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task.completed else "✗"
        print(f"{idx}. [{status}] {task.title} - {task.description} (Category: {task.category})")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)  # Display tasks to choose from
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number].mark_completed()  # Mark the selected task as completed
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)  # Display tasks to choose from
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)  # Remove the selected task from the list
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    tasks = load_tasks()  # Load tasks from the file at the start
    while True:
        print("\n--- Personal To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)  # Call the function to add a task
        elif choice == '2':
            view_tasks(tasks)  # Call the function to view tasks
        elif choice == '3':
            mark_task_completed(tasks)  # Call the function to mark a task as completed
        elif choice == '4':
            delete_task(tasks)  # Call the function to delete a task
        elif choice == '5':
            save_tasks(tasks)  # Save tasks before exiting
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point of the application
if __name__ == '__main__':
    main()  # Run the main function to start the application
