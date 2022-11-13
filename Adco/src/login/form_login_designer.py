import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

#Login class named loginForm
class formLoginDesigner:

    def verification(self):
        pass

    def userRegistration(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('200x200')
        self.window.config(bg='#c6c786')
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 800, 500)

        logo = utl.read_image("/home/danielrobl3s/Adco/src/Adcologo.png", (400, 600))
    


        #frame_logo container
        frame_logo = tk.Frame(self.window, bd=0, width=300, relief=tk.SOLID, padx=1, pady=1, bg='black')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo, bg = 'yellow')
        label.place(x=0,y=0,relwidth=1, relheight=1)

        #frame_form container
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg='gray')
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)
        
        #frame_form_top container
        frame_form_top = tk.Frame(frame_form,height = 100, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(fill=tk.X)
        title = tk.Label(frame_form_top, text="Login", font=('Helvetica', 100), fg="black", bg='white', pady=100)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        
        #end frame_form_top container

        #frame form fill container

        frame_form_fill = tk.Frame(frame_form, height = 800, bd=0, relief=tk.SOLID, bg='#c6c786')
        frame_form_fill.pack(side="bottom", expand=tk.YES,fill=tk.BOTH)

        #user field

        etiqueta_usuario = tk.Label(frame_form_fill, text="user", font=('Times', 14), fg="black", bg="#DADCB5", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        #password field

        etiqueta_password = tk.Label(frame_form_fill, text="Password", font=('Times', 14), fg="black",bg="#DADCB5", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        #submit button
        submit = tk.Button(frame_form_fill, text="Login", font=('Times', 14, BOLD), bg='#fff', bd=0, fg="black", command=self.verification)
        submit.pack(fill=tk.X, padx=20, pady=20)
        submit.bind("<Return>", (lambda event: self.verification()))

        #Register user button
        submit = tk.Button(frame_form_fill, text="Register", font=('Times', 14, BOLD), bg='#fff', bd=0, fg="black", command=self.userRegistration)
        submit.pack(fill=tk.X, padx=20, pady=20)
        submit.bind("<Return>", (lambda event: self.userRegistration()))

        #end frame_form_fill container
        self.window.mainloop()