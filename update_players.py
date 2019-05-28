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

#player_id = str(form.getvalue('player_id'))
player_name = form.getvalue('player_name')
player_number = form.getvalue('player_number')
player_height = form.getvalue('player_height')
player_weight = form.getvalue('player_lbs')
player_position = form.getvalue('player_position')
player_id = str(form.getvalue('player_id'))

values = (player_name, player_number, player_height, player_weight, player_position, player_id,)
query = ('update players set player_name = %s, player_number = %s, player_height = %s, player_lbs = %s, player_position = %s where player_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Updated a Player!</title>")
print("</head>")
print("<body>")
print("The Player has been Updated!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
