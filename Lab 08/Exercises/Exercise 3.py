import tkinter as tk
from math import factorial


def calculate_factorial():
    try:
        n = int(entry_n.get())
        result = factorial(n)
        label_result.config(text=f"Factorial is -> {result}")
    except ValueError:
        label_result.config(text="n is invalid")


def calculate_power():
    try:
        n = int(entry_n.get())
        m = int(entry_m.get())
        result = n ** m
        label_result.config(text=f"{n} to power {m} is -> {result}")
    except ValueError:
        label_result.config(text="n or m is invalid")


root = tk.Tk()
root.title("Math Operations")
root.geometry("400x210")

entry_n = tk.Entry(root)
entry_n.pack(pady=10)
entry_n.insert(0, "Enter n")

entry_m = tk.Entry(root)
entry_m.pack(pady=10)
entry_m.insert(0, "Enter m")

btn_factorial = tk.Button(root, text="Calculate n!", command=calculate_factorial)
btn_factorial.pack(pady=5)

btn_power = tk.Button(root, text="Calculate n^m", command=calculate_power)
btn_power.pack(pady=5)

label_result = tk.Label(root, text="Result will be shown here")
label_result.pack(pady=20)

root.mainloop()
