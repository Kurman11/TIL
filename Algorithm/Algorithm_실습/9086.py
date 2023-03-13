# 문자열

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(T):
    word = str(input())

    print(word[0],word[-1], sep='')