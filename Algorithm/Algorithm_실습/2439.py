# 별 찍기-2

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = []
for t in range(1,T+1):
    print(' '*(T-t)+'*'*t)
