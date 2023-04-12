# Many_to_one_relationships2

# Article(N) - User (1)
> 0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음

# Comment(N) - User(1)
> 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음

##
* django에서는 User 모델을 직접 참조하는 것을 권장하지 않는다 (사실상 강하게 금지)

* 간접적으로 참조할 수 있는 함수를 제공 == get_user_model() => 현재 프로젝트에 활성화된 user객체'를 반환해주는 함수

## Article & User

둘은 같은 방법 이지만 반환 값이 달라 사용하는 곳이 다름
> get_user_model()
  * 반환 값 :'User object'(객체)
    * **models.py가 아닌 다른 모든 곳에서 참조할 때 사용**
> settings.AUTH_USER_MODEL
  * 반환 값:'accounts.User'(문자열)
    * **models.py의 모델 필드에서 참조할 떄 사용**

## Migration 진행
* 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
* 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
* 1을 입력하고 Enter진행

* article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
* 마창가지로 1 입력하고 Enter 진행
* 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨

* 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용
```python
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request,'create.html',context)
```
* detail 템플릿에서 각 게시글의 작성자 출력 및 확인
```html
<p>후기 작성자 : {{review.user}}</p>
```
* 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함
```python
@login_required
def update(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST,request.FILES,instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail',review.pk)
        else:
            form = ReviewForm(instance=review)
    context= {
        'review' : review,
        'form' :form,
    }
    return render(request,'update.html',context)
```
# Comment & User
## User 외래 키 정의
> user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

* 이전에 Article 와 User 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations파일이 곧바로 만들어지지 않고 일려의 과정이 필요