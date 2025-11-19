from itertools import permutations


N = int(input())

arr = list(map(int,input().split()))
arr1 = list(permutations(arr,N))
result = []
for lst in arr1:
    cnt = 0
    for i in range(1,len(lst)):
        cnt += abs(lst[i] - lst[i-1])
    result.append(cnt)

print(max(result))