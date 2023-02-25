# 창용 마을 무리의 개수
# 수업 내용을 참고했습니다 ㅠㅠ
import sys
sys.stdin = open('input.txt','r')
a = []
T = int(input())

for t in range(T):
    N,M= map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(start):
        stack =[start]
        visited[start] = True
        cnt = 0
        while stack:
            cur = stack.pop()
            for adj in graph[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)              
        for x in range(0,len(visited)-1):
            if visited[x] and visited[x+1] == True:
                cnt += 1

        print(f'#{t+1} {visited.count(True)-cnt}') 
        
    dfs(1)
