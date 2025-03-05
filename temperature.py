import tkinter as tk
from tkinter import ttk

def convert():

    result_l.config(text = f"{number.get()}")

root = tk.Tk()
con_var = tk.IntVar()

title = ttk.Label(root, text = "Temperature Converter")
title.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

number = ttk.Entry(root)
number.grid(row = 1, column = 0, columnspan = 2)

c_to_f_rb = ttk.Radiobutton(root, text = "C to F", variable = con_var, value = 1)
c_to_f_rb.grid(row = 2, column = 0)

f_to_c_rb = ttk.Radiobutton(root, text = "F to C", variable = con_var, value = 2)
f_to_c_rb.grid(row = 2, column = 1)

convert_b = ttk.Button(root, text = "Convert", command = convert)
convert_b.grid(row = 3, column = 0, columnspan = 2)

result_l = ttk.Label(root, text = "")
result_l.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()