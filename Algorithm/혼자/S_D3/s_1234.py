# 비밀번호

import sys
sys.stdin = open('input.txt','r')

for i in range(1,2):
    M, N = map(str,input().split())
    check = -1

    for j in range(int(M)):
        if check == int(N[j]):
            N = N[:j-1] + N[j:]

        else:
            check = int(N[j])

    print(N)


