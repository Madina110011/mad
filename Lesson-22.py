import tkinter as tk 
root=tk.Tk()
root.title()
label=tk.Label(root,text="Главное меню",font=("Arial", 18), fg="blue", bg="yellow")
label.pack()
def button_click():
    label.config(text="Операция") 
button=tk.Button(root,text="Кнопка 1", command=button_click)
button.pack()
root.mainloop()