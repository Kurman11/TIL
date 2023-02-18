# 화학식량

from collections import deque
import sys
sys.stdin = open('input.txt','r')

word = input()
word_dict = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}
a = deque()
b = []
cnt1 = 0
cnt2 = 0
for i in word:
    a.append(i)
for key,value in word_dict.items():   
    for x in range(len(a)):
        if a[0] == key:
            a.append(value)
            a.popleft()
        else:
            a.append(a[0])
            a.popleft()

for q in range(len(a)):
    cnt1 += a[q]
    if '(' == a[q]:
        

    


    



# for key,value in word_dict.items():
#     for x in a:
#      temp = word.replace
#     if key in word:
#         word = word.replace(key,value)

# print(word)

# a = []
# b = []
# c = []
# d = []
# f = []
# word = input()
# word_dict = {
#     'H' : 1,
#     'C' : 12,
#     'O' : 16
# }

# for i in word:
#     if '(' == i:
#         b.append(i)
#     elif ')' == i:
#         b.append(i)
#     else:
#         a.append(i)
# # c.append(''.join(a))


# for x in a:
#     try:
#         c.append(int(x))
#     except:
#         c.append(x)

# print(c)
# for t in c:
#     if t not in word_dict:
#         word_dict[t] = t

# print(c)
# for key,value in word_dict.items():
#     for q in c:
#         if q in word_dict.keys:
#             print(q)
#         else:
#             print(q)





