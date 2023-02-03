# 직사각형 네개의 합집합의 면적 구하기

import sys
sys.stdin = open('input.txt','r')

a = [[0 for i in range(100)]for x in range(100)]
z = []
for q in range(4):
    num = list(map(int,input().split()))

    for t in range(num[0],num[2]):
        for j in range(num[1],num[3]):
            a[t][j] = 1
# print(*a,sep='\n')
for k in a:
    z.append(k.count(1)) 
print(sum(z))


# square = []
# add = 0
# for _ in range(4):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             square.append((i,j))


# square = set(square)
# print(len(square))






# list1 = []
# num_list =[]
# a = 0
# for i in range(4):
#     num = list(map(int,input().split()))
#     list1.append(num)
#     num_list = abs(num[0]-num[2]) * abs(num[1]-num[3])
#     a += num_list

# print(list1)