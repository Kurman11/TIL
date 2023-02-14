# A+B -4

import sys
sys.stdin = open('input.txt','r')

while 1:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break