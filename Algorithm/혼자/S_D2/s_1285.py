# 아름이의 돌 던지기

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1 , T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    a = 1e9
    cnt = 1
    for j in range(len(arr)):
        arr[j] = abs(arr[j])
        
        
    print(f'#{i} {min(arr)} {arr.count(min(arr))}')
