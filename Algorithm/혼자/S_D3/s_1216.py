# 회문2

import sys
sys.stdin = open('input.txt','r')

def Longstring(word):
    global cnt
    n = len(word)
    
    for i in range(n,0,-1):
        for j in range(n-i+1,0,-1):
            check = word[i+j:i]
            if check == check[::-1]:
                cnt = max(cnt, len(check))
                continue
    
    return cnt



for i in range(1, 11):
    T = int(input())
    arr = [list(map(str,input())) for _ in range(100)]
    cnt = 0
    arr2 = []
    
    for j in range(100):
        check = ''
        check_word = ''
        for k in range(100):
            check += arr[k][j]
            check_word += arr[j][k]
        arr2.append(check)
        arr2.append(check_word)

    for j in arr2:
        Longstring(j)
    
    print(f'#{i} {cnt}')

# T = 10
# for test_case in range(1, T + 1):
#     case = int(input())
#     N = 100
#     arr = [list(input()) for _ in range(N)]
#     mx = 0
 
#     for i in range(N):
#         for n in range(N, 1, -1):
#             if mx > n:
#                 break
#             for j in range(N-n+1):
#                 if arr[i][j:j+n//2] == list(reversed(arr[i][j+n-n//2:j+n])):
#                     mx = max(mx, n)
 
#     arr = list(map(list, zip(*arr)))
 
#     for i in range(N):
#         for n in range(N, 1, -1):
#             if mx > n:
#                 break
#             for j in range(N-n+1):
#                 if arr[i][j:j+n//2] == list(reversed(arr[i][j+n-n//2:j+n])):
#                     mx = max(mx, n)
 
#     print(f"#{case} {mx}")
    