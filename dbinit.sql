DROP DATABASE IF EXISTS thesaurus;

CREATE DATABASE thesaurus;
USE thesaurus;

CREATE TABLE Terms
(
id INT PRIMARY KEY AUTO_INCREMENT,
term VARCHAR(20) NOT NULL UNIQUE,
count_links INT
);

CREATE TABLE Files
(
id INT PRIMARY KEY AUTO_INCREMENT,
file_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE term_links
(
term_from INT,
term_to INT,
UNIQUE(term_from, term_to)
);

CREATE TABLE term_file
(
file_name INT NOT NULL,
term INT NOT NULL,
count_term INT NOT NULL
);

CREATE USER 'user'@'192.168.%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON thesaurus.* TO 'user'@'192.168.%'
