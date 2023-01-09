str = list(map(str,input('문자열을 입력하세요 > ').split()))
a = {}
cnt = 0
for i in str:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

for key,value in a.items():
    print(key,value)