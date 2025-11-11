from itertools import combinations

n = int(input())
result = []
for _ in range(n):
    v1 = 0
    arr = list(map(int,input().split()[:5]))
    arr1 = list(combinations(arr,3))
    for lst in arr1:

        v1 = max(v1,sum(lst)%10)

    result.append(v1)

final = []

cnt = max(result)
for i in range(len(result)):
    if cnt == result[i]:
        final.append(i+1)
print(max(final))


