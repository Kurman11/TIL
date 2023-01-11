import sys
sys.stdin = open('input(3).txt','r')

T = int(input())

for t in range(1,T+1):
    num = int(input())
    for i in range(1,num+1):
        print(i)
    pass