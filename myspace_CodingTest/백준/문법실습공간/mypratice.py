def bfs(si,sj):
    q = []
    v[si][sj] = 1
    q.append((si,sj))
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci + di,cj +dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt


N,M,V = map(int,input().split())

##a,b,c  = map(int,input().split())
arr = [[0]*M for i in range(N)]
v = [[0]*M for _ in range(N)]
a = 0
b = 0
for i in range(V):
    l1 = list(map(int,input().split()))

    c,d,e,f  = l1[0],l1[1],l1[2],l1[3]
    l2  = [i for i in range(c, e)] # 열
    l3 =  [i for i in range(d, f)] # 행
    for i in l3:
        for j in l2:
            arr[i][j] = 1


result = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and v[i][j] == 0:
            result.append(bfs(i,j))

result.sort()
print(len(result))
for i in result:
    print(i,end = " ")

# DFS

import sys

sys.setrecursionlimit(10 ** 6)  # 재귀의 깊이 변경 (RecursionError)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0


def dfs(x, y):
    global count
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    if graph[x][y] == 1:
        return 0

    graph[x][y] = 1
    count += 1
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

    return count


result = []
for i in range(m):
    for j in range(n):
        cnt = dfs(i, j)
        if cnt:
            result.append(cnt)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')






