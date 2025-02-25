


# implement GUI calculator by using tkinter 


import tkinter as tk 


expression = ""
root = None 
entry = None 


def getResult():
    pass 


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
    entry.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20, sticky = "nsew")
    

    root.mainloop()




if __name__ == "__main__":
    main()

