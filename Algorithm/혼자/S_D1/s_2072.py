# 홀수만 더하기 D1

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1, T+1):
    cnt = 0
    arr = list(map(int,input().split()))
    for j in arr:
        if j%2 == 1:
            cnt += j
    
    print(f"#{i} {cnt}")