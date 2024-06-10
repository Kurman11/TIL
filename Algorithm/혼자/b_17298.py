# 오큰수

# import sys
# sys.stdin = open('input.txt','r')

# n = int(input())
# o = input().split()

# b = []

# for i in range(len(o)):
#     current_value = int(o[i])
#     found = False
#     for j in range(i + 1, len(o)):
#         if int(o[j]) > current_value:
#             b.append(int(o[j]))
#             found = True
#             break
#     if not found:
#         b.append(-1)

# print(*b)



import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

stack.append(0)

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)