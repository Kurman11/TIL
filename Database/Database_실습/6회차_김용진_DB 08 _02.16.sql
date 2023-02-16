-- DB 08 - SQL Nested queries

-- 문제1
SELECT * FROM products;

SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY
	MSRP ASC;
    
-- 문제2
SELECT * FROM customers;
SELECT * FROM orders;

SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY
	customerNumber ASC;
    
-- 문제3

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP IN(
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = 'Classic Cars'
);

-- 문제4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	SELECT country
    FROM(
		SELECT country, COUNT(country) AS cnt
		FROM customers
		GROUP BY country
		) AS hi
	ORDER BY cnt DESC LIMIT 1
    )
ORDER BY customerNumber ASC;
    
    
-- SELECT customerNumber, customerName, country
-- FROM customers
-- WHERE country IN(
-- 	SELECT MAX(country)
--     FROM customers
-- )
-- ORDER BY
-- 	customerNumber ASC; country가 사전적으로 MAX라 USA가 나오므로 이건 틀림

-- 문제5
SELECT * FROM customers;
SELECT * FROM orders;

SELECT customers.customerNumber, customerName, COUNT(customers.customerNumber) AS order_count
FROM customers
INNER JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE customers.customerNumber IN(
	SELECT customers.customerNumber
    FROM orders)
GROUP BY
	customers.customerNumber
ORDER BY
	order_count DESC
LIMIT 1;

-- 문제6
SELECT * FROM orderdetails;
SELECT * FROM orders;
SELECT * FROM products;

SELECT DISTINCT t1.productCode, productName
FROM products AS t1
INNER JOIN	orderdetails AS t2
	ON t1.productCode = t2.productCode
INNER JOIN orders AS t3
	ON t2.orderNumber = t3.orderNumber
WHERE orderDate IN (
	SELECT orderDate
    FROM orders
    WHERE orderDate LIKE '2004-__-__'
    )
ORDER BY
	productCode DESC;
