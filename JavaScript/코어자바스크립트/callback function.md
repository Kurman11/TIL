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
  - this