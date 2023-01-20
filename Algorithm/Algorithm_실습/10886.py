# not cute/1 =cute

T = int(input())
a = []

for t in range(1,T+1):
    num = int(input())
    a.append(num)

not_cute = a.count(0)
cute = a.count(1)

if not_cute > cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
        
