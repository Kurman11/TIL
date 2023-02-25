T = int(input())

for t in range(1,T+1):
    cnt = 0
    a = []
    
    num = list(map(int,input().split()))
    for i in range(1,10**6):
        x = num[0] * i
        while x> 0:
            b = x%10
            a.append(b)
            x //= 10
            c = set(a)
            d = len(c)
            if d == 10:
                print(i)
            

  
    pass

# num = int(input())
# a = []
# b = 0
# while num> 0:
#     b = num%10
#     a.append(b)
#     num //= 10
    
# print(a)