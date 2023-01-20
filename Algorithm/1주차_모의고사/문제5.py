import sys
sys.stdin = open('input.txt','r')

T = int(input())
y = []
for t in range(1,T+1):
    x = 0
    cnt = 0
    num = list(map(int,input().split()))
    for i in range(len(num)):        
        if i % 2 == 0:
            x += num[i]*2            
        else:
            x += num[i]
    y.append(x)
    for w in range(15):
        if x % 10 != 0 :
            x += 1
            cnt += 1
        else:
            break
    print(f'#{t} {cnt}')