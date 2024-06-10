# 오등큰수

import sys
from collections import Counter
sys.stdin = open('input.txt','r')

n = int(input())
lst = list(map(int,input().split()))
dic = dict(Counter(lst))
result = [-1] * n
st = []

for i in range(n):
    while st and dic[lst[st[-1]]] < dic[lst[i]]: # 즉 st의 마지막 이전숫자를 비교
        result[st.pop()] = lst[i]
    st.append(i)

print(*result)


#================ 내가 푼거 시간초과
# 딕셔너리를 표현하고 딕셔너리의 최대값을 사용하면서 시간초과 예상했지만 일단 완성해봄

# import sys
# from collections import Counter
# sys.stdin = open('input.txt','r')

# n = int(input())
# lst = list(map(int,input().split()))
# st = []

# dic = dict(Counter(lst))

# max_key = None
# max_value = -float('inf')

# for key,value in dic.items():
#     if value > max_value :
#             max_value = value
#             max_key = key

# for i in range(len(lst)):
#     if lst[i] == max_key:
#         st.append(-1)
#     else:
#         for j in range(i,len(lst)):
#             if dic[lst[i]] < dic[lst[j]]:
#                 st.append(lst[j])
#                 break
# print(*st)