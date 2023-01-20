# 단어 뒤집기

T = int(input())

for t in range(1,T+1):
    str1 = input().split()
    for i in str1:
        print(i[::-1],end=' ')

