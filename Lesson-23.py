import tkinter as tk
from tkinter import ttk

# Функция, вызываемая при выборе элемента из списка
def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text=selected_item)

# Создание главного окна
root = tk.Tk()
root.title("Пример интерфейса с Tkinter")

# Фрейм для списка элементов
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=10, pady=10)

# Создание списка элементов
listbox = tk.Listbox(frame1)
listbox.pack()

# Добавление элементов в список
for item in ["Элемент 1", "Элемент 2", "Элемент 3"]:
    listbox.insert(tk.END, item)

# Привязка функции к событию выбора элемента
listbox.bind("<<ListboxSelect>>", on_select)

# Фрейм для выпадающего списка
frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, padx=10, pady=10)

# Метка для отображения выбранного элемента из списка
label = tk.Label(frame2, text="", font=("Arial", 14))
label.pack()

# Создание выпадающего списка
options = ["Вариант 1", "Вариант 2", "Вариант 3"]
combo = ttk.Combobox(frame2, values=options)
combo.pack()

# Размещение компонентов и запуск главного цикла
root.mainloop()