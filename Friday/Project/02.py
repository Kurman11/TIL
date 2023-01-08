
f = open('./02.txt','w',encoding='UTF-8')
with open('./data/fruits.txt','r',encoding='UTF8') as x:
    text = x.readlines()
    x = list()
    a = 0
    for i in text:
        if i in x:
            a = a
        else:
            a += 1
    print(a)
    f.write(str(a))
f.close()

