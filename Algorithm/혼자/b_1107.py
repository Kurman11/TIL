# 리모컨

import sys
sys.stdin = open('input.txt','r')

N = int(input())
M = int(input())
channel = list(map(int,input().split()))

print(N,M,channel)