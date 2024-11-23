# 암호생성기

import sys
# from collections import deque
sys.stdin = open('input.txt','r')

for i in range(1, 11):
    T = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    while 1:
        cnt += 1
        if arr[0] - cnt <= 0:
            arr.append(arr.pop(0)-cnt)
            arr[-1] = 0
            break
        else:
            arr.append(arr.pop(0)-cnt)
        
        if cnt == 5:
            cnt = 0

    
    print(f'#{i} {" ".join(map(str,arr))}')