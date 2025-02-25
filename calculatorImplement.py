
import tkinter as tk




def main():

    root = tk.Tk()
    root.title("Calculator using Tkinter")
    root.geometry("400x500")
    root.config(bg="#282c35")

    # make an entry
    
    entry = tk.Entry(root,font=("Arial", 40),bd=10, justify=tk.RIGHT)
    


    # now make grid for that entry
    entry.grid(row = 0, column = 0)



    root.mainloop()




if __name__ == "__main__":
    main()
