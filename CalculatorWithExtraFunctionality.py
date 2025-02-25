import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate():
    try:
        expression = entry.get()
        # Replace function names with math module equivalents
        expression = expression.replace("^", "**")  # Replace ^ with ** for power
        expression = expression.replace("√", "math.sqrt")  # Handle square root
        # Evaluate the expression using eval with math functions
        result = eval(expression, {"math": math, "__builtins__": None})  
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="#282c35")  

entry = tk.Entry(root, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=20, sticky="nsew")

# Buttons
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'sec',
    '√', '^', '(', ')', 'x²'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, padx=20, pady=20, font=('Arial', 16),
        command=lambda b=button: button_click(
            b if b not in ['sin', 'cos', 'tan', 'sec', 'x²', '√', '^'] else
            f"math.{b}(" if b in ['sin', 'cos', 'tan'] else
            "1/math.cos(" if b == 'sec' else
            "**2" if b == 'x²' else
            "math.sqrt(" if b == '√' else
            "^"
        ) if b != '=' else evaluate(),
        bg="#61dafb", fg="#282c35"
    ).grid(row=row_val, column=col_val, sticky="nsew")
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Extra function buttons
tk.Button(
    root, text='C', padx=20, pady=20, font=('Arial', 16),
    command=clear_entry, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")
col_val += 1

tk.Button(
    root, text='Del', padx=20, pady=20, font=('Arial', 16),
    command=backspace, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")

# Configure grid for resizing
for i in range(0, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Main loop
root.mainloop()
