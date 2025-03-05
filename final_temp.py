import tkinter as tk

def convert(event):
    
    num = int(number.get())

    if con_var.get() == 1:
        result = round((num - 32) * (5/9), 2)
        result_l.config(text = f"{num}°C is equal to {result}°F")
    
    elif con_var.get() == 2:
        result = round(num * (9/5) + 32, 2)
        result_l.config(text = f"{num}°F is equal to {result}°C")

    else:
        result_l.config(text = "Please try again.")

root = tk.Tk()
root.title("Temperature Converter")

con_var = tk.IntVar(value = 1)

title = tk.Label(root, text = "Temperature\nConverter")
title.grid(row = 0, column = 0)

number = tk.Entry(root)
number.grid(row = 1, column = 0)

f_to_c = tk.Radiobutton(root, text = "F to C", variable = con_var, value = 1)
f_to_c.grid(row = 2, column = 0)

c_to_f = tk.Radiobutton(root, text = "C to F",  variable = con_var, value = 2)
c_to_f.grid(row = 2, column = 1)

convert_b = tk.Button(root, text = "Convert", command = convert)
convert_b.grid(row = 3, column = 0)

result_l = tk.Label(root, text = "")
result_l.grid(row = 4, column = 0)

root.bind("<Return>", convert)

root.mainloop()