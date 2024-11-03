# 큰 놈, 작은 놈, 같은 놈 D1

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1, T+1):
    arr = list(map(int,input().split()))
    if arr[0] > arr[1]:
        print(f"#{i} {'>'}")
    elif arr[0] == arr[1]:
        print(f"#{i} {'='}")
    else:
        print(f"#{i} {'<'}")