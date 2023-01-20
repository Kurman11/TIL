# 회사에 있는 사람
import sys
sys.stdin = open('input.txt','r')

# T = int(input())
# a = dict()
# b = {}
# for t in range(1,T+1):
#     A,B =list(map(str,input().split()))
#     a[A] = B

# for key,value in a.items():
#     if value == 'enter':
#         print(1)
#     else:
#         del(a[key])
# print(a)


T = int(input())
a ={}
for t in range(1,T+1):
    key ,value = input().split()
    if value == 'enter':
        a[key] = 'enter'
    else:
        del(a[key])

for key,value in sorted(a.items(),reverse=True):
    print(key)