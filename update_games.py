#!/usr/bin/env python                                                             

import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

DB_NAME = 'mladenhe3'
cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe3')

cursor = cnx.cursor(buffered=True)
form = cgi.FieldStorage()

# get data from feilds

#player_id = str(form.getvalue('player_id'))
stadium = form.getvalue('stadium')
date = form.getvalue('date')
game_id = str(form.getvalue('game_id'))

values = (date, stadium, game_id,)
query = ('update games set date = %s, stadium = %s where game_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Updated a Game!</title>")
print("</head>")
print("<body>")
print("The Game has been Updated!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
