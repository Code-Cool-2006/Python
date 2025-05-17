import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        tasks.remove(selected_task)
        update_list()
    except:
        messagebox.showwarning("Warning", "No task selected!")

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()