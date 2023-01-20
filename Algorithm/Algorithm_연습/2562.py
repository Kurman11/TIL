# 최댓값
# a = []
# cnt = 0
# for i in range(9):
#     num = list(map(int,input().split()))
#     a.append(*num)
#     b = sorted(a)

# print(b[-1], a.index(max(a))+1, sep='\n')

a = []
cnt = 0


for x in range(9):
    num = list(map(int,input().split()))
    num_list = num[0]
    a.append(num)

    for i in a:
        if num_list < i:
            num_list = i

print(num_list)