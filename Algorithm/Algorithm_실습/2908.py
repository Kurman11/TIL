# 상수

import sys
sys.stdin = open('input.txt','r')

A, B = map(str,input().split())

if A[::-1] > B[::-1]:
    print(A[::-1])
else:
    print(B[::-1])


