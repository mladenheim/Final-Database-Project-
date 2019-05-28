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

values = (game_id,)


#query1 = ('delete from player_inGame  where game_id = %s')
query1 = ('delete from teams_playing where game_id = %s')
query2 = ('delete from player_inGame where game_id = %s')
query3 = ('delete from games where game_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Deleted a Game!</title>")
print("</head>")
print("<body>")
print("The Game has been Deleted!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query1, values)
cursor.execute(query2, values)
cursor.execute(query3, values)

cnx.commit()
cursor.close()
cnx.close()
