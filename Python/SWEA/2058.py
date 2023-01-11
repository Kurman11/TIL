num = int(input())

# a = num //10 
# b = num % 10
# c = a // 10
# d = a % 10
# e = c // 10
# f = c % 10
# g = e //10
# h = e % 10

# print(b+d+f+h)
a = 0
while num> 0:
    a += num%10
    num //= 10
    
print(a)
    

