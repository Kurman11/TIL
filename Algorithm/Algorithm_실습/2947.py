# 나무 조각

num = list(map(int,input().split()))

while 1:
    for i in range(4):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1] , num[i]
            print(*num)
        else:
            num[i], num[i+1] = num[i], num[i+1]  
    if num == sorted(num):
        break




