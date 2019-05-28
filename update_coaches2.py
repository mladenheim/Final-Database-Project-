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
coach_name = form.getvalue('coach_name')
coach_id = str(form.getvalue('coach_id'))

values = (coach_name, coach_id,)
query = ('update coaches set coach_name = %s  where coach_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Updated a Coach!</title>")
print("</head>")
print("<body>")
print("The coach has been Updated!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
