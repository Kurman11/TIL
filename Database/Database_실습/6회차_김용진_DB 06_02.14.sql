-- DB 06 - SQL Modifying data
-- 문제1
CREATE TABLE users(
	userid INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(userid)
);

SHOW COLUMNS FROM users;
SELECT * FROM users;

-- 문제2
INSERT INTO 
	users (first_name, last_name, birthday, city, country,email)
VALUES 
	('Beemo', 'Jeong' , '1000-01-01', NULL , NULL , 'beemo@hphk.kr'), 
	('Jieun', 'Lee' , '1993-05-16', 'Seoul', 'Korea', NULL), 
	('Dami', 'Kim' , '1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee' , '1985-07-14', 'Seoul', 'Korea', NULL);
-- 문제3
INSERT INTO
	users(first_name, last_name, birthday, city, country,email)
VALUES 
	('hi', 'Lee' , '1993-05-16', 'Seoul', 'Korea', '123@hphk.kr'), 
	('ho', 'Kim' , '1995-04-09', 'Seoul', 'Korea', '456@hphk.kr'),
    ('hu', 'Lee' , '1995-07-14', 'Seoul', 'Korea', '789@hphk.kr'),
	('he', 'Kim'  , '1995-05-14', 'Seoul', 'Korea', '159@hphk.kr'),
    ('do', 'Lee' , '1993-01-14', 'Seoul', 'Korea', '753@hphk.kr');

-- 문제4
UPDATE users
SET
	first_name = 'YONGJIN', 
    last_name = 'KIM',
    birthday = '1995-08-07'
WHERE
	userid = 2;
    
-- 문제5
UPDATE
	users
SET
	country = 'korea'
WHERE
	country IS NULL ;

-- 문제6
DELETE FROM
	users
WHERE
	first_name = 'Beemo';

-- 문제7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo'
    OR last_name = 'Lee';

-- 문제8
DELETE FROM
	users
ORDER BY
	created_at DESC
LIMIT 1;



