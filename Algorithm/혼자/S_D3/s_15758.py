# 무한 문자열

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1,T+1):
    S, T = map(str,input().split())
    num_1,num_2  = len(S), len(T)

    if S * num_2 == T * num_1:
        print(f"#{i} yes")
    else:
        print(f"#{i} no")


# import sys, math
# sys.stdin = open('input.txt','r')

# T = int(input())

# for i in range(1 , T+1):
#     S, T = map(str,input().split())
#     num_1,num_2  = len(S), len(T)
    
#     lcm = (num_1 * num_2) // math.gcd(num_1, num_2)

#     a = S * (lcm//num_1)
#     b = T * (lcm//num_2)

#     if a == b:
#         print(f"#{i} yes")
#     else:
#         print(f"#{i} no")
