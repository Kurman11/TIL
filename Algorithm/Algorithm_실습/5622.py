# 다이얼

str1 = input()
a = []
number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for i in number:
    for x in i:
        for t in str1:
            if t in x:
                a.append(number.index(i)+3) 
print(sum(a))