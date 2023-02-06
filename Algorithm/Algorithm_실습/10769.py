# 행복한지 슬픈지

import sys
sys.stdin = open('input.txt','r')

word = input()

happy = word.count(':-)')
sad = word.count(':-(')

if happy > sad :
    print('happy')
elif happy == 0 and sad == 0 :
    print('none')    
elif happy == sad :
    print('unsure')
elif happy < sad :
    print('sad')


# a = []
# b = []
# c = []
# d = []
# q = [] 
# for i in word:
#     if ':' in i:
#         a.append(i)
#     if '-' in i:
#         a.append(i)
#     if ')' in i:
#         a.append(i)
#     if '(' in i:
#         a.append(i)

# for x in range(6):
#     b = a[x]


# if (c+d)*2 == (a+b):
#     if c > d :
#         print('happy')
#     elif c == d:
#         print('unsure')
#     elif c < d:
#         print('sad')
# elif a+b+c == (a-1+b-1+c):
#     print('unsure')
# else:
#     print('none')

# print(a,b,c,d)

