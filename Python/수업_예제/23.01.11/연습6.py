import sys
sys.stdin = open('input(6).txt','r')

T = int(input())

for t in range(1,T+1):
    num = int(input())
    for i in range(num):
        numbers = input().split()
        print(*numbers)
    pass