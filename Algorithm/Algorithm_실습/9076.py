# 점수 집계

import sys
sys.stdin = open('input.txt','r')

# T = int(input())

# for t in range(1,T+1):
#     num = list(map(int,input().split()))
#     num.remove(max(num)) 
#     num.remove(min(num))
#     # num = sorted(num)
#     if (max(num) - min(num)) < 4:
#         print(sum(num))
#     else:
#         print('KIN')

min_ = 0

for _ in range(int(input())):
    N = list(map(int,input().split()))
    N.sort()
    N.pop(0)
    N.pop()

    if (N[2]-N[0]) >= 4:
        print('KIN')
    else:
        min_ = sum(N)
        print(min_)