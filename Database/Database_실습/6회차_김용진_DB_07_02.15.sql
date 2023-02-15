-- DB-07-SQL - Multi Table Queries

SELECT * FROM productlines;

-- 문제1
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	on employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber ASC;

-- 문제2
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers 
LEFT JOIN offices 
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제3
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- 문제4
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
INNER JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
    
-- 문제5
-- 문제2의 LEFT JOIN은 offices 테이블의 일치하는 레코드와 함께 customers 테이블의 모든 레코드를 반환합니다. NULL은 customers 테이블의 모든 레코드중 offices 테이블이 존재하지 않기 때문에 나옵니다.
-- 문제3의 RIGHT JOIN은 customers 테이블의 일치하는 레코드와 함께 offices 테이블의 모든 레코드를 반환합니다. NULL은 offices 테이블의 모든 레코드중 customers 테이블이 존재하지 않기 때문에 나옵니다.
-- 문제4의 INNER JOIN은 customers 테이블과 offices의 테이블에서 데이터를 검색하는 방법입니다.

-- 문제6
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
union
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- 문제7
SELECT t1.orderNumber, orderDate
FROM orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
ORDER BY 
	orderNumber ASC;

-- 문제8
SELECT orderNumber, t1.productCode, productName
FROM orderdetails AS t1
INNER JOIN products AS t2
	ON t1.productCode = t2.productCode
ORDER BY
	orderNumber ASC;

-- 문제9
SELECT t1.orderNumber, t1.productCode, orderDate, productName
FROM orderdetails AS t1  -- orderNumber, productCode, productName다 가지고있음
INNER JOIN orders AS t2 -- 문제7 orderNumber, orderDate 가지고있음
	ON t1.orderNumber = t2.orderNumber 
INNER JOIN products AS t3 -- 문제8 orderNumber, productCode, productName 가지고있음
	ON t1.productCode = t3.productCode
ORDER BY
	orderNumber ASC;
