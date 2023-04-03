# Form,Handling_HttP_requests

# HTML Form
> 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용중

> **우리가 원하는 데이터 형식이 맞는지에 대한 '유효성 검증' 필요**

## 유효성 검사
> 수집한 데이터가 정확하고 유효한지 확인하는 과정
> 유효성 검증에는 입력 값, 형식, 중복, 범위, 보안 등 부가적인 많은 것들을 고려해야 함
> 이런 과정과 기능을 제공해주는 **도구**가 필요

# Django Form
> 사용자 입력 데이터를 수집하고, 처리 및 유효성 검증을 수행하기 위한 도구
**유효성 검사를 단순화하고 자동화 할 수있는 기능을 제공**

```python
  <h1>New</h1>
  <form action="{% url 'articles:create' %}" method ='POST'>
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
```

# Widgets
> HTML 'input' element의 표현을 담당
```python
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.CheckboxInput)
```

# Django ModelForm
* Form
  > 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex.로그인)

* ModelForm
  > 사용자 입력 데이터를 DB에 저장해야 할 때 (ex.회원가입)
```python
from django import forms
from .models import Articles

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.CheckboxInput)

class ArticleForm(forms.ModelForm):
    # inner class? 개념? 파이썬 문법과 아무런 상관없고
    # 그냥 django ModelForm의 구조가 이렇게 설계되었을 뿐
    class Meta:
        model = Articles
        fields = '__all__'
        # fields = ('title','content')
        # exclude = ('titlc',)
```


#### 메타 데이터
> 데이터에 대한 데이터

* 컴퓨터에게 사진은 데이터

* 사진의 메타 데이터
- 화소
- 언제
- 어떤 기종
- 조리개 값
....

## is_vaslid()
> 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
```python
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        context ={
            'form': form,
        }

    return render(request,'articles/new.html',context)
```

## save()
> 데이터베이스 객체를 만들고 저장 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정


#### 참고
##### Widget 응용

```python
class ArticleForm(forms.ModelForm):
    # inner class? 개념? 파이썬 문법과 아무런 상관없고
    # 그냥 django ModelForm의 구조가 이렇게 설계되었을 뿐
    title = forms.CharField(
        label= '제목',
        widget= forms.TextInput(
            attrs ={
                'class' : 'my-title',
                'placeholder' : '제목을 입력해주세요.',
            }
        )
    )
```

##### Meta class ?
* 클래스 안애 클래스..? 파이썬에는 inner class라고 하는데..
* 파이썬의 문법적 개념으로 접근하지 말 것
* 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐 우리는 **ModelForm의 역할과 사용법을 숙지하는데 집중** 할 것

# Handling HTTP requests
HTTP requests 처리에 따른 view 함수 구조 변화

## new & create view 함수간 공통점과 차이점

* 공통점
  > '데이터 생성 로직을 구현하기 위함'

* 차이점
  > 'new는 GET method 요청만을, create는 POST method 요청만을 처리'


## new 와 view 함수 결합
```python
def create(request):
    # HTTP requests method POST라면
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    # POST가 아니라면
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request,'articles/new.html',context)
```

## 새로운 update view 함수

```python
def update(request, article_pk):
    article = Articles.objects.get(pk=article_pk) # ORM
    if request.method == 'GET':        # HTTP method
        form = ArticleForm(instance=article) # Class, 인스턴스
    
    else:
        article = Articles.objects.get(pk=article_pk)
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk) # URL, 

    context ={
        'form': form,
        'article' : article,
    }
    return render(request,'articles/edit.html',context)
```
