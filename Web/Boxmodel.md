# The box model

## CSS Box Model
> 모든 HTML 요소를 (사각형) 박스로 표현
**박스에 대한 크기, 여백, 테두리 등의 스타일을 지정하는 디자인 개념**

### Box의 구성
* Margin : 이 박스와 다른 요소 사이의 공백 가장 바깥쪽 영역
* Border : 콘텐츠와 패딩을 감싸는 테두리 영역
* Padding : 콘텐츠 주위에 위치하는 공백 영역
* Content : 콘텐츠가 표시되는 영역

### Box 구성의 방향 별 명칭
* Box(상단)
  * Margin - top
  * Border - top
  * Padding - top
  * Content - top

* Box(오른쪽)
  * Margin - right
  * Border - right
  * Padding - right
  * Content - right

* Box(왼쪽)
  * Margin - left
  * Border - left
  * Padding - left
  * Content - left

* Box(하단)
  * Margin - bottom
  * Border - bottom
  * Padding - bottom
  * Content - bottom

* Box(내용물)
  * height (세로)
  * width (가로)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box1 {
      border-style: solid;
      border-width: 3px;
      border-color: red;
      border-bottom-color: blue;
      margin-top: 50px;
      margin-left: 30px;
      width: 300px;
      padding-left: 50px;
    }
    .box2{
      width: 300px;
      /* shorthand - 작성 순서 무관 */
      border: 1px solid black;
      /* shorthand - 작성 순서 무관 */
      margin: 25px auto;
    }
    .box3{
      width: 300px;
      border: 1px solid black;
      /* 우측 정렬 */
      /* 오른쪽의 마진을 왼쪽으로 모두 보낸다 */
      margin-left: auto;
    }
  </style>
</head>
<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
  <div class="box3">box3</div>
</body>
</html>
```

### width & height 속성
* 요소의 너비와 높이를 지정
* 이떄 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

### box-sizing 속성
* 요소의 너비와 높이를 계산하는 방법을 지정

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
      border: 2px solid black;
      background-color: gray;
      margin: 20px;
      padding: 25px;
    }
    .border-box {
      box-sizing: border-box;
    }
  </style>
</head>
<body>
  <div class="box">content - box</div>
  <div class="box border-box">border - box</div>
</body>
</html>
```
## 박스 타입
> Block & inline

### Normal flow
> CSS를 적용하지 않았을 경우 Block 및 inline 요소가 기봊거으로 배치되는 방향

### block 타입 특징
* 항상 새로운 행으로 나뉨
* width 와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
* 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함 (너비를 사용가능한 공간의 100%로 채우는 것)
* 대표적인 block 타입 태그
  * h1~6, p, div

### inline 타입 특징
* 새로운 행으로 나뉘지 않음
* width와 height 속성을 사용할 수 없음
* 수직 방향
  * padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
* 수평 방향
  * padding, margins, borders가 정용되어 다른 요소를 밀어낼 수 있음
* 대표적인 inline 타입 태그
  * a, img, span
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    a,
    span,
    img {
      border: 1px solid red;
      padding-top: 50px;
      padding-right: 50px;
    }
    h1,
    p,
    div {
      border: 1px solid blue;
    }
  </style>
</head>
<body>
  <h1>Normal Flow</h1>
  <p>p태그도 대표적인block 요소입니다.</p>
  <div>
    <p>block요소는 기본적으로 부모 요소 너비의 100%를 차지하며, 높이는 자식 콘텐츠의 최대 높이를 취한다.</p>
    <p>block요소의 총 너비와 총 봎이는 content + padding + border(상하/좌우 두께)</p>
  </div>
  <p>block 요소는 서로 margins로 구분된다.</p>
  <p>inline 요소는 <span>이 span 태그 처럼</span> 자기 콘텐츠의 너비와 높이만 차지한다. 그리고 inline 요소는 <a href="#">width 나 height 속성을 지정할 수 없다.</a> 
  </p>
  <p>
    이미지 <img src="#" alt="#"> 또한 inline 요소 중 하나이다.
    단, 이미지는 다른 inline 요소들과 달리 width나 height 값을 지정할 수 있다.
  </p>
  <p>
    만약 inline 요소의 크기를 제어하려면 block으로 변경해버리거나
    inline-block 요소로 설정해주어야 한다.
  </p>
</body>
</html>
```

## 참고

### shorthand 속성 - border
* border-width, border-style, border-color를 한번에 설정하기 위한 속성

### shorthand 속성 - margin & padding
* 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성
  <!-- 상우하좌 -->
  margin  : 10px 20px 30px 40px;
  padding : 10px 20px 30px 40px;
  <!-- 상/좌우/하 -->
  margin  : 10px 20px 30px;
  padding : 10px 20px 30px;
  <!-- 상하/좌우 -->
  margin  : 10px 20px;
  padding : 10px 20px;
  <!-- 공통 -->
  margin  : 10px;
  padding : 10px;
  
### display: inline-block
* inline과 block요소 사이의 중간 지점을 제공하는 display값
* 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
* block 요소의 특징을 가짐
  * 너비 및 높이 속성이 준수
  * 패딩, 여백 및 테두리로 인해 다른 요소가 상자에서 밀려납니다.

### Margin collapsing(마진 상쇄)
* 두 block 타입 요소의 martin top과 bottom이 만나 큰 margin으로 결합되는 현상
* 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
  * 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정할 수 있음
