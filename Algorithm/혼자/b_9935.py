# 문자열 폭발

import sys
sys.stdin = open('input.txt','r')

# 내가 푼거 시간초과 확실히 밑에 코드가 더 효율적임

# word1 = str(input())
# word2 = str(input())
# b = []
# i = 0

# while 1:
#     if word2 in word1:
#         if i >= len(word1):
#             word1 = ''.join(b)
#             b = []
#             i = 0
#         else:
#             if word1[i:i+len(word2)] == word2:
#                 i += len(word2)
#             else:
#                 b.append(word1[i])
#                 i += 1
#     else:
#         break

# if len(word1) == 0: 
#     print('FRULA')
# else:
#     print(word1)

# ================ 정답코드
word1 = str(input())
word2 = str(input())
stack = []
word2_len = len(word2)

for char in word1:
    stack.append(char)
    if len(stack) >= word2_len and ''.join(stack[-word2_len:]) == word2:
        del stack[-word2_len:]  # stack에서 word2 제거

result = ''.join(stack)
if result:
    print(result)
else:
    print('FRULA')



