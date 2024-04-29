import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []

        # Create UI elements
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            self.tasks[selected_index] = updated_task
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, updated_task)
            self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
