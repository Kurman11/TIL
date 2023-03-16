# Functions
## 개요
* 참조 자료형 : Objects(Object, Array, Function)

* Function : 참조 자료형에 속하며 모든 함수는 Function object

* 함수의 구조
  * 함수의 이름
  * 함수의 매개변수
  * 함수의 body를 구성하는 statement

## 함수의 정의
* 선언식 : function declaration
* 표현식 : function expression

### 함수 표현식 특징
* 함수 이름이 없는 '익명 함수'를 사용할 수 있음
* 선억식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 코드에서 나타나기 전에 먼저 사용할 수 없음

### 선언식과 표현식
||선언식|표현식|
|---|---|---|
|특징| 익명 함수 / 사용 불가능  호이스팅 있음| 익명 함수 사용 가능 / 호이스팅 없음|
|비고||사용 권장|

### 기본 함수 매개변수
> Default function parameter
> 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

### 나머지 매개변수(Rest parameters) (가변 인자)
> 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법
* 함수 정의에는 하나의 나머지 매개변수만 있을 수 있음
* 나머지 매개변수는 함수 정의에서 마지막 매개변수여야 함

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

    console.log(add(3 , 9))

    function add (num1, num2) {
      return num1 + num2
    }


    const sub = function (num1 , num2) {
      return num1 - num2
    }
    
    console.log(sub(3,9))

    // 기본 함수 매개변수
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }

    console.log(greeting())

    // 매개변수 개수와 인자 개수의 불일치 상황
    // 매개변수 개수 < 인자 개수
    const noArgs = function () {
      return 0
    }

    console.log (noArgs(1, 2, 3))

    const twoArgs = function (num1, num2) {
      return [num1, num2]
    }

    console.log(twoArgs(1, 2, 3))

    // 매개변수 개수 > 인자 개수
    const threeArgs = function (num1, num2, num3) {
      return [num1, num2, num3]
    }

    console.log(threeArgs(1))


    // 나머지 매개변수(가변 인자)
    const myFunc = function (num1, num2, ...restArgs) {
      return [num1, num2, restArgs]
    }

    console.log (myFunc(1,2,3,4,5))
    console.log (myFunc(1,2))
  </script>
</body>
</html>
```

## 화살표 함수 표현식 (Arrow function expressions)
> 함수 표현식의 간결한 표현법

### 화살표 함수 표현식 작성 순서
1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>)작성
2. 함수의 매개변수가 하나 뿐이라면 매개변수의 `()` 제거 가능
3. 함수 본문의 표현식이 한 줄이라면 `{}` 와 `return` 제거 가능

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
    const greeting = function (name) {
      return `hello, ${name}`
    }

    const arrow1 = (name) => {
      return `hello, ${name}`
    }

    console.log(arrow1('harry'))

    const arrow2 = (name) => `hello, ${name}`

    console.log(arrow2('herry'))
  </script>
</body>
</html>
```
