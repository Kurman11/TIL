import sys
sys.stdin = open('input(5).txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    for i in range(N):
        string = input().split()
        print(*string)
    pass