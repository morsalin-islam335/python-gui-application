


# implement GUI calculator by using tkinter 


import tkinter as tk 


expression = ""
root = None 
entry = None 


def getResult():
    global expression
    global entry
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END) # erase all
        entry.insert(tk.END, result)

    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END, "Error")





def buttonPress(value):
    pass 

def pressBackspace():
    pass 


def main():
    global root, entry 

    ###### create a root widget ######
    root = tk.Tk()
    root.title("Calculator using GUI")
    root.config(bg = "#242c32")
    root.geometry("600x600")

    ########## now works with entry ######

    entry = tk.Entry(root, font= ("Arial", 35,), justify = tk.RIGHT)
    entry.grid(row = 0, column = 0, columnspan = 5, padx = 30, pady = 20, ipady=20,  sticky = "nsew")
    
    buttons  = [
        "√", "^", "(", ")",  "x²",
        "7", "8", "9", "/", "sin",
        "4", "5", "6", "*", "cos", 
        "1", "2", "3", "-", "tan",
        "0", "00", ".", "+", "sec",
        "Clear", "Del", "="

    ]


    rowVal = 1  # 0 th row works for entry
    colVal = 0

    for button in buttons:
        calculatorCell = tk.Button(
            root,
            text=button,
            bg= "red" if (button == "Clear" or button == "Del") else "#61dafb",
            fg="black",
            padx= 10,
            pady = 20,
            font = ("Arial", 16)

        )

        
        if button != "=":
            
            calculatorCell.grid(
                row = rowVal,
                column = colVal,
                sticky = "nsew"
                )
        else:
            calculatorCell.grid(
            row = rowVal,
            column = colVal,
            sticky = "nsew",
            columnspan=3
            )





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

