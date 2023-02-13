# Filtering data 관련 Keywords
## 데이터를 필터링하여 중복 제거, 조건 설정 등 SQL Query를 제어하기
* Clause
  * DISTINCT
  * WHERE
  * LIMIT
* Operator
  * BETWEEN
  * IN
  * LIKE
  * Comparison
  * Logical

  ## **DISTINCT** clause
  > 조회 결과에서 중복된 레코드를 제거

  DISTINCT syntax
  ```SQL
  SELECT DISTINCT
    select_list
  FROM
    table_name;
  ```
  * SELECT 키워드 바로 뒤에 작성
  * SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

테이블 employees에서 lastName 필드의 모든 데이터를 중복없이 오름차순 조회
  ```SQL
  SELECT DISTINCT
  	lastName
  From
  	employees
  ORDER BY
  	lastName ASC;
  ```