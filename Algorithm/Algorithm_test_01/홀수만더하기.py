
T = int(input())


for t in range(1,T+1):
    num = map(int,input().split())
    a = 0
    for i in num:
        if i%2==1:
            a += i

    print(f"#{t} {a}")

    pass