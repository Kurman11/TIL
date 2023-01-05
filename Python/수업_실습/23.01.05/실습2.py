str = input('문자열을 입력하세요 > ')
words = ['a','A','e','E','i','I','o','O','u','U']
t = 0

for i in str:
    for x in words :
        if i == x:
            t += 1
print(t)
