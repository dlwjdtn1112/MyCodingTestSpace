# 내가 작성한 코드
N = int(input())

arr = []

final = []
for i in range(N):
    arr.append(input())


arr_set = list(set(arr))
arr1 = [0 for _ in range(len(arr_set))]

arr_result = dict(zip(arr_set,arr1))

for lst in arr:
    arr_result[lst] += 1

mx = 0
for lst in arr_result:
    mx = max(mx,arr_result[lst])
for lst in arr_result:
    if arr_result[lst] == mx:
        final.append(lst)
final.sort()
for lst in final:
    print(lst)