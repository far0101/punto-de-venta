import sqlite3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="basededatos"

)

mycursor = mydb.cursor()

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('pos_system.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self):
        id = input("Escanea o ingresa el código: ")
        name = input("Nombre del producto: ")
        price = input("Precio: ")

        mycursor.execute(f"INSERT INTO productos (id, nombre, precio) VALUES ({id},'{name}',{price})")
        mydb.commit()

        print("Producto agregado!")

    def get_product(self, id):
        mycursor.execute('SELECT name, price FROM products WHERE id = {id}')
        result = mycursor.fetchone()
        if result:
            return result
        return None

def main():
    db = Database()
    print("1. Agregar producto")
    print("2. Modo escaneo")
    option = input("Seleccione opción: ")
   
    if option == "1":
        db.add_product()
       
    elif option == "2":

        interruption = 1

        while(interruption):

            code = int(input("Escanee o ingrese codigo manualmente: "))

            if(code == 0 ):
                interruption = 0
            else:
                db.get_product(code)

if __name__ == "__main__":
    main()