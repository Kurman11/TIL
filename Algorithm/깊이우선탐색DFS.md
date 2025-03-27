# DFS

> 깊이 우선탐색(DFS)

- **모든 정점을 방문**할 때 유리하다. 따라서 **경우의 수,순열과 조합** 문제에서 많이 사용한다.
- 너비우선탐색(BFS)에 비해 코드 구현이 간단하다.
- 단 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우에는 너비우선탐색(BFS)이 유리하다.

# 인접 행렬

```python
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
```

# 인접 리스트

```python
graph = [[] for _ in range(4)]

# 노드 A
graph[0].append('B')
graph[0].append('C')

# 노드 B
graph[1].append('A')

...

graph = [['B', 'C'], ['A', 'C', 'D'], ['A', 'B'], ['B']]

```

```python
# 인접 행렬과 인접 리스트 구현 방식

입력 값
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# V : 정점의 개수, E : 간선의 개수
V,E = map(int,input().split())
arr = list(map(int,input().split()))

# 인접 행렬
adj = [[0]*(V+1) for _ in range(V+1)]

# 인접 리스트
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]

    adj[n1][n2] = 1 # n1과 n2 인접
    adj[n2][n1] = 1 # 방향 표시가 없는 경우

    adjList[n1].append(n2)
    adjList[n2].append(n1)


print(adj)
print(adjList)
```

# 반복문을 이용한 DFS 구현 방식

> DFS는 직전에 방문한 정점으로 차례로 돌아가야 하므로, 후입선출(LIFO)구조의 스택을 사용한다.(BFS는 큐 를 사용한다.)

```python
visited = [False] * n # 방문 처리 리스트 만들기

def dfs(start):
  stack = [start] # 돌아갈 곳을 기록
  visited[start] = True # 시작 정점 방문 처리

  while stack: # 스택이 빌 때까지(돌아갈 곳이 없을떄까지) 빈벅
    cur = stack.pop() # 현재 방문 정점(후입선출)

    for adj in graph[cur]: # 인접한 모든 정점에 대해
      if not visited[adj]: # 아직 방문하지 않았다면
        visited[adj] = True # 방문 처리
        stack.append(adj) # 스택에 넣기

dfs(0) # 0번 점점에서 시작.
```
