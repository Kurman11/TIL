# 퇴사

import sys
sys.stdin = open('input.txt','r')

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())


dp = [0] *(N+1)
for n in range(N-1, -1, -1):
    if n+T[n] <= N:
        dp[n] = max(dp[n+1], dp[n+T[n]]+ P[n])
    else:
        dp[n] = dp[n+1]

print(dp[0])

# 백트래킹 N 이 15 이하 이기때문에 가능

# def dfs(n,sm):
#     global ans

#     if n >= N:
#         ans = max(ans, sm)
#         return

#     if n+T[n] <= N:
#         dfs(n+T[n], sm+P[n])
#     dfs(n+1, sm)

# N = int(input())
# T = [0] * N
# P = [0] * N
# for i in range(N):
#     T[i], P[i] = map(int, input().split())

# ans = 0
# dfs(0,0)
# print(ans)


# def dp(Day):
#     if Day >= n:
#         return 0
#     if memo[Day] != -1:
#         return memo[Day]

#     # 선택하는 경우
#     if Day + T[Day][0] <= n:
#         take = T[Day][1] + dp(Day + T[Day][0])
#     else:
#         take = 0

#     # 선택하지 않는 경우
#     skip = dp(Day + 1)

#     memo[Day] = max(take, skip)
#     return memo[Day]

# n = int(input())
# T = [list(map(int, input().split())) for _ in range(n)]

# # 메모이제이션을 위한 배열 초기화
# memo = [-1] * n

# # dp 함수를 호출하여 최대 수익 계산
# max_profit = dp(0)
# print(max_profit)

# def dp(Day):
#     global n
#     if Day == n:
#         return
    
#     for i in range(Day,Day+1):
#         a = 0
#         lst = [0] * (n+1)
#         for j in range(i,n):
#             if Day + i >= n:
#                 sm.append(sum(lst))
#                 return dp(Day + 1)
#             else:
#                 if a < n:
#                     lst[i] += T[i+j][1]
#                     i += T[i+j][0] -1 
#                     a += i

#     return sm.append(sum(lst))
            
# n = int(input())
# T = []
# sm = []
# for i in range(n):
#     T.append(list(map(int,input().split())))

# result = dp(0)
# print(sm)
