# 색종이

import sys
sys.stdin = open('input.txt','r')

arr = [[0 for _ in range(100)] for _ in range(100)]

T = int(input())
a = []
for t in range(T):
    X,Y = map(int,input().split())
    for x in range(X,X+10):
        for y in range(Y,Y+10):
            arr[x][y] = 1

for x in range(100):
    a.append(sum(arr[x]))

print(sum(a))
