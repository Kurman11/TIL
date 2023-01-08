f = open('./01.txt','w',encoding='UTF-8')

data = 'Hello, Python!\n'
f.write(data)
a = 1
for i in range(1,5):
    a= '%d일차 파이썬 공부중\n'%i
    print(a)
    f.write(a)

f.close()