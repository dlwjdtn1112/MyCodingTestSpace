def solution(n):
    n1 = list(str(n))
    n1.sort()
    n1.reverse()
    int_n1 = int("".join(n1))
    return int_n1
