# Cookie&Session
> 우리가 서버로부터 받은 페이지를 둘러볼 때 우리는 서버와 연결되어 있는 상태일까? - **NO**

## HTTP
> HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약 웹(www)에서 이루어지는 모든 데이터 교환의 기초

### HTTP 특징
1. 비 연결 지향(connectionless)
  * 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

2. 무상태(stateless)
  * 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

### 무상태로 인한 문제
* 장바구니에 담은 상품을 유지할 수 없음
* 로그인 상태를 유지할 수 없음
* ...

# 쿠키 (Cookie)
> 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
> 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 사용자 추적, 상태 유지등에 사용되는 데이터 저장 방식

## 쿠키 사용 예시
web ->  The browser requests a web page
The server sends the page and the cookie  <- web server
web -> The browser requests another page from the same server

1. 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
2. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
> 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  * 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  * 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 떄문


## 쿠키 사용 목적
1. 세션 관리(Session management)
  * 로그인,아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화(Personalization)
  * 사용자 선호, 테마 등의 설정

3. 트래킹(Tracking)
  * 사용자 행동을 기록 및 분석

* 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송한다.
> **로그인 되어있다는 사실을 입증할 데이터를 계속 보내는 것**

## 세션(Session)
> 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지 상태 정보를 저장하는 데이터 저장 방식
> **쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄**

### 세션 작동 예시
1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장
2. 생성된 session 데이터에 인증 할 수 있는 session id를 발급
3. 발급한 session id를 클라이언트에게 응답
4. 클라이언트는 응답 받은 session id를 쿠키에 저장
5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
6. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인ㄴ해 로그인 되어있다는 것을 알도록 함

* 세션은 서버 측에서 저장됨
* 서버 측에서는 세션 ID를 생성하고, 이 ID를 클라이언트 측으로 전달하여, 클라이언트는 쿠키에 이ID를 저장

### 쿠키와 세션의 목적
> 클라이언트와 서버 간의 상태를 유지

#### 참고
##### 쿠키 종류별 Lifetime(수명)
1. Session cookie
  * 현재 세션(current session)이 종료되면 삭제됨
  * 브라우저 종료와 함께 세션이 삭제됨

2. Persistent cookies
  * Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

##### 세션 in django
* Django는 'database-backed sessions'저장 방식을 기본 값으로 사용
* session 정보는 DB의 django_session 테이블에 저장
* session 정보는 DB의 **django_session** 테이블에 저장
* Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
* Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

# Authentication_system1 (인증 시스템)
> 사용자 인증과관련된 기능을 모아 놓은 시스템 인증과 권한 부여를 함께 제공 및 처리

```python
INSTALLED_APPS = [
    'articles',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth', # user
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Authentication(인증)
> 사용자가 자신이 누구인지 확인하는 것 신원 학인

## Authorization(권한,허가)
> 인증된 사용자가 수행할 수 있는 작업을 결정 권한 부여

### 사전 설정
* 두번째 app accounts생성 및 등록
> **auth와 관련한 경로나 키워드들을 django내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장**

# Custom User model
## Custom User model로 대체하기
> django가 기본적으로 제공하는 User model은 내장된 auth모듈의 User클래스를 사용
> **별도의 설정 없이 사용할 수 있어 간편하지만, 직접 수정할 수 없는 문제**

### 반드시 User 모델을 대체해야 할까?
* Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분하더라도 커스텀 User모델을 설정하는 것을 강력하게 권장(highly recommended)
* 커스텀 User모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 떄문
* 단,User모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

# Login
> Session을 Create하는 과정

## AuthenticationForm()
> 로그인을 위한 built-in form

## login(request, user)
> 인증된 사용자를 로그인 하는 함수

## get_user()
> AuthenticationForm의 인스턴스 메서드 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

```python
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }

    return render(request,'accounts/login.html', context)
```


# Logout
> Session을 Delete 하는 과정

## Logout(request)
1. 현재 요청에 대한 session data를 DB에서 삭제
2. 클라이언트의 쿠키에서도 sessionid를 삭제

```python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

# Template with Authentication data

## 템플릿에서 인증 관련 데이터를 출력하는 방법
```html
 <h3>안녕하세요.{{ user }} 님!</h3>
```

## context processors
* 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
* 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
* 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것


#### 참고
##### 'AbstractUser' class
* '관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스'

* Abstract base classes(추상 기본 클래스)
  * 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  * 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨

* 유저 대체하기
* 세셔을 만들고 지우기 (로그인 & 로그아웃)
* 템플릿에 유저 출력하기