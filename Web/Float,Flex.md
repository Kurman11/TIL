# Floating for CSS layout

## CSS Float
> 요소를 띄워서 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치
**왼쪽 혹은 오른쪽으로 띄워 Normal flow에서 벗어남**

### Float 탄생 배경
* 텍스트 열 내부에 떠다니는 이미지를 포함하면서도 해당 이미지의 좌우에 텍스트를 둘러싸는 간단한 레이아웃을 구현하기 위해 도입(ex.신문 레이아웃)

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
      width: 10rem;
      height: 10rem;
      border: 1px solid black;
      background-color: lightcoral;
      margin: 1rem;
    }

    .float-left{
      float: left;
    }

    .flow-right{
      float: right;
    }
  </style>
</head>

<body>
  <div>
    <div class="box float-left">float left</div>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quia maxime dolore laboriosam atque non sequi, eum,
      odit, minus itaque quibusdam minima a reiciendis placeat nemo perspiciatis? Natus ipsam blanditiis, quos rem
      soluta nam quas esse repellendus illum a eum iure sed iste ex deleniti explicabo consectetur sit, debitis culpa
      officia unde? Qui eligendi distinctio suscipit cum quos excepturi deleniti non assumenda dicta dolorum delectus
      saepe porro, asperiores harum repellat quia voluptates incidunt itaque doloremque, expedita quam tempora
      veritatis! Tempore laborum fuga totam cum! Repudiandae, quisquam adipisci excepturi, voluptates non omnis ratione
      placeat inventore ab laudantium modi porro. Culpa eos enim voluptas deleniti quis suscipit ipsam eaque. Maiores
      vitae ipsa, excepturi repudiandae quia aut culpa laborum mollitia magni earum optio labore est! Eveniet expedita
      architecto excepturi hic iusto? At modi adipisci tenetur sed quod, unde corrupti animi iste, perferendis
      voluptatibus odio quis ea id itaque architecto voluptate laudantium inventore quasi est necessitatibus vel
      voluptates dolores. Vero perspiciatis consectetur aspernatur tempore nobis porro, fugit cum tenetur repellat harum
      sed quae laborum quos dolorum quaerat incidunt optio dicta voluptate voluptatem nihil. Nostrum, impedit quae earum
      illo ut veniam molestias? Mollitia nisi eum doloribus laboriosam ducimus deleniti voluptate porro corrupti nostrum
      ab, alias necessitatibus?</p>
    <div class="box flow-right">float right</div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis explicabo provident recusandae quibusdam ipsam rem
      impedit reprehenderit fugiat quod maiores excepturi eius perferendis est perspiciatis natus magnam quasi culpa a
      magni aut, expedita, dolorem sed. Vel provident similique id quam nemo culpa saepe hic ipsum mollitia quod rerum
      adipisci, dolor voluptas commodi ex inventore in. Nesciunt autem expedita accusamus corporis ex doloribus
      voluptates quia, neque deleniti distinctio adipisci odit incidunt. Distinctio ipsum, velit temporibus nam nulla
      maiores nihil hic ducimus. Atque quidem repellat molestiae sint laboriosam voluptatum, in totam autem debitis
      libero non. Repellat hic sequi dolorum, beatae ratione sed magnam placeat quos itaque reiciendis pariatur cum
      recusandae enim sit amet veritatis delectus voluptatibus repudiandae, explicabo accusamus aliquam facilis sunt nam
      assumenda. Alias non laudantium quia perspiciatis debitis. Mollitia tempora praesentium, culpa molestiae, ab esse
      itaque saepe libero tempore nesciunt maiores, sapiente quas dignissimos dolorem aspernatur corporis veniam minima
      quod similique optio. Optio animi laborum amet nostrum et aperiam! Corporis, aliquam odio incidunt asperiores
      animi in unde quo. Tempora exercitationem, inventore quo commodi cumque veritatis. Iste, ea. Voluptates quis
      blanditiis perspiciatis vitae est possimus explicabo atque ex maiores dignissimos cumque animi laudantium,
      voluptate culpa minima, deleniti saepe eaque aperiam omnis.</p>
  </div>
</body>

