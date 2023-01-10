# 2029. 몫과 나머지 출력하기

# 파이썬 몫 : a//b
# 파이썬 나머지 : a%b

T = int(input())

for t in range(1, T+1):
    a,b = list(map(int,input().split()))
    y = a // b
    u = a % b

    print(f"#{t} {y} {u}")