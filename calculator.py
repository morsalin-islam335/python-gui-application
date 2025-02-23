from tkinter import Tk, StringVar, Toplevel, Frame, Label, Button, Entry, Text,Listbox,Grid, Menu, Menubutton
expression =  ""
equation = None 

def press(num):
    global expression
    global equation

    expression = expression + str(num)
    equation.set(expression)


    

def equalPress():
    try:
        global expression, equation 
        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("error")
        expression = ""

def clearPress():
    global  expression, equation 
    expression = ''
    equation.set("")
    



def main():

    global equation
    
    gui = Tk()# create a gui
    gui.configure(background="light green")
    gui.title("Calculator Using Tkniter By Morsalin Islam")
    gui.geometry("270x160")
    equation = StringVar()
    
    expression_field = Entry(gui, textvariable= equation)
    expression_field.grid(columnspan=4, ipadx=70)

    button1 = Button(gui, text= "1", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(1))
    button1.grid(row = 2, column= 0)

    button2 = Button(gui, text= "2", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(2))
    button2.grid(row = 2, column= 1)

    button3 = Button(gui, text= "3", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(3))
    button3.grid(row = 2, column= 2)

    
    ## 4-6 number button
    button4 = Button(gui, text= "4", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(4))
    button4.grid(row = 3, column= 0)

    button5 = Button(gui, text= "5", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(5))
    button5.grid(row = 3, column= 1)

    button6 = Button(gui, text= "6", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(6))
    button6.grid(row = 3, column= 2)


    button7 = Button(gui, text= "7", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(7))
    button7.grid(row = 4, column= 0)

    button8 = Button(gui, text= "8", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(8))
    button8.grid(row = 4, column= 1)

    button9 = Button(gui, text= "9", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(9))
    button9.grid(row = 4, column= 2)

    button0 = Button(gui, text= "0", fg="black", bg="red", height= 1 , width= 7,
                     command = lambda: press(0))
    button0.grid(row = 5, column= 0)

    plus = Button(gui, text = " + ", fg = "black", bg= "red", command = lambda: press("+"), height = 1, width = 7)
    plus.grid(row = 2 , column = 3)
    
    minus = Button(gui, text = " - ", height = 1, width = 7, command = lambda: press("-"))
    minus.grid(row = 3, column = 3)


    multiply = Button(gui , text = "*", width = 7, height = 1, bg= "red", fg= "black", command = lambda: press("/"))
    multiply.grid(row = 4, column = 3)


    divide = Button(gui, text = " / ", bg= "red", fg = "black", width = 7, height = 1, command = lambda : press("/"))
    divide.grid(row = 5, column = 3)

    equal = Button(gui, text = " = ", bg= "red", fg = "black", width = 7, height = 1, command = equalPress)
    equal.grid(row = 5, column = 2)

    clear = Button(gui, text = "Clear", bg= "red", fg = "black", width = 7, height = 1, command = clearPress)
    clear.grid(row = 5, column = 1)

    decemal = Button(gui, text = " . ", bg= "red", fg = "black", width = 7, height = 1, command = lambda : press("."))
    decemal.grid(row = 6, column = 0)


    



    gui.mainloop() # it start gui

    


if __name__ == "__main__":
    main()
