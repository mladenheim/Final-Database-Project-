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
coach_name = form.getvalue('coach_name')                                   

values = (coach_id, coach_name)

query = ("insert into coaches values(%s, %s)")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Added a Coach!</title>")
print("</head>")
print("<body>")
print("The new Coach has been added!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')                                                                              
cursor.execute(query, values)

print("</body>")
print("</html>")
cnx.commit()                                                                 
cursor.close()
cnx.close()
