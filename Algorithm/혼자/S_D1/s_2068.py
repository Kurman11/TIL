# 최대수 구하기 D1

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1, T+1):
    arr = list(map(int,input().split()))
    print(f'#{i} {max(arr)}')