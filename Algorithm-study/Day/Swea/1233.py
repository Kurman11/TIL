# [S/W 문제해결 기본] 9일차 - 사칙연산 유효성 검사

import sys
sys.stdin = open('input.txt','r')

T = 1

num = int(input())
node = [input().split()[1:] for _ in range(num)]

print(node)