-- To creates the database named (hbtn_0d_usa) and a table named (states) (in the database hbtn_0d_usa)
-- To create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- To use database
USE hbtn_0d_usa;
-- To create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
