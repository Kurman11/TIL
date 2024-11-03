# 백만 장자 프로젝트

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_num = 0
    num = 0

    for j in range(n-1, -1, -1):
        if arr[j] > max_num:
            max_num = arr[j]
        else:
            num += max_num - arr[j]

    print(f'#{i} {num}')