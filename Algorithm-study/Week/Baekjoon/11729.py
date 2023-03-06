# 하노이 탑 이동 순서
import sys
sys.stdin = open('input.txt','r')

a = []
b = []
c = []

num = int(input())

for i in range(num,0,-1):
    a.append(i)


while 1:
    if len(c) == 0:
        c.append(a.pop())
    else:
        if a.pop() > c[-1]:
            if a.pop() < b[-1]:
                b.append(a.pop())
        else:
            c.append(a.pop())
    
    if len(b) == 0:
        b.append(a.pop())
    else:
        if a.pop() > b[-1]:
            
            c.append(a.pop())
