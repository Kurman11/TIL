# 단어 뒤집기2

import sys
sys.stdin = open('input.txt','r')

data = input()

stack = []
ans = ''
check = False # 괄호안의 여부를 체크
for d in data:
    # 스택에 존재하는 값을 역으로 추가합니다.
    if d == '<':
        check = True
        for _ in range(len(stack)):
            ans += stack.pop()

    stack.append(d)
    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가합니다.
    if d == '>':
        check = False
        for _ in range(len(stack)):
            ans += stack.pop(0)
    # 스택에 존재하는 값을 역으로 추가합니다.
    if d == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += ' '
# 스택에 값이 남아있는 경우는 괄호의 경우가 아니기에 역으로 추가합니다.
if stack:
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)



# word1 = str(input())
# a = []
# b = []
# for i in word1:
#     if '<'in word1:
#         if i == '<':
#             if len(a) == 0:
#                 pass
#             else:
#                 b.append(a)
#             a = []

#         elif i == '>':
#             a.append(i)
#             b.append(a)
#             a = []
#             continue
#         a.append(i)
#     else:
#         if i == ' ':
#             b.append(a)
#             a = []
#             continue
#         a.append(i)

# if len(a) == 0:
#     pass
# else:
#     b.append(a)

# for i in range(len(b)):
#     if b[i][0] == '<':
#         pass
#     else:
#         b[i] = b[i][::-1]


# for i in b:
#     for j in i:
#         print(j, end='')