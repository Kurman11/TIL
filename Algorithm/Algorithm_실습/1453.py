# 피시방 알바

import sys
sys.stdin = open('input.txt','r')

T = int(input())
cnt = 0
num = list(map(int,input().split()))
PC = [0]*101
for i in num:
    if PC[i] != 0:
        cnt += 1
    else:
        PC[i] += 1
print(cnt)
