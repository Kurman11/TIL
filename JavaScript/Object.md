# (plain)Object
> 키로 구분된 데이터 집합(date collection)을 저장하는 자료형

## 객체의 구조
* 중괄호를 이용해 작성
* 중괄호 안에는 key : value 쌍으로 구성된 속성(property)를 여러 개 넣을 수 있음
* key는 문자형, value는 모든 자료형이 허용

## 객체의 속성

### Property 활용
### property 존재 여부 확인 - 'in'
### 단축 Property
> 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
### 계산된 Property
> 키가 대괄호([])로 둘러싸여 있는 프로퍼티
> 고정된 값이 아닌 변수 값을 사용할 수 있음

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const user = {
      name : 'Sophia',
      age : 30,
      'key with space' : true,
    }

    // 조회 (점 표기법, 대괄호 표기법)
    console.log(user.age)
    console.log(user['key with space'])
    console.log(user['age'])

    // 추가
    user.address = 'korea'
    console.log(user)

    // 수정 
    user.age = 40
    console.log(user)

    // 삭제
    delete user.address
    console.log(user)

    // in 연산자
    console.log('age' in user)
    console.log('country' in user)

    const age = 30
    const address = 'korea'

    const oldUser = {
      age : age,
      address : address,
    }

    const newUser = {
      age,
      address
    }

    // 계산된 속성
    const product = prompt('물건 이름을 입력해주세요.')
    const a = 'my'
    const b = 'property'

    const bag = {
      [product] : 5,
      [a + b] : true,
    }

    console.log(bag)
  </script>
</body>
</html>
```
## 객체와 함수

### Methot
> 객체 속성에 정의된 함수
> **'this'키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음**
> object.method()
> 메서드는 객체를 '행동' 할 수 있게 함

### 'this' keyword
> 함수나 메서드를 호출한 객체를 가리키는 키워드(함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용)

* JS에서 this는 함수를 **호출하는 방법**에 따라 가리키는 대상이 다름

1. 단순 호출 시 -> 전역 객체
2. 메서드 호출 시 -> 메서드를 호출한 객체

### Nested 함수에서의 문제점과 해결책
* forEach의 인자로 들어간 함수는 일반 함수 호출이기 때문에 this가 전역 객체를 가리킴

* **화살표 함수**는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this값을 가져옴

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const person ={
      name : 'Sophia',
      greeting: function () {
        return `hello, ${this.name}` 
      },
    }

    // greeting 메서드 호출
    console.log(person.greeting())


    // this
    // 단순 호출 시
    const myFunc = function (){
      return this
    }

    console.log(myFunc())

    // nested 함수에서의 this
    const myObj2 = {
      numbers : [1,2,3],

      myFunc: function () {
        this.numbers.forEach(function (number) {
          // console.log(number)
          console.log(this)
        })
      }
    }

    console.log(myObj2.myFunc())
    
    const myObj3 = {
      numbers : [1,2,3],

      myFunc: function () {
        this.numbers.forEach((number) => {
          // console.log(number)
          console.log(this)
        })
      }
    }
    console.log(myObj3.myFunc())
  </script>
</body>
</html>
```

#### 참고

##### JavaScript 'this' 특징
* JavaScript에서 this는 함수가 '호출되는 방식'에 따라 결정되는 현재 객체를 나타냄

* python의 self와 Java의 this는 선언시 값이 이미 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적)

##### JSON(JavaScript Object Notation)
* key-value 형태로 이루어진 자료 표기법
* JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 '문자열'
* JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야함