# 더하기 사이클
num = int(input())
cnt =0
num_str = str(num)

if len(num_str) == 1:
    num_str = '0' + num_str

while 1:
    result = 0
    for i in str(num_str):
        result +=int(i)
    for t in str(result):
        pass
    num_str = int(i + t)

    cnt += 1

    if num == num_str:
        break



print(cnt)




# N = int(input())
# M  = str(N)     # 시작 N의 값이 변하면 while에서 비교 불가 => M을 따로 지정하고 while에 들어갈수 있게 str로 변경
# result = 0
# cnt = 0
# if len(M) == 1:
#     M = "0" + M

# while N != M:   # N과 M이 동일할때까지 반복, 시작 M은 문자지만 while 겉치면서 int로 변환하여 맞춤
#     result = 0
#     for m in str(M):    # 문자로 변경
#         result += int(m)
#     for R in str(result):
#         pass    # 필요없으니 pass
#     M = int(m + R)  # m, R의 끝 문자를 더하고 int로 변환
#     cnt += 1
# print(cnt)