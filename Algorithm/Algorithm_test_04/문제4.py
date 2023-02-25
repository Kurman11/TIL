# 퍼펙트 셔플

import sys,math
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    word_left = []
    word_right = []
    num = int(input())
    word = list(map(str,input().split()))
    for i in range(math.ceil(num/2)):
        word_left.append(word[i])
    if num%2 == 1:
        for q in range(math.ceil(num/2)):
            word.remove(word[0])
    elif num%2 == 0:
        for q in range(math.ceil(num/2)):
            word.remove(word[0])

    for x in range(math.ceil(num/2)):
        try:
            word_right.append(word_left[x])
            word_right.append(word[x])
        except:
            pass
    print(f'#{t}', *word_right)



# T = int(input())
# num = int(input())
# word_left = []
# word_right = []
# for t in range(1,T+1):
#     word = list(map(str,input().split()))
#     for i in range(round(num//2)):
#         word_left.append(word[i])
#     if num%2 == 1:
#         for q in range(round(num//2)-1):
#             word.remove(word[q])
#     elif num%2 == 0:
#         for q in range(round(num//2)):
#             word.remove(word[q])
# # print(word_left)
# # print(word)

# for x in range(3):
#      word_right.append(word_left[x])
#      word_right.append(word[x])

# print(word_right)
