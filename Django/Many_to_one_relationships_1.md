# Many_to_one_relationships_1

# 관계형 데이터베이스의 N:1 관계
* 외래키(Foreign Key)를 가지고 있는 쪽이 N쪽의 관계이다

## 외래키(Foreign Key)
> 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
> 각 레코드에서 서로 다른 테이블 간의 '관계'를 만드는 데 사용

# Comment & Article

## Many to one relationships
> N:1 or 1:N

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

## Comment(N) - Article(1)
> '0개 이상의 댓글은 1개의 게시글에 작성 될 수 있다.'

외래키를 들고 있는 쪽은 참조
1을 들고있는 곳은 역참조라고함

## Foreignkey()
> django에서 N:1 관계 설정 모델 필드

## Comment 모델 정의
* ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

* Foreignkey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨

* ForeignKey(to, on_delete)
  * to ('참조하는 모델 class이름')
  * on_delete('참조하는 모델 class가 삭제 될 때 연결된 하위 객체의 동작을 결정')
    > 외래 키가 참조하는 객체(1)가 사라졌을 때 외래 키를 가진(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    > 'CASCADE' 부모 객체(참조 된 객체)각 삭제 됐을 떄 이를 참조하는 객체도 삭제


# Comment & Article
## 역참조
> 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것 N:1 관계에서는 1이 N을 참조하는 상황
> **하지만 Article에는 Comment를 참조할 어떠한 필드도 없다.**

article.comment_set.all()
(모델 인스턴스). (related manager). (QuerySetAPI)

## related manager
> N:1 혹은 M:N관계에서 역참조 시에 사용하는 manager
(objects라는 매니저를 통해 queryset.api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨)

### related manager가 필요한 이유
* article.comment형식으로는 댓글 객체를 참조 할 수 없음
* 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
* 대신 Django가 역참조 할 수 있는 'comment_set'manager를 자동으로 생성해 article.comment_set형태로 댓글 객체를 참조할 수 있음
* N:1 관계에서 생성되는 Related manager의 이름은 참조하는 **'모델명_set'**이름 규칙으로 만들어짐

# Comment & Article

* 사용자로부터 댓글 데이터를 받기 위한 CommentForm 작성
```python
class CommentForm(forms.ModelForm):
     class Meta:
        model =  Comment
        fields = '__all__'
```

* detail페이지에서 CommentForm출력(view함수)
```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form' :comment_form,
    }
    return render(request, 'articles/detail.html', context)

```

* detail 페이지에서 CommentForm 출력(템플릿)
```html
<form action="{% url 'articles:comment_create' article.pk %}" method = 'POST'>
    {% csrf_token %}
    {{comment_form}}
    <input type="submit">
  </form>
```
* 다음과 같이 출력되는 이유는 Comment 클래스의 외래 키 필드 article또한 데이터 입력이 필요하기 때문에 출력되고 있는 것

* 하지만,외래 키 필드는 **사용자의 입력으로 받는 것이 아니라 view함수 내에서 받아 별도로 처리되어 저장**되어야 함

* detail 페이지에서 CommentForm 출력(템플릿)
```python
class CommentForm(forms.ModelForm):
     class Meta:
        model =  Comment
        fields = ('content',)
```

* 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?
* detail페이지의 url을 살펴보면 path(<int:pk>/',views.detail,name='datail) url에 해당 게시글의 pk값이 사용 되고 있음
* 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값
```python
# urls.py
path('<int:article_pk>/comments/',views.comment_create,name='comment_create'),

# views.py
def comment_create(request,article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit=False는 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않는 속성 값
        comment=comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail',article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request,'articles/detail.html',context)
```
* save(**commit=False**)
> 'Create,but don't save the new instance.'
> DB에 저장하지 않고 인스턴스만 반환

#### 참고

##### 댓글 개수 출력하기
DTL filter-length 사용
{{comments|length}}
{{article.comment_set.all|length}}

QuerysetAPI-count() 사용
{{article.comment_set.count}}


###### 댓글이 없는 경우 대체 컨텐츠 출력
DTL tag-for empty사용


##### 댓글 수정을 구현하지 않는 이유
* 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form부분만 변경되어 수정 할 수 있도록 함

* 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이기 때문에 JavaScript를 사용해 도전해 볼 수 있도록 함
