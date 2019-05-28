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
coach_id = str(form.getvalue('coach_id'))

values = (team_id, coach_id,)
#query = ('insert into plays_for where player_id = %s and team_id = %s')
query = ('update coaches_for set team_id = %s where coach_id = %s')                                                   

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Swapped a Coach!</title>")
print("</head>")
print("<body>")
print("The Coach has been Swapped!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
