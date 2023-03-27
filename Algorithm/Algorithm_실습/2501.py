# 약수 구하기

import sys
sys.stdin = open('input.txt','r')

N,K = map(int,input().split())
b = []
for i in range(1,N+1):
    if N%i == 0:
        b.append(i)
        if len(b) == K:
            print(i)
            break
else:
    print(0)