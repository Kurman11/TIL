# 신용카드 만들기 2
import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    num = input()
    num = list(num.replace('-',''))
    if len(num) == 16:
        if num[0] in '34569':
            number = 1
        else:
            number = 0
    else:
        number = 0
    print(f'#{t} {number}')