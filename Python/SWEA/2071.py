
# 평균값 구하기
T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    # result = 0
    # cnt = 0
    # for x in numbers:
    #     result += x
    #     cnt += 1
    # average = round(result/cnt,0)
    
    # print(f'#{t} {int(average)}')
    
    
    x = sum(numbers)/len(numbers)
    average = round(x,0)

    print(f"#{t} {int(average)}")