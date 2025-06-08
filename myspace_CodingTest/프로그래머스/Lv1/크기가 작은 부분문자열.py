def solution(t, p):
    result = 0

    len_p = len(p) - 1
    arr = []

    for i in range(len(t) - len_p):
        arr.append(t[i:i + len(p)])

    for lst in arr:
        if int(lst) <= int(p):
            result += 1

    answer = result
    return answer