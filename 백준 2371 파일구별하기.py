
N = int(input())


arr = []
arr1 = []
for _ in range(N):
    l1 = list(map(int,input().split()))
    a = l1.index(-1)
    arr.append(l1[0:a])

mx = 0

for i in arr:
    mx = max(mx,len(i))

for i in arr:
    for j in range(mx-len(i)):
        i.append(0)

for i in arr:
    l2 = [str(j) for j in i]
    arr1.append(l2)
cnt = 0
for i in range(1,mx+1):
    arr3 = []
    for j in arr1:
        arr3.append("".join(j[0:i]))

    if N == len(set(arr3)):
        cnt = i
print(cnt)













