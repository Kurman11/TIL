# 유기농 배추
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')

dx = [0,0,-1,1]
dy = [1,-1, 0,0]

def dfs(x,y):
    global visited
    visited[x][y] = 1
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < N and 0 <= newY< M:
            if visited[newX][newY] == 0 and graph[newX][newY] == 1:
                dfs(newX, newY)
        # if graph[newX][newY] and not visited[newX][newY]:
        #     dfs(newX,newY)



T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b =map(int,input().split())
        graph[b][a] = 1


    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and  not visited[i][j]:
                dfs(i,j)
                answer += 1


    print(answer)
# for q in graph:    
#     print(q)











# ### 2
# # dfs 정의
# def dfs(x, y):
#     # 상하좌우 확인을 위해 dx, dy 생성
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]

#     # 네 방향 탐색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < M) and (0 <= ny < N):  # nx:ny ↔ M:N 범위 참고
#             if graph[ny][nx] == 1:
#                 graph[ny][nx] = -1  # 배추가 인접할 때 체커
#                 dfs(nx, ny)

# ### 1                    
# T = int(input())

# for i in range(T):
#     M, N, K = map(int, input().split())  # M:가로, N:세로, K:개수
#     graph = [[0]*M for i in range(N)]
#     cnt = 0

#     # 배추 위치에 1 표시
#     for j in range(K):
#         X, Y = map(int, input().split())
#         graph[Y][X] = 1

# ### 3        
#     # dfs 활용해서 배추 그룹 수 세기
#     for x in range(M):
#         for y in range(N):
#             if graph[y][x] == 1:
#                 dfs(x, y)
#                 cnt += 1

#     # 정답을 위한 출력
#     print(cnt)