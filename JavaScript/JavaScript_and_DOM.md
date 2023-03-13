# Web - JavaScript and DOM

## JavaScript 개요
## JavaScript는
* 웹 페이지의 동적인 기능을 구현하기 위한 **웹 브라우저에서의 JavaScript**를 학습
* 웹 브라우저에 내장된 JavaScript엔진에 의해 브라우저에서 실행됨

# DOM 기본 개념
## DOM
> 웹 페이지(Document)를 구조화된 객체로 제공하며 **프로그래밍 언어가 웹 페이지를 사용할 수 있게** 연결 시킴

## 브라우저가 웹 페이지를 불러오는 과정
* 문서(Document)는 웹 브라우저를 통해 해석되어 화면에 나타남 DOM은 이러한 문서를 조작하는 방법을 제공한든 API
* 브라우저는 HTML 문서를 해석하여 **DOM tree**라는 객체의 트리로 구조화 함
* DOM에서 모든 요소, 속성, 텍스트는 하나의 객체이며 모두 document 객체의 자식

웹 페이지를 동적으로 만드는 것 == 웹 페이지를 **조작**(생성,추가,삭제) 하는 것

조작하기 위한 순서
1. 조작 하고자 하는 요소를 **선택** 또는 **탐색**
2. 선택된 요소의 콘텐츠 또는 속성을 **조작**

## 'document' object
* 웹 페이지 객체
* DOM Tree의 진입점
* 페이지를 구성하는 모든 객체 요소를 포함

## 'document' 객체 접근 예시
* HTML <title> 값을 변경하기

# DOM Query(선택)

* 요소 하나 선택 : document.**querySelector()**
* 요소 여러 개 선택 : document.**querySelectorAll()**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1 class="title heading">DOM 선택</h1>
    <a href="https://www.google.com/">google</a>
    <div class="text">content1</div>
    <div class="text">content2</div>
    <div class="text">content3</div>
    <ul>
      <li>list1</li>
      <li>list2</li>
    </ul>
    <script>
      // console.log('hello')
      // 클래스가 title인 요소 선택
      console.log(document.querySelector('.title'))
      console.log(document.querySelector('.text'))
      console.log(document.querySelectorAll('.text'))
      console.log(document.querySelectorAll('ul > li'))
      
    </script>
  </body>
  </html>
  ```

## 서택 메서드 정리
* doucument.querySelector(selector)
  * 제공한 선택자와 일치하는 element 한 개 선택
  * 제공한 Css selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)

* document.querySelectorAll(selector)
  * 제공한 선택자와 일치하는 여러 element를 선택
  * 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  * 제공한 CSS selector를 만족하는 NodeList를 반환

# DOM Manipulation(조작)
## 조작 목차
1. 속성(attribute) 조작
  * 클래스 속성 조작
  * 일반 속성 조작

2. HTML 콘텐츠 조작
3. DOM 조작
4. style 조작

## 클래스 속성 조작
> 'classList' property
> 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
**add()**와 **remove()**


## classList 메서드 정리
* element.classList.add()
  * 지정한 클래스 값을 추가
* element.classList.remove()
  * 지정한 클래스 값을 제거

## 조회/설정(수정)/삭제
.getAttribute() / .setAttribute()/ removeAttribute()

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="title heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="text">content1</p>
  <p class="text">content2</p>
  <p class="text">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul> 


  <script>
    // 속성 요소 조작
    // 클래스 속성 조작
    console.log(document.querySelector('h1'))
    const h1Tag = document.querySelector('h1')
    console.log(h1Tag.classList)

    h1Tag.classList.add('test')
    console.log(h1Tag.classList)

    h1Tag.classList.remove('test')
    console.log(h1Tag.classList)

    // 일반 속성 조작
    const aTag = document.querySelector('a')
    console.log(aTag)
    console.log(aTag.getAttribute('href'))

    aTag.setAttribute('href', 'https://www.naver.com/')
    console.log(aTag.getAttribute('href'))

    aTag.removeAttribute('href', 'https://www.naver.com/')
    console.log(aTag.getAttribute('href'))

    const pTag = document.querySelector('.text')
    console.log(pTag.getAttribute('class'))

    
  </script>
</body>
</html>
```

## 속성 조작 메서드 정리
* Element.getAttribute()
  * 해당 요소에 지정된 값을 반환
* Element.setAttribute()
  * 지정된 요소의 속성 값을 설정
  * 속성이 이미 있으면 값이 업데이트/ 그렇지 않으면 지정된 이름과 값으로 새 속성이 추가
* Element.removeAttribute()
  * 요소에서 지정된 이름을 가진 속성 제거

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1 class="title heading">DOM 선택</h1>
    <a href="https://www.google.com/">google</a>
    <p class="text">content1</p>
    <p class="text">content2</p>
    <p class="text">content3</p>
    <ul>
      <li>list1</li>
      <li>list2</li>
    </ul> 
  
  
    <script>
      // h1 tag 선택
      const h1Tag = document.querySelector('.heading')
      console.log(h1Tag.textContent)
      
      h1Tag.textContent = '콘텐츠 수정'
      console.log(h1Tag.textContent)
    </script>
  </body>
  </html>
  ```
## 요소의 텍스트 콘텐츠를 표현
생성/추가/삭제
.createElement()/.appendChild()/.removeChild()

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
    <div></div>

    <script>
      // 1. 생성
      console.log(document.createElement('h1'))
      const h1Tag = document.createElement('h1')
      h1Tag.textContent = '제목'
      console.log(h1Tag)

      // 2. 추가
      // 어디에? 추가할 부모를 선택
      const divTag = document.querySelector('div')
      divTag.appendChild(h1Tag)

      // 3. 제거
      divTag.removeChild(h1Tag)


    </script>
  </body>
  </html>
  ```

## 스타일 조작
> 해당 요소의 모든 스타일 속성 목록을 포함하는 속성

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
    <p>Heading</p>

    <script>
      const pTag = document.querySelector('p')
      pTag.style.color ='red'
      pTag.style.fontSize = '3rem'
    </script>
  </body>
  </html>
  ```
#### 종합 정리
1. 속성(attribute)조작
  * 클래스 속성 조작:classList&add() &remove()
  * 일반속성 조작: getAttribute()&setAttribute()&removeAttribute()
2. HTML 콘텐츠 조작
  * textContent
3. Dom조작
  * createElement()& appendChild() & removeChile()

4. style 조작