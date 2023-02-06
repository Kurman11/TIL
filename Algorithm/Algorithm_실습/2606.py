# 바이러스

import sys
sys.stdin = open('input.txt','r')

T = int(input()) # 정점 개수  (지금 문제에서는 0이 제외)
num = int(input())  # 간선 개수 (그림1의 선 개수)

graph = [[] for _ in range(T+1)] # 0~7까지 T+1개 
visited = [False] * (T+1) # graph 갯수와 동일한 방문 처리할 False 리스트 생성

for _ in range(num): # 인접 리스트 만들기 
    v1,v2 = map(int,input().split())  # 입력 1 2
    graph[v1].append(v2) # graph[1]에 2 append [[],[2],[]...]
    graph[v2].append(v1) # graph[2]에 1 append [[],[2],[1]...]

    # 완성하면 [[], [2,5], [1,3,5], [2], [7], [1,2,6], [5], [4]]

def dfs(start): 
    stack =[start] # 돌아갈 곳을 기록
    visited[start] = True # 시작 방문점 True

    while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 빈복
        cur = stack.pop() # 현재 방문 정점(후입선출) cur = 1 / stack =[2,5] 에서 pop으로 인해 5가 cur에 저장 
        for adj in graph[cur]: # graph[1] -> [2,5]
            if not visited[adj]: # visited[2]가 True가 아니라면  / visited[5]가 True가 아니라면 
                visited[adj] = True  # visited[2]을 True (방문했다) 변경 / visited[5]을 True (방문했다) 변경
                stack.append(adj) # stack[2]에 append /stack[5]에 append 
                print(stack)
                print(visited)
dfs(1)
print(visited.count(True)-1) # True를 카운트 하고 처음 시작 True값 1을 뺴준다