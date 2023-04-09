# 안전 영역

import sys
sys.stdin = open('input.txt','r')

T = int(input())
arr = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,h):
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < len(arr[0]) and 0 <= newY< len(arr):
            if visited[newX][newY] and arr[newX][newY] >h:
                visited[newX][newY] = 1
                dfs(newX, newY, k)



for t in range(T):
    num = [list(map(int,input().split()))]
    for i in num:
        arr.append(i)
       
visited = [[0] * len(arr[0]) for _ in range(len(arr))]
ans = 0
# for i in range(len(arr[0])):
#     for j in range(len(arr)):
#         if arr[i][j] < 4:
#             arr[i][j] = 0

for k in range(max(map(max, arr))):
    cnt = 0
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if not visited[i][j] and arr[i][j] > k :
                cnt += 1
                visited [i][j]=1
                dfs(i,j,k)
    ans = max(ans,cnt)            
                
print(ans)
# print(answer)


# print(visited)
# print(arr)