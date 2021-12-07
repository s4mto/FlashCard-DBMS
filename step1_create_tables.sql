create table if not exists users (
user_id serial PRIMARY KEY,
username VARCHAR ( 15 ) UNIQUE NOT NULL,
password VARCHAR (15) NOT NULL,
user_level int not null
);

create table if not exists words (
word_id serial PRIMARY KEY,
dutch VARCHAR ( 50 ) NOT NULL,
english VARCHAR (50) NOT NULL,
word_level int not null
);
