# Static_files
> 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지,JS,CSS 파일 등)

## 웹 서버와 정적 파일
* 웹 서버의 기본동작은
  * 특정 위치(URL)에 있는 자원을 요청(HTTP requese)받아서
  * 응답(HTTP requese)을 처리하고 제공(serving)하는 것
* 이는 '자원에 접근 가능한 주소가 있다' 라는 의미
* 웹 서버는 요청받은 URL로 서버에 존재한는 정적 자원(static resource)을 제공함
* **결국, 정적 파일을 제공하기 위한 경로(URL)가 있어야 함**

# Static files 제공하기
* 기본 경로
  > app/static/

* 추가 경로
 >STATICFILES_DIRS

```html
{% load static %}
<img src="{% static 'articles/sample-1.png' %}" alt="img">
```

## STATIC_URL
> 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL 실제 파일이나 디렉토리가 아니며, URL로만 존재
  **비어 있지 않은 값으로 설정한다면 반드시 slash[/]로 끝나야함**

URL + STATIC_URL + 정적파일 경로

# Media Files
> 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

## ImageField()
> 이미지 업로드에 사용하는 모델 필드
**이미지 객체가 직접 저장되는 것이 아닌 '이미지파일의 경로 문자열'이 DB에 저장**

## 미디어 파일을 제공하기 전 준비
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정


### MIDIA_URL
> MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
(STATIC_URL과 동일한 역할)

# 이미지 업로드 및 제공하기

models.py 에서 
image = models.ImageField(blank=True) 작성
blank = True 속성을 작성해 빈 문자열이 저장될 수 있도록 설정


* url속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
```html
<img src="{{article.image.url}}" alt="image" >
```
  * article.image.url - 업로드 파일의 경로
  * article.image - 업로드 파일의 파일 이름

* 수정 페이지 form 요소에 enctype 속성 추가
```html
enctype ='multipart/form-data'
```
* view 함수에서 업로드 파일에 대한 추가 코드 작성
request.FILES 작성

