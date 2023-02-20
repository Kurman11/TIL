import sys
sys.stdin = open('input.txt','r')

word = input()
a = []
b = []
c = []
x = 0
t = 0
z = 0
for i in range(len(word)):
    b.append(word[i])
    if word[i] =='(':
        x = i
    if word[i] == ')':
        t = i
        a = range(x+1,t)
        for z in list(a):
            b.append(word[z])
        if i != len(word) - 1:
            if word[t+1].isdigit() == True:
                z = int(word[t+1])
                b = b 
            else:
                z = word[t+1]
                b += z
print(b)
                
            
    # for w in range(x+1,t):
    #     a.append(word[w]) 
    # b = ''.join(a)

# print(b)
