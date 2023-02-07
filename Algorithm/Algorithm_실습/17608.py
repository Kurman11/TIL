# 막대기
# 딕셔너리로 풀려고 접근했지만 풀은건 리스트방식....
import sys
sys.stdin = open('input.txt','r')

num = int(input())
d = dict()
a = []
temp = 0
for i in range(1,num+1):
    d[i] = int(input())

for x in range(num,0,-1):
    temp = max(d[x],temp)
    if d[x] > temp : 
        a.append(d[x])
    else:
        a.append(temp)

b = list(set(a))
print(len(b))




