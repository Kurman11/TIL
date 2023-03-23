# Django_Template

## django template system
> 데이터 **표현**을 제어하면서, **표현**과 관련된 로직을 담당

## Django Template Language (DTL)
> Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

### Variable (변수)
* view 함수에서 render 함수의 세번쨰 인자로 딕셔너리 타입으로 넘겨 받을 수 있음
* 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
* dot(.)를 사용하여 변수 속성에 접근할 수 있음

### Filters
* 표시할 변수를 수정할 때 사용
* chained가 가능하며 일부 필터는 인자를 받기도 함
* 약 60개의 built-in template filters를 제공

### Tags
* 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
* 일부 태그는 시작과 종료 태그가 필요 {%if%} {% endif%}
* 약 24개의 built-in template tags를 제공

### Comments
* DTL에서의 주석 표현


# 템플릿 상속

## 만약 모든 템플릿에 bootstrap을 적용 하려면?
> 모든 템플리세 CDN을 작성해야할까?

## 템플릿 상속 (Temlplate inheritance)

> 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton'템플릿을 작성하여 상속 구조를 구축

## 'extends' tag
> 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
> **반드시 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)**

## 'block' tag
> 하위 템플릿에서 재정의(overridden) 할 수 있는 블록을 정의
> (하위 템플릿이 작성할 수 있는 공간을 지정)

# 요청과 응답 with HTML form

## 데이터를 보내고 가져오기 (sending and Retrieving form data)

> HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

## 'form' element
> 사용자로부터 할당된 데이터를 서버로 전송 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공

## 'action' & 'method'
> form의 핵심 속성 2가지
> "데이터를 어디(**action**)로 어떤 방식(**method**)으로 보낼지"

## 'name'
> input의 핵심 속성
> 데이터를 제출했을 떄 서버는 name속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음

## Query String Parameters
* 사용자의 입력 데이터를 URL주소에 파라미터를 통해 넘기는 방법
* 문자열은 앰퍼샌드(&)로 연결된 key = value 쌍으로 구성되며, 기본 URL과 물음표(?)로 구분됨
* 예시
  * http://host:port/path?**key=value&key=value**

# 요청과 응답 활용

## 사용자 입력 데이터를 받아 그대로 출력하는 서비스 제작
> view 함수는 몇 개가 필요할까? 2개
1. throw 뷰 함수
  * form 태그를 출력하는 템플릿을 응답

2. catch 뷰 함수
  * throw페이지에서 보낸 요청을 받고
  * 사용자 입력 데이터를 찾고
  * 찾은 데이터를 템플릿에 변수로 넣어서 응답


1. 유저는 /throw/ 주소로 요청을 보냄
2. django는 /throw/ 주소에 맞는 throw 뷰 함수를 호출(응답)
3. 유저는 django의 응답 결과(throw 페이지)를 받음
4. input에 데이터를 입력하고 제출을 누름(action 쪽으로 요청을 보낸 것)
5. action 주소는 /catch/였고, /catch/로 django에 요청을 보내는 행위
6. django는 /catch/주소에 맞는 catch 뷰함수를 호출(응답)
7. 유저는 django의 응답 결과(catch페이지)를 받음

## form 데이터는 어디에 들어 있을까?

> 모든 요청 데이터는 **HTTP request** 객체에 들어있음(view 함수의 첫번째 인자)


##### 참고
* 우리가 원하는 장소에 temple를 생성할수 있다?