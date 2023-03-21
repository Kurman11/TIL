# Django_design_pattern

# django 프로젝트와 앱
## django project
> 애플리케이션의 집합(DB설정, URL연결, 전체 앱 설정 등을 처리)

## django application
> 독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)
> **MTV패턴에 해당하는 파일 및 폴더를 담당**

## 만약 블로그를 만든다면

* 프로젝트
> 블로그(전체 설정 담당)

* 앱
> 게시글, 댓글, 카테고리 회원 관리 등(DB,로직,화면)

## 앱 생성
python manage.py startapp 이름(**앱의 이름은 '복수형'으로 지정하는 것을 권장**)

# django 디자인 패턴
## (소프트웨어) 디자인 패턴
> 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책(공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)

## MVC 디자인 패턴
* (Model-View-Controller)
> 애플리케이션을 구조화하는 대표적인 패턴(데이터, 사용자 인터페이스, 비즈니스 로직을 분리)
> **시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수할 수 있는 애플리케이션을 만들기 위해**

## MTV 디자인 패턴
* (Model-Template-View)
> django에서 애플리케이션을 구조화하는 패턴(기존 MVC패턴과 동일하나 명칭을 다르게 정의)

View -> Template 
Controller -> View  우리가 이게더 적절해 보여서 바꿈 
근본적인 거는 MVC와 똑같다 하지만 명칭이 다르니 주의하자

## 프로젝트 구조
### 봐야할 것
* settings.py
  * 프로젝트의 모든 설정 관리

* urls.py
  * URL과 이에 해당하는 적절한 views를 연결


### 내용을 몰라도 되는... 아직 사용안함
* __init__.py
  * 해당 폴더를 패키지로 인식하도록 설정

* asgi.py
  * 비동기식 웹 서버와의 연결 관련 설정

* wsgi.py
  * 웹 서버와의 연결 관련 설정

* manage.py
  * Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
> **모두 현재단계에서는 별도로 수정하지 않음**

## 앱 구조

### 봐야할 것
* admin.py
  * 관리자용 페이지 설정

* models.py
  * DB와 관련된 Model을 정의
  * MTV패턴의 M

* views.py
  * HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환(url,mode,template과 연계)
  * MTV 패턴의 V

  ### 안봐도됨

  * apps.py
    * 앱의 정보가 작성된 곳
  
  * tests.py
    * 프로젝트 테스트 코드를 작성하는 곳
  > **모두 현재단계에서는 별도로 수정하지 않음**


  ### 데이터 흐름
  3.요청을 2.urls.py가 가장 먼저 받고 3.views.py (함수)로 보내준다 4.(models.py,templates)로 정보를 주고 받고 다시 views.py 에서 5. 응답으로 보내준다.

  # 요청과 응답

  ## URLs
  > http://128.0.0.1:8000/**articles/** 로 요청이 왔을 때 **views** 모듈의 **index** 뷰 함수를 호출한다는 뜻

  ## View
  > 특정 경로에 있는 template과 request객체를 결합해 응답 객체를 반환하는 index뷰 함수 정의

  ## Template
  1. articles 앱 폴더안에 templates 폴더 생성
  2. templates 폴더 안에 템플릿 페이지 작성
  > **반드시 templates폴더명이어야하며 개발자가 직접 생성해야함**

  ### django에서 template을 인식하는 경로 규칙
  **app폴더 / templates/** articles/ index.html
  **app폴더 / templates/** example.html
  > django는 bold지점 까지 기본 경로로 인식하기 때문에 이 지점 이후의 template경로를 작성해야 함

  ### 데이터 흐름에 따른 코드 작성
  > URLs -> View -> Template

  ### 데이터 흐름에 따른 코드 작성
  URLs : path('articles/', **views.index**),
  View : def **index** (request):
            return render(request,**'articles/index.html'**)
  Template : articles/templates/**articles/index.html**

  #### 참고

  ##### render 함수
  * 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
  
  1. request
    * 응답을 생성하는 데 사용되는 요청 객체
  2. template_name
    * 템플릿 이름의 경로
  3. context
    * 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)