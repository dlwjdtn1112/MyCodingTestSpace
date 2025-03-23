def bfs(si,sj):
    q = []
    cnt = 1
    q.append((si,sj))
    V[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci + di,cj + dj
            if 0<= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and V[ni][nj] == 0:
                q.append((ni,nj))
                V[ni][nj] = 1
                cnt += 1
    return cnt



N = int(input())

V = [[0]*N for _ in range(N)]

arr = [list(map(int,input())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1  and V[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
for i in result:
    print(i)


