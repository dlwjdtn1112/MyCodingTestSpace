def solution(n, s):
    arr = []
    if n > s:
        return [-1]
    else:
        v1 = s // n
        v2 = s % n
        for i in range(n - v2):
            arr.append(v1)
        for i in range(v2):
            arr.append(v1 + 1)
        return arr
