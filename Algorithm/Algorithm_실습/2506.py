# 점수계산

T = int(input())
a = 0
b = 0
num = list(map(int,input().split()))
for i in range(T):
    if num[i] == 0:
        a = 0
    else:        
        a += 1
        b += a
print(b)