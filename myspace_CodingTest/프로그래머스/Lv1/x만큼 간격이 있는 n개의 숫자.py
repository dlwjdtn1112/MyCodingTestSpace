def solution(x, n):
    answer = []
    a = x
    for i in range(n):
        answer.append(x)
        x += a
    return answer

print(solution(2,5))
