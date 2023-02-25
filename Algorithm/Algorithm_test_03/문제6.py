# 괄호 짝짓기

import sys
sys.stdin = open('input.txt','r')

for t in range(10):
    T = int(input())

    cnt = 0
    cnt1 =0
    cnt2 =0
    cnt3 =0

    bracket = input()

    for i in bracket:
        if i == '{':
            cnt += 1
        elif i == '}':
            cnt -= 1
        if i == '[':
            cnt1 += 1
        elif i == ']':
            cnt1 -= 1
        if i == '<':
            cnt2 += 1
        elif i == '>':
            cnt2 -=1
        if i == '(':
            cnt3 += 1
        elif i == ')':
            cnt3 -= 1    
    if cnt == 0 :
        if cnt1 == 0 :
            if cnt2 == 0 :
                if cnt3 == 0 :
                    print(f'#{t+1} {1}')
                else:
                    print(f'#{t+1} {0}')
            else:
                print(f'#{t+1} {0}')
        else:
            print(f'#{t+1} {0}')
    else:
        print(f'#{t+1} {0}')