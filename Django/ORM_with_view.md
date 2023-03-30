# ORM UPDATE
## 데이터 수정
article = Articles.objects.get(pk=5)
article.title='수정제목'

## 데이터 삭제
article.delete()

# ORM_with_view

## 사전준비
* app URLs 분할 및 연결
* index 페이지 작성

# READ
* 전체 게시글 조회
* 단일 게시글 조회

## 전체 게시글 조회
```python
# views
from django.shortcuts import render
from articles.models import Articles
# Create your views here.

def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request,'articles/index.html',context)

# urls
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.index , name='index'),

]
```
```html
  <h1>Articles</h1>
  <p>{{articles}}</p>
  {% for article in articles %}
    <p>제목: {{article.title}}</p>
    <p>내용: {{article.content}}</p>
    <hr>
  {% endfor %}
```
## 단일 게시글 조회
```python
# views
def detail(request, number):
    article = Articles.objects.get(pk=number)
    # print(article)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html',context)
```

```html
  {% for article in articles %}
    <p>제목: 
      <a href="{% url 'articles:detail' article.pk %}">{{article.title}}</a></p>
    <p>내용: {{article.content}}</p>
    <hr>
  {% endfor %}
```

# CREATE
## Create 로직을 구현하기 위해 필요한 view 함수
* 사용자의 입력을 받는 페이지를 렌더링 **new**
* 사용자가 입력한 데이터를 받아 DB에 저장 **create**


# ORM_with_view
## HTTP request methods
> 게시글 작성 후 작성 완료를 나타내는 페이지를 렌더링 하는 것
> 게시글을 '조회해줘!'라는 요청이 아닌 '작성해줘!' 라는 요청이기 때문에 페이지 랜더링은 적절한 응답이 아님

* 데이터 저장 후 유저를 어디론가 다시 보내야 한다.
## redirect()
> 인자에 작성된 주소로 다시 요청을 보냄
```python
from django.shortcuts import render,redirect
def create(request):
    # new에서 보낸 사용자 데이터를 받아서 변수에 할당
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 받은 데이터를 DB에 저장
    # 1 
    # article = Articles()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2
    article = Articles(title=title, content = content)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법을 택함
    article.save()

    # 3
    # Articles.objects.create(title=title, content = content)
    # 결과 페이지 반환
    # return render(request,'articles/create.html')

    # 결과 페이지(전체 조회 템플릿) 반환
    # return render(request,'articles/index.html')

    # 이동 주소(URL)를 사용자에게 응답
    # return redirect('articles:index')

    # 생성한 글의 단일 조회 주소로 이동 응답
    return redirect('articles:detail', article.pk)
  ```

## HTTP
> 네트워크 상에서 데이터를 주고 받기위한 약속

### HTTP request methods
> 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
> **GET&POST**

### 'GET' Method
> 특정 리소스를 조회하는 요청(GET으로 데이터를 전달하면 Query string 형식으로 보내짐)
> **반드시 데이터를 (조회)가져올 대만 사용해야 함**

### 'POST' Method
> 특정 리소스에 변경사항을 만드는 요청 (POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐)

### HTTP response status code
> 특정 HTTP요청이 성공ㅈ거으로 완료되었는지 알려줌
> 5개의 그룹으로 나뉘어짐(1xx,2xx,3xx,4xx,5xx)

### 403Forbidden
> 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

### CSRF
> 사이트 간 요청 위조
> 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정,삭제등의 작업을 하게 만드는 공격 방법

### Security Token(CSRF Token)
> 대표적인 CSRF 방어 방법

1. 서버는 사용자 입력 데이터에 임의의 난수 값(token)을 부여
2. 매 요청마다 해당 token을 포함시켜 전송 시키도록 함
3. 이후 서버에서 요청을 받을 때마다 전달된 token이 유효한지 검증

POST Method는 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것

```python
<form action="{% url 'articles:create' %}" method ='POST'>
    {% csrf_token %}

title = request.POST.get('title')
content = request.POST.get('content')
```

# DELETE
```python
# 데이터 삭제를 위한 URL 패턴
path('<int:pk>/delete/',views.delete, name='delete')

def delete(request,pk):
    # 삭제할 데이터 조회
    article = Articles.objects.get(pk=pk)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect('articles:index')

 <form action="{% url 'articles:delete' article.pk %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value = '삭제'>
  </form>
```

# Update
## Update로직을 구현하기 위해 필요한 view함수
* 사용자의 입력을 받는 페이지를 렌더링 **edit**
* 사용자가 입력한 데이터를 받아 DB에 저장 **update**

```python
# 데이터 수정 로직에 대한 URL 패턴
path('<int:pk>/update/',views.update,name='update'),

def update(request,pk):
    # 수정 작업 과정
    # 1. 데이터 조회
    article = Articles.objects.get(pk=pk)
    # 2. 데이터 수정
    # 2-1 사용자가 입력한 form 데이터 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2-2 조회한 데이터(article)의 필드 값 변경
    article.title = title
    article.content = content

    # 3. 데이터 저장
    article.save()

    return redirect('articles:detail', article.pk)

      <h1>Edit</h1>
  {{article}}
  <form action="{% url 'articles:update' article.pk %}" method ='POST'>
    {% csrf_token %}
    <div>
      <label for="title">제목: </label>
      <input type="text" name='title' id ='title' value='{{article.title}}'>
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
    </div>
    <input type="submit" value='[UPDATE]'>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
</body>
</html>
```

#### 참고
메서드를 분리함으로써 효율적으로 관리할수있는 방법이 있다 나중에 배울 예정

