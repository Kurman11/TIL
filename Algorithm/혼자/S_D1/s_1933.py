# 간단한 N의 약수

import sys
sys.stdin = open('input.txt','r')

# T = int(input())
# num = T//2
# a = []
# for i in range(1, num+1):
#     if (T%i) == 0:
#         b = T // i
#         a.append(i)
#         a.append(b)

# a = list(set(a))
# a.sort()
# print(*a)


T = int(input())

for i in range(1, T+1):
    if T % i == 0:
        print(i, end=' ')