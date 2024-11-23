# 쉬운 거스름돈

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = [50000,10000,5000,1000,500,100,50,10]

for i in range(1, T+1):
    N =int(input())
    b = []

    for j in a:
        if N >= j:
            c = N // j
            N = N % j
            b.append(c)
        else:
            b.append(0)
    print(f'#{i}')
    print(*b)
# for i in range(1, T+1):
#     N = int(input())
#     cnt_50000 = 0
#     cnt_10000 = 0
#     cnt_5000 = 0
#     cnt_1000 = 0
#     cnt_500 = 0
#     cnt_100 = 0
#     cnt_50 = 0
#     cnt_10 = 0
    
#     cnt_50000 = N // 50000
#     N = N % 50000
#     cnt_10000 = N // 10000
#     N = N % 10000
#     cnt_5000 = N // 5000
#     N = N % 5000
#     cnt_1000 = N // 1000
#     N = N % 1000
#     cnt_500 = N // 500
#     N = N % 500
#     cnt_100 = N // 100
#     N = N % 100
#     cnt_50 = N // 50
#     N = N % 50
#     cnt_10 = N // 10
#     N = N % 10

#     print(f'#{i}')
#     print(cnt_50000,cnt_10000,cnt_5000,cnt_1000,cnt_500,cnt_100,cnt_50,cnt_10)

