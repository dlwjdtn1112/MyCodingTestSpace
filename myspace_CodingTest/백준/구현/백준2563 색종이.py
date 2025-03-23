N = int(input())

ans = 0

arr = [[0]*30 for i in range(30)]

for i in range(N):
    X,Y = map(int,input().split())

    for j in range(X,X+10):
        for k in range(Y,Y+10):
            arr[j][k] = 1

for i in arr:
    ans += i.count(1)

print(ans)

