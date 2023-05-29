# 소트인사이드

import sys
sys.stdin = open('input.txt','r')

num = input()
a = []
b = []
c = []
for i in num:
    a.append(i)

for i in a:
    b.append(int(i))

for i in sorted(b)[::-1]:
    print(i,end='')
