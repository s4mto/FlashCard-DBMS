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

<<<<<<< HEAD
=======
create table if not exists succes_percentage (
user_id int Not NULL,
percentage numeric not null,
currente_level int not null );
>>>>>>> 7a3a04b2fc2c8f6d43d309549183846697cc3997
