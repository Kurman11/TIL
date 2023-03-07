# Bootstrap을 사용하는 이유

* 손쉬운 반응형 웹 디자인 구현
* 빠른 개발과 유지보수
  * 미리 디자인된 다양한 컴포넌트 및 기능
  * 일관된 코드와 문서

* 커스터마이징(customizing)이 용이
* 크로스 브라우징(Cross browsing) 지원
  * 모든 주요 브라우저에서 작동하도록 설계되어 있음

# Carousel
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
    <div id="carouselExample-first" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../23.03.07/images/01.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../23.03.07/images/02.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../23.03.07/images/03.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample-first" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample-first" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <h2>두번째 carousel</h2>

    <div id="carouselExample-second" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../23.03.07/images/04.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../23.03.07/images/05.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../23.03.07/images/06.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample-second" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample-second" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```
# Modal
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
  <!-- 1. model 버튼과 modal 요소는 반드시 같이 다닐 필요가 없음. -->
  <!-- modal 코드가 다른 요소들에 중첩되어 있을경우 검은 배경뒤로 감춰질 수 있기 때문에 다른 요소에 중첩해서 두지 않는다. -->
  <!-- body 태그가 닫히는 부분에 modal 요소를 모아두는 것이 일반적 -->
  <!-- Button trigger modal -->
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal-first">
    Launch demo modal
  </button>

  <!-- Button trigger modal -->
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal-second">
    Launch demo modal
  </button>

  <!-- Modal -->
  <div class="modal fade" id="exampleModal-first" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          첫번째 모달
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal -->
  <div class="modal fade" id="exampleModal-second" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          두번째 모달
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```

# Bootstrap Grid system
> 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
**반응형 디자인을 지원해 웹 페이지를 모바일,테블릿,데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움**

### 12
> 적당히 크고 많은 약수를 가진 수


## Grid system 클래스와 기본 구조

### Grid system 핵심 클래스
> 1개의 row안에 12칸의 column영역이 구성 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨

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
  <h2>Basic</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col</div>
      <div class="box col-4">col</div>
      <div class="box col-4">col</div>
    </div>
    <div class="row">
      <div class="box col-2">col</div>
      <div class="box col-8">col</div>
      <div class="box col-2">col</div>
    </div>
    <div class="row">
      <div class="box col-4">col</div>
      <div class="box col-2">col</div>
    </div>
  </div>

  <h2>nesting</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col</div>
      <div class="box col-8">
        <div class="row">
          <div class="box col-6">col</div>
          <div class="box col-6">col</div>
          <div class="box col-6">col</div>
          <div class="box col-6">col</div>
        </div>
      </div>
    </div>
  </div>

  <h2>offset</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col</div>
      <div class="box col-4 offset-4">col</div>
    </div>
    <div class="row">
      <div class="box col-3 offset-3">col</div>
      <div class="box col-3 offset-3">col</div>
    </div>
    <div class="row">
      <div class="box col-6 offset-3">col</div>
    </div>
  </div>

  <h2>gutter</h2>
  <div class="container">
    <div class="row gx-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <br>

  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <br>

  <div class="container">
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```

### Gutters
> grid system에서 column 사이에 padding 영역
* gx-* : 수평
* gy-* : 수직
* g-* : 수평 수직