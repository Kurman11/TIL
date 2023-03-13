# 그대로 출력하기

import sys
sys.stdin = open('input.txt','r')


while 1:
    try:
        print(input())
    except:
        break