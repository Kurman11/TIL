# 파리 퇴치

import sys,pprint
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    N, M = list(map(int,input().split()))
    num = [list(map(int,input().split())) for _ in range(N)]
    num1 = [[0 for _ in range(M)] for _ in  range(M)]
    n = M-1
    t = 4
    i = 0
while 1: 
    a= 0
    i = 0
    for x in range(M):           
        q = t-x
        a += num[i][q]
        i += 1
    t -= 1
    if q == 0:
        break
    print(a)
        
        #     print(num[i][x-1])
        # print()             
        
        