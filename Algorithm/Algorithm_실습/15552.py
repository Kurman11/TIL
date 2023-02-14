# 빠른 A+B

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)
