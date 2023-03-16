# Controlling event

## 일상속의 이벤트
* 버튼을 눌러서 도어락을 열거나, 전화기의 버튼을 눌러서 통화를 시작하는 것
* 키보드를 사용하여 글을 쓰거나, 리모컨을 사용하여 채널을 변경하는 것
* 알람 시계를 설정하여 특정 시간에 알림을 받는 것

## 웹에서의 이벤트
* 버튼을 클릭했을 떄 모달이 출력되는 것
* 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
* 사용자가 입력한 값에 따라 새로운 요소를 생성하는 것
> **일상생활에서의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작을 수행한다.**

# 이벤트 (event)
> 무언가 일어났다는 신호, 사건 (모든 DOM 요소는 이러한 신호를 만들어냄)

## event (종류)
* 마우스, 인풋, 키보드, 터치 등
* DOM요소는 event를 받고 받은 event를 '처리'(**이벤트 핸들러(처리기)**)할 수 있음

## event handler
> 이벤트가 발생했을 때 실행되는 함수 (사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것)

### .addEventListener()
> 대표적인 이벤트 핸들러 중 하나 (특정 이벤트를 DOM요소가 수신할 때마다 콜백 함수를 호출)

* **1.EventTarget**.addEventListener(**2.type**,**3.handler**)
* **1.DOM요소**               **2.특정 이벤트** **3.콜백함수**
* **1.대상**에 **2.특정 Event**가 발생하면, **3.할 일**을 등록한다.

* type
  * 이벤트 이름(ex.'click')

* handler
  * 발생한 이벤트 객체를 수신하는 콜백 함수
  * 콜백 함수는 발생한 Event object를 유일한 매개변수로 받음

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
  <button id="btn">버튼</button>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')
    console.log(btn)

    // 2. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click',(event) => {
      // 이벤트 객체
      console.log(event)
    
    // 이벤트가 발생한 대상
    // console.log(this) // 화살표 함수에서는 window
    console.log(event.target)
  })
  </script>
</body>

</html>
```

# 이벤트 핸들러 활요
## click 이벤트
* 버튼을 클릭하면 숫자를 1씩 증가

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
  <button id="btn">버튼</button>
  <p id="counter">0</p>

  <script>
    // 0. 초기값 할당 (0)
    let cnt = 0
    // 1. 버튼 요소 선택
    const btn = document.querySelector('#btn')
    // 2. 버튼에 이벤트 핸들러 부착(클릭 이벤트)
    btn.addEventListener('click',(event)=>{
      // 2.1 버튼에 클릭 이벤트가 발생할때마다 실행할 코드를 작성
      // 2.2 초기값 += 1
      cnt +=1
      // 2.3 p 요소를 선택
      const pTag = document.querySelector('#counter')
      // 2.4 p 요소의 컨텐츠를 1증가한 초기값으로 설정
      pTag.textContent = cnt
    })
      

    // cnt = 0
    // const btn = document.querySelector('#btn')
    // btn.addEventListener('click',(event)=>{
    //   console.log(cnt)
    //   cnt += 1
    //   const pTag = document.querySelector('#counter')
    //   pTag.textContent = cnt
    // })

  </script>
</body>

</html>
```
## input 이벤트
> 사용자의 입력 값을 실시간으로 출력하기
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
  <input type="text" id="text-input">
  <p></p>

  <script>
    // 1. input 요소 선택
    const inputTag = document.querySelector('#text-input')
    console.log(inputTag)

    // 2. p 요소 선택
    const pTag = document.querySelector('p')

    // 3. input 요소에 이벤트 핸들러 부착(input 이벤트)
    inputTag.addEventListener('input',(event) => {
      // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
      // console.log(event)
      console.log(event.target.value)

      // 3.2 p요소의 컨텐츠에 작성하는 데이터를 추가
      pTag.textContent = event.target.value
    })
  </script>
