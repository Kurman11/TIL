# 절댓값 힙


import heapq,sys

T = int(input())
heap =[]
for t in range(T):
    num = int(sys.stdin.readline())
    if num != 0 :
        heapq.heappush(heap,(abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)





