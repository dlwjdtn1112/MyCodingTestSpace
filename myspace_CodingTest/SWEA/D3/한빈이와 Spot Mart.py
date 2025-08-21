from itertools import combinations

result = []

T = int(input())

for _ in range(T):
    l1 = []
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    arr1 = list(combinations(arr,2))
    for lst in arr1:
        if sum(lst) <= b:
            l1.append(sum(lst))
    if len(l1) == 0:
        result.append(-1)
    else:
        result.append(max(l1))



for i in range(len(result)):
    print("#"+str(i+1) , result[i])