# 피보나치 함수
import sys
sys.stdin = open('input.txt','r')

T = int(input())

a = [1, 0, 1, 1, 8]
b = [0, 1, 1, 2, 13]

for i in range(T):
    num = int(input())
    b[i] = a[i-1] + b [i-1]
    b.append(b[i])
    a[i] = b[i] - a[i-1]
    a.append(a[i])
    print(max(a),max(b))