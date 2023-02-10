# SQL
SQL : Structure(구조) Query(질의->질문->요청) Language(언어)  
테이블의 형태로 **구조화**된 관계형 데이터베이스 에게 요청을 **질의(요청)**  
데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

## SQL Syntax
* SQL 키워드는 대소문자를 구분하지 않음
  * 하지만 대문자로 작성하는 것을 권장(명시적 구분)
* 각 SQL Statements의 끝에는 세미콜론(;)이 필요
  *  세미콜론은 각 SQL Statements을 구분하는 방법

## SQL Statements (SQL문)
SQL 언어를 구성하는 가장 기본적인 코드 블록

데이터베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉨
* DDL - 데이터 정의 -> 구조
  * 역할 : 데이터의 기본 구조 및 형식 변경
  * SQL 키워드 : CREATE,DROP,ALTER
* **DQL** - 데이터 검색 -> R
  * 역할 : 데이터 검색 
  * SQL 키워드 : **SELECT**
* DML - 데이터 조작 -> C,U,D
  * 역할 : 데이터 조작(추가,수정,삭제)
  * SQL 키워드 : INSERT,UPDATE,DELETE
* DCL - 데이터 제어 -> 컨트롤 : 권한,계정
  * 역할 : 데이터 및 작업에 대한 사용자 권한 제어
  * SQL 키워드 : COMMIT,ROLLBACK,GRANT,REVOKE

SQL은 데이터 베이스와 상호작용하고 데이터베이스에서 데이터를 **반환**하기 위한 언어

