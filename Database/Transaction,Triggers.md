# Transaction
> (다 성공하던지 혹은 다 실패하던지 해야하는)여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법

## Transaction 예시
* 계좌이체 (인출 & 입금)
  * 송금중에 알 수 없는 문제로 인출에는 성공했는대 입금에 실패한다면?
  * 인출과 입금 모두 성공적으로 끝나야 거래가 최종 승인되고, 중간에 문제가 발생한다면 거래를 처음부터 없었던 거래로 만들어야 함
  * 결국 함께 성공하던지실패해야 함

## Transaction Syntax
* START TRANSACTION
  * 트랙잭션 구문의 시작을 알림
* COMMIT
  * 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
* ROLLBACK
  * 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림


<!-- Transaction 문제1 -->
트랜잭션을 사용해 users테이블에 데이터를 삽입하고 ROLLBACK을 했을 떄와 COMMIT을 했을 떄 users테이블의 데이터 사앹를 비교

```SQL
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
```

## Transaction 정리
* 쪼개질 수 없는 업무처리의 단위
* 전체가 수행되거나 또는 전혀 수행되지 않아야 함 (All or Nothing)

# Triggers
> 특정 이벤트에 대한 응답으로 자동으로 실행되는 것
> (INSERT, UPDATE, DELETE) -> 데이터 베이스에 변화가 생긴다.
* ~를 추가한 후에 ~하겠다.
* ~를 수정하기 전에 ~하겠다.
* ~를 삭제한 후에 ~하겠다.

## Triggers Syntax
* CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
* 각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입,수정,삭제 전/후)
* ON키워드 뒤에 트리거가 속한 테이블의 이름을 지정
* 트리거가 활성화될 때 실행할 코드를 trigger_body에 지정
  * 여러 명령문을 실행하려면 BEGIN END키워드로 묶어서 사용

<!-- Triggers 문제1 -->
트리거를 사용해 기존 게시글이 수정되면, 게시글의 수정일자 필드 값을 최신 일자로 업데이트 하기

```SQL
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
```

INSERT = OLD : NO , NEW : YES
UPDATE = OLD : YES, NEW : YES
DELETE = OLD : YES, NEW : NO

<!-- Triggers 문제2 -->
트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 해당 게시글이 작성되었다는 것을 기록하기
```SQL
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
```
<!-- Triggers 문제2 심화 -->
트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 몇 번 게시글이 작성되었다는 것을 기록하기

```SQL
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
```
<!-- Triggers 문제3 -->
트리거를 사용해 기존 게시글이 삭제되면, 삭제된 게시글의 구조 그대로 별도의 테이블에 기록하기
```SQL
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
```
### 참고
#### Triggers 관련 추가 명령문
```SQL
-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;
```
#### Triggers 생성 시 에러 해결
* 트랜잭션 생성 후 정상 적으로 종료되지 않아 발생하는 에러 발생 시 해결법
* Error Code:2013 Lost connection to MySQL server during query
* Error Code:2015 LOCK wait timeout exceeded; try restarting transaction
```SQL
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB.TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```

