create table players(
player_id varchar(5),
player_name varchar(25),
player_number int(2),
player_height int(2),
player_lbs int(3),
player_position char(10),
primary key (player_id));

create table coaches(
coach_id varchar(5),
coach_name varchar(25),
primary key (coach_id));


create table teams(
team_id varchar(5),
team_name varchar(25),
city_name varchar(25),
primary key (team_id));


create table plays_for(
player_id varchar(5),
team_id varchar(5),
primary key(player_id),
foreign key (player_id) references players(player_id),
foreign key (team_id) references teams(team_id));
                                                                                                            

create table coaches_for(
coach_id varchar(5),
team_id varchar(5),
primary key(coach_id),
foreign key (coach_id) references coaches(coach_id),
foreign key (team_id) references teams(team_id));

create table games(
game_id varchar(5),
game_name varchar(30),
date timestamp(6),
stadium varchar(20),
primary key (game_id));

create table teams_playing(
game_id varchar(5),
hometeam_id varchar(5),
awayteam_id varchar(5),
primary key (game_id),
foreign key (hometeam_id) references teams(team_id),
foreign key (awayteam_id) references teams(team_id));

create table player_inGame(
player_id varchar(5),
game_id varchar(5),
primary key (player_id, game_id),
foreign key (player_id) references players(player_id),
foreign key (game_id) references games(game_id));
