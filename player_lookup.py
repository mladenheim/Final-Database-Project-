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
player_name = form.getvalue('player_name')

values = (player_name,)
query = ('select players.player_id, player_name, player_number, player_height, player_lbs, player_position, city_name, team_name, coach_name, games.game_id from players, plays_for, coaches, coaches_for, teams, player_inGame, games where players.player_id = plays_for.player_id and plays_for.team_id = teams.team_id and coaches.coach_id = coaches_for.coach_id and coaches_for.team_id = teams.team_id and players.player_id = player_inGame.player_id and player_inGame.game_id = games.game_id and players.player_name =%s')


##select players.player_id, player_name, games.game_id from players, player_inGame, games where players.player_id = player_inGame.player_id and player_inGame.game_id = games.game_id and players.player_name = 'Chris Monn';
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - You Found the Player!</title>")
print("</head>")
print("<body>")
print("<p>This is the Players information!</p>")
print("PLAYER ID | PLAYER NAME | PLAYER NUMBER | PLAYER HEIGHT (in inches) | PLAYER WEIGHT (in pounds) | PLAYER POSITION | TEAM CITY | TEAM NAME | COACH NAME | GAMES WITH PLAYER")
      
cursor.execute(query, values)

for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + ' | #' + str(line[2]) + ' | ' + str(line[3]) + '" | ' + str(line[4]) + 'lbs | ' + str(line[5]) + ' | ' + str(line[6]) + ' | ' + str(line[7]) + ' | ' + str(line[8]) + ' | ' + str(line[9]) + '</p>')

print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
print("</body>")
print("</html>")

cnx.commit()
cursor.close()
cnx.close()
