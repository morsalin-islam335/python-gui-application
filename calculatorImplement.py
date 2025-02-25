
import tkinter as tk




def main():
   root = tk.Tk()
   root.title("Calculator using GUI")
   root.config(bg="#242c32")

   entry = tk.Entry(root, font=("Arial", 40), bd=10, justify=tk.RIGHT)

   entry.grid(row = 0, column = 0, columnspan = 4, padx = 40, pady = 40, sticky = "nsew")

   buttons = [
       
   ]


   root.mainloop()




if __name__ == "__main__":
    main()
