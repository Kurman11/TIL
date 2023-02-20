# 평균

import sys
sys.stdin = open('input.txt','r')

stack = []

T = int(input())
num = list(map(int,input().split()))
num = sorted(num)
for i in range(T):
    stack.append(num[i]/max(num)*100)

print(sum(stack)/T)