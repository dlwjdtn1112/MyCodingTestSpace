from itertools import combinations

result = []

s1 = 'abcdefghijklmnopqrstuvwxyz'

T = int(input().strip())

for _ in range(T):
    a = int(input().strip())
    cnt = 0
    arr = []
    for i in range(a):
        arr.append(input().strip())

    for j in range(1, a + 1):
        l1 = combinations(arr, j)
        for lst in l1:
            l2 = list(set("".join(lst)))
            l2.sort()
            if "".join(l2) == s1:
                cnt += 1
    result.append(cnt)

for i in range(len(result)):
    print("#" + str(i + 1), result[i])
