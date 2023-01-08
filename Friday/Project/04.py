f = open('./04.txt','w',encoding='UTF8')
with open('./data/fruits.txt','r',encoding='UTF8') as x:
    text = x.readlines()
    a = []
    c = []
    count = {}
    for i in text:
        if i in text:
            a.append(i[:-1])
    for x in a:
        try: count[x] += 1
        except: count[x] = 1

for key,value in count.items():
    print(key,value)
    f.write(f'{str(key)} {int(value)}\n')
f.close()