str = list(map(str,input('문자열을 입력하세요 > ').split(',')))
for i in str:
    if 'e' in i:
        print(1)
        print(i.index('e'))
    else:
        print(-1)
