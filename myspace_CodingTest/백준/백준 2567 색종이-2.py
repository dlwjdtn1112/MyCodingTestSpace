


N = int(input())

arr  = [[0]*100 for i in range(100)]

ans = 0

for i in range(N):
    X,Y = map(int,input().split())
    for j in range(X,X+10):
        for k in range(Y,Y+10):
            arr[j][k] = 1

for lst in arr:
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            ans += 1
arr1 = list(zip(*arr))
for lst in arr1:
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            ans += 1
print(ans)





