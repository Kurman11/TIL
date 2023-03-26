# 배수와 약수

import sys
sys.stdin = open('input.txt','r')

while 1:
    A,B = map(int,input().split())
    if A == 0 and B==0:
        break

    if B % A == 0:
        print('factor')

    elif A % B == 0:
        print('multiple')
    else:
        print('neither')
