# 중앙 이동 알고리즘

import sys
sys.stdin = open('input.txt','r')

num = int(input())
cnt = 2
for i in range(num):
    cnt += 2**i

print(cnt*cnt)