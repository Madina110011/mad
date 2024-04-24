import tkinter as tk

def on_check():
if var1.get() == 1:
print("Checkbox 1 is checked")
else:
print("Checkbox 1 is unchecked")
if var2.get() == 1:
print("Checkbox 2 is checked")
else:
print("Checkbox 2 is unchecked")

root = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()

checkbox1 = tk.Checkbutton(root, text="Checkbox 1", variable=var1)
checkbox1.pack()

checkbox2 = tk.Checkbutton(root, text="Checkbox 2", variable=var2)
checkbox2.pack()

check_button = tk.Button(root, text="Check", command=on_check)
check_button.pack()

root.mainloop()