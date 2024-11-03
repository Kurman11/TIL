# 알파벳을 숫자로 변환

import sys
sys.stdin = open('input.txt','r')

T = list(map(str,input()))
a = []
for i in T:
    a.append(ord(i) - 64)

print(*a)