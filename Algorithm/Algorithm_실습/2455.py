# 지능형 기차

import sys
sys.stdin = open('input.txt','r')

a = 0
b = []

for i in range(4):
    v1, v2= list(map(int,input().split()))
    a = a - v1+ v2
    b.append(a)
print(b)
print(max(b))