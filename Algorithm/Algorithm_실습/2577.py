# 숫자의 개수

import sys
sys.stdin = open('input.txt','r')

# from collections import Counter


# A = int(input())
# B = int(input())
# C = int(input())

# product = list(str(A * B * C))

# for i in range(10):
#     print(product.count(str(i)))
    
A = int(input())
B = int(input())
C = int(input())

product = A * B * C

d = dict()
for i in str(product):
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] +1
for x in range(10):
    if str(x) not in d.keys():
        d[str(x)] = 0

for key,velue in sorted(d.items()):
    print(velue)


# a = {
#     '2' : '0',
#     '4' : '0',
#     '5' : '0',
#     '6' : '0',
#     '8' : '0',
#     '9' : '0',
# }