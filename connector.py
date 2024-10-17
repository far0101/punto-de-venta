import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="basededatos"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM clientes")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)