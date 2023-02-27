# Web - Positioning for CSS layout
## CSS Layout
> 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 겨정하는 것
**Display,Position,Floats,Flexbox...**

## CSS Position
> Normal Flow에서 요소를 끄집어내서 다른 위치로 배치하는 것
**다른 요소 위에 놓기, 화면 특정 위치에 고정시키기 등**

### Normal flow
> CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향

### Position 이동 방향
* 기본
  * top
  * left
  * right
  * bottom
* Z,Y,X 축 

### Position 유형
* static (기본)
* relative (상대 위치)
* abolute (절대 위치)
* fixed (고정 위치)
* sticky (끈끈이)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      height: 1500px;
    }

    .box {
      width: 100px;
      height: 100px;
      border: 1px solid black;
    }
    
    .container{
      width: 300px;
      height: 300px;
      border: 1px solid black;
      position: relative;
    }

    .static{
      position: static;
      background-color: lightblue;
    }

    .absolute{
      position: absolute;
      background-color: lightcoral;
      left : 100px;

    }

    .relative{
      position: relative;
      background-color: lightgreen;
      top : 100px;
      left : 100px;
    }

    .fixed{
      position: fixed;
      background-color: lightseagreen;
      right: 0;
      top : 0;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="box static">static</div>
    <div class="box absolute">absolute</div>
    <div class="box relative">relative</div>
    <div class="box fixed">fixed</div>
  </div>
</body>
</html>
```

### Position 유형별 특징
* Static
  * 기본값
  * 요소를 Normal Flow에 따라 배치

* relative
  * 요소를 Normal Flow에 따라 배치
  * 자기 자신을 기준으로 이동
  * 요소가 차지하는 공간은 static일 떄와 같음

* absolute
  * 요소를 Normal Flow에서 제거
  * 가장 가까운 relative 부모 요소를 기준으로 이동
  * 문서에서 요소가 차지하는 공간이 없어짐

* fixed
  * 요소를 Normal Flow에서 제거
  * 현재 화면영역(viewport)을 기준으로 이동
  * 문서에서 요소가 차지하는 공간이 없어짐

* sticky
  * 요소를 Normal Flow에 따라 배치
  * 가장 가까운 block부모 요소를 기준으로 이동
  * 요소가 특정 임계점(ex.viexport의 상든으로 부터 10px)에 스크롤될 때 그위체엇 고정됨(fixed)
  * 만약 다음 sticky요소가 나오면 다음 sticky요소가 이전 sticky요소의 자리를 대체
    * 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정 되어야 할 위치가 겹치게 되기 떄문
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      box-sizing: border-box;
    }

    .container{
      position: relative;
    }

    .link {
      width: 10rem;
      height: 10rem;
      background-color: black;
      color: white;
      text-align: center;
      line-height: 10rem;
      border-radius: 50%;
      text-decoration: none;
    }
    
    .link-position{
      position: absolute;
      left: 0;
      left : 50%;
      top: 50%;
      transform: translate(-50%,-50%);
    }

    .img {
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="container">
    <img src="C:\Users\YJ\Desktop\멀티캠퍼스실습\23.02.27\bespoke.webp" alt="#" class="img">
    <a href="#" class="link link-position">비교하기</a>
  </div>
</body>
</html>
```


```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      height: 1500px;
    }

    .sticky{
      position: sticky;
      background-color: lightblue;
      border : 1px solid black;
      top: 0;
    }
  </style>
</head>
<body>
  <div class="sticky">sticky</div>
  <div>
    <p>aa</p>
    <p>aa</p>
    <p>aa</p>
  </div>
  <div class="sticky">sticky</div>
    <p>aa</p>
    <p>aa</p>
    <p>aa</p>
  <div class="sticky">sticky</div>
    <p>aa</p>
    <p>aa</p>
    <p>aa</p>
</body>
</html>
```

### z-index
> 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
* z축 (스크린 표면으로부터 사용자 얼굴 쪽으로 향하는 라인) 기준 정렬

#### z-index특징
* 정수 값을 사용해 z축 순서를 지정
* 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      height: 100px;
      position: absolute;
    }

    .red {
      background-color: red;
      top : 75px;
      left: 75px;
      z-index: 3;
    }

    .blue {
      background-color: blue;
      top : 100px;
      left: 100px;
      z-index: 2;
    }

    .green {
      background-color: green;
      top : 150px;
      left : 150px;
      /* z-index: -1; */
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="box red"></div>
    <div class="box blue"></div>
    <div class="box green"></div>
  </div>
</body>
</html>
```

### 참고
#### Position의 역할
> CSS Position은 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지의 특정 항목의 위치를 조정하는 것에 관한 것
