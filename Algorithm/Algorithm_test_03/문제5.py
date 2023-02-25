# 암호생성기
from collections import deque
import sys
sys.stdin = open('input.txt','r')
from collections import deque
for x in range(10):
    num = int(input())
    num1 = list(map(int,input().split()))
    q = deque(num1)
    a = []
    while 1:
        for i in range(1,6):
            q[0] = q[0]-i
            if q[0]<=0:
                q[0] = 0
                q.append(q.popleft())
                break
            else:
                q.append(q.popleft())
                continue
        if q[-1] == 0: 
            break
    print(f'#{x+1}',*q)
