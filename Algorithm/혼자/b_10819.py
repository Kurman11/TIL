#  차이를 최대로

import sys
sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split())) 
arr = []
visited = [False] * n

max_ans = float('-inf')

def dfs(depth):
    global max_ans
    if depth == n:
        ans = 0
        for i in range(n-1):
            ans += abs(graph[arr[i]] - graph[arr[i+1]])
        max_ans = max(max_ans,ans)
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(depth + 1)
            visited[i] = False
            arr.pop()


dfs(0)
print(max_ans)

# import sys
# from itertools import permutations
# sys.stdin = open('input.txt','r')


# n = int(input())
# lst = list(map(int, input().split()))

# max_result = 0

# # 모든 가능한 순열을 검사
# for perm in permutations(lst):
#     result = 0
#     for i in range(n-1):
#         result += abs(perm[i] - perm[i + 1])
#     if result > max_result:
#         max_result = result

# print(max_result)