# 나는 요리사다

import sys
sys.stdin = open('input.txt','r')

num_list =[]
for i in range(5):
    num = list(map(int,input().split()))
    num_list.append(sum(num))

print(num_list.index(max(num_list))+1,max(num_list))