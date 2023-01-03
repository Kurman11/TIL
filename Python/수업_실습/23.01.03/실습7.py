num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 > num2:
    for i in range(num2 +1,num1):
        print(i)
elif num1 < num2 :
    for i in range(num1 +1, num2):
        print(i)
else:
    print('False')