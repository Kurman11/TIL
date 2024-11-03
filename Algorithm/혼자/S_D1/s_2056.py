# 연월일 달력

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1,T+1):
    num = int(input())
    Y = num//10000
    M = (num%10000)//100
    D = (num%10000)%100

    if Y <= 0:
        print(f'#{i} -1')
        continue
    if M <= 0:
        print(f'#{i} -1')
        continue
    if D <= 0:
        print(f'#{i} -1')
        continue
    if M == 2:
        if D>28:
            print(f'#{i} -1')
            continue
    
    if M == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
        if D>31:
            print(f'#{i} -1')
            continue
    
    if M == 4 or 6 or 9 or 11:
        if D > 30:
            print(f'#{i} -1')
            continue

    if Y < 1000:
        Y = '0' + str(Y)
    if M < 10:
        M = '0' + str(M)
    if D < 10:
        D = '0' + str(D)

    print(f'#{i} {Y}/{M}/{D}')