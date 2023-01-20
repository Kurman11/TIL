# 더하기

T = int(input())
a =0
for t in range(1,T+1):
    num = int(input())
    num_list = list(map(int,input().split()))
    a = 0
    for i in range(num):
        if num_list[i] <= 10:
            a += num_list[i]
    print(a)
    
