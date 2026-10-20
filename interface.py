import tkinter as tk
from tkinter import ttk


class Interface:
    """Главный интерфейс приложения Task Manager."""

    def __init__(self):
        # Создаём главное окно приложения
        self.root = tk.Tk()

        # Настройки главного окна
        self.root.title("Task Manager")
        self.root.geometry("600x420")
        self.root.minsize(450, 300)
        self.root.configure(bg="#f2f4f8")

        # Список задач
        self.tasks = []

        # Заголовок
        title = ttk.Label(
            self.root,
            text="Task Manager",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=(18, 12))

        # Поле для ввода новой задачи
        input_frame = ttk.Frame(self.root, padding=(16, 4))
        input_frame.pack(fill="x")

        self.task_entry = ttk.Entry(input_frame)
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_button = ttk.Button(
            input_frame,
            text="Добавить задачу",
            command=self.add_task
        )
        add_button.pack(side="right")

        # Список задач с прокруткой при необходимости
        list_frame = ttk.Frame(self.root, padding=16)
        list_frame.pack(fill="both", expand=True)

        self.task_list = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            activestyle="dotbox",
            height=10
        )
        self.task_list.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.task_list.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.task_list.configure(yscrollcommand=scrollbar.set)

        # Кнопки управления задачами
        buttons = ttk.Frame(self.root, padding=(16, 0, 16, 16))
        buttons.pack(fill="x")

        ttk.Button(
            buttons,
            text="Выполнено",
            command=self.complete_task
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            buttons,
            text="Удалить",
            command=self.delete_task
        ).pack(side="left")

    def add_task(self):
        """Добавляет задачу в список."""
        task = self.task_entry.get().strip()
        if not task:
            return

        self.tasks.append({"text": task, "done": False})
        self.task_list.insert(tk.END, f"☐ {task}")
        self.task_entry.delete(0, tk.END)

    def complete_task(self):
        """Отмечает выбранную задачу выполненной."""
        selection = self.task_list.curselection()
        if not selection:
            return

        index = selection[0]
        task = self.tasks[index]
        if not task["done"]:
            task["done"] = True
            self.task_list.delete(index)
            self.task_list.insert(index, f"✓ {task['text']}")
            self.task_list.selection_set(index)

    def delete_task(self):
        """Удаляет выбранную задачу."""
        selection = self.task_list.curselection()
        if not selection:
            return

        index = selection[0]
        self.task_list.delete(index)
        self.tasks.pop(index)


if __name__ == "__main__":
    app = Interface()
    app.root.mainloop()
