num = list(map(int,input().split()))
a = []
Grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in Grades:
    for x in range(num[0]):
        a.append(i)
print(a)



