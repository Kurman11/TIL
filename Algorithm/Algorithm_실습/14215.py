# 세 막대

import sys
sys.stdin = open('input.txt','r')

li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(res)