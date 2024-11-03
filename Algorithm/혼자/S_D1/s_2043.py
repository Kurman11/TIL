# 서랍의 비밀번호

import sys
sys.stdin = open('input.txt','r')

K,P = map(int,input().split())

rst = abs(K - P) + 1

print(rst)