# 소득 불균형

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    cnt =0
    num = int(input())
    num1 = list(map(int,input().split()))
    b =sum(num1)//num
    for i in num1:
        if b >= i:
            cnt += 1
    print(f'#{t} {(cnt)}')
