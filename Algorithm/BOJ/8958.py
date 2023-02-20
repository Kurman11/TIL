# OX 퀴즈

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = []
b = []
for t in range(T):
    cnt = 0
    word = input()
    for i in word:
        if i == 'O':
            cnt += 1
            a.append(cnt)
        elif i =='X':
            cnt = 0
            a.append(cnt)
    b.append(sum(a))
    a = []
print(*b,sep='\n')