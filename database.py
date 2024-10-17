import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('pos_system.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Crear tabla de productos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
       
        # Crear tabla de clientes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT
            )
        ''')
       
        # Crear tabla de ventas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                date TEXT NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
        ''')
       
        self.conn.commit()

    def close(self):
        self.conn.close()

    # Aquí puedes agregar más métodos para interactuar con la base de datos
    # como add_product(), get_product(), update_product(), delete_product(), etc.


 