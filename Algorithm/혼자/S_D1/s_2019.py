# 더블더블

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(T+1):
    print(2**i, end=' ')

