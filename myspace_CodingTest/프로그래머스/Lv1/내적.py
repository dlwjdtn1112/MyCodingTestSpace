def solution(a, b):
    answer = 0
    arr = list(zip(a, b))

    for lst in arr:
        answer += lst[0] * lst[1]
    return answer