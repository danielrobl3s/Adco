import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from master.form_master import masterpanel
from login.form_login_designer import formLoginDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
import util.encoding_decoding as end_dec

#Login class named App
class formLogin(formLoginDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def verification(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)

    def isUser(self, user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe, por favor registrese", title="Error"
            )
        return status

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.window.destroy()
            masterpanel()
        else:
            messagebox.showerror(message="Contraseña invalida", title="Error")

    