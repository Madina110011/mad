'''import tkinter as tk
root= tk.Tk()
label = tk.Label(root, text="Hello, world!")
label.pack()

button = tk.Button(root, text="Изменить текст", command=lambda: change_text())
button.pack()

def change_text():
    label.config(text="Goodbye, world!")

root.mainloop()'''

import tkinter as tk

def clear_text():
    text.delete(1.0, "end")

def handle_enter(event):
    if event.keysym == "Return":
        clear_text()

root = tk.Tk()
root.title("Clear Text Example")

text = tk.Text(root, height=5, width=30)
text.pack()

clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

entry = tk.Entry(root, width=30)
entry.pack()

entry.bind("KeyPress", handle_enter)

root.mainloop()