</body>
</html>
```
## click & input 이벤트
> 사용자의 입력 값을 실시간으로 출력하기 번튼을 클릭하면 출력한 값의 스타일을 변경하기

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .blue {
      color: lightblue;
    }

  </style>
</head>

<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // input 요소 선택
    const inputTag = document.querySelector('#text-input')
    // h1 요소 선택
    let hTag = document.querySelector('h1')

    // input 핸들러 부착
    inputTag.addEventListener('input',(event) => {
      // h1 요소에 텍스트 넣기
      hTag.textContent = event.target.value
    })

    // 버튼 요소 선택
    const btn = document.querySelector('#btn')
    // 버튼 핸들러 부착
    btn.addEventListener('click',(event) => {
      // console.log(hTag.classList.value)
      // 1. toggle 방법
      // hTag.classList.toggle('blue')

      // 2. if 방법
      if (hTag.classList.value){
        hTag.classList.remove('blue')
      } else {
        hTag.classList.add('blue')
      }
    })
  </script>

</body>

</html>
```

## 이벤트 취소하기
> 텍스트를 복사하려고 하면 알림 창을 띄우면서 복사를 중단하기

## .preventDefault()
> 현재 Event의 기본 동작을 중단
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
  <h1>정말 중요한 내용</h1>

  <script>
    const hTag = document.querySelector('h1')
    hTag.addEventListener('copy',(event) =>{
      console.log(event)
      event.preventDefault()
      alert('복사 할 수 없습니다.')
    })
  </script>
</body>

</html>
```
## todo
> 할 일을 입력하고 버튼을 클릭하면 할 일 요소를 생성 input 컨텐츠를 작성하지 않는다면 경고 알림 출력

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
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>

  <script>
    // 1. 필요한 요소 모두 선택
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')

    // const addTodo = inputTag.value =''

    // 2. 
    // btn.addEventListener('click',(event) => {
    //   // 2.1 사용자 입력 데이터 저장
    //   const inputData = inputTag.value
    //   console.log(inputData)

    //   // 2.2 데이터를 저장할 li 요소를 생성
    //   const liTag = document.createElement('li')

    //   // 2.3 li 요소 컨텐츠에 데이터 입력
    //   liTag.textContent = inputData
    //   console.log(liTag)
      
    //   // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
    //   ulTag.appendChild(liTag)

    //   // 2.5 todo 추가 후 input의 입력 데이터는 초기화
    //   inputTag.value =''
    // })

    const addTodo = (event) => {
      // 2.1 사용자 입력 데이터 저장
      const inputData = inputTag.value
      console.log(inputData)

      // 2.6 사용자 입력 데이터 공백 제거 후 확인
      if (inputData.trim()) {
        // 2.2 데이터를 저장할 li 요소를 생성
        const liTag = document.createElement('li')
  
        // 2.3 li 요소 컨텐츠에 데이터 입력
        liTag.textContent = inputData
        console.log(liTag)
        
        // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
        ulTag.appendChild(liTag)
  
        // 2.5 todo 추가 후 input의 입력 데이터는 초기화
        inputTag.value =''
      } else {
        // 2.7 사용자 입력 데이터가 없을 때
        alert('할 일을 입력하세요.')
      }


    }

    // 2. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click',addTodo)

  </script>

</body>

</html>
```

## 로또 번호 생성기 실습
### lodash
* 모듈성, 성능 및 추가 기능을 제고앟는 JavaScript 유틸리티 라이브러리
* array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수들을 제공

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
  <h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>

  <script src="
https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js
"></script>
  <script>
    // 1. 필요한 모든 요소 선택
    const t1Tag = document.querySelector('h1')
    const btn = document.querySelector('#btn')
    const divTag = document.querySelector('div')

    // 2. 버튼 요소에 이벤트 핸들러 부착
    btn.addEventListener('click',(event) => {
      // 2.1 1부터 45까지의 값이 필요
      const numbers = _.range(1,46)

      // console.log(numbers)
      // 2.2 45개의 요소가 있는 배열에서 6개 번호 추출
      const sixnumbers = _.sampleSize(numbers,6)
      // console.log(sixnumbers)


      const ulTag = document.createElement('ul')

      // 2.3 추출한 번호를 반복하면서 li 요소를 생성
      sixnumbers.forEach((number) => {
        const liTag = document.createElement('li')
        liTag.textContent = number
        // console.log(liTag)
        ulTag.appendChild(liTag)
      })
      // console.log(ulTag)
      divTag.appendChild(ulTag)
    })

  </script>

</body>

</html>
```

#### 참고

##### addEventListener 와 this
* addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상을(event.target)뜻함