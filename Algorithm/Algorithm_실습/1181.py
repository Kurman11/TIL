# 단어정렬

import sys
sys.stdin = open('input.txt','r')


T = int(input())
a = []
x = []
for t in range(1,T+1):
    word = input()
    a.append(word)

x = sorted(set(a))
x.sort(key=len)
print(*x, sep= '\n')
    
