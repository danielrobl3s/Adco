#Import corresponding libraries
from matplotlib import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#We declare a connection function with sqlite3 managable with DBbrowser
def connectionDB():
    myconnection=sqlite3.connect("db")
    mycursor=myconnection.cursor()

    #variables
    myId=StringVar()
    myName=StringVar()
    myAge=StringVar()
    myPosition=StringVar()
    myPhone=StringVar()

    try:
        mycursor.execute("""
        CREATE TABLE users IF NOT EXISTS (id_user INTEGER PRIMARY KEY AUTOINCREMENT
        nombre VARCHAR(50)
        edad INTEGER(2)
        posicion VARCHAR(50)
        telefono INTEGER(10))
        """)
        messagebox.showinfo("CONEXION","Base de datos creada exitosamente","tablas creadas exitosamente")
    except Exception as e:
        print(e)

def exitApp():
    valor=messagebox.askquestion("Salir","¿estas seguro que deseas salir?")
    if valor == "yes":
        root.destroy()

def clearFields(): 
    myId.set("")
    myName.set("")
    myAge.set("")
    myPosition.set("")
    myPhone.set("")

def message():
    about="""
    Adco App
    version Alpha 1.0
    Tecnologia Python
    """

#CRUD methods
def show():
    myConnection=sqlite3.connect("db")
    myCursor=myConnection.cursor()
    rows=tree.get_children()
    for element in rows:
        tree.delete(element)
    try:
        myCursor.execute("SELECT * FROM users")
        for row in myCursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))

    except Exception as e:
        messagebox.showwarning("Algo salio mal, intentelo mas tarde")
        pass

####Table#####
tree=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.heading('#0', text="id", anchor=CENTER)
tree.heading('#1', text="nombre", anchor=CENTER)
tree.heading('#2', text="edad", anchor=CENTER)
tree.heading('#3', text="posicion", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#4', text="telefono", anchor=CENTER)


def create():
    myConnection=sqlite3.connect("db")
    myCursor=myConnection.cursor()
    try:
        data=myName.get(), myAge.get(), myPosition.get(), myPhone.get()
        myCursor.execute("INSERT INTO users VALUES(NULL,?,?,?", (data))
        myConnection.commit()

    except Exception as e:
        messagebox.showwarning("Algo salio mal, intentelo mas tarde")
        pass
    clearFields()
    show()

def run():
    #GUI
    #At first the main frame from tkinter library is named root
    root=Tk()
    root.title("Adco")
    root.geometry("1000x600")
    root.mainloop()


#Entry point
if __name__=="__main__":
    run()
