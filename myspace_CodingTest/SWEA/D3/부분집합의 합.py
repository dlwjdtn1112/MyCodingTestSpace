from itertools import combinations,permutations


result = []

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    cnt = 0
    l1 = [i+1 for i in range(12)]

    l2 = list(combinations(l1,a))
    for lst in l2:
        if sum(lst) == b:
            cnt += 1

    result.append(cnt)





for lst in range(len(result)):
    print("#"+str(lst+1), result[lst])
