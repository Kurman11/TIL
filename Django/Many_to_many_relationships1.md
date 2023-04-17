# Many_to_many_relationships1

# M:N 관계 맛보기
> 병원 진료 시스템 모델 관계 만들기 (환자-의사)

## N:1의 한계
> 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정

1. 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정
```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

2. 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 에약 했다고 가정
```python
doctor1 = Doctor.objects.create(name='alice')
doctor2 = Doctor.objects.create(name='bella')
patient1 = Patient.objects.create(name='carol', doctor=doctor1)
patient2 = Patient.objects.create(name='dane', doctor=doctor2)
```

3. 1번 환자(carol)가 두 의사 모두에게 방문하려고 함
```python
patient4 = Patient.objects.create(name='dane', doctor=doctor1, doctor2)
```

4. 동시에 예약 할 수는 없을까?

5.  * 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행 해야 함
    * 새로운 환자 객체를 생성할 수 밖에 없음
    * 외래 키 컬럼에 '1,2' 형태로 참조하는 것은 integer 타입이 아니기 때문에 불가능
    > **그렇다면 '예약 테이블을 따로 만들자'**
  
## 중개 모델
> 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
> 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```python
# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

* 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
* 의사와 환자 생성 후 예약 만들기

<!-- 다 대 다 관계는 reservation과 같은 중개 모델이 생선 된다! -->

* 예약 정보 조회
```python
doctor1.reservation_set.all()
patient1.reservation_set.all()
```

* 1번 의사에게 새로운 환자 예약이 생성 된다면
```python
patient2 = Patient.objects.create(name='dane')
Reservation.objects.create(doctor=doctor1, patient=patient2)
# 1번 의상의 예약 정보 조회
doctor1.reservation_set.all()
```

## Django ManyToManyField
* 환자 모델에 Django ManyManyField 작성
```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

* 데이터베이스 초기화
* 생성된 중개 테이블 hospitals_patient_doctors 확인

* 의자 1명과 환자 2명 생성
```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

* 예약 생성 (환자가 의사에게 예약)
```python
patient1.doctors.add(doctor1)
patient1.doctors.all()
doctor1.patient_set.all()
```
* 예약 취소하기(삭제)
* 기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 .remove()을 사용
```python
doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
patient1.doctors.all()

patient2.patient_set.remove(doctor1)
patient2.doctors.all()
doctor1.patient_set.all()
```

## 'through' argument
* 그렇다면 중개 모델을 직접 장성하는 경우는 없을까?
* 중개 테이블을 수동으로 지정하려는 경우 through옵션을 사용하여 사용하려는 중개 테이블을 나타내느 Django 모델을 지정할 수 있음
* 가장 일반적인 용도는 **'중개테이블에 '추가데이터'를 사용해 다대다 관계와 연결하려는 경우'**


### 정리
* M:N 관계로 맺어진 두 테이블에는 변화가 없음
* ManyToManyField는 중개 테이블을 자동으로 생성함
* ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
* 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
* N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능

# ManyToManyField
ManyToManyField(to, options)
> many-to-many 관계 설정 시 사용하는 모델 필드
> 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성 add(), remove(), create(), clear()...

1. related_name_name
  * 역참조시 사용하는 manager name을 변경

2. through
  * 중개테이블을 직접 작성하는 경우, through옵션을 사용하여 중개테이블을 나타내는 Django모델을 지정
  * 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용됨

3. symmetrical
  * ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
  * 기본 값 : True


## M:N에서의 methods
  * add()
    * '지정된 객체를 관련 객체 집합에 추가'
    * 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  
  * remove()
    * '관련 객체 집합에서 지정된 모델 개체를 제거'

# Article & user
Many to many relationships 
N:M or M:N
> 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
**양쪽 모두에서 N:1 관계를 가짐**

* Article(M) - User(N)
> 0개 이상의 게시글은 0명 이상의 회원과 관련된다.
**게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.**

# 모델 관계 설정
* ManyToManyField 작성
* migrations이후 에러 확인

* like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨
* 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
  * user.article_set.all() => 해당 유저가 작성한 모든 게시글 조회
* user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨
* user와 관계된 ForeignKey 혹은 ManyToManyField중 하나에 related_name을 작성해야 함
* related_name 작성 후 Migration
```python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```


Article - User(N:1)
1. article.user
2. user.article_set

Article - User(N:M)
1. article.users
  * article.like_users.all() => 게시글에 좋아요를 누른 모든 유저
2. user.article_set 하면
  * user.like_articles.all() => 유저가 좋아요를 누른 모든 게시글

여기서 두개의 2번이 같아 충돌이 발생한다


## User-Article간 사용 가능한 related manager 정리
* article.user
  * 게시글을 작성한 유저-N:1
* user.article_set
  * 유저가 작성한 게시글(역참조)-N:1
* article.like_users
  * 게시글을 좋아요한 유저 - M:N
* user.like_articles
  * 유저가 좋아요한 게시글(역참조)-M:N


# 좋아요 구현
* url 및 view함수 작성
```python
path('<int:article_pk>/likes/', views.likes,name='likes'),

def likes(request, article_pk):
    # 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)
    # 좋아요 관계를 추가 or 삭제
    # 게시글에 좋아요를 누른 모든 유저

    # 좋아요 관계를 추가 or 삭제
    # 현재 좋아요를 요청하는 유저가 해당 게시글의 좋아요를 누른 유저 목록에 있는지 없는지를 확인
    # if request.user in article.like_users.all():

    # 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회   
    if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        print(article.like_users)
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article)
    return redirect('articles:index')

    # article.like_users.all()
    # 지금 좋아요를 요청하는 유저가 목록에 있는지 없는지??
    # 목록에 있으면? => 좋아요 취소
    # 목록에 없으면? => 좋아요 추가
```

* index템플릿에서 각 게시글에 좋아요 버튼 출력
```python
<form action="{% url 'articles:likes' article.pk %}" method ='POST'>
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value='좋아요 취소'>
      {% else %}
        <input type="submit" value='좋아요'>
      {% endif %}
    </form>
```


#### 참고
##### .exists()
> Queryset에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환 특히 큰 QuerySet에 있느 ㄴ특정 개체의 존재와 관련된 검색에 유용