

N,M = map(int,input().split())

cnt = 0
arr = [[0]*101 for _ in range(101)]

for i in range(N):
    a,b,c,d = map(int,input().split())

    for j in range(a,c+1):
        for k in range(b,d+1):
            if arr[j][k] == 0:
                arr[j][k] = 1
            else:
                arr[j][k]  = arr[j][k] + 1



for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] > M:
            cnt += 1

print(cnt)





