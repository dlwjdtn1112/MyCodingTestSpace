
arr = [list(map(int,input().split())) for i in range(3)]

for i in arr:
    print(*i)
arr1 = list(zip(*arr))
for i in arr1:
    print(*i)


