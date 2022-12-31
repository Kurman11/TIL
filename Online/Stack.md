## 스택(Stack) 자료구조

* 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
* 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.

## 삽입 과 삭제

삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() (7데이터 삭제) - 삽입(1) - 삽입(4) - 삭제() (4데이터 삭제)

데이터 결과 : 5,2,3,1

```python
list=[] # 리스트 생성
list.append(1) # 리스트에 원소1 추가
list.pop() # 리스트 가장 마지막에 추가된 1 삭제
print(list) # 출력
print(list[::-1]) # 원소의 순서를 뒤집었다
```


```Python
stack =[]
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() (7데이터 삭제) - 삽입(1) - 삽입(4) - 삭제() (4데이터 삭제)
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력       # 결과 [1,3,2,5]
print(stack) # 최하단 원소부터 출력             #      [5,2,3,1]
```

c++   
데이터 삽입 push  
데이터 삭제 pop  
최상단 원소 top

java  
데이터 삽입 push  
데이터 삭제 pop  
최상단 원소 peek  