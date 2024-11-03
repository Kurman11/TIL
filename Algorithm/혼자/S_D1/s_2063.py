# 중간값 찾기

import sys
sys.stdin = open('input.txt','r')

T = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[len(arr)//2])