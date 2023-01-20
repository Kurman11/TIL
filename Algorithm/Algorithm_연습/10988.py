# 팰린드롬인지 확인하기

# str_list = input()
# a = []
# for i in str_list:
#     a.append(i)

# if a == a[::-1]:
#     print(1)
# else:
#     print(0)

str_list = input()
cnt = 0
cnt1 = len(str_list)-1
is_pal = True
while cnt < cnt1:
    if str_list[cnt] != str_list[cnt1]:
        is_pal =False
        break
    cnt += 1
    cnt1 -= 1

if is_pal:
    print(1)
else:
    print(0)