from itertools import combinations


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False


    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

a,b = map(int,input().split())

arr = list(map(int,input().split()))

arr1  = list(combinations(arr,b))

result  = []

for lst in arr1:
    if is_prime(sum(lst)) == True:
        result.append(sum(lst))
result1 = list(set(result))
result1.sort()

if len(result1) == 0:
    print(-1)
else:
    for i in result1:
        print(i,end = " ")

