# 내가 작성한 코드

def solution1(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i

    return result

# chat gpt4o
def solution2(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

