
import tkinter as tk
import math 


class Calculator:
    buttons = [
        '√', '^', '(', ')', 'x²',
        '7', '8', '9', '/', 'sin',
        '4', '5', '6', '*', 'cos',
        '1', '2', '3', '-', 'tan',
        '0', '00', '.', '+', 'MOD',
         "Clear", "Del", "="
        ]
    expression = ""
    allowedFunctions = {
        "sin" : lambda x : math.sin(math.radians(x)),
        "cos": lambda x : math.cos(math.radians(x)),
        "tan": lambda x : math.tan(math.radians(x)),
        "sqrt": lambda x: math.sqrt(x)

    }

    def getResult(self):
        try:
            result = eval(self.expression,{"__builtins__":None},self.allowedFunctions)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            resultExpression = str(result)
            if isinstance(result, float):
                resultExpression = f"{result:.2f}".rstrip("0").rstrip(".")
            self.expression = resultExpression
            self.entry.delete(0, tk.END)

            self.entry.insert(tk.END, resultExpression)



        except Exception:
            self.expression = "" 
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error!")


    def pressBackspace(self):
        current = self.entry.get()
        self.expression = self.expression[:-1] # remove last char
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])


    def pressButton(self, button):
        if button in ["sin", "cos", "tan"]:
            self.entry.insert(tk.END,f"{button}(")
            self.expression += f"{button}("
        elif button == "MOD":
            self.entry.insert(tk.END,"%")
            self.expression += "%"
        elif button == "√":
            self.expression += "sqrt("
            self.entry.insert(tk.END, "√(")
        elif button == "x²":
            self.expression += "**2"
            self.entry.insert(tk.END, "²")
        
        elif button == "^":
            self.expression += "**"
            self.entry.insert(tk.END, "^")
        
        else:
            self.expression += button 
            self.entry.insert(tk.END, button)





    def pressClear(self):
        self.entry.delete(0, tk.END) 
        self.expression = ""


   
    def handleKeyboardPress(self, event):
        key = event.char
        if key in  ['.', '+', '-', '*', '/', '^', '(', ')'] or key.isdigit():
            self.pressButton(key)
        elif key == "\r":
            self.getResult()
        elif key == "\x08":
            self.pressBackspace()


    
    def main(self):
        self.root = tk.Tk()
        self.root.title("GUI Calculator Using Tkinter")
        self.root.config(bg= "#242c32")


        self.entry = tk.Entry(self.root, bg="#34495E", fg= "white", bd = 10, justify = tk.RIGHT, font = ("Arial", 35))
        self.entry.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 20, sticky = "nsew")

        ### now make button grid


        rowCnt = 1
        colCnt = 0

        for button in self.buttons:
            # make closer function
            def handleClick( b = button):
                if b == "Clear":
                    self.pressClear()
                elif b == "Del":
                    self.pressBackspace()
                elif b == "=":
                    self.getResult()
                else:
                    self.pressButton(b)



            cell = tk.Button(self.root,font = ("Arial", 16), text = button, fg = "black", bg="red" if button == "Clear" else "tomato" if button == "Del" else "lightblue", command = handleClick)



            cell.grid(row = rowCnt, column = colCnt, padx = 10, pady=10, sticky = "nsew", columnspan= 3 if button == "=" else 1)

            colCnt += 1
            if colCnt == 5:
                colCnt = 0
                rowCnt += 1

        for i in range(7):
            self.root.columnconfigure(i, weight = 1)
            self.root.rowconfigure(i, weight = 1)

        
        # TODO make handle keyboard click

        self.root.bind("<KeyPress>", self.handleKeyboardPress)
        


        self.root.mainloop()



            







if __name__ == "__main__":
    object = Calculator()
    object.main()
