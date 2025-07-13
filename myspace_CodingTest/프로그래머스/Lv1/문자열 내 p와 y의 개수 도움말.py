def solution(s):
    s1 = s.lower()
    v1 = s1.count('p')
    v2 = s1.count('y')

    if v1 == v2:
        return True
    else:
        return False
