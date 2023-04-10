# 연결 요소의 개수

# import sys
# sys.stdin = open('input.txt','r')
# sys.setrecursionlimit(10000)

# N, M = map(int,input().split())

# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     X, Y = map(int,input().split())
#     arr[X].append(Y)
#     arr[Y].append(X)

# visited = set()
# def dfs(start):
#     visited.add(start)
#     for adj in arr[start]:
#         if adj not in visited:
#             dfs(adj)

# cnt = 0
# for i in range(1, N+1):
#     if i not in visited:
#         dfs(i)
#         cnt += 1

# print(cnt)


import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    X, Y = map(int,input().split())
    arr[X].append(Y)
    arr[Y].append(X)


def dfs(start):
    stack = [start]
    visited[start] = True
    cnt = 0
    while stack:
        cur = stack.pop()
        for adj in arr[cur]:
            if not visited[adj]:
                visited[adj]=True
                stack.append(adj)

