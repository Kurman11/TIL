# Grid system for responsive web design

# Responsive Web design
> 디바이스 종류나 화면 크기에 상관없이, 어디에서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
> Bootstrap grid system의 12개 column과 **6개 breakpoints**를 사용하여 반응형 디자인을 구현

## Grid system Breakpoints
> 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
> **화면 너비에 따라 6개의 분기점 제공(xs,sm,md,lg,xl,xxl)**

* xs < 576px 
  * container (max-width) : None(auto)
  * Class prefix : .col-
* sm >= 576px
  * container (max-width) : 540px
  * Class prefix : .col-sm-
* md >= 768px
  * container (max-width) : 720px
  * Class prefix : .col-md-
* lg >= 992px
  * container (max-width) : 960px
  * Class prefix : .col-lg-
* xl >= 1200px
  * container (max-width) : 1140px
  * Class prefix : .col-xl-
* xxl >= 1400px
  * container (max-width) : 1320px
  * Class prefix : .col-xxl-

> 각 breakpoints 마다 설정된 최대 너비 값 **"이상으로"** 화면이 커지면 grid system 동작이 변경됨

> Grid System은 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것

> 각각의 길술은 용도와 장단점이 있음 
> 어떤 기술도 독립적인 용도를 가지지 않으며, 어떤 기술이 적합한 도구가 될지는 특정 상황에 따라 다름
> 이를 파악하기 위해서는 충분한 경험이 필요
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  <style>
    .box{
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>breakpoints</h2>
    <div class="row g-0">
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
        <div class="box">col</div>
      </div>
    </div>
    <hr>
    <h2>breakpoints + offset</h2>

    <div class="row g-0">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
        <div class="box">col</div>
      </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```

#### Grid cards
* row-cols 클래스를 사용하여 해당 표시할 열(카드) 수를 손쉽게 제어할 수 있음


```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```