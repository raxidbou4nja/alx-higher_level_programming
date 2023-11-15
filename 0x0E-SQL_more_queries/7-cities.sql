-- To create database named (hbtn_0d_usa) and a table (cities) in the database hbtn_0d_usa
-- To create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- To use database
USE hbtn_0d_usa;
-- To create a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
