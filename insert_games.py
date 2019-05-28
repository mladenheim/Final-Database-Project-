#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

DB_NAME = 'mladenhe3'
cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe3')

cursor = cnx.cursor(buffered=True)
form = cgi.FieldStorage()

# get data from feilds
game_id = str(form.getvalue('game_id'))
date = form.getvalue('date')
stadium = form.getvalue('stadium')
values = (game_id, date, stadium,)

# example values = (12345, 'Ballers', 'Brooklyn')
query = ("insert into games values(%s, %s, %s)")

# html to connect with the data
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Added a Game!</title>")
print("</head>")
print("<body>")
print("The new game has been created!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
#cursor.execute(query)
cursor.execute(query, values)

print('</body>') 
print('</html>')

cnx.commit()
cursor.close()
cnx.close()
