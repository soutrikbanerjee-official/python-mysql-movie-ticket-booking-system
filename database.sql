CREATE DATABASE sb_theatres;
USE sb_theatres;

DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    Name VARCHAR(20) NOT NULL,
    Mobile_No DECIMAL(10,0) NOT NULL PRIMARY KEY,
    Email VARCHAR(320) UNIQUE,
    Gender CHAR(1),
    DOB DATE,
    Booking_Nos TEXT
);

DROP TABLE IF EXISTS Action;
DROP TABLE IF EXISTS Crime;
DROP TABLE IF EXISTS Fantasy;
DROP TABLE IF EXISTS Horror;
DROP TABLE IF EXISTS Romance;
DROP TABLE IF EXISTS Fiction;
DROP TABLE IF EXISTS Thriller;

CREATE TABLE Action (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Crime (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Fantasy (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Horror (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Romance (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Fiction (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Thriller (
    Sl_No CHAR(1) PRIMARY KEY,
    Show_Name VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO Action (Sl_No, Show_Name) VALUES
('1','Avatar: The Way of Water'),
('2','Black Panther: Wakanda Forever'),
('3','Heads of State'),
('4','Mission: Impossible - Dead Reckoning Part Two'),
('5','Predator: Badlands'),
('6','Shazam! Fury of the Gods'),
('7','The Killer''s Game'),
('8','Top Gun: Maverick');

INSERT INTO Crime (Sl_No, Show_Name) VALUES
('1','A Haunting in Venice'),
('2','Bugonia'),
('3','Companion'),
('4','Glass Onion: A Knives Out Mystery'),
('5','Lake George'),
('6','Lift'),
('7','Marmalade'),
('8','Rebel Ridge');

INSERT INTO Fantasy (Sl_No, Show_Name) VALUES
('1','A Knight''s War'),
('2','Coraline'),
('3','Dune: Part Two'),
('4','How to Train Your Dragon'),
('5','In the Lost Lands'),
('6','Spirited Away'),
('7','The Chronicles of Narnia: The Lion, the Witch and the Wardrobe'),
('8','The Fantastic Four: First Steps');

INSERT INTO Horror (Sl_No, Show_Name) VALUES
('1','28 Years Later'),
('2','A Quiet Place Part II'),
('3','Fear Street Trilogy'),
('4','Good Boy'),
('5','Holy Spider'),
('6','Imaginary'),
('7','Lisa Frankenstein'),
('8','Night Swim');

INSERT INTO Romance (Sl_No, Show_Name) VALUES
('1','A Big Bold Beautiful Journey'),
('2','Challengers'),
('3','Companion'),
('4','It Ends with Us'),
('5','Love Lies Bleeding'),
('6','Love Me'),
('7','Materialists'),
('8','The Idea of You');

INSERT INTO Fiction (Sl_No, Show_Name) VALUES
('1','Alien: Romulus'),
('2','Dune: Part Two'),
('3','Eli Roth''s The House'),
('4','Furiosa: A Mad Max Saga'),
('5','Mar.IA'),
('6','Primitive War'),
('7','The Beast'),
('8','The Becomers');

INSERT INTO Thriller (Sl_No, Show_Name) VALUES
('1','Captain Phillips'),
('2','Catch Me If You Can'),
('3','Minority Report'),
('4','Source Code'),
('5','The Bourne Identity'),
('6','The Bourne Supremacy'),
('7','The Bourne Ultimatum'),
('8','The Fugitive');

