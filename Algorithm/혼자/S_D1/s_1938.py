# 아주 간단한 계산기

import sys
sys.stdin = open('input.txt','r')

K,P = map(int,input().split())

print(K+P)
print(K-P)
print(K*P)
print(K//P)