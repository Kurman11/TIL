# 대표값2
import sys
sys.stdin = open('input.txt','r')

x = []
for i in range(5):
    x.append(int(input()))
x.sort()
print(int(sum(x)/5))
print(x[2])