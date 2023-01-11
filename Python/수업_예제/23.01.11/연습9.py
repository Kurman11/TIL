import sys
sys.stdin = open('input(9).txt','r')

T, num = map(int,input().split())

for t in range(1,T+1):
    for i in range(num):
        numbers = map(int,input().split())
        print(*numbers)
    
    pass