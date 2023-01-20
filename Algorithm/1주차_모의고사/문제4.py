# 문자열 거울상
import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
    }
pnt = ''

for t in range(1,T+1):
    b = []
    str1 = input()
    for i in str1:
        b.append(a[i])
    print(f"#{t} {''.join(b[::-1])}")
