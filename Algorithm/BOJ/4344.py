# 평균은 넘겠지

import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = []
b = 0
c = []
for i in range(T):
    num = list(map(int,input().split()))
    c = num
    for x in range(1,len(num)):
        a.append(num[x])
    b = int(sum(a)/num[0])
    a = []
    for q in range(1,len(num)):
        if num[q] < b:
            print(num[q])
        
# # print(b)
# print(c)
# for t in c:
#     for q in b:
#         if q < t:
#             print()
