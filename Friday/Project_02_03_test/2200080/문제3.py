# 조교의 성적 매기기

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    a = {}
    b = []
    num = list(map(int,input().split()))
    Grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for s in Grades:
        for y in range(num[0]//10):
            b.append(s)
    for i in range(num[0]):
        num1 = list(map(int,input().split()))
        a[num1[0] * 0.35 + num1[1] * 0.45 + num1[2] * 0.2] = i+1
    for q,(key, value) in enumerate(sorted(a.items(),reverse=True)):
        if value == num[1]:
            print(f'#{t} {b[q]}')
            # if q < 10:
            #     print(b[q])
            #     print(q)
            # else:
            #     print(b[q%10])
            #     print(q)