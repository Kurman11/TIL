# 소인수 분해

import sys
sys.stdin = open('input.txt','r')

def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            print(d)

            x = x/d
        else:
            d = d +1

factorization(int(input()))
