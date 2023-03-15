# 바구니 순서 바꾸기

import sys
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
num = [_ for _ in range(1,N+1)]

for i in range(M):
    i, j, k = map(int, input().split())
    num[i-1:j] = num[k-1:j] + num[i-1:k-1]

print(*num)