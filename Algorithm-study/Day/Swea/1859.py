# 백만 장자 프로젝트

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    a = []
    num = int(input())
    Hoarding = list(map(int,input().split()))
    cnt = 0
    max_num = 0
    while 1:
        if Hoarding[-1] > max_num:
            max_num = Hoarding[-1]
            Hoarding.pop()
        else:
            cnt += max_num - Hoarding[-1]
            Hoarding.pop()

        if len(Hoarding) == 0:
            break
    
    print(f'#{t} {cnt}')















# T = int(input())

# for t in range(1,T+1):
#     a = []
#     num = int(input())
#     Hoarding = list(map(int,input().split()))
#     max_num = 0
#     cnt = 0
#     for i in range(len(Hoarding)-1,-1,-1):
#         if Hoarding[i] > max_num:
#             max_num = Hoarding[i]
#         else:
#             cnt += max_num - Hoarding[i]
            
            
#     print(cnt)



