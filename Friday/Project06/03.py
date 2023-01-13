
f = open('./03.txt','w',encoding='UTF8')
with open('./data/fruits.txt','r',encoding='UTF8') as x:
    text = x.readlines()
    count = 0
    a = []
    c = []
    for i in text:
        if 'berry' in i[-7:]:
            a.append(i[:-1])


for w in a :
    if w not in c :
        c.append(w)

f.write(str(f'{len(c)}\n'))

for l in c:
    print(l)
    f.write(f'{l}\n')

print(l)
f.close()

