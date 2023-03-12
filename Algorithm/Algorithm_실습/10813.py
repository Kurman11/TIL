# 공 바꾸기

import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

basket = [_ for _ in range(N+1)]

for t in range(M):
    i, j = map(int,input().split())
    basket[i] , basket[j] = basket[j], basket[i]
print(*basket[1:])