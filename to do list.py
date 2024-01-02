import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

class TaskScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Scheduler")
        self.root.geometry("500x400")

        self.task_list = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.pack(pady=10)

        self.priority_entry = tk.Entry(root, width=5)
        self.priority_entry.pack(pady=10)

        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(root, width=10)
        self.time_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_display = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_display.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Scheduler", command=self.start_scheduler)
        self.start_button.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        priority_text = self.priority_entry.get()
        time_text = self.time_entry.get()

        if task_text and priority_text and time_text:
            priority = int(priority_text)
            self.task_list.append({"task": task_text, "priority": priority, "time": time_text, "completed": False})
            self.update_task_display()
            self.task_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task, priority, and time must be provided.")

    def update_task_display(self):
        self.task_display.delete(0, tk.END)
        for task in sorted(self.task_list, key=lambda x: x["priority"]):
            status = " (Completed)" if task["completed"] else ""
            self.task_display.insert(tk.END, f"{task['task']} - Priority: {task['priority']} - Time: {task['time']}{status}")

    def mark_completed(self):
        selected_task_index = self.task_display.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            self.task_list[selected_task_index]["completed"] = True
            self.update_task_display()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.task_display.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            del self.task_list[selected_task_index]
            self.update_task_display()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def execute_tasks(self):
        while True:
            current_time = datetime.now().strftime("%H:%M")

            for task in self.task_list:
                if not task["completed"] and current_time == task["time"]:
                    self.root.after(0, self.show_task_reminder, task)

            time.sleep(60)  # Check every minute

    def show_task_reminder(self, task):
        messagebox.showinfo("Task Reminder", f"It's time to do: {task['task']}")

    def start_scheduler(self):
        if not self.task_list:
            messagebox.showwarning("No Tasks", "Please add tasks before starting the scheduler.")
            return

        self.start_button.config(state=tk.DISABLED)
        scheduler_thread = threading.Thread(target=self.execute_tasks)
        scheduler_thread.daemon = True
        scheduler_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskScheduler(root)
    root.mainloop()
