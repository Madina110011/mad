import tkinter as tk
def button_click():
    entered_text = entry.get()
    label_output.config(text="Привет, " + entered_text)

root = tk.Tk()
root.title("Пример приложения Tkinter")

label = tk.Label(root, text="Введите ваше имя:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Поздороваться", command=button_click)
button.pack()

label_output = tk.Label(root, text="")
label_output.pack()

root.mainloop()