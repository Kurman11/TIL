# 프린터
import sys
sys.stdin = open('input.txt','r')

from collections import deque
stack = []
priorities = list(map(int,input().split()))
dq= deque([(v,i) for i,v in enumerate(priorities)])
location = int(input())
idx = []


while 1:
    mdq = max([x[0] for x in dq])
    z = dq.popleft()
    if mdq != z[0]:
        dq.append(z)
    elif mdq == z[0]:
        stack.append(z)
    
    if len(dq) == 0:
        break

for a,b in stack:
    idx.append(b)

print(idx)
print(idx.index(location)+1)