-- Transaction 문제1

DROP TABLE users;

-- 자동 COMMIT 비활성화
SET autocommit = 0;
-- users 테이블 생성
CREATE TABLE users(
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY(id)
);

START TRANSACTION;

INSERT INTO users(name)
VALUES ('harry'),('test');

SELECT * FROM users;

-- ROLLBACK;

COMMIT;

DROP TABLE articles;

-- Triggers 문제1

SELECT * FROM articles;

CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updateAt DATETIME NOT NULL,
    PRIMARY KEY (id)
); 


INSERT INTO articles (title, createdAt, updateAt)
VALUES ('title1',CURRENT_TIME(), CURRENT_TIME());


DELIMITER //
CREATE TRIGGER myTrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updateAt = CURRENT_TIME();
END//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id =1;

-- -- Triggers 문제2


CREATE TABLE articleLogs(
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
); 

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs(description, createdAt)
    VALUES('글이 작성되었어요.', CURRENT_DATE());
END//
	
DELIMITER ;

INSERT INTO articles (title, createdAt, updateAt)
VALUES ('title2',CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;
SELECT * FROM articleLogs;

-- 심화
DROP TRIGGER recordLogs;

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs(description, createdAt)
    VALUES(CONCAT(NEW.id,'글이 작성되었어요.'), CURRENT_DATE());
END//
	
DELIMITER ;

INSERT INTO articles (title, createdAt, updateAt)
VALUES ('title3',CURRENT_TIME(), CURRENT_TIME());

-- Triggers 문제3
CREATE TABLE backupArticles(
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backUpLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles(title,createdAt,updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updateAt);
END//
DELIMITER ;

SHOW TRIGGERS;

DELETE FROM articles
WHERE id = 1;

SELECT * FROM articles;
SELECT * FROM backuparticles;
	