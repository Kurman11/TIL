# 공 넣기

import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

basket = [0 for _ in range(N+1)]


for t in range(M):
    i, j, k = map(int,input().split())
    for x in range(i,j+1):
        basket[x] = k

print(*basket[1:])

    