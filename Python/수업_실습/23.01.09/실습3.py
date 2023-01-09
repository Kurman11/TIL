str = list(map(str,input('문자열을 입력하세요 > ')))
a = []
for i in str:
    if 'e' not in i:
        a.append(i)
t = ''
for x in a:
    t +=x
print(t)