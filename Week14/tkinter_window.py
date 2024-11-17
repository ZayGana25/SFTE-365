# import tkinter
# window = tkinter.Tk()

# window.mainloop()




#2. import tkinter as tk

# class App(tk.Tk):
#    def __init__(self):
#       super().__init__()
        
# def main():
#     app = App()
#     app.mainloop()
    
# if __name__=="__main__":
#     main()



# from tkinter.simpledialog import askinteger
# from tkinter import *
# from tkinter import messagebox

# def show():
#    num = askinteger("Input", "Input an Integer")
#    print(num)
   
# def main():
#     app = Tk()
#     app.geometry("100x100")   

#     B = Button(app, text ="Click", command = show)
#     B.place(x=50,y=50)

#     app.mainloop()
    
# if __name__=="__main__":
#      main()

from tkinter.simpledialog import askstring
from tkinter import *
  
def show():
   name = askstring("Input", "Enter your name")
   print(name)   
   
def exit_window(window):
    window.destroy()
   
def main():
    window = Tk()
    window.geometry("300x300")
    window.title("This is My Window")
    B = Button(window, text ="EXIT!", command = lambda: exit_window(window))
    B.place(x=50,y=50)
    window.mainloop()
    
if __name__=="__main__":
      main()