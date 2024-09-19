# ThisBinding : 실행컨텍스트 활성화될 때 한다.(함수가 호출될 때 결정된다.)
* 호출하는 방식에 따라 다르다.
  - 전역공간에서 (전역 객체를 가리킨다.) : 브라우저 window / node.js에서는 global 
  - 함수 호출시 (전역 객체를 가리킨다.) : 브라우저 window / node.js에서는 global
  - 메서드 호출시 : 메서드 호출 주체 (메서드명 앞) 메소드 명의 '점' 바로 앞에 있는 애가 this가 된다.
  ```
  var a = {
    b : function(){
      console.log(this);
    }
  }
  a.b();
  ```
  b함수를 a객체의 '메서드'로서 호출  
  인스턴스(객체)와 관련된 동작

  ```
    var a = {
      b: {
        c : function(){
          console.log(this)
        }
      }
    }
    a.b.c(); // c라는 함수한테 'a.b라는 객체와 관련된 동작을 수행해라'
  ```
  a.b 까지가 this가 된다.  
  
  대괄호 표기법
  obj.func();
  obj['func']();

  person.info.getName();
  person.info['getName']();
  person['info'].getName();
  person['info']['getName']();

> 메서드 내부함수에서의 우회법
  ```
  var a= 10;
  var obj = {
    a:20,
    b: function(){
      console.log(this.a); //여기서의 this는 obj를 뜻한다. 그러므로 this.a는 20이 나오는게 맞다.

      function c() { //c함수에서 내부의 this는 전역 객체를 가리킬 것이다. 
        console.log(this.a); // 전역객체의 a 프로퍼티를 찾아라 라는 명령이 되는데 여기서는 10이 나온다.
      }
      c(); // 앞에 this가없다.
    }
  }
  obj.b();
  ```
  여기서의 this가 전역객체가 아닌 obj를 바라보게끔 하려면 어떻게 해야 할까??  
  아쉽게도 call,apply 같은 명시적인 this 바인딩 명령을 쓰지 않고는 this 자체를 직접 다른 값으로 덮어씌울 수는 없다.  

  스코프 체인 방식을 사용해본다.
  ```
  var a= 10;
  var obj = {
    a:20,
    b: function(){
      console.log(this.a); 

      function c() { 
        var self = this; // 내부함수보다 상위에서 self라고 하는 변수에 this를 담고 
        console.log(self.a);  // 안쪽에서는 self를 사용한다.
      }
      c(); 
    }
  }
  obj.b();

  ```


  원래는 함수인데 어떤 객체와'관련된 동작을 하게 되면' 그때는 메서드라고 부르겠다는 거다. 이때 어떤객체가 바로 .앞인 것이다.

  - callback 호출시 : 기본적으로는 함수내부에서와 동일
  > call,apply,bind 메소드에 대하여
  ```
  function a(x,y,z){
    console.log(this, x, y, z);
  }
  var b = {
    bb : 'bbb'
  };

  a.call(b,1,2,3);
  a.apply(b,[1,2,3]);

  var c = a.bind(b);
  c(1,2,3);

  var d = a.bind(b,1,2);
  d(3);
  ```

  #### 콜백함수 정리
  * 기본적으로 함수의 this와 같다.
  * 제어권을 가진 함수가 콜백의 this를 지정해둔 경우도 있다.
  * 이 경우에도 개발자가 this를 바인딩해서 콜백을 넘기면 그에 따른다.


- 생성자함수 호출시 : 인스턴스


