# 모음이 보이지 않는 사람

import sys
sys.stdin = open('input.txt','r')

T = int(input())
word_list = []
for t in range(1,T+1):
    word = input()
    table = word.maketrans({
        'a' : '',
        'i' : '',
        'o' : '',
        'e' : '',
        'u' : ''
    })
    print(f'#{t} {word.translate(table)}')