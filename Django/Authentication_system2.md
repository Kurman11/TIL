# Authentication_system2

# 회원가입
> User 객체를 create 하는 것

## UserCreationForm()
> 회원 가입을 위한 built-in ModelForm

```python
# create와 매우 똑같음
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('articles/index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)

```
회원가입 진행 후 에러 페이지 

```python
from django.contrib.auth.forms import UserCreationForm
# django User 객체에 대한 직접 창조를 권장하지 않는다.
# from .models import User

# 대신 다음과 같은 함수를 제공한다.
# get_user.model은 현재 프로젝트에 활성화 되어있는 User 객체를 반환해준다.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        # 현재 우리가 사용하는 User class로 재정의
        model = get_user_model()

```
## 회원 탈퇴
> User 객체를 Delete 하는 것
```python
def delete(request):
    # print(dir(request.user))
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
```

## 회원정보 수정
### UserChangeForm()
> 회원 가입을 위한 built-in ModelForm

```python
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form' : form,
    }
    return render(request,'accounts/update.html',context)
```

### UserChangeForm 사용 시 문제점
* 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐
* admin 인터페이스에서 사용되는 ModelForm이기 때문
* 따라서 CustomUserChangeForm에서 접근 가능한 필드를 조정해야 함

#### UserChangeForm fields 재정의
```python
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name')
```

## 비밀번호 변경
* django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소로 안내

### PasswordChangeForm()
> 비밀번호 변경을 위한 built-in Form
```python
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경시 세션 무효화 방지
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request,'accounts/change_password.html',context)
```
### 암호 변경 시 세션 무효화
  * 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함
  * 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

### update_session_auth_hash(request,user)
> 암호 변경 시 세션 무효화 방지
> 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 ㅅsession data로 기존 session을 업데이트

## 로그인 사용자에 대한 접근 제한
* is_authenticated
  > 속성
    * 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성(attributes)
       > 모든 User인스턴스에 대해 항상 True인 읽기 전용 속성이며, AnonymousUser에 대해서는 항상 False임
        > 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음
```html
 {% if request.user.is_authenticated %}
    <h3>안녕하세요.{{ user }} 님!</h3>
    <form action="{% url 'accounts:logout' %}" method = 'POST'>
      {% csrf_token %}
      <input type="submit" value = 'Logout'>
    </form>

    <form action="{% url 'accounts:delete' %}" method = 'POST'>
      {% csrf_token %}
      <input type="submit" value ='회원탈퇴'>
    </form>
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">signup</a>
  {% endif %}
```

* login_required
  > 데코레이터
    * 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
    * 로그인 하지 않은 사용자의 경우/accounts/login/주소로 redirect 시킴
  
```python
@login_required
```
