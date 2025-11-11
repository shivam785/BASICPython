# Day 3: To-Do List (GUI Version)

import tkinter as tk
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x450")
        self.configure(bg="white")

        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="My To-Do List", font=("Arial", 18), bg="white")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14), width=22)
        self.entry.pack(pady=10)

        self.add_btn = tk.Button(self, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_listbox = tk.Listbox(self, font=("Arial", 14), width=30, height=10)
        self.task_listbox.pack(pady=10)

        self.remove_btn = tk.Button(self, text="Remove Selected", font=("Arial", 12), command=self.remove_task)
        self.remove_btn.pack(pady=5)

        self.clear_btn = tk.Button(self, text="Clear All Tasks", font=("Arial", 12), command=self.clear_tasks)
        self.clear_btn.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.task_listbox.delete(0, tk.END)
            self.tasks.clear()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
