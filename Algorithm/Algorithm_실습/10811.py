# 바구니 뒤집기

import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

basket = [_ for _ in range(N+1)]

for t in range(M):
    i, j = map(int,input().split())
    basket[i:j+1] = reversed(basket[i:j+1])
print(*basket[1:])
