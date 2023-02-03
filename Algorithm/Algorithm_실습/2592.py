# 대표값

import sys
sys.stdin = open('input.txt','r')

a = []
d = dict()

for i in range(10):
    num = input()
    a.append(int(num))
print(sum(a)//10)


for x in a:
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] +1

for key,value in d.items():
    if max(d.values()) == value:
        print(key)

# nums = [int(input()) for _ in range(10)]


# print(sum(nums) // len(nums))


# c = 0
# for i in nums:

#     cnt = 0
#     for j in nums:
    
#         if i == j:
#             cnt += 1
#     if c < cnt:
#         c = cnt
#         mode = i

# print(mode)

