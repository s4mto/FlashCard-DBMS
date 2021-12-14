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


create table if not exists success_percentage (
user_id int Not NULL,
currente_level int not null,
percentage numeric not null);
