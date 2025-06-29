def solution(s):
    m1 = 10000000
    for i in range(1, s):
        if s % i == 1:
            m1 = min(m1, i)

    return m1
