# 파리 퇴치

import sys,pprint
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    N, M = list(map(int,input().split()))
    num = [list(map(int,input().split())) for _ in range(N)]
    num1 = [[0 for _ in range(M)] for _ in  range(M)]
    n = M-1
    t = 0
    
    for i in range(N):
        a = 0
        for x in range(M):
            a += num[i][x+t]
            if (x+t) != N-1:
                t += 1
            else:
                break
                
        #     print(num[i][x-1])
        # print()             
        print(a)