# 최대 힙
import sys,heapq
sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline())
a = []
b = []
for i in range(T):
    num = int(sys.stdin.readline())
    a.append(num)
for x in a:
    if x != 0:
        heapq.heappush(b,x)
    else:
        if len(b) != 0:
            print(max(b))
            b.remove(max(b))
        else:
            print(0)
            


