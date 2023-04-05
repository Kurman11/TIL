# 달팽이는 올라가고 싶다

import sys
sys.stdin = open('input.txt','r')

A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
