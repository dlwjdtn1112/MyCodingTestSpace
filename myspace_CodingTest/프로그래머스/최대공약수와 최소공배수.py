def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


def solution_my(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    return answer