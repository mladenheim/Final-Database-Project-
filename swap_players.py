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

team_id = str(form.getvalue('team_id'))
player_id = str(form.getvalue('player_id'))

values = (team_id, player_id,)
#query = ('insert into plays_for where player_id = %s and team_id = %s')
query = ('update plays_for set team_id = %s where player_id = %s')                                                   

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Swapped a Player!</title>")
print("</head>")
print("<body>")
print("The Player has been Swapped!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
