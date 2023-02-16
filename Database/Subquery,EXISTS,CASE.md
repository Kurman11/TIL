# SQL - Nested Queries
## Subquery
> 'A query inside a query' 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법

### Subquery 예시
table1에서 가장 나이가 어린 사람을 삭제해야 한다면?
```SQL
DELETE FROM table1
WHERE age = (
  SELECT MIN(age) FROM table1 -- <-가 Subquery
);
```
### Subquery 특징
* 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
* SELECT, FROM, WHERE, HAVING절 등에서 다양한 맥락에서 사용

<!-- SubQuery 문제1 -->
한번에 가장 많은 돈을 소비한 고객 번호 조회(payments 테이블 활용)
```SQL
SELECT MAX(amount)
FROM payments;

SELECT customerNumber, amount
FROM payments
WHERE  amount = (
	SELECT MAX(amount)
	FROM payments
    );
```

<!-- SubQuery 문제2 -->
미국에 있는 사무실에서 근무하는 직원의 성과 이름 조회
(직원 정보는 employess, 사무실 정보는 offices테이블에 존재)
```SQL
-- 미국 사무실에서 일하는 직원의 이름과 성 조회
-- 미국 사무실 코드를 가지고 있는 목록
-- 직원 테이블의 officescode가 1, 2, 3인지 확인

SELECT officeCOde
FROM offices
WHERE country = 'USA';

SELECT lastName, firstName
FROM employees
WHERE officeCode IN (
	SELECT officeCode
	FROM offices
	WHERE country = 'USA'
    );
```
<!-- SubQuery 문제3 -->
주문한 적이 없는 고객 목록 조회
(고객 정보는 customers, 주문 정보는 orders 테이블에 존재)
```SQL
-- orders에는 주문한 고객들만 들어있음 -> NOT IN 
-- orders에서 고객목록을 가져와서
-- customers의 모든 정보와 위에서 가져온 고객 주문 목록을 비교
-- 결국 위에서 가져온 고객 주문 목록에 포함되지 않는 고객이 범인

SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT customerNumber
    FROM orders
);
```
<!-- SubQuery 문제4 (문제1 심화문제)-->
소비를 한 고객들 중 한번에 지불한 금액이 가장 높은 고객의 customerNumber, amount, contactFirstName을 조회
(고객 테이블은 customers,지불 테이블은 payments를 활용)
```SQL
SELECT * FROM payments;
SELECT * FROM customers;

SELECT MAX(amount)
FROM payments;

SELECT payments.customerNumber, amount, contactFirstName
FROM payments 
INNER JOIN customers
	ON payments.customerNumber = customers.customerNumber
WHERE  amount = (
	SELECT MAX(amount)
	FROM payments
    );

-- Sub사용 --
SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT *
	FROM payments
	INNER JOIN customers USING (customerNumber)
) AS mySub
WHERE  amount = (
	SELECT MAX(amount)
	FROM payments
    );
```
# **EXISTS** operator
> 쿼리 문에서 반환된 레코드의 존재 여부를 확인

## EXISTS syntax
* subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
* 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용

<!-- EXISTS 문제1 -->
적어도 한번 이상 주문을 한 고객들의 번호와 이름 조회
(고객 테이블은 customers, 주문 테이블은 orders이며 두 테이블의 customerNumber 필드를 기준으로 비교)
```SQL
SELECT customerNumber , customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);

-- 틀린값을 넣는다면?
SELECT customerNumber , customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.city = orders.customerNumber
);
-- 에러는 발생 안하지만 아무것도 출력되지 않는다!
```

<!-- EXISTS 문제2 -->
Paris에 있는 사무실에서 일하는 모든 직원의 번호,이름,성을 조회
(직원 테이블은 employees,사무실 테이블은 offices이며 두 테이블의 officecode필드를 기준으로 비교)
```SQL
SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT *
	FROM offices
	WHERE city = 'Paris' AND employees.officeCode = offices.officeCode
    );
```

# Conditional Statements

# **CASE** statement
> SQL문에서 조건문을 구성

## CASE syntax
* case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
* when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
* 동일한 값을 찾지 못하면 ELSE절의 코드를 실행
  * ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생

<!-- CASE 문제1 -->
고객들의 creditLimit에 따라 VIP,Platinum,Bronze등급을 매겨 조회
(VIP는 100000초과, Platinum은 70000초과 그 외는 Bronze로 지정)
```SQL
SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END AS grade
FROM customers;
```

<!-- CASE 문제2 -->
orders 테이블의 status에 따라 상세 정보를 매겨 조회
(in Process는 '주문중,'Shipped'는 '발주완료', 'Cancelled'는 '주문취소 그 외는'기타사유'로 지정)
```SQL
SELECT orderNumber, status,
	CASE
		WHEN status = 'In process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS details
FROM orders;
```