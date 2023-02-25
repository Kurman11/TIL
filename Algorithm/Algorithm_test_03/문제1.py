#민석이의 과제 체크하기

import sys
sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1):
    A,B = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    num1_list = []
    for i in range(1,A+1):
        if i not in num2:
            num1_list.append(i)

    print(f'#{t}',*num1_list)

