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

import tkinter as tk
import  math 

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

    allowedFunctins = {
        "sin": lambda x : math.sin(math.radians(x)),
        "cos": lambda x : math.cos(math.radians(x)),
        "tan": lambda x : math.tan(math.radians(x)),
        "sqrt": lambda x: math.sqrt(x)
    }

    def handelKeyboardPress(self, event):
        key = event.char
        if key  in ['.', '+', '-', '*', '/', '^', '(', ')'] or key.isdigit():
            self.buttonPress(key)

        elif key == "=":
            self.getResult()
        elif key == "\r":
            self.getResult()
        elif key == "\x08":
            self.pressBackspace()


    def pressBackspace(self):
        self.expression = self.expression[:-1]
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])
    

    
    def pressClear(self):
        self.entry.delete(0, tk.END)
        self.expression = ""


    def getResult(self):
        try:
            result = eval(self.expression,{"__builtins__": None}, self.allowedFunctins)

            if isinstance(result, float) and result.is_integer():
                result = int(result)
            resultString = str(result)

            if isinstance(result, float):
                resultString = f"{result:.2f}".strip("0").strip(".")

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END,resultString)
            self.expression = resultString

        except Exception:
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error!")


    def buttonPress(self, button):
        if button == "√":
            self.entry.insert(tk.END, "√(")
            self.expression += "√("
        elif button == "^":
            self.entry.insert(tk.END, "^")
            self.expression += "**"
        
        elif button == "x²":
            self.entry.insert(tk.END,"²")
            self.expression += "**2"
        
        elif button in ["sin","cos", "tan"]:
            self.entry.insert(tk.END, f"{button}(")
            self.expression += f"{button}("
        else:
            self.entry.insert(tk.END, button)
            self.expression += button
            





    def main(self):
        self.root = tk.Tk()
        self.root.title("Calculator Using GUI")
        self.root.config(bg="#242c32")
        self.root.geometry("600x600")


        self.entry = tk.Entry(self.root, bd=10, font = ("Arial", 35), bg="#34495E", fg="white", justify = tk.RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10, sticky = "nsew")


        #TODO make all button and perform their  operation

        rowCont = 1
        colCnt = 0
        for button in self.buttons:
            def handleClick(b = button): # closer function
                if b == "Clear":
                    self.pressClear
                elif b == "=":
                    self.getResult()
                
                elif b == "Del":
                    self.pressBackspace()
                else:
                    self.buttonPress(b)

            cell = tk.Button(self.root, font= ("Arial", 16), text = button, command = handleClick, padx = 10, pady = 10, bg = "tomato" if button == "Del" else "red" if button == "Clear" else "lightblue")


            cell.grid(row = rowCont, column = colCnt, sticky = "nsew", columnspan = 3 if button == "=" else 1)

            
            colCnt += 1

            if colCnt == 5:
                colCnt = 0
                rowCont += 1
            

        for i in range(7):
            self.root.rowconfigure(i, weight = 1)
            self.root.columnconfigure(i, weight = 1)


            

        # todo perform keyboard press

        self.root.bind("<KeyPress>", self.handelKeyboardPress)

        self.root.mainloop()





if __name__ == "__main__":
    object = Calculator()
    object.main()
