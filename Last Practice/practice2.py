"""
root bg = "#242c32"
entryBg= "#34495E"
entryfg = "white"
button = "lightblue, tomato, red"

'.', '+', '-', '*', '/', '^', '(', ')'

     self.buttons = [
        '√', '^', '(', ')', 'x²',
        '7', '8', '9', '/', 'sin',
        '4', '5', '6', '*', 'cos',
        '1', '2', '3', '-', 'tan',
        '0', '00', '.', '+', 'MOD',
         "Clear", "Del", "="
        ]
\x08" => backspace
\r =>   enter


"""


import math
import tkinter as tk
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
       "sin" : lambda x: math.sin(math.radians(x)),
       "cos": lambda x : math.cos(math.radians(x)),
       "tan": lambda x : math.tan(math.radians(x)),
       "sqrt": lambda x: math.sqrt(x)

    }



    def pressBackspace(self):
        self.expression = self.expression[:-1]
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])


    def pressClear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)
        



    def getResult(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, self.allowedFunctions)

            if isinstance(result, float) and result.is_integer():
                result = str(result)
            resultString = str(result)
            if isinstance(result, float):
                resultString = f"{result:.2f}".strip("0").strip(".")
            

            self.expression = resultString
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, resultString)



        except Exception:
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.entry.inser(tk.END, "Error!")




    def buttonPress(self, button):
        if button == "√":
            self.expression += f"sqrt("
            self.entry.insert(tk.END, "√(")
        
        elif button == "^":
            self.expression += "**"
            self.entry.insert(tk.END, "^")

        elif button in ["sin", "cos", "tan"]:
            self.expression += f"{button}("
            self.entry.insert(tk.END, f"{button}(")

        elif button == "x²":
            self.expression += "**2"
            self.entry.insert(tk.END, "²")
        
        else:
            self.expression += button
            self.entry.insert(tk.END, button)

            

    def handleKeyBordPress(self,event):
        key = event.char
        if key == "\r" or key == "=":
            self.getResult()
        elif key == "\x08":
            self.pressBackspace()
        
        elif key in ['.', '+', '-', '*', '/', '^', '(', ')'] or key.isdigit():
            self.buttonPress(key)






    def main(self):
        self.root = tk.Tk()
        self.root.config(bg="#242c32")
        self.root.geometry("600x600")
        self.root.title("Calculator using tkinter")


        self.entry = tk.Entry(self.root, bd = 10, justify = tk.RIGHT, font = ("Arial", 35), bg="#34495E", fg="white")
        self.entry.grid(row =  0, column = 0, columnspan = 5, sticky = "nsew", padx=10, pady=10)

        colCnt = 0
        rowCnt = 1

        for button in self.buttons:
            def handleClick(b = button): # closour function
                if  b == "=":
                    self.getResult()
                elif b == "Del":
                    self.pressBackspace()
                elif b == "Clear":
                    self.pressClear()
                
                else:
                    self.buttonPress(b)


            cell = tk.Button(self.root, command=handleClick, font= ("Arial", 16), text = button, bg = "red" if button == "Clear" else "tomato" if button == "Del" else "lightblue")

            cell.grid(row = rowCnt, column = colCnt, columnspan = 3 if button == "=" else 1, sticky = "nsew", padx = 10, pady = 10)

            colCnt += 1
            if colCnt == 5:
                colCnt = 0
                rowCnt += 1



        for i in range(7):
            self.root.rowconfigure(i, weight = 1)
            self.root.columnconfigure(i, weight = 1)






        


        self.root.bind("<KeyPress>", self.handleKeyBordPress)


        self.root.mainloop()



if __name__ == "__main__":
    object = Calculator()
    object.main()
