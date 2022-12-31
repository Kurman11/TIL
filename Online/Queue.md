## 큐(Queue) 자료구조
* 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
* 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
* 큐를 구현할 때는 파이썬에서 기본적으로 제공하는 리스트 자료형이 아닌 deque를 이용하는게 시간적으로 우수하다.
삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() (5데이터 삭제) - 삽입(1) - 삽입(4) - 삭제() (2데이터 삭제)

데이터 결과 : 3,7,1,4

```python
from collections import deque
# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

결과 : 3.7.1.4
결과 : 4.1.7.3
```
```python
import deque # deque라이브러리 선언
queue = deque() # deque() = queue
queue.append() # Stack와 같이 append로 리스트 추가
queue.popleft() # 가장 왼쪽의 데이터를 꺼낸다 /제일 먼저 추가된 데이터 삭제
queue.reverse() # 역순으로 바꾼다
```
c++   
데이터 삽입 push  
데이터 삭제 pop  
최상단 원소 front

java   
데이터 삽입 offer  
데이터 삭제 poll  
최상단 원소 peek  

## 우선순위 큐(Priorriy Queue)
* `우선순위 큐`는 <U>우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조</U> 이다.
* 우선순위 큐는 데이터를 `우선순위에 따라` 처리하고 싶을 때 사용한다.  
  * ex)물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우  

  |자료구조|추출되는데이터
  |:---|:---|
  |스택(Stack)|가장 나중에 삽입된 데이터|
  |큐(Queue)|가장 먼저 삽입된 데이터|
  |우선순위 큐(Priorty Queue)|가장 우선순위가 높은 데이터|
