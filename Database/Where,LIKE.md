# WHERE

**WHERE** clause
> 조회 시 특정 검색 조건을 지정

테이블 employees에서 officeCode 필드 값이 1인 데이터의 lastName,firstName,officeCode 조회
```SQL
SELECT
	lastName , firstName, officecode
FROM
	employees
WHERE
	officeCode = '1'
  ```

테이블 employees에서 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName,firstName,jobTitle 조회
```SQL
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != 'Sales REP';
```

테이블 employees에서 officeCode 필드 값이 3이상이고 jobTitle 필드 값이 'Sales Rep'인 데이터의 lastName,firstName,officeCode,jobTitle 조회

```SQL
SELECT
	lastName, firstName,officecode, jobTitle 
FROM
	employees
WHERE
	officecode >= 3 
    AND jobTitle = 'Sales Rep'; 
```
테이블 employees에서 officeCode 필드 값이 5미만이거나 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName,firstName,officeCode,jobTitle 조회

```SQL
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 5
    OR jobTitle != 'Sales Rep';
```
테이블 employees에서 officeCode 필드 값이 1에서4 사이 값인 데이터의 lastName,firstName,officeCode를 조회
```SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
-- 동일한 코드
-- WHERE
-- 	 officeCode >= 1
--     AND officeCode <= 4;
	officeCode BETWEEN 1 AND 4;
```
테이블 employees에서 officeCode 필드 값이 1에서4 사이 값인 데이터의 lastName,firstName,officeCode 오름차순 조회
```SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
-- 	officeCode >= 1
--     AND officeCode <= 4;
	officeCode BETWEEN 1 AND 4
ORDER BY
	officeCode ASC;
```
테이블 employees에서 officeCode 필드 값이 1또는 3또는 4값인 데이터의 lastName,firstName,officeCode 조회
```SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
-- 	officeCode = '1'
--     or officeCode = '3' 
--     or officeCode = '4';
	officeCode in (1,3,4);
```
테이블 employees에서 officeCode 필드 값이 1또는 3또는 4값이 아닌 데이터의 lastName,firstName,officeCode 조회
```SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1,3,4);
```

테이블 employees에서 lastName 필드 값이 son으로 끝나느 데이터의 lastName,firstName 조회
```SQL
SELECT
	lastName,firstName
FROM
	employees
WHERE
	lastName LIKE '%son';
```

테이블 employees에서 lastName 필드 값이 4자리면서 y로 끝나느 데이터의 lastName,firstName 조회
```SQL
SELECT
	lastName,firstName
FROM
	employees
WHERE
	firstName LIKE '____y';
```

### **LIKE** operateor
> 값이 특정 패턴에 일치하는지 확인 wihh Wildcards

### Comparison Operators
> 비교 연산자
* =, >=, <=, !=, IS, LIKE, IN, BETWEEN ... AND

### Logical Operators
> 논리 연산자
* AND(&&), OR(||), NOT(!)

### **IN** operators
> 값이 특정 목록 안에 있는지 확인

### **LIKE** operator
> 값이 특정 패턴에 일치하는지 확인 with wildcards

### Wildcard Characters
* '%' = **0개 이상의 문자열**과 일치 하는지 확인
* '_' = **단일 문자**와 일치 하는지 확인

### **LIMIT** clause
* 조회하는 레코드 수를 제한