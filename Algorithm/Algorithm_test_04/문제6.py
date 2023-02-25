# Flatten

import sys,math
sys.stdin = open('input.txt','r')


for x in range(10):
    T = int(input())
    num = list(map(int,input().split()))
    for i in range(T):
        a = max(num) - 1
        b = min(num) + 1
        num.append(a)
        num.append(b)
        num.remove(max(num))
        num.remove(min(num))
    print(f'#{x+1} {max(num)-min(num)}')