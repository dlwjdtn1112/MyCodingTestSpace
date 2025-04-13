from itertools import product

def solution(word):
    l1 = ['A','E','I','O','U']
    result = []
    cnt = 1

    for i in range(1, len(l1) + 1):
        arr = list(product(l1, repeat=i))
        for j in arr:
            result.append(j)

    result.sort()

    for i in result:
        if word == "".join(i):
            return cnt
        cnt += 1

    return 0
