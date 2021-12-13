create table if not exists users (
user_id serial PRIMARY KEY,
username VARCHAR ( 15 ) UNIQUE NOT NULL,
password VARCHAR (200) NOT NULL,
user_level int not null,
user_time int not null
);

create table if not exists words (
word_id serial PRIMARY KEY,
dutch VARCHAR ( 50 ) NOT NULL,
english VARCHAR (50) NOT NULL,
word_level int not null
);

create table if not exists statistics (
id serial PRIMARY KEY,
user_id int Not NULL,
total_words int  NOT NULL,
known_words int not null,
level_name int not null );