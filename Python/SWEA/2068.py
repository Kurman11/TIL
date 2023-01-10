# 최대수 구하기

T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    a = 0
    for i in numbers:
        if i > a:
            a = i



#     # a = max(numbers)

    print(f"#{t} {a}")


# T = int(input())
# for i in range(T):
#     a = list(map(int, input().split()))
#     a.sort(reverse=True)
#     print(f"#{i+1} {a[0]}")


# T = int(input())
# for t in range(1, T+1) :
#     num_list = sorted(list(map(int, input().split())))
#     test_num = '#' + str(t)
#     print(test_num, num_list[-1])