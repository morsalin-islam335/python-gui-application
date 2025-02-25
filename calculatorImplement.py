
import tkinter as tk




def main():
   root = tk.Tk()
   root.title("Calculator using GUI")
   root.config(bg="#242c32")

   entry = tk.Entry(root, font=("Arial", 40), bd=10, justify=tk.RIGHT)

   entry.grid(row = 0, column = 0, columnspan = 4, padx = 40, pady = 40, sticky = "nsew")

   buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
   
   row_val = 1
   col_val = 0

   for button in buttons:
       pass 
   

   tk.Button(
       root,
       text = "Clear",
       padx =10,
       bg="red",
       fg = "black",
       row = row_val,

       column = col_val
   )

   root.mainloop()




if __name__ == "__main__":
    main()
