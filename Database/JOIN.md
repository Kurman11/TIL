# SQL - Multi Table Queries
## introduction to Join
* 권미자가 작성한 모든 게시글을 조회하기
> 동명이인이 있따면.. 혹은 특정 데이터가 수정된다면 **데이터 관리**가 너무 어렵다
### JOIN
* 테이블을 분리하면 관리는 용이해질 수 있으나 출력 할 때는 테이블 한개만을 출력할 수 밖에 없어 **다른 테이블과 연결지어 출력**하는 것이 필요

# Joining tables
## JOIN clause
> 둘 이상의 테이블에서 데이터를 검색하는 방법

## INNER JOIN syntax
* FROM 절 이후 메인 테이블 지정(table1)
* INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정 (table2)
* ON 키워드 이후 조인 조건을 작성
  * 조인 조건은 table1과 table2간의 레코드를 일치시키는 규칙을 지정

<!-- INNER JOIN 문제1 -->
제시된 두 테이블을 참고하여 productLine 값이 같은 레코드의 productCode, productName, textDescription 필드를 조회

```SQL
SELECT
	productCode, productName, textDescription
FROM 
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;
```

<!-- INNER JOIN 문제2 -->
제시된 두 테이블을 참고하여 orderNumber 갑이 같은 레코드의 orders 테이블 orderNumber, status, priceEach 필드를 조회
```SQL
SELECT
	orders.orderNumber, status, priceEach
FROM
	orders
INNER JOIN orderdetails
	on orders.orderNumber = orderdetails.orderNumber;
```

<!-- INNER JOIN 문제3 -->
직전 조회 결과를 바탕으로 각 주문번호 별 총 판매액을 요약(주문 번호는 orderNumber 필드, 총 판매액은 quantityOrdered와 priceEach필드의 곱셈 결과)
```SQL
SELECT
	orders.orderNumber, status, SUM(priceEach*quantityOrdered) AS totalSales
FROM
	orders
INNER JOIN orderdetails
	on orders.orderNumber = orderdetails.orderNumber
GROUP BY
	orderNumber;
```

## **LEFT JOIN** clause
> 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

## LEFT JOIN syntax
* FROM절 이후 왼쪽 테이블 지정(table1)
* LEFT JOIN절 이후 오른쪽 테이블 지정(table2)
* ON키워드 이후 조인 조건을 작성
  * 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴

### LEFT JOIN 특징
* 왼쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
* 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 왼쪽 레코드를 여러 번 표시

<!-- LEFT JOIN 문제1 -->
제시된 두 테이블을 참고하여 customers를 기준으로 customerNumber 필드가 일치하는 레코드와 함께 customers 테이블 contactFirstName와 orders테이블의 orderNumber, status필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 orders. 일치하지 않는 경우 NULL)
```SQL
SELECT
	contactFirstName, orderNumber, status
FROM
	customers
LEFT JOIN
	orders
	ON customers.customerNumber = orders.customerNumber;
```

<!-- LEFT JOIN 문제2 -->
직전 조회 결과를 바탕으로 주문내역이 없는 고객의 이름과 주문번호 및 배송상태 조회 (고객의 이름은 contactFirstName필드, 주문번호는 orderNumber, 배송상태는 status필드)
```SQL
SELECT
	contactFirstName, orderNumber, status
FROM
	customers
LEFT JOIN
	orders
	ON customers.customerNumber = orders.customerNumber
WHERE
	orderNumber IS NULL;
```

# **RIGHT JOIN clause
> 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

## RIGHT JOIN syntax
* FROM 절 이후 왼쪽 테이블 지정(table1)
* RIGHT JOIN 절 이후 오른쪽 테이블 지정(table2)
* ON키워드 이후 조인 조건을 작성
  * 오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴

### RIGHT JOIN 특징
* 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
* 오른쪽 테이블 한 개의 레코드에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러 번 표시

<!-- RIGHT JOIN 문제1 -->
제시된 두 테일블을 참고하여 employeeNumber 필드와 salesRepEmployeeNumber 필드가 일치하는 레코드와 함께 employeeNumber, firstName, customerNumber, contactFirstName 필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 employees, 일치하지 않는 경우 NULL)

```SQL
SELECT
	employeeNumber, firstName,customerNumber,contactFirstName
FROM
	customers	
RIGHT JOIN
	employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber;
```

<!-- RIGHT JOIN 문제2 -->
직전 조회 결과를 바탕으로 고객에게 판매한 내역이 없는 직원 목록 조회
(직원 번호와 이름은 employeeNumber, firstName 필드이며 고객 번호와 이름은 customerNumber, contactFirstName필드)
```SQL
SELECT
	employeeNumber, firstName,customerNumber,contactFirstName
FROM
	customers	
RIGHT JOIN
	employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE
	customerName IS NULL;
```