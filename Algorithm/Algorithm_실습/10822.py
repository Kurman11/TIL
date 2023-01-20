# 더하기

import sys
sys.stdin = open('input.txt','r')

num = list(map(int,input().split(',')))
print(sum(num))