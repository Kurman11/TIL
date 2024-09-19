# Execution Context(실행 컨텍스트)

### 전역공간   
* 전역공간은 자바스크립트 코드가 실행되는 순간에 바로 전역 컨텍스트가 생성되고 전체 코드가 끝날 떄에 비로소 전역 컨텍스트가 종료 되니까 이를 하나의 거대한 함수 공간이라고 봐도 무방하다.
 
### module  
* 어딘가에서 import 되는 순간에 그 모듈 내부에 있는 컨텍스트가 생성이 되고 그 모듈 코드가 전부 끝났을 떄에 컨텍스트가 종료되니까 역시 하나의 함수 공간이라고 간주를 해도 될 것 같다.

### 함수
* 결국 자바스크립트의 독립된 코드뭉치라고 할 수 있는 것은 곧 함수라고 볼 수 가 있다.

전역 공간, 모듈, 또는 함수로 묶인 내부에서는 ``결국 같은 환경 안에 있다`` 라는 게 성립된다.

### if / for / switch / while ... 문?
* ES6에서 블록스코프 개념이 추가되면서 let과 const에 대해서 별개의 독립된 공간으로서의 역할을 하고는 있지만 별개의 실행 컨텍스트를 생성하지는 않습니다.
* 중요한 점은 자바스크립트는 오직 함수에 의해서만 컨텍스트를 구분할 수 있다는 점이다.


## 실행 컨텍스트란
* "함수를 실행할 때 필요한 조건, 환경정보'를' 담은 객체" 가 된다.

```
var a = 1;

function outer(){
  console.log(a);

  function inner(){
    console.log(a);
    var a = 3;
  }

  inner();

  console.log(a);
}

outer();
console.log(a);

```

제일 마지막에 들어온 게 제일 먼저 빠지고 제일 먼저 들어왔던 게 제일 마지막에 빠지는 개념을 스택 이라고 한다.

코드 실행해 관여하는 스택을 "콜스택" 이라고 한다.

### Call stack
현재 어떤 함수가 동작중인지, 다음에 어떤 함수가 호출될 예정인지 등을 제어하는 자료구조

## 실행 컨텍스트 내부

현재 환경과 관련된 식별자 정보들  
inner
* VariableEnvironment (식별자 정보 수직) (변화 반영 X)
  - environmentRecord (snapshot)
  - outerEnvironmentReference (snapshot) : 바로 밑에있는 outer의 실행컨텍스트인 LexicalEnvironment 전체를 참조한다. 

outer
* LexicalEnvironment (각 식별자의 '데이터' 추적) (변화 반영 O)
  - environmentRecord
  - outerEnvironmentReference : outer의 outerEnvironmentReference는 그 밑에있는 전역의 LexicalEnvironment전체를 참조한다.

전역
* LexicalEnvironment
* environmentRecord

* ThisBinding
  


### LexicalEnvironment (어휘적/사전적 환경)
Ex)영한 사전 : 어떤 단어가 있을 떄 그 영어단어들을 한글로 설명해주는 내용들로 이루어진 사전  
#### LexicalEnvironment : 어떤 실행 컨텍스트 A에 대한 환경정보가 담겨 있는 사전  
Ex)내부식별자 a : 현재 값은 undefined 이다.  
내부식별자 b : 현재값은 20 이다.  
외부 정보 : D를 참조한다.

* 실행컨텍스트를 구성하는 환경 정보들을 모아 사전처럼 구성한 객체.
* environmentRecord : 현재 문맥의 식별자 정보가 수집된다.  
* HOISTING : 현재 컨텍스트 식별자 정보들을 수집해서 environmentRecord에 담는 과정
  - 식별자 정보를 끌어올리다.

#### outerEnvironmentReference : 외부 환경에 대한 참조
여기서 환경은 LexicalEnvironment를 말한다.  
외부의 LexicalEnvironment에 대한 참조가 된다.   
즉 현재 문맥에 관련 있는 외부 식별자 정보  

* outerEnvironmentReference가 관여하는게 바로 SCOPE CHAIN 이다.
  - SCOPE CHAIN현상은 바로 outerEnvironmentReference에 의해서 만들어지는 거다.
  - 외부로는 나갈 수 있는데 자기보다 더 안쪽으로는 들어갈 수 없는게 SCOPE이다.

* SCOPE CHAIN : inner에서 어떤 변수를 찾아라 명령이 나오면 일단 inner에서 찾고 없다면 outerEnvironmentReference를 타고 outer에서 찾는다. outer의 변수를 찾고 만약 또 없다면
다시 outerEnvironmentReference를 타고 전역컨텍스트를 가서 environmentRecord를 찾는다.  
``가장 가까운 자기 자신부터 점점 멀리있는 스코프로 찾아 나가는 것.``


#### 정리
* Execution Context : 함수를 실행할 때 필요한 환경정보를 담은 객체

* Variable Environment : 최조에는 식별자 정보를 가지고 있지만 그 값이 게속 변하지 않는다.
* Lexical Environment : 실행 컨텍스트의 실행 내용에 따라서 변수 값이 바뀔떄 그 변경 사항을 계속 트랙킹을 하는 정보.
  - environmentRecord : 현재문맥에서의 식별자(hoisting)
  - outerEnvironmentReference : 외부 식별자(scope chain)
* this