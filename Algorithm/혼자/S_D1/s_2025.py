# N줄 덧셈

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = 0
for i in range(1,T+1):
    a += i

print(a)