def Depth_First_Search(c):
    ans_dfs.append(c)
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            Depth_First_Search(n)

def Depth_First_Search(s):
    q = []

    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)


for i in range(1, N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
Depth_First_Search(V)

v = [0]*(N+1)
ans_bfs = []
Depth_First_Search(V)

print(*ans_dfs)
print(*ans_bfs)
