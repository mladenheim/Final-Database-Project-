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
game_id = str(form.getvalue('game_id'))

values = (game_id,)
query1 = ('select teams_playing.hometeam_id, teams.team_name, teams.city_name from teams, teams_playing, games where teams.team_id = teams_playing.hometeam_id and teams_playing.game_id = games.game_id and games.game_id = %s')

query2 = ('select teams_playing.awayteam_id, teams.team_name, teams.city_name from teams, teams_playing, games where teams.team_id = teams_playing.awayteam_id and teams_playing.game_id = games.game_id and games.game_id = %s')


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Found the Game!</title>")
print("</head>")
print("<body>")
#print("<p>This is the " + val + " information!</p>")
#print ("<p>Here Are The Games For The 2020 Season!</p>")
#print ('<p>STR = Stringer, VIK = Vikings, CRU = Crusaders, DRE = Dreamers, TIG = Tigers</p>')                                                                   
#print ('For Example: 2020-01-10 03:30:00 = January 10, 2019, at 3:30 pm')
print('HOMETEAM ID | HOMETEAM NAME | HOMETEAM CITY')
cursor.execute(query1, values)
for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + ' | ' +  str(line[2]) + '</p>')

print('AWAYTEAM ID | AWAYTEAM NAME | AWAYTEAM CITY')
cursor.execute(query2, values)
for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + ' | ' +  str(line[2]) + '</p>')

print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')    
print("</body>")
print("</html>")

cnx.commit()
cursor.close()
cnx.close()
