


CALCULATOR PROJECT



import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(num)))
    except:
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num ** 2))
    except:
        entry.insert(0, "Error")

def cube():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num ** 3))
    except:
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('%',4,1), ('+',4,2), ('=',4,3),
]

# Create number and operator buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2,
                  command=lambda t=text: click(t)).grid(row=row, column=col)

# Extra function buttons
tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=0)
tk.Button(root, text="√", width=5, height=2, command=sqrt).grid(row=5, column=1)
tk.Button(root, text="x²", width=5, height=2, command=square).grid(row=5, column=2)
tk.Button(root, text="x³", width=5, height=2, command=cube).grid(row=5, column=3)

# Run app
root.mainloop()






