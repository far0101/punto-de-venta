import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="puntodeventa",
  password="carlitosxd"
)

print(mydb)