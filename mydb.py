import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Maramica1997!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sendItStore")

print('Done')
