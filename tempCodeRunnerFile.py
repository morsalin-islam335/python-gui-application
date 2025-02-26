
# import math
# import tkinter as tk

# class Calculator:
#     allowedFunction = {
#         "sin": lambda x: math.sin(math.radians(x)),
#         "cos": lambda x: math.cos(math.radians(x)),
#         "tan": lambda x: math.tan(math.radians(x)),
#         "sec": lambda x: 1 / math.cos(math.radians(x)),
#         "sqrt": lambda x: math.sqrt(x)
#     }

    
#     expression = ""

#     def pressBackspace(self):
#         self.expression = self.expression[:-1]  # remove last char
#         current = self.entry.get()
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, current[:-1])

#     def calculation(self):
#         try:
#             result = eval(self.expression, {"__builtins__": None}, self.allowedFunction)
#             self.entry.delete(0, tk.END)
#             self.entry.insert(tk.END, str(result))
#             self.expression = str(result)
#         except Exception:
#             self.entry.delete(0, tk.END)
#             self.entry.insert(tk.END, "Error")
#             self.expression = ""

#     def clear(self):
#         self.expression = ""
#         self.entry.delete(0, tk.END)

#     def handleClick(self, button):
#         if button in ["sin", "cos", "tan", "sec"]:
#             self.expression += f"{button}("
#             self.entry.insert(tk.END, f"{button}(")  # Fix: Insert only function, not full expression
#         elif button == "√":
#             self.expression += "sqrt("
#             self.entry.insert(tk.END, "√(")
#         elif button == "^":
#             self.expression += "**"
#             self.entry.insert(tk.END, "^")
#         elif button == "x²":
#             self.expression += "**2"
#             self.entry.insert(tk.END, "²")
#         else:
#             self.expression += button
#             self.entry.insert(tk.END, button)

#     def main(self):
#         self.root = tk.Tk()
#         self.entry = tk.Entry(self.root, font=("Arial", 35), bd=10, justify=tk.RIGHT, bg="#444")
#         self.entry.grid(column=0, row=0, columnspan=5, sticky="nsew", padx=20, pady=20)
#         self.root.title("Calculator using Tkinter")
#         self.root.config(bg="#242c32")
#         self.root.geometry("600x600")

        

#         self.buttons = [
#             '√', '^', '(', ')', 'x²',
#             '7', '8', '9', '/', 'sin',
#             '4', '5', '6', '*', 'cos',
#             '1', '2', '3', '-', 'tan',
#             '0', '00', '.', '+', '%',
#             "Clear", "Del", "="
#         ]

#         rowCnt, colCnt = 1, 0
#         for button in self.buttons:
#             def handleClickCell(b=button):
#                 if b == "Clear":
#                     self.clear()
#                 elif b == "Del":
#                     self.pressBackspace()
#                 elif b == "=":
#                     self.calculation()
#                 else:
#                     self.handleClick(b)

#             calculatorCell = tk.Button(
#                 self.root,
#                 command=handleClickCell,
#                 padx=20, pady=20,
#                 font=("Arial", 16),
#                 text=button,
#                 bg="#61dafb" if button not in ["Clear", "Del"] else "red",
#                 fg="black"
#             )

#             columnSpan = 3 if button == "=" else 1
#             calculatorCell.grid(row=rowCnt, column=colCnt, sticky="nsew", columnspan=columnSpan)

#             colCnt += 1
#             if colCnt == 5:
#                 colCnt = 0
#                 rowCnt += 1

#         for i in range(6):
#             self.root.rowconfigure(i, weight=1)
#             self.root.columnconfigure(i, weight=1)

#         self.root.mainloop()

# myCalculator = Calculator()

# if __name__ == "__main__":
#     myCalculator.main()
