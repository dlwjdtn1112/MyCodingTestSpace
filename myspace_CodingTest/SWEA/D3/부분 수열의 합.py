from itertools import combinations

T = int(input())

result = []

for _ in range(T):
    cnt = 0
    a,b = map(int,input().split())
    l1 = list(map(int,input().split()[:a]))

    for i in range(1,a+1):
        arr = list(combinations(l1,i))
        for lst in arr:
            if sum(lst) == b:
                cnt += 1

    result.append(cnt)

for i in range(len(result)):
    print("#"+str(i+1), result[i])