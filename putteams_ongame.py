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
hometeam_id = str(form.getvalue('hometeam_id'))
awayteam_id = str(form.getvalue('awayteam_id'))

values = (game_id, hometeam_id, awayteam_id,)

query = ("insert into teams_playing values(%s, %s, %s)")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Added a Teams to a Game!</title>")
print("</head>")
print("<body>")
print("The Teams have been added to a Game!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')                                                                              
cursor.execute(query, values)

print("</body>")
print("</html>")
cnx.commit()
cursor.close()
cnx.close()
