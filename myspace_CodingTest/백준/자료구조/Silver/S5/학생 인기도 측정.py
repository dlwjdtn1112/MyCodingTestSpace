

N = int(input())

arr = list(input().split())

l1 = [0] * len(arr)

result = dict(list(zip(arr,l1)))

for _ in range(N):
    l2 = list(input().split())
    for lst in l2:
        result[lst] += 1

arr1 = []

for i,j in result.items():
    arr1.append([i,j])

arr2 = sorted(arr1,reverse=True,key=lambda x:(x[1]))

for lst in arr2:
    print(*lst)

