# 파리 퇴치

import sys,pprint
sys.stdin = open('input.txt','r')

T = int(input())
a = []
b = []
for t in range(1,T+1):
    N, M = list(map(int,input().split()))
    num = [list(map(int,input().split())) for _ in range(N)]
    num1 = [[0 for _ in range(M)] for _ in  range(M)]
    n = M-1
    for i in range(N-n):
        for x in range(N-n):
            print(num[i][x])
# pprint.pprint(num)
# pprint.pprint(num1)
    # for i in range(N):
    #     num = list(map(int,input().split()))
    #     for x in range(M):
    #         num1 = list(map(int,input().split()))
    #     print(num)
        