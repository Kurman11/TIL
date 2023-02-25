# 최수빈 구하기

import sys
sys.stdin = open('input.txt','r')

T = int(input())
d = dict()
a = []
for t in range(1,T+1):
    d = dict()
    num = int(input())
    num1 = list(map(int,input().split()))
    for i in num1:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
            
    for key, value in d.items():
        if max(d.values()) == value:
            print(f'#{num} {key}')

# print(num ,num1, sep= '\n')