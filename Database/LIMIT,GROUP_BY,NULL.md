### LIMIT syntax
* LIMIT clause는 하나 또는 두 개의 인자를 사용(0또는 양의 정수)
* row_count는 조회할 최대 레코드 수를 지정

테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 7개만 조회
```SQL
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 7;
```
테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 4번쨰부터 7번째 데이터만 조회
```SQL
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 3,5;
```

### GROUP BY clause
> 레코드를 그룹화하여 요약본 생성 with **집계 함수**

### Aggregation Functions
값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
SUM, AVG, MAX, MIN, COUNT

테이블 customers에서 country필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균 값을 내림차순 조회
```SQL
SELECT
	country, AVG(creditLimit) AS avgOFCreditLimit
FROM
	customers
GROUP BY
	country
ORDER BY
	avgOFCreditLimit DESC;
```

테이블 customers에서 country필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균 값이 80000을 초과하는 데이터만 조회
```SQL
SELECT
	country, AVG(creditLImit)
FROM
	customers
-- WHERE
-- 	AVG(creditLImit) > 80000
GROUP BY
	country
HAVING
	AVG(creditLImit) > 80000;
```
### SELECT statement 실행 순서
1. 테이블에서 (FROM)
2. 특정 조건에 맞춰(WHERE)
3. 그룹화 하고 (GROUP BY)
4. 만약 그룹 중에서 조건이 있다면 맞추고 (HAVING)
5. 조회하여 (SELECT)
6. 정렬하고 (ORDER BY)
7. 특정 위치의 값을 가져온다 (LIMIT)

### 정렬에서의 NULL
* MySQL에서 NULL은 NULL이 아닌 값 앞에 위치
  * NULL값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

```SQL
SELECT
	postalCode
FROM
	customers
WHERE
	postalCode IS NOT NULL
ORDER BY
	postalCode;
```