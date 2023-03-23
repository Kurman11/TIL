# django_URLs

# URL dispatcher (운항 관리자, 분배기)
> URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑: mapping)

# 변수와 URL

* 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까? -> 각 게시글의 세부 페이지

## Variable Routing
> URL 일부에 변수를 포함시키는 것 (변수는 view함수의 인자로 전달 할 수 있음)

### Variable Routing작성법

<path_converter:variable_name>
    (타입)     (:) (변수 이름)

### Path converters
> URL 변수의 타입을 지정 (str,int등 5가지 타입 지원)
* URL로 문자열 타입의 변수를 받아서 받은 문자열을 템플릿에서 출력하도록 작성

# App 의 URL

## App URL mapping
> 각 앱에 URL을 정의하는 것
> 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소 관리를 편하게 하기 위함

## include()
> 다른 URL들을 참조할 수 있도록 돕는 함수 (URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 후속 처리를 위해 include된 URL로 전달)

# URL이름 지정
> 기존 'articles/' 주소가 'articles/index/'로 변경됨
> 기존에 articles/주소를 사용했던 모든 위치를 찾아 변경해야 함

## Naming URL patterns
> URL에 이름을 지정하는 것 (path 함수의 name 인자를 정의해서 사용)
### 'url' tag
> 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
{% url 'url-name' arg1 arg2 %}

#### NoReverseMatch
> 무조건 url 관련 문제

## URL 이름 지정 후 남은 문제
> articles 앱의 url 이름과 pages앱의 url 일므이 같음 단순히 이름만으로는 분리가 어려운 상황

### app_name 속성 지정
> url 이름 + app 이름표 붙이기
### URL tag의 변화
{% url 'index' %} -> { url 'articles:index %}

#### 참고
##### app_name 지정후 주의사항
* app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용할 수 있음
* 그렇지 않으면 NoreverseMatch에러가 발생
* 즉, app_name 지정 후 다음과 같은 표기는 사용 불가
    * {% url 'index' %}

##### Trailing Slashes
* django는 URL끝에 '/'가 없다면 자동으로 붙임
* django의 url 설계 철학
    * "기술적인 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL 이다."
* 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이두 주소를 서로 다른 페이지로 봄
* 그래서 django는 검색 엔진이 혼동하지 않게 하기 위해 사용
* 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님