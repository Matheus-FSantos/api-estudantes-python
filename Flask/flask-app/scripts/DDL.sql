create table students(
	id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(45) NOT NULL,
	mail VARCHAR(60) NOT NULL,
	fone VARCHAR(20) NOT NULL,
);

create table class(
	id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(45) NOT NULL
);