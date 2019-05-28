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
coach_name = form.getvalue('coach_name')

values = (coach_name,)
query = ('select coaches.coach_id, coach_name, city_name, team_name from coaches, coaches_for, teams where coaches.coach_id = coaches_for.coach_id and coaches_for.team_id = teams.team_id and coaches.coach_name = %s')
                                                   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Found the Coach!</title>")
print("</head>")
print("<body>")
print("<p>This is the Coaches information!</p>")
print("COACH ID | COACH NAME | COACH CITY | COACH TEAM  NAME")
      
cursor.execute(query, values)

for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + ' | ' + str(line[2]) + ' | ' + str(line[3]) + '</p>')
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
print("</body>")
print("</html>")

cnx.commit()
cursor.close()
cnx.close()
