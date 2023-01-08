count={}
lists = ["a","a","b",'apple','w','wf']
for i in lists:
    try: count[i] += 1
    except: count[i]=1
print(count)

