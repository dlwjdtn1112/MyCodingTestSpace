
def bfs(si,sj,s): ## 일반인
    q = []
    q.append((si,sj))
    V1[si][sj] = 1
    cnt = 1
    while q:
        ci,cj = q.pop(0)

        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci +di,cj +dj
            if 0<= ni < N and 0<= nj < N and V1[ni][nj] == 0 and arr[ni][nj] == s:
                q.append((ni,nj))
                V1[ni][nj] = 1
                cnt += 1

    return cnt

def bfs1(si,sj,s): ## 색약
    q = []
    q.append((si,sj))
    V2[si][sj] = 1
    cnt = 1
    while q:
        ci,cj = q.pop(0)

        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci +di,cj +dj
            if 0 <= ni < N and 0 <= nj < N and V2[ni][nj] == 0 and arr[ni][nj] == s:
                q.append((ni,nj))
                V2[ni][nj] = 1
                cnt += 1

    return cnt

N = int(input())
r1 = []
r2 = []
arr = [list(input()) for _ in range(N)]
V1 = [[0]*N for _ in range(N)] ## 일반인
V2 = [[0]*N for _ in range(N)] ## 색약

for i in range(N):
    for j in range(N):
        if (arr[i][j] == "R" and V1[i][j] == 0) or (arr[i][j] == "G" and V1[i][j] == 0) or (arr[i][j] == "B" and V1[i][j] == 0):
            r1.append(bfs(i,j,arr[i][j]))


for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr[i][j] = "R"



for i in range(N):
    for j in range(N):
        if (arr[i][j] == "R" and V2[i][j] == 0)  or (arr[i][j] == "B" and V2[i][j] == 0):
            r2.append(bfs1(i,j,arr[i][j]))
print(len(r1),len(r2))