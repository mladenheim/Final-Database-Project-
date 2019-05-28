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

values = (team_id,)

query1 = ('delete from coaches_for where team_id = %s')
query2 = ('delete from plays_for where team_id = %s')
#query = ('delete from coaches_for where team_id = %s')
query3 = ('delete from teams_playing where hometeam_id = %s')
query4 = ('delete from teams_playing where awayteam_id = %s')
query5 = ('delete from teams where team_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Deleted a Team!</title>")
print("</head>")
print("<body>")
print("The Team has been Deleted!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query1, values)
cursor.execute(query2, values)
cursor.execute(query3, values)
cursor.execute(query4, values)
cursor.execute(query5, values)

cnx.commit()
cursor.close()
cnx.close()
