# 직사각형 길이 찾기
# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    d = dict()
    num1 = list(map(int,input().split()))
    for i in num1:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    for key,value in d.items():
        if value == 3:
            break
        elif value == 1:
            break
    print(f'#{t} {(key)}')