#!/usr/bin/env python                                                             

import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

DB_NAME = 'mladenhe3'
cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost\
', database='mladenhe3')

cursor = cnx.cursor(buffered=True)
form = cgi.FieldStorage()

# get data from feilds

player_id = str(form.getvalue('player_id'))
player_name = form.getvalue('player_name')
player_number = (form.getvalue('player_number'))
player_height = (form.getvalue('player_height'))
player_lbs = (form.getvalue('player_lbs'))
player_position = form.getvalue('player_position')

values = (player_id, player_name, player_number, player_height, player_lbs, player_position)
  
query = ("insert into players values(%s, %s, %s, %s, %s, %s)")
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Added a Player!</title>")
print("</head>")
print("<body>")
print("The new player has been added!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


print("</body>")
print("</html>")
cnx.commit()
cursor.close()
cnx.close()
