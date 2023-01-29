# 나머지
import sys
sys.stdin = open('input.txt','r')

a =[]

for i in range(10):
    num = list(map(int,input().split()))
    for i in num:
        a.append(i % 42) 

print(len(set(a)))