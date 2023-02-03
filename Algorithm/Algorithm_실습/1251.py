# 단어 나누기

import sys
sys.stdin = open('input.txt','r')
list1=[]
num = input()
for i in range(1, len(num)):
    for x in range(i+1,len(num)):
        a = num[:i][::-1]
        b = num[i:x][::-1]
        c = num[x:][::-1]
        list1.append(a+b+c)
list1.sort()
print(list1[0])



# a = input()
# lst = []
# for i in range(1, len(a)):       # 모든 경우의 수를 구한다
#     for j in range(i+1, len(a)):
#         first = a[:i][::-1]   # m
#         second = a[i:j][::-1] # o
#         third = a[j:][::-1] # letib 
#         lst.append(first + second + third) # 글자수를 유지하며 반복한 모든 수를 더한다
# lst.sort()
# print(lst[0]) # 정렬 시 정답이 알파벳 순서상 첫번째로 나오기 때문에 [0]을 통해 출력


# a = []
# b = []
# def list_chunk(lst,n):
#     return [lst[i:i+n] for i in range(0, len(lst),n)]

# word =input().split() # list(map(str,input().split()))
# for i in word:
#     a.append(i)
# list_chunked = list_chunk(i,3)

# # list__chunked = list_chunked.reverse()
# # print(list__chunked)

# for x in list_chunked:
#     b.append(list(reversed(x)))
# t = sum(b,[])

# for q in t:
#     print(q,end='')




# list_test = list(range(1,32))
# print("분할 전 : ", list_test)

# list_chunked = list_chunk(list_test, 7)
# print("분할 후 : ", list_chunked)