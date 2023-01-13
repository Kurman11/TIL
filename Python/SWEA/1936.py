
scissors = int(1)
rock = int(2)
paper = int(3)

A , B= map(int,input().split())

if rock > scissors:
    print(A)
elif scissors > paper:
    print(A)
elif paper > rock:
    print(A)

