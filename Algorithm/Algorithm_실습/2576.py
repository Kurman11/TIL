# 홀수

import sys
sys.stdin = open('input.txt','r')

a = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        a.append(num)
        b = [sum(a),min(a)]      
    elif a == []:
        b = [-1]
    
print(*b,sep='\n')
