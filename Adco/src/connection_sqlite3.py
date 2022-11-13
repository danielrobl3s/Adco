import sqlite3

def run():
    try: 
        miconexion = sqlite3.connect("database/adcodb")
        cursor=miconexion.cursor()
        cursor.execute("CREATE TABLE usuarios(id_usuario INTEGER NOT NULL PRIMARY KEY, nombre VARCHAR, edad INTEGER, posicion VARCHAR, telefono INTEGER)")
    except Exception as ex:
        print(ex)



if __name__=="__main__":
    run()