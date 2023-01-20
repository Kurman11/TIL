# 열 개씩 끊어 출력하기

str1 = input()
cnt = 0
for i in str1:
    cnt += 1  # 문자열 수만큼 카운트
for x in range(0,cnt,10): # 0부터 문자열 수 까지 10씩 증가
    print(str1[x:x+10]) # 0,10 / 10,20 / 20,30 값을 프린트