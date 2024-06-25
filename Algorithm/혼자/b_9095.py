# 1,2,3 더하기

import sys
sys.stdin = open('input.txt','r')

def num(T):
    if T == 1:
        return 1
    elif T == 2:
        return 2
    elif T == 3:
        return 4
    else:
        return num(T-1) + num(T-2) + num(T-3)

n = int(input())

for i in range(n):
    T = int(input())
    print(num(T))



# T = int(input())

# for i in range(T) :
#     n = int(input())
#     dp = [0]*(n+1)
#     if n == 1 :
#         print(1)
#     elif n == 2 :
#         print(2)
#     elif n == 3 :
#         print(4)
#     else :
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 4
#         for j in range(4,n+1) :
#             dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
#         print(dp[n])


# def count_ways(target, numbers, current_sum=0, index=0):
#     if current_sum == target:
#         return 1
#     if current_sum > target:
#         return 0

#     ways = 0
#     for i in range(len(numbers)):
#         ways += count_ways(target, numbers, current_sum + numbers[i], i)

#     return ways

# n = int(input())
# numbers = [1, 2, 3]
# for i in range(n):
#     target_value = int(input())
#     result = count_ways(target_value, numbers)
#     print(result)