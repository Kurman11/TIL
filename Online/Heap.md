## 힙(heap)
최소힙(min heap)
  * 루트 노드가 가장 작은 값을 가진다.
  * 따라서 값이 작은 데이터가 우선적으로 제거
* 최대 힙(max heap)
  * 루트 노드가 가장 큰 값을 가진다.
  * 따라서 값이 큰 데이터가 우선적으로 제거
완전 이진 트리(Complete Binary Tree)
* 완전 이진 트리란 루트 노드 부터 시작하여 `왼쪽 자식 노드, 오른쪽 자식 노드 순서`대로 데이터가 차례대로 삽입되는 트리

최소 힙 구성 함수(Min-Heapify())
* (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치 교체

파이썬의 경우 min heap를 지원 오름차순 정렬

```python
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽임
  for value in iterable:
    heapq.heappus(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

  n= int(input())
  arr =[]

  for i in range(n):
    arr.append(int(input()))
  
  res = heapsort(arr)

  for i in range(n):
    print(res[i])
```
데이터를 넣을때 꺼낼때 - 붙여서 max heap 으로 동작할수 있다.

> 힙 파이썬 예시인대 아직 잘 모름;; 이게 무슨소리??