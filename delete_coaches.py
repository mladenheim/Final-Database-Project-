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

coach_id = str(form.getvalue('coach_id'))

values = (coach_id,)

query1 = ('delete from coaches_for where coach_id = %s')
query2 = ('delete from coaches where coach_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Deleted a Coach!</title>")
print("</head>")
print("<body>")
print("The Coach has been Deleted!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query1, values)
cursor.execute(query2, values)
print("</body>")
print("</html>")

cnx.commit()
cursor.close()
cnx.close()
