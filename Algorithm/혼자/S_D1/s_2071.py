# 평균값 구하기 D1

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1,T+1):
    cnt = 0
    cnt1 = 0
    arr = list(map(int,input().split()))
    for j in arr:
        cnt += j
        cnt1 += 1
    
    print(f"#{i} {round(cnt/cnt1)}")