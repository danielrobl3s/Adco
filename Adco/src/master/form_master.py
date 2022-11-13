import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

#Master panel class
class masterpanel():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Login')
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("300x300")
        self.window.config(bg='red')
        self.window.resizable(width=0, height=0)
        logo = utl.read_image("/home/danielrobl3s/Adco/src/Adcologo.png", (200, 200)) 
        label = tk.Label(self.window, image=logo, bg='red')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        self.window.mainloop()