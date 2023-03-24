# Django_Model

## SQLite
> 오픈소스 RDBMS중 하나이며 django의 기본 DB로 사용됨(DB가 파일로 존재하며 가볍고 호환성이 좋음)

# Model
## django Model
> DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공 테이블 구조를 설계하는 **청사진(blueprint)**

## model 클래스 이해하기
* django.db.models 모듈의 Model이라는 부모 클래스를 상속 받아 작성
* model 기능에 관련된 모든 설정이 담긴 클래스
* 개발자는 테이블 구조를 어떻게 설계할 지에 대한 코드만 작성하도록 하기 위함

* 클래스 변수명
  * 테이블의 각 필드 이름

* model Field 메서드
  * 테이블 필드의 데이터 타입

* model Field 메서드의 키워드 인자
 * 테이블 필드의 제약조건 관련 설정

# Migrations
> model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법

1. model class 내용 작성
2. python manage.py makemigrations
  * model class를 기반으로 설계도(migration)작성
3. 0001 파일이 생성된걸 확인했다면
4. python manage.py migrate
  * 만들어진 설계도를 DB에 전달하여 반영
5. db 파일에 생성된걸 확인

## 이미 생성된 테이블에 추가 필드를 추가해야 한다면?
### 추가 모델 필드 작성
* 이미 기존 테이블이 존재하기 때문에 필드를 추가 할 때 필드의 기본 값 설정이 필요
* 1번은 직접 기본 값을 입력 하는 방법
* 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법

* 추가하는 필드의 기본 값을 입력해야 하는 상황
* 날짜 데이터이기 때문에 직접 입력하기 보다 django가 제안하는 기본 값을 사용하는 것을 권장
* **아무것도 입력하지 않고 enter**를 누르면 django가 제안하는 기본 값으로 설정 됨
* migrations과정 종료 후 2번째 migration 파일이 생성됨을 확인
* migrate 후 추가 필드가 적용 되었는지 확인

> model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고, 이를 DB에 반영해야 한다.
1. model class 작성 및 수정 
2. makemigrations
3. migrate

### CharField()
> 길이의 제한이 있는 문자열을 넣을 때 사용(필드의 최대 길이를 결정하는 max_length는 필수 인자)

### TextField()
> 글자의 수가 많을 때 사용

### DateTimeFielf()
> 날짜와 시간을 넣을 때 사용

### DateTimeField의 선택인자
1. auto_now
  * 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장

2. auto_now_add
  * 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

# Admin site
## Automatic admin interface
> django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
> **데이터 관련 테스트 및 확인을 하기에 매우 유용**

## admin 계정 생성
python manage.py createsuperuser
> **email은 선택사항이기 때문에 입력하지 않고 진행 가능**

> **비밀번호 생성 시 보안상 터미널에 출력되지 않으니 무시하고 입력을 이어가도록 함**

#### 참고
##### Migrations 기타 명령어
python manage.py showmigrations
* migratuins 파일들이 migrate됐는지 안됐는지 여부를 확인하는 용도
* [X]표시가 있으면 migragte가 완료되었음을 의미

python manage.py sqlmigrate articles 0001
* 해당 migrations 파일이 SQL문으로 어떻게 해석 되어 DB에 전달되는지 확인하는 용도

##### 첫 migrate 시 출력 내용이 많은 이유는?
* 기본적으로 Django 프로젝트가 동작하기 위해 작성되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate되기 때문