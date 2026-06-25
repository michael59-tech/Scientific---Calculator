import tkinter as tk
from tkinter import messagebox
import math
import statistics

# =========================
# Calculator Functions
# =========================

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Expression")

# =========================
# Scientific Functions
# =========================

def scientific(func):
    try:
        value = float(entry.get())

        if func == "sin":
            result = math.sin(math.radians(value))

        elif func == "cos":
            result = math.cos(math.radians(value))

        elif func == "tan":
            result = math.tan(math.radians(value))

        elif func == "sinh":
            result = math.sinh(value)

        elif func == "cosh":
            result = math.cosh(value)

        elif func == "tanh":
            result = math.tanh(value)

        elif func == "sqrt":
            result = math.sqrt(value)

        elif func == "log":
            result = math.log10(value)

        elif func == "ln":
            result = math.log(value)

        elif func == "fact":
            result = math.factorial(int(value))

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        messagebox.showerror("Error", "Invalid Input")

# =========================
# Permutation & Combination
# =========================

def permutation():
    try:
        values = entry.get().split(",")

        n = int(values[0])
        r = int(values[1])

        result = math.perm(n, r)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        messagebox.showerror(
            "Error",
            "Enter values like: n,r"
        )

def combination():
    try:
        values = entry.get().split(",")

        n = int(values[0])
        r = int(values[1])

        result = math.comb(n, r)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        messagebox.showerror(
            "Error",
            "Enter values like: n,r"
        )

# =========================
# Statistics Functions
# =========================

def stats(operation):
    try:
        numbers = list(map(float, entry.get().split(",")))

        if operation == "mean":
            result = statistics.mean(numbers)

        elif operation == "median":
            result = statistics.median(numbers)

        elif operation == "stdev":
            result = statistics.stdev(numbers)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        messagebox.showerror(
            "Error",
            "Enter numbers separated by commas"
        )

# =========================
# GUI Setup
# =========================

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.configure(bg="lightblue")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15, pady=10)

# =========================
# Button Layout
# =========================

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('C',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('(',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), (')',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:

    if text == "=":
        btn = tk.Button(root, text=text, width=8, height=2,
                        command=calculate)

    elif text == "C":
        btn = tk.Button(root, text=text, width=8, height=2,
                        command=clear)

    else:
        btn = tk.Button(root, text=text, width=8, height=2,
                        command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# =========================
# Scientific Buttons
# =========================

scientific_buttons = [
    ("sin",5,0), ("cos",5,1), ("tan",5,2),
    ("sinh",5,3), ("cosh",5,4),
    ("tanh",6,0), ("sqrt",6,1), ("log",6,2),
    ("ln",6,3), ("fact",6,4),
]

for (text, row, col) in scientific_buttons:
    btn = tk.Button(
        root,
        text=text,
        width=8,
        height=2,
        command=lambda t=text: scientific(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# =========================
# Extra Feature Buttons
# =========================

tk.Button(root, text="nPr", width=8, height=2,
          command=permutation).grid(row=7, column=0)

tk.Button(root, text="nCr", width=8, height=2,
          command=combination).grid(row=7, column=1)

tk.Button(root, text="Mean", width=8, height=2,
          command=lambda: stats("mean")).grid(row=7, column=2)

tk.Button(root, text="Median", width=8, height=2,
          command=lambda: stats("median")).grid(row=7, column=3)

tk.Button(root, text="Std Dev", width=8, height=2,
          command=lambda: stats("stdev")).grid(row=7, column=4)

# =========================
# Run Application
# =========================

root.mainloop()
