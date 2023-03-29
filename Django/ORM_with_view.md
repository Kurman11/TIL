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