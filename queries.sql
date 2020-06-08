/*** Various Queries and test inserts ***/

show databases;

CREATE TABLE IF NOT EXISTS articles (
    id INT,
    title VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS article (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    views DECIMAL(15 , 2 ),
    likes BIGINT,
    date_posted VARCHAR(255),
    date_updated VARCHAR(255),
    content MEDIUMTEXT
);


alter table article modify views bigint;