'''import tkinter as tk

window = tk.Tk()
window.title("Tkinter")
label=tk.Label(window, text="Привет,Tkinter!")
label.pack()
window.mainloop()'''

import tkinter as tk
window = tk.Tk()
window.title("Анкета о себе")
label = tk.Label(window, text="Анкета о себе")
label.pack()
question1 = tk.Label(window, text="Ваше имя:")
question1.pack()

question2 = tk.Label(window, text="Ваш возраст:")
question2.pack()

question3 = tk.Label(window, text="Ваш любимый цвет:")
question3.pack()
window.mainloop()