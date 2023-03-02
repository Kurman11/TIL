# Semantic Web
> 웹 데이터를 의미론적으로 표현하고 연결하는 개념
> **for컴퓨터가 데이터의 내용과 문맥을 더 효율적으로 이해하고 더 지능적으로 활용**

## Semantic HTML

### h1
> 이 페이지의 최상위 제목
* 페이지 최상위 제목 의미를 제공하는 semantic 요소 h1
* 브라우저의 의해 제목처럼 보이도록 큰 글꼴로 스타일이 지정됨

* 모든 요소를 최상위 제목 '처럼' 보이게 할 수는 있으나 의미론적 가치는 없음

### HTML Semantic Element
> 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
**검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어줌**

### 각자의 책임과 역할
HTML : 채워질 데이터를 나타내기 위한
CSS : 어떻게 보여야 하는지

### 페이지 구조화를 위한 대표적인 semantic element
* header
* nav
* main
* article
* section
* asode
* footer
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
  <header>
    <h1>Heading</h1>
  </header>

  <p><b>Lorem</b> ipsum, <strong>dolor</strong> sit amet consectetur adipisicing elit. Recusandae iste laudantium repellat dolore voluptatum temporibus repellendus, vitae aperiam. Laudantium recusandae obcaecati animi rem repellat quia molestias dolorum, accusamus aliquam ratione.</p>

  <nav>
    <ul>
      <li><a href="#">nav</a></li>
      <li><a href="#">nav</a></li>
      <li><a href="#">nav</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <article>article</article>
      <div>div</div>
      <section></section>
    </article>
    <article></article>
    <aside></aside>
  </main>
</body>
</html>
```
## Semantics in CSS

### OOCSS
> Object-Oriented CSS 객체 지향적 접근법을 정용하여 CSS를 구성하는 방법론

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 기본 카드 구조 */
    .card{
      border: 1px solid black;
      border-radius: 5px;
      padding: 1rem;
    }

    /* 카드 제목 */
    .card-title {
      font-size: 1rem;
      font-weight: bold;
    }

    /* 카드 내용 */
    .card-description{
      font-size: 0.7rem;
    }
    
    /* 기본 버튼 구조 */
    .btn{
      padding: 1rem;
      cursor: pointer;
      border-radius: 5px;
    }

    .bg-red{
      background-color: red;
    }

    .bg-blue{
      background-color: lightblue;
    }
  </style>
</head>

<body>
  <div class="card">
    <p class="card-title">Card Title</p>
    <p class="card-description">This is a card description.</p>
    <button class="btn bg-red">Learn More</button>
    <button class="btn bg-blue">Learn More</button>
  </div>
</body>

</html>

```
### BEM
> Bloch Element Modifier 블록,요소,수정자를 사용해 클래스 이름을 구조화하는 방법론

### BEM구성
* Block
  * 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너
  * 재사용 가능한 독립적 블록, 가장 바깥쪽 상위요소
  * 재사용을 위해 margin 또는 padding을 적용하지 않음

* Element
  * block이 포함하고 있는 한조각
  * 블록을 구성하는 종속적인 하위요소

* Modifier
  * block 또는 element의 속성


```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* Block */
    .card{
      display: flex;
      flex-direction: column;
    }


    /* Element */
    .card__title{
      font-size: 2rem;
    }

    .card__list{
      margin: 0;
    }

    .card__button{
      font-size: 1rem;
      padding: 1rem;
      cursor: pointer;
    }
    /* Modifier */
    .card__list--nont{
      list-style: none;
    }

    .card__button--red{
      background-color: crimson;
    }
  </style>
</head>

<body>
  <div class="card">
    <h2 class="card__title">제목</h2>
    <ul class="card__list">
      <li class="card__list--nont">항목 1</li>
      <li class="card__list--nont">항목 2</li>
    </ul>
    <button class="card__button card__button--red">버튼</button>
  </div>
</body>

</html>
```

#### 참고

#### 의미론적인 마크업의 이점
* 검색 엔진이 해당 웹 사이트를 분석하기 쉡게 만들어 검색 순위에 영향을 줌
* 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 떄 추가적으로 도움

#### 클래스 이름이 너무 길어지는 건 아닐까?
* 클래스를 만들 떄 가장 중요한 부분은 클래스 이름이 무엇을 나타내는지 분명하게 전달할 수 있는가에 대한 것

* 각각의 명명법은 개인적인 취향에 따라 다르지만, 빠르고 명확한 표기를 우선적으로 해야 함

* 이 부분에 대해 너무 고민하지 않도록 하는 것도 중요

#### OOCSS & BEM의 목적
* 재사용 가능한 모듈로 분리함으로써 유지보수성과 확장성을 향상
* 개발자 간의 협력이 향상되어 공통 언어와 코드 이해를 확립

* Airbnb의 CSS스타일 가이드의 경우 OOCSS 및 BEM 방법론을 조합하여 사용