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
team_name = form.getvalue('team_name')
city_name = form.getvalue('city_name')
team_id = str(form.getvalue('team_id'))

values = (team_name, city_name,  team_id,)
query = ('update teams set team_name = %s, city_name = %s where team_id = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Updated a Team!</title>")
print("</head>")
print("<body>")
print("The Team has been Updated!")
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
      
cursor.execute(query, values)


cnx.commit()
cursor.close()
cnx.close()
