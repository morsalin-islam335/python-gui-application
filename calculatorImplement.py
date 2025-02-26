


# # implement GUI calculator by using tkinter 


# import tkinter as tk 


# expression = ""
# root = None 
# entry = None 


# def getResult():
#     global expression
#     global entry
#     current = entry.get()
#     try:
#         result = eval(current)
#         entry.delete(0, tk.END) # erase all
#         entry.insert(tk.END, result)

#     except Exception as e:
#         entry.delete(0,tk.END)
#         entry.insert(tk.END, "Error")





# def buttonPress(value):
#     global entry, expression
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(value))

#     expression += value
    

# def pressBackspace():
#     global expression, entry
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current[:-1])

#     expression = current[:-1]


# def clearEntry():
#     global entry, expression
#     current = entry.get()
#     entry.delete(0, tk.END),




# def main():
#     global root, entry 

#     ###### create a root widget ######
#     root = tk.Tk()
#     root.title("Calculator using GUI")
#     root.config(bg = "#242c32")
#     root.geometry("600x600")

#     ########## now works with entry ######

#     entry = tk.Entry(root, font= ("Arial", 35,), justify = tk.RIGHT)
#     entry.grid(row = 0, column = 0, columnspan = 5, padx = 30, pady = 20, ipady=20,  sticky = "nsew")
    
#     buttons  = [
#         "√", "^", "(", ")",  "x²",
#         "7", "8", "9", "/", "sin",
#         "4", "5", "6", "*", "cos", 
#         "1", "2", "3", "-", "tan",
#         "0", "00", ".", "+", "sec",
#         "Clear", "Del", "="

#     ]


#     rowVal = 1  # 0 th row works for entry
#     colVal = 0

#     for button in buttons:
#         calculatorCell = tk.Button(
#             root,
#             text=button,
#             bg= "red" if (button == "Clear" or button == "Del") else "#61dafb",
#             fg="black",
#             padx= 10,
#             pady = 20,
#             font = ("Arial", 16)

#         )

        
#         if button != "=":
            
#             calculatorCell.grid(
#                 row = rowVal,
#                 column = colVal,
#                 sticky = "nsew"
#                 )
#         else:
#             calculatorCell.grid(
#             row = rowVal,
#             column = colVal,
#             sticky = "nsew",
#             columnspan=3
#             )





#         colVal += 1

#         if colVal == 5:
#             colVal = 0
#             rowVal += 1

    
#     for i in range(6):
#         root.grid_rowconfigure(i, weight=1)
#         root.grid_columnconfigure(i, weight=1)

      

            

#     root.mainloop()




# if __name__ == "__main__":
#     main()



import tkinter as tk
import math

expression = ""  # Stores the mathematical expression
root = None
entry = None



allowed_functions = {
    "sin": lambda x : math.sin(math.radians(x)),
    "cos": lambda x : math.cos(math.radians(x)),
    "tan": lambda x : math.tan(math.radians(x)),
    "sec": lambda x : 1/math.cos(math.radians(x)), # 1/cos = sec
    "sqrt": lambda x : math.sqrt
}

def getResult():
    global expression, entry
    try:
        # Replace ^ with ** for exponentiation
        # temp_expression = expression.replace("^", "**")

        # Evaluate the expression safely
        # result = eval(expression, {"__builtins__": None}, allowed_functions)
        result = eval(expression, {"__builtins__": None}, allowed_functions)


        entry.delete(0, tk.END)  # Clear entry
        entry.insert(tk.END, result)  # Show result
        expression = str(result)  # Update stored expression
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

def getResult():
    global expression, entry 
    try:
        value = eval(expression, {"__builtins__": None}, allowed_functions)
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)
        expression = str(value)
    except Exception:
        expression = ""
        entry.delete(0, tk.END)
        entry.insert("Error", tk.END)
        
    

def buttonPress(value):
    """Handles button clicks, updates expression & entry field."""
    global expression, entry

    if value == "√":  # Square root
        expression += "sqrt("
        entry.insert(tk.END, "√(")
    elif value == "^":  # Power
        expression += "**"
        entry.insert(tk.END, "^")
    elif value == "x²":  # Square
        expression += "**2"
        entry.insert(tk.END, "²")
    elif value in ["sin", "cos", "tan", "sec"]:  # Trigonometry
        expression += f"{value}("
        entry.insert(tk.END, f"{value}(")
    else:  # Regular numbers and operators
        expression += value
        entry.insert(tk.END, value)

def pressBackspace():
    """Deletes the last character from expression & entry field."""
    global expression, entry
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clearEntry():
    """Clears the entire expression & entry field."""
    global expression, entry
    expression = ""
    entry.delete(0, tk.END)

def main():
    global root, entry

    root = tk.Tk()
    root.title("Calculator using GUI")
    root.config(bg="#242c32")
    root.geometry("600x600")

    # Entry field (User input display)
    entry = tk.Entry(root, font=("Arial", 35), justify=tk.RIGHT)
    entry.grid(row=0, column=0, columnspan=5, padx=30, pady=20, ipady=20, sticky="nsew")

    buttons = [
        "√", "^", "(", ")", "x²",
        "7", "8", "9", "/", "sin",
        "4", "5", "6", "*", "cos",
        "1", "2", "3", "-", "tan",
        "0", "00", ".", "+", "sec",
        "Clear", "Del", "="
    ]

    rowVal = 1  # First row is for the entry
    colVal = 0

    for button in buttons:
        def clickHandler(b=button):
            if b == "=":
                getResult()
            elif b == "Clear":
                clearEntry()
            elif b == "Del":
                pressBackspace()
            else:
                buttonPress(b)

        calculatorCell = tk.Button(
            root,
            text=button,
            bg="red" if button in ["Clear", "Del"] else "#61dafb",
            fg="black",
            padx=10,
            pady=20,
            font=("Arial", 16),
            command=clickHandler
        )

        if button != "=":
            calculatorCell.grid(row=rowVal, column=colVal, sticky="nsew")
        else:
            calculatorCell.grid(row=rowVal, column=colVal, sticky="nsew", columnspan=3)

        colVal += 1
        if colVal == 5:
            colVal = 0
            rowVal += 1

    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
