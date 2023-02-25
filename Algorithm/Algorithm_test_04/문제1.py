# 반반

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    word = input()
    word_list = []
    for i in word:        
        word_list.append(i)
    if len(set(word_list)) == 2:
        print(f"#{t} {'Yes'}")
    else :
        print(f"#{t} {'No'}")
