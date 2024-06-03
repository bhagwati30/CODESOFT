import tkinter as tk
from tkinter import messagebox
import json

tasks = []
selected_index = None
tasks_file = "tasks.json"

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open(tasks_file, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task_description = entry.get()
    if task_description:
        tasks.append({"description": task_description, "status": "pending"})
        save_tasks()  # Save tasks after adding
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task description.")

# Update the task list in the listbox
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["status"] == "completed" else "✘"
        listbox.insert(tk.END, f"{task['description']} - {status}")

# Handle task selection in the listbox
def on_task_select(event):
    global selected_index
    try:
        selected_index = listbox.curselection()[0]
    except IndexError:
        selected_index = None

# Delete a selected task
def delete_task():
    global selected_index
    if selected_index is not None:
        tasks.pop(selected_index)
        save_tasks()  # Save tasks after deletion
        update_task_list()
        selected_index = None
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Modify a selected task
def modify_task():
    global selected_index
    if selected_index is not None:
        new_description = entry.get()
        if new_description:
            tasks[selected_index]["description"] = new_description
            save_tasks()  # Save tasks after modification
            update_task_list()
            entry.delete(0, tk.END)
            selected_index = None
        else:
            messagebox.showwarning("Warning", "You must enter a new task description.")
    else:
        messagebox.showwarning("Warning", "You must select a task to modify.")

# Toggle the status of a selected task
def toggle_task_status():
    global selected_index
    if selected_index is not None:
        current_status = tasks[selected_index]["status"]
        tasks[selected_index]["status"] = "completed" if current_status == "pending" else "pending"
        save_tasks()  # Save tasks after status change
        update_task_list()
        selected_index = None
    else:
        messagebox.showwarning("Warning", "You must select a task to change its status.")

# Main GUI setup
def main_gui():
    global entry, listbox
    
    load_tasks()  # Load tasks at the beginning
    
    app = tk.Tk()
    app.title("To-Do List")

    frame = tk.Frame(app)
    frame.pack(pady=10)

    entry = tk.Entry(frame, width=30)
    entry.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(frame, text="Add Task", command=add_task)
    add_button.pack(side=tk.LEFT)

    modify_button = tk.Button(frame, text="Modify Task", command=modify_task)
    modify_button.pack(side=tk.LEFT)

    delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
    delete_button.pack(side=tk.LEFT)

    status_button = tk.Button(frame, text="Toggle Status", command=toggle_task_status)
    status_button.pack(side=tk.LEFT)

    listbox = tk.Listbox(app, width=50, height=10)
    listbox.pack(pady=10)
    listbox.bind('<<ListboxSelect>>', on_task_select)

    update_task_list()  # Update the task list initially

    app.mainloop()

if __name__ == "__main__":
    main_gui()
