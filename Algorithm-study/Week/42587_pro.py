# 프린터
import sys
sys.stdin = open('input.txt','r')

from collections import deque
stack = []
priorities = list(map(int,input().split()))
dq= deque([(v,i) for i,v in enumerate(priorities)])
location = int(input())
idx = []
stack = []
# mdq = max(priorities)
# print(mdq)
# z = dq.popleft()
# print(z[0])
while 1:
    mdq = max(dq)
    z = dq.popleft()
    if mdq != z:
        dq.append(z)
    elif mdq == z:
        stack.append(z)
    
    if len(dq) == 0:
        break

print(stack)

# for a,b in dq:
#     idx.append(b)

# print(dq)
# print(idx)
# print(idx.index(location)+1)