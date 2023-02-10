# 용어 정리
## Query
* 질의,질문
* "데이터베이스로부터 정보를 요청" 하는 것
* 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라한다.  

## SQL표준
* SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨
* 널리 사용되는 모든 RDBMS에서 SQL 표준을 지원
* **다만 RDBMS별로 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의**

# Querying data

**SELECT** statement
테이블에서 데이터를 조회

SELECT syntax
```SQL
SElECT
  select_list -- 필드 : 테이블의 열 
FROM
  tanele_name;
```
* SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정
* FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

```SQL
SELECT lastName FROM employees;
-- 테이블 employees에서 lastName 필드의 모든 데이터를 조회
SELECT lastName,firstName FROM employees;
-- 테이블 employees에서 lastName,firstName 필드의 모든 데이터를 조회
SELECT * FROM employees;
-- 테이블 employees에서 모든 필드의 데이터를 조회
SELECT firstName AS '이름' FROM employees;
-- 테이블 employees에서 firstName 필드의 모든 데이터를 조회(단, 조회 시 firstName이 아닌 '이름'으로 출력 될 수 있도록 출력명 변경)
SELECT productCode, quantityOrdered * priceEach AS '주문 총액'  FROM orderdetails;
-- 테이블 orderdetails에서 productCode, 주문총액필드의 모든 데이터를 조회(단, 주문 총액 필드는 quantityOrdered 와 priceEach필드를 곱한 결과 값  )
```
### SELECT 정리
* SELECT문을 사용하여 테이블의 데이터를 조회 및 반환
* SELECT *(asterisk)를 사용하여 테이블의 모든 필드 선택

# Sorting date
ORDER BY clause
조회 결과의 레코드를 정렬
```SQL
SELECT firstName FROM employees ORDER BY firstName ASC;
-- 테이블 employees에서 fristName필드의 모든 데이터를 오름차순으로 조회
SELECT firstName FROM employees ORDER BY firstName DESC;
-- 테이블 employees에서 fristName필드의 모든 데이터를 내림차순으로 조회
SELECT lastName,firstName FROM employees ORDER BY lastName DESC, firstName ASC;
-- 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음 firstName 필드 기준으로 오름차순 정렬하여 조회
SELECT productCode, quantityOrdered * priceEach as 'totalSales' FROM orderdetails ORDER BY totalSales DESC;
-- 테이블 orderdetails에서 totalSales필드를 기준으로 내림차순으로 정렬한 다음 productCode와 totalSales 필드의 모든 데이터를 조회 (단, totalSales 필드는 quantityOrdered * priceEach필드의 모든 데이터를 조회 )
```
SELECT statement 순서
1. 테이블에서(FROM)
2. 조회하여 (SELECT)
3. 정렬(ORDER BY)