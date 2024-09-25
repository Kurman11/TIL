# Callback 회신하다/답신하다

간단히  
함수처리 요청 -> 알아서 처리후 알려줌  
여기서 요청에서는 콜백함수에 대한 제어권을 넘긴다는 뜻이다.

* 제어권 위임
  - 실행 시점
  ```
  setInterval(function(){
    console.log('1초마다 실행될 겁니다.');
  }, 1000);
  ```
  setInterval : 일정 시간 간격으로 한번씩 함수를 실행해주는   
  인자 1 : 콜백함수  
  인자 2 : 주기(ms) 

  ```
  var cb = function(){
    console.log('1초마다 실행될 겁니다.');
  };
  setInterval(cb,1000);
  ```

  - 매개변수
  ```
  var arr = [1,2,3,4,5];
  var entries = [];

  arr.forEach(function(v,i){
    entries.push([i,v,this[i]]);
  }, [10,20,30,40,50]);

  console.log(entries);

  [[0,1,10],[1,2,20],[2,3,30],[3,4,40],[4,5,50]]ㄴ
  ```
  forEach라고 하는 메서드 자체에 첫번쨰 인자는 callback를 받고 두번째 인자에는 thtsArg를 받는다 라고 하는 규칙이 있다.
  - this
  ```
  document.body.innerHTML = '<div id = "a">abc</div>;
  function cbFunc(x) {
    console.log(this,x);
  }
  document.getElementById('a').addEventListener('click',cbFunc);
  ```
  id가 a인 element를 클릭했을 때 cbFunc를 호출하도록 addEvenListener에 넘기고 있다.
  이후 a를 클릭하면 this에는 클릭한 대상인 id가 a인 div가 나온다.
  x에는 PointerEvent라고 해서 click event에 대한 이벤트 객체가 나왔다.

* 공식문서(MDN)
  ```
  addEventListener(type, callback, options)
  ```
  type : click,mousemove,keyup,dragstart,scroll 반응할 이벤트 유형을 나타내는 대소문자 구분 문자열  
  listener (callback) : 단일 매개변수를 허용한다. 발생한 이벤트를 설명하는 Event에 기반한 객체이며, 아무것도 반환하지 않는다. 그리고 this에는 전달된 이벤트 아규먼트의 currentTarget 속성과 같다.

  options : 다양한 옵션들을 담은 객체가 오거나, 캡쳐 여부에 관한 useCapture라는 boolean값이 올 수도 있다.

## 콜백함수의 특징
* 다른 함수(A)의 인자로 콜백함수(B)를 전달하면, A가 B의 제어권을 갖게 된다.
* 특별한(bind)이 없는 한 A에 미리 정해놓은 방식에 따라 B를 호출한다.
  * 미리 정해놓은 방식이란 어떤 시점에 콜백을 호출할지, 인자에는 어떤 값들을 지정할지, this에 무엇을 바인딩할지 등이다.

## 주의!
* 콜백은 함수이다.
```
//메소드로 호출
obj.logValues(1,2);

//콜백함수로 전달
arr.forEach(obj.logValues);
```