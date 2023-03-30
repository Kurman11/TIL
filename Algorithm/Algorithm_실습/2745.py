# 진법 변환

import sys
sys.stdin = open('input.txt','r')

B ,N = map(str,input().split())

print(int(B,int(N)))