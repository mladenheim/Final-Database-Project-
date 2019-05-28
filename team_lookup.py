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
team_name = form.getvalue('team_name')

values = (team_name,)
val = (team_name)
query = ('select player_name, coach_name from players, plays_for, coaches, coaches_for, teams where players.player_id = plays_for.player_id and plays_for.team_id = teams.team_id and coaches.coach_id = coaches_for.coach_id and coaches_for.team_id = teams.team_id and teams.team_name = %s')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Found the Team!</title>")
print("</head>")
print("<body>")
print("<p>This is the " + val + " information!</p>")

print('PLAYERS | COACH')

cursor.execute(query, values)
for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + '</p>')

print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
print("</body>")
print("</html>")

cnx.commit()
cursor.close()
cnx.close()
