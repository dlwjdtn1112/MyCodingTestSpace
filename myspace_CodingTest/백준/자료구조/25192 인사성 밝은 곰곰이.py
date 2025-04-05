N = int(input())

arr = []

for i in range(N):
    s = input()
    arr.append(s)
cnt = 0
l1 = []
for i in arr:
    if i == 'ENTER':
        cnt += len(set(l1))
        l1 = []

    else :
        l1.append(i)
cnt += len(set(l1))
print(cnt)


