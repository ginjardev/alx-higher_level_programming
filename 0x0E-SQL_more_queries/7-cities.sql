-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id NOT NULL FOREIGN KEY(id) REFERENCES states(id),
	name VARCHAR(256)
);