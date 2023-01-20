# 크로아티아 알파벳

str1 = ['c=','c-','dz=','d-','lj','nj','s=','z=']
result = input()
for i in str1:
    result = result.replace(i,'?')
    
print(len(result))
