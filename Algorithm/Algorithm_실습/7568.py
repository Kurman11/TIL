# 덩치

import sys
sys.stdin = open('input.txt','r')

T = int(input()) # 전체 사람수 N
a = [] # 몸무게 키를 담을 리스트

for t in range(1,T+1):
    weight, height = map(int,input().split()) # 몸무게,키를 받는다
    a.append((weight,height)) # a 리스트에 튜플로 담아준다

for x in a: # x에 리스트 튜플 값을 넣어준다.
    cnt = 1 # 카운트 초기 값을 1로
    for w in a: # w에 리스트 튜플 값
        if (x[0] < w[0]) and (x[1] < w[1]): # 만약 키 그리고 몸무게가 모두다 크다면 
            cnt += 1 # 카운트에 1을 더한다
    print(cnt,end =' ')

# # height_1 = dict()
# # weight_1 = dict()
# d = dict()
# for t in range(1,T+1):
#     num = list(map(int,input().split()))
#     x = chr(64+t)
#     d[x] = num
#     for q in range(T,0,-1):
#         if d[x][0] > d[x][0] :
#             if d[x][1] > d[x][1]:
#                 print(d[x])



