# 거꾸로 출력해 보아요

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(T,-1,-1):
    print(i, end=' ')