# 별 찍기 -4

num = int(input())
a = ['*'for i in range(num)]
for i in range(num,0,-1):
    print(' '*(num-i) + '*'* i)