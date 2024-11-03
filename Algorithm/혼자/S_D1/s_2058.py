# 자릿수 더하기

import sys
sys.stdin = open('input.txt','r')

T = list(map(int,input()))
cnt = 0
for i in T:
    cnt += i

print(cnt)