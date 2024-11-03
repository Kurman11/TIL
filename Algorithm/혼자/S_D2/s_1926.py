# 간단한 369 게임

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(1, T+1):
    num_str = str(i)
    clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')
    
    if clap_count > 0:
        print('-' * clap_count, end=' ')
    else:
        print(i, end=' ')
    # if i == 36 or i == 39 or i == 69:
    #     print('--', end=' ')
    # elif i == 369:
    #     print('---', end='')
    # elif i == 3 or i == 6 or i == 9:
    #     print('-', end =' ')
    # else:
    #     print(i, end = ' ')