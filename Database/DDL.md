# Managing Tables
## DDL
DDL(Data Definition Language) = 데이터의 기본 구조 및 형식 변경 CREATE,DROP,ALTER

# CREATE
## **CREATE TABLE** statement
> 테이블 생성

* 각 필드에 적용할 데이터 타입(data type) 작성
* 테이블 및 필드에 대한 제약조건(constraints) 작성
```SQL
CREATE TABLE examples (
	examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);
```
* CHAR(50) = 고정 길이 (들어오는 글자 길이가 50이 아니더라도 설정한 길이만큼 50 고정)
* VARCHAR(50) = 가변 길이(들어오는 글자 길이가 3글자 이면 3으로)

### 대표적인 MySQL Data Types
* Numeric       숫자형 INT,FLOAY,....
* String        문자형 VARCHAR, TEXT,....
* Date and Time 날짜형 DATE,DATETIME,...

# Constraint
> 제약 조건
* 데이터 **무결성**(데이터의 정확성과 일관성을 보증)을 지키기 위해 데이터를 입력 받을 떄 실행하는 검사 규칙

## 대표적인 MySQL Constraints
* PRIMARY KEY
  * 해당 필드를 기본 키로 지정
* NOT NULL
  * 해당 필드에 NULL값을 저장하지 못하도록 지정

## **AUTO_INCREMENT** attribute
* 테이블의 기본 키에 대한 번호 자동 생성

### AUTO_INCREMENT 특징
* 기본 키 필드에 사용
  * 고유한 숫자를 부여
* 시작 값은 1이며 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
* 이미 사용한 값을 재사용하지 않음
* 기본적으로 NOT NULL제약 조건을 포함

# Delete a table
## **DROP TABLE** statement
> 테이블 삭제
* DROP TABLE statemant 이후 삭제할 테이블 이름 작성
```SQL
SHOW COLUMNS FROM examples;
```
# Modifying table statement
## **ALTER TABLE** statement
* 테이블 필드 조작 (생성,수정,삭제)

* ALTER TABLE ADD           필드 추가 C
* ALTER TABLE MODIFY        필드 속성 변경 U
* ALTER TABLE CHANGE COLUMN 필드 이름 변경 U
* ALTER TABLE DROP COLUMN   필드 삭제 D

* ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성

<!-- ADD 문제1 -->
examples 테이블에 country 필드 추가
(단, country 필드는 가변길이 문자열 최대 100자이며 NULL 값을 허용하지 않음)

```SQL
ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;
```

<!-- ADD 문제2 -->
examples 테이블에 age와 address 필드 추가
(단, age 필드는 정수 타입이 저장되며 NULL 값을 허용하지 않음 address 필드는 가변길이 문자열 최대 100자이며 NULL 값을 허용하지 않음)

```SQL
ALTER TABLE	examples
ADD	age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;
```
### ALTER TABLE MODIFY syntax
> MODIFY키워드 이후 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약 조건 작성

<!-- MODIFY 문제1 -->
examples 테이블의 address 필드를 가변길이 문자열 최대 50자까지 그리고 NULL값을 허용하지 않도록 변경

```SQL
ALTER TABLE
	examples
MODIFY
	address VARCHAR(50) NOT NULL;
```

<!-- MODIFY 문제2 -->
examples 테이블의 lastName,firstName 필드를 가변길이 문자열 최대 10자까지 그리고 NULL값을 허용하지 않도록 변경

```SQL
ALTER TABLE examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY firstName VARCHAR(10) NOT NULL;
```

### ALTER TABLE CHANGE CCOLUMN syntax
> CHANGE COLUMS 키워드 이후
> 기존 필드 이름, 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약조건 작성

<!-- CHANGE COLUMN 문제1 -->
examples 테이블의 country 필드 이름을 state로 변경
(단, 데이터 타입 및 제약 조건은 기존과 동일)
```SQL
ALTER TABLE
	examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;
```

### ALTER TABLE DROP COLUMN syntax
> DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성

<!-- DROP COLUMN 문제1 -->
examples 테이블의 address 필드 삭제
```SQL
ALTER TABLE
	examples
DROP COLUMN
	address;
```
<!-- DROP COLUMN 문제2 -->
examples 테이블의 state와 age필드 삭제
```SQL
ALTER TABLE examples
DROP COLUMN state,
DROP COLUMN age;
```
## 참고
### 반드시 NOT NULL제약을 사용해야 할까
* "NO"
* 데이터베이스를 사용하는 프로그램에 따라 NULL을 저장할 필요가 없는 경우가 많으므로 되도록 NOT NULL로 정의
* "값이 없다."라는 표현을 테이블에 기록하는 것은 0이나 빈 문자열 등을 사용하는 것으로 대체하는 것을 권장
