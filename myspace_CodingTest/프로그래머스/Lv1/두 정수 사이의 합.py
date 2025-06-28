def solution(a, b):
    l1 = [a, b]
    l1.sort()

    result = [i for i in range(l1[0], l1[1] + 1)]
    answer = sum(result)
    return answer