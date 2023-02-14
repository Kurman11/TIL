-- DB 05 - SQL Managing table
-- 문제 1
CREATE TABLE posts(
    postid INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postid)
);
SHOW COLUMNS FROM posts;
SELECT * FROM posts;

-- 문제2
ALTER TABLE posts
ADD	writer VARCHAR(100) DEFAULT 'Anonymous',
ADD created_at DATETIME DEFAULT CURRENT_TIMESTAMP;

-- 문제3
ALTER TABLE 
	posts
MODIFY
	content TEXT;

-- 문제4
ALTER TABLE 
	posts
DROP COLUMN
	writer;
    
-- 문제5
DROP TABLE posts;

-- 문제6
CREATE TABLE IF NOT EXISTS posts(
	postid INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NUll,
    content TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postid)
);

-- 문제7
DROP TABLE IF EXISTS posts;
    
    
    
    