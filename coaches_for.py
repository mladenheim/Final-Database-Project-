#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

DB_NAME = 'mladenhe3'
cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe3')

cursor = cnx.cursor(buffered=True)
form = cgi.FieldStorage()

# get data from feilds                                                              
coach_id = str(form.getvalue('coach_id'))
team_id = str(form.getvalue('team_id'))

values = (coach_id, team_id)

query = ("insert into coaches_for values(%s, %s)")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Added the Coach to a Team!</title>")
print("</head>")
print("<body>")
print("The new coach has been added to your new team!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')

cursor.execute(query, values)

print("</body>")
print("</html>")
cnx.commit()
cursor.close()
cnx.close()
