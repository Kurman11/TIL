str = input('문자열을 입력하세요 > ')
dict = {}
a = 0
x = 0

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for key in dict:
    print(key,dict[key])