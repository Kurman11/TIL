# django_with_Ajax

## 비동기(Asynchronous)
* 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
* 시간잉 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
* 예시)
  * Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨

## Ajax (Aynchronous JavaScript And XML)
> 비동기적인 웹 애플리케이션 개발을 위한 프로그래밍 기술명
> **사용자의 요청에 대한 즉각적인 반응을 제공하면서, 페이지 전체를 다시 로드하지 않고 필요한 부분만 업데이트 하는 것을 목표**

### XMLHttpRequest(XHR)객체
> JavaScripc객체로, 클라이언트와 서버간에 데이터를 비동기적으로 주고받을 수 있도록 해주는 객체
> **JavaScript 코드에서 서버에 요청을 보내고, 서버로부터 응답을 받을 수 있음**

# 비동기 요청
## Axios
> JavaScript에서 HTTP 요청을 보내는 라이브러리 주로 프론트엔드 프레임워크에서 사용

## Axios 기본 문법
* get, post등 여러 method 사용가능
* then을 이용해서 성공하면 수행할 로직을 작성
* catch를 이용해서 실패하면 수행할 로직을 작성

* 고양이 사진 가져오기 (결과 비교)
* 동기식 코드(python)는 위에서부터 순서대로 처리가 되기때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력되는 반면
* 비동기식 코드(JavaScript)는 바로 처리가 가능한 작업(console.log)은 바로 처리하고 오래걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내 놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨

# 팔로우 with ajax

* axios CDN 작성
```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

* axios 요청 준비
```html
      axios({
        methot:'POST',
        url:`/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},
      })
```
* 현재 axios로 POST요청을 보내기 위해 필요한 것
1. url에 작성할 user pk는 어떻게 작성해야 할까?
2. csrftoken은 어떻게 보내야 할까?

* url에 작성할 user pk 가져오기 (HTML -> JavaScript)
```html
<form id='follow-form' data-user-id='{{person.pk}}'>
  const userId = event.target.dataset.userId
```
### 'data-*' attributes
> 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법
> 예를 들어 Data-text-value라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.textValue로 접글할 수 있음

* 요청 url 작성 마치기
```html
 axios({
        methot:'POST',
    ->    url:`/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},
      })
```

* 먼저 htidden 타입으로 숨어있는 csrf값을 가진 input 태그를 선택해야 함
```html
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
```

* AJAX로 csrftoken을 보내는 방법
```hmtl
      axios({
        methot:'POST',
        url:`/accounts/${userId}/follow/`,
   ->     headers: {'X-CSRFToken': csrftoken},
      })
```

* 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요
* axios 요청을 통해 받는 response객체를 활용해 view 함수를 통해서 팔로우 관계 여부를 파악 할 수 있는 변수를 담아 JSON 타입으로 응답하기
```python
@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed= False
        else:
            you.followers.add(me)
            is_followed = True
        context={
            'is_followed':is_followed,
            'followings_count':you.followings.count(),
            'followers_count':you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)
```

### 최조 코드 JS

```html
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    form.addEventListener('submit', function(event){

      //이벤트 기본 동작 취소
      event.preventDefault()
      const userId = event.target.dataset.userId
      //console.log(event.target)
      //console.log(event.target.dataset)
      // axios로 요청 보내기
      axios({
        methot:'POST',
        url:`/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},
      })
      .then((response) =>{
        //console.log(response.data)
        const isFollowed = response.data.is_followed
        const followbtn = document.querySelector('#follow-form>input[type=submit]')
        if (isFollowed === true) {
          //버튼을 언팔로우로 조작
          followbtn.value = '언팔로우'
        } else{
          //버튼을 팔로우로 조작
          followbtn.value = '팔로우'
        }
        const followingCountTag = document.querySelector('#followings-count')
        const followerCountTag = document.querySelector('#followers-count')
        
        const followingsCountData = response.data.followings_count
        const followersCountData = response.data.followers_count

        // 선택한 span 태그와 내용을 팔로잉과 팔로워 수 데이터로 채워넣기
        followingCountTag.textContent = followingsCountData
        followerCountTag.textContent = followersCountData
      })
    })

  </script>
```