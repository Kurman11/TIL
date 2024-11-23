def dfs(c):
    ans_dfs.append(c)
    v[c] = 1

    for i in arr[c]:
        if not v[i]:
            dfs(i)

def bfs(c):
    q = []
    q.append(c)
    ans_bfs.append(c)
    v[c] = 1

    while q:
        s = q.pop(0)
        for i in arr[s]:
            if not v[i]:
                q.append(i)
                ans_bfs.append(i)
                v[i] = 1


N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(1, N+1):
    arr[i].sort()

v = [0] * (N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = []
bfs(V)

print(ans_dfs)
print(ans_bfs)