</html>
```

### Float
* Float는 원래 탄생 목적에서 더 나아가 웹 페이지 전체 레이아웃을 구성하는 데 사용되었으나, Flexbox와 Grid의 등장으로 인해 다시 원래의 목적으로 돌아감

# Flexible box for CSS layout

## CSS Flexbox
> 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
**요소 간'공간 배열'과 '정렬'**
* 요소를 행과 열 형태로 배치하는 **1차원** 레이아웃 방식

### Flexbox 기본 사항
* main axis(주 축)
  * flex item들이 배치되는 기본 축
  * main start에서 시작하여 main end 방향으로 배치

* cross axis(교차 축)
  * main axis에 수직인 축
  * cross start에서 시작하여 cross end 방향으로 배치

* Flex Container
  * display: flex; 혹은 display: inline-flex;가 설정된 부모 요소
  * 이 컨테이너의 1차 자식 요소들이 Flex item이 됨
  * flexbox속성 값들을 사용하여 자식 요소 Flex item들을 배치

## Flexbox 레이아웃 구성

### Flexbox 속성
* Flex Container 관련 속성
  * display, flex-direction, flex-wrap, justify-content, align-items,align-content
  * align-self, flex-grow, flex-shrink, flex-basis, order

### Flex Container 지정
* flex item은 행으로 나열
* flex item은 주축의 시작 선에서 시작
* flex item은 교차축의 크기를 채우기 위해 늘어남

### Flex-direction 지정
* flex item이 나열되는 방향을 지정
* column으로 지정할 경우 주 축이 변경됨
* -reverse로 지정하면 시작 선과 끝 선이 서로 바뀜

### flex-wrap
* flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정

### justify-content
* 주 축을 따라 flex item과 주위에 공간을 분배

### align-content
* 교차 축을 따라 flex item과 주위에 공간을 분배
  * flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
  * 한 줄 짜리 행에는(flex-wrap이 nowrap으로 설정된 경우) 효과 없음

### align-items
* 교차 축을 따라 flex item 행을 정렬

### align-self
* 교차 축을 따라 개별 flex item을 정렬

### 목적에 따른 분류
* 배치 설정
  * flex-direction : 주축
  * flex-wrap : 개행
* 공간 분배
  * justify-content : 여러행
  * align-content : 여러행
* 정렬
  * align-items : 행1/요소1
  * align-items : 행1/요소1

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
      /* flex-direction: row; */
      /* flex-direction: column; */
      /* flex-direction: row-reverse; */
      /* flex-direction: column-reverse; */

      /* flex-wrap: nowrap; */
      /* flex-wrap: wrap; */

      /* 주축 정렬 */
      /* justify-content: flex-start; */
      /* justify-content: center; */
      /* justify-content: flex-end; */

      /* 교차축 정렬 행이 여러개 일떄*/
      /* align-content: flex-start; */
      /* align-content: center; */
      /* align-content: flex-end; */

      /* 행이 하나 일때 */
      /* align-items: flex-start; */
      /* align-items: center; */
      /* align-items: flex-end; */


    }

    .post {
      background-color: grey;
      border: 1px solid black;
      margin: 0.5rem;
      padding: 0.5rem;
    }

    .item1 {
      align-self: center;
    }

    .item2 {
      align-self: flex-end;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="post item1">
      <h2>Post Title 1</h2>
      <p>Post Content 1</p>
    </div>
    <div class="post item2">
      <h2>Post Title 2</h2>
      <p>Post Content 2</p>
    </div>
    <div class="post">
      <h2>Post Title 3</h2>
      <p>Post Content 3</p>
    </div>
    <div class="post">
      <h2>Post Title 4</h2>
      <p>Post Content 4</p>
    </div>
  </div>

</body>

</html>
```

#### 속성명 Tip
* justify : 주 축
* align : 교차 축
* content : 여러 행
* items : 행 1
* self : 요소 1

### flex-grow
* 남은 행 여백을 비율에 따라 각 flex item에 분배
* flex-grow의 반대는 flex-shrink
  * 넘치는 너비를 분배해서 줄임

### flex-basis
* flex item의 초기 크기 값을 지정
* flex-basis와 width값을 동시에 적용한 경우 flex-basis가 우선

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      width: 100%;
      display: flex;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-grow: 1;
    }

    .item-2 {
      background-color: green;
      flex-grow: 2;
    }

    .item-3 {
      background-color: blue;
      flex-grow: 3;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
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
    .container {
      width: 100%;
      display: flex;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-basis: 300px;
    }

    .item-2 {
      background-color: green;
      flex-basis: 600px;
    }

    .item-3 {
      background-color: blue;
      flex-basis: 300px;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```


# Flexbox 반응형 레이아웃
* flex-wrap을 사용해 반응형 레이아웃 작성 (feat flex-grow & flex-basis)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card{
      border: 1px solid black;
      width: 80%;
      display: flex;
      flex-wrap: wrap;
    }

    img{
      width: 100%;
    }

    .card-img{
      flex-basis: 700px;
      flex-grow: 1;
    }

    .content{
      flex-basis: 350px;
      border: 1px solid black;
      flex-grow: 1;
    }
  </style>
</head>
<body>
  <div class="card">
    <img class="card-img" src="sample.jpg" alt="">
    <div class="content">
      <h2>Heading</h2>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem temporibus corporis non in autem doloremque veritatis inventore error sapiente nesciunt! Dolores esse odio consectetur dolorem possimus sint, quod obcaecati magni.</p>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas, aspernatur amet! Id, nulla quidem inventore officia nesciunt vero doloribus unde accusamus quisquam deserunt natus esse temporibus sit fuga rerum illo quos ex at asperiores dolorem quo aliquid! Porro ipsam dignissimos explicabo impedit reiciendis dolor omnis sunt praesentium labore doloremque error eligendi nulla, blanditiis ad corrupti quos obcaecati aspernatur tempore qui quae! Cupiditate itaque dicta adipisci impedit. Quia reiciendis, ab, quisquam, beatae sit molestias iusto ea eveniet sapiente tempora error earum. Fugiat repellendus delectus nostrum alias adipisci magni voluptas! A ut laborum saepe voluptate quasi qui tenetur eveniet sequi in at?</p>
    </div>
  </div>
</body>
</html>
```