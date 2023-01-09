str,comp = list(map(str,input('문자열을 입력하세요 > ').split()))
a = []
cnt = 0
for i in str:
    for x in comp:
        if x in i:
            cnt += 1

print(cnt)