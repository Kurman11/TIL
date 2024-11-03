# 1대1 가위바위보

import sys
sys.stdin = open('input.txt','r')

a,b = map(int,input().split())

if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
else:
    print('A')