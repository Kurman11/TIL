# 날짜 계산

import sys
sys.stdin = open('input.txt','r')

# 지피티가 준 더 간단한 코드

E, S, M = map(int, input().split())

cnt = 1
Earth, Sun, Moon = 1, 1, 1

while (Earth, Sun, Moon) != (E, S, M):
    Earth = (Earth % 15) + 1
    Sun = (Sun % 28) + 1
    Moon = (Moon % 19) + 1
    cnt += 1

print(cnt)

# 내가 만든 코드 

# E, S, M = map(int,input().split())

# cnt = 1
# Earth = 1
# Sun = 1
# Moon = 1

# while 1:
#     if (Earth, Sun, Moon) ==  (E, S, M):
#         break

#     if 1 <= Earth <= 15 and 1 <= Sun <= 28 and 1 <= Moon <= 19:
#         Earth += 1
#         Sun += 1
#         Moon += 1
#         cnt += 1

#     elif Earth > 15:
#         Earth = 1
        
#     elif Sun > 28:
#         Sun = 1

#     elif Moon > 19:
#         Moon = 1
    
# print(cnt)