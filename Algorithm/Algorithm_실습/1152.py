# 단어의 개수

import sys
sys.stdin = open('input.txt','r')

word = list(map(str,input().split()))
print(len(word))