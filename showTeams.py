#!/usr/bin/env python

#import cgi, cgitb                                                                
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

DB_NAME = 'mladenhe3'
cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe3')
                              
cursor = cnx.cursor(buffered=True)

form = cgi.FieldStorage()

query = 'select teams.team_id, city_name, team_name, coaches.coach_id, coach_name, players.player_id, player_name, player_number, player_height, player_lbs, player_position from teams, players, plays_for, coaches, coaches_for where players.player_id = plays_for.player_id and coaches.coach_id = coaches_for.coach_id and plays_for.team_id = teams.team_id and coaches_for.team_id = teams.team_id;'

# html to connect with the data                                                   
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello - THE TEAMS!</title>')
print ('</head>')
print ('<body>')
print('<p><a href="/~mladenheim/secondpage.html">Return to the Home Page</a></p>')
print ("<p>Here Are The Teams And Their Players And Coaches For The 2020 Season!</p>")
print('TEAM ID | TEAM CITY/NAME | COACH ID | TEAM COACH | PLAYER ID | TEAM PLAYER')

cursor.execute(query)
for line in cursor:
    print('<p>' + str(line[0]) + ' | ' + str(line[1]) + ' ' + str(line[2]) + ' | ' + str(line[3]) + ' | ' + str(line[4])+ ' | ' + str(line[5]) + ' | ' + str(line[6]) + ' ,  #' + str(line[7]) + ' , ' + str(line[8]) + ' , ' + str(line[9]) + ' lbs, ' + str(line[10]) + '</p>')    
print ('</body>')
print ('</html>')
cursor.close()
cnx.close